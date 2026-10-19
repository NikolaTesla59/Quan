# BỘ QUY CHUẨN KỸ THUẬT SENIOR TOÀN TẬP: CORE TECH STACKS
> Tổng hợp chắt lọc từ `awesome-cursorrules` & `cursor.directory`.  
> Tiêu chuẩn: 100% Kỹ thuật thực chiến, Mật độ tri thức cao, Không quy tắc đạo đức hay triết lý chung chung.

---

## MỤC LỤC
1. [MODERN PYTHON (3.12+)](#1-modern-python-312)
   - 1.1 Type Hinting & Static Typing Hệ Thống
   - 1.2 Pydantic v2 Production Patterns
   - 1.3 Clean Architecture & Phân Tầng Trách Nhiệm (4-Layer)
   - 1.4 Dependency Injection (IoC) & Protocol-driven Decoupling
   - 1.5 Error Handling & Contextual Defensive Patterns
2. [HIGH-PERFORMANCE DATA: PANDAS & POLARS](#2-high-performance-data-pandas--polars)
   - 2.1 Kỷ Luật Tối Thượng: Triệt Tiêu 100% Vòng Lặp `for` & `.iterrows()`
   - 2.2 Polars: Expression-First & LazyFrame Architecture
   - 2.3 Pandas 2.0+ Vectorization & PyArrow Engine
   - 2.4 Quản Trị Bộ Nhớ (Memory Footprint Reduction)
   - 2.5 Time Series & High-Frequency Tick Data
3. [FASTAPI: PRODUCTION ASYNC ARCHITECTURE](#3-fastapi-production-async-architecture)
   - 3.1 Async Event Loop & Non-Blocking Concurrency
   - 3.2 Thin Router Design & API Contract Enforcement
   - 3.3 Schema Validation & Anti-Corruption Layer (ACL)
   - 3.4 Lifespan Management, Middleware & Bulkhead Isolation
4. [MODERN WEB: NEXT.JS 15+ / REACT 19](#4-modern-web-nextjs-15--react-19)
   - 4.1 Server Components (RSC) vs Client Components Boundary
   - 4.2 State Management Hierarchy (URL State, Local State, Zustand, TanStack Query)
   - 4.3 Rendering Performance, Streaming SSR & Core Web Vitals
5. [SYSTEMS PROGRAMMING: MODERN C++20 & RUST](#5-systems-programming-modern-c20--rust)
   - 5.1 C++20: RAII, Smart Pointers & Memory Safety
   - 5.2 C++20: Concepts, Ranges & Functional Error Handling
   - 5.3 Rust: Ownership, Borrowing & Zero-Cost Abstractions
   - 5.4 Rust: Production Error Handling (`thiserror` vs `anyhow`)
   - 5.5 Rust: Concurrency & Async Runtime (Tokio)

---

# 1. MODERN PYTHON (3.12+)

### 1.1 Type Hinting & Static Typing Hệ Thống
- **PEP 585 & PEP 604:** Luôn dùng builtin generics (`list[str]`, `dict[str, Any]`, `tuple[int, ...]`) và union operator `|`. Nghiêm cấm import `List`, `Dict`, `Tuple`, `Optional`, `Union` từ module `typing`.
- **Type Statement (PEP 695 - Python 3.12+):** Sử dụng cú pháp `type` cho generic type alias thay cho `TypeVar`:
  ```python
  # DO:
  type ResultPair[T, E] = tuple[T | None, E | None]
  type Coordinate = tuple[float, float]

  # DON'T:
  from typing import TypeVar, Tuple, Optional
  T = TypeVar("T")
  ResultPair = Tuple[Optional[T], Optional[Exception]]
  ```
- **Self & Protocol:** Sử dụng `typing.Self` cho method chaining/fluent interfaces. Sử dụng `typing.Protocol` (Structural Subtyping / Duck Typing có kiểm tra tĩnh) thay vì ép kế thừa từ abstract base classes (`ABC`) khi chỉ cần interface contract:
  ```python
  from typing import Protocol, Self

  class Serializable(Protocol):
      def serialize(self) -> bytes: ...

  class Builder:
      def set_id(self, item_id: str) -> Self:
          self.item_id = item_id
          return self
  ```
- **Strict Return Types:** 100% hàm phải khai báo kiểu trả về, bao gồm cả `-> None`.

---

### 1.2 Pydantic v2 Production Patterns
- **Triệt tiêu toàn bộ cú pháp legacy v1:**
  - Cấm dùng: `.dict()`, `.json()`, `parse_obj()`, `root_validator`, `@validator`, `class Config:`.
  - Bắt buộc dùng: `model_dump()`, `model_dump_json()`, `model_validate()`, `@model_validator(mode="before"|"after")`, `@field_validator`, `model_config = ConfigDict(...)`.
- **ConfigDict Chuẩn Mực:**
  ```python
  from pydantic import BaseModel, ConfigDict, Field

  class ImmutableDTO(BaseModel):
      model_config = ConfigDict(
          strict=True,
          frozen=True,
          extra="forbid",
          populate_by_name=True,
          from_attributes=True  # Thay thế orm_mode=True
      )
      user_id: str = Field(..., pattern=r"^[a-zA-Z0-9_-]+$")
      credit_limit: float = Field(..., ge=0.0)
  ```
- **TypeAdapter cho generic & collection parsing:**
  ```python
  from pydantic import TypeAdapter

  order_list_adapter = TypeAdapter(list[ImmutableDTO])
  orders = order_list_adapter.validate_python(raw_records)
  ```
- **Computed Fields:** Dùng `@computed_field` thay vì properties không nằm trong schema serialization:
  ```python
  from pydantic import computed_field

  class OrderItem(BaseModel):
      price: float
      quantity: int

      @computed_field
      @property
      def total_amount(self) -> float:
          return round(self.price * self.quantity, 2)
  ```

---

### 1.3 Clean Architecture & Phân Tầng Trách Nhiệm (4-Layer)
Dự án backend bắt buộc tuân thủ luồng phụ thuộc 1 chiều (Dependency Rule):
`Router (HTTP/API) -> Service (Use Cases / Domain Logic) -> Repository (Data Access) -> ORM / External Drivers`.

| Tầng | Nhiệm Vụ | Quy Tắc Nhập Thư Viện (Import Boundaries) |
| :--- | :--- | :--- |
| **Routers (`app/routers`)** | Parse HTTP request, validate DTO, gọi 1 method service, trả về response DTO. Độ dài hàm $\le$ 10 dòng. | **Cho phép:** FastAPI, DTO Schemas, Services.<br>**CẤM:** SQLAlchemy, Raw SQL, DB Models, external HTTP clients. |
| **Services (`app/services`)** | Chứa toàn bộ business logic, transactional flow, domain rules. | **Cho phép:** Domain Entities, Repository Protocols, Domain Exceptions.<br>**CẤM:** FastAPI Request/Response/HTTPException, DB Sessions, SQLAlchemy. |
| **Repositories (`app/repositories`)** | Tương tác CSDL, thực thi query tối ưu, map ORM model sang Domain Entity. | **Cho phép:** SQLAlchemy, SQL, Caching clients.<br>**Trả về:** Pure Domain Entities (dataclass / Pydantic), không trả về SQLAlchemy ORM model sống. |
| **Infrastructure / Providers** | Tương tác bên thứ 3 (Payment, Cloud, Email, External API). | Phải bọc qua Anti-Corruption Layer (ACL), trả về kiểu dữ liệu đóng gói `Result[T, E]`. |

---

### 1.4 Dependency Injection (IoC) & Protocol-driven Decoupling
- **Constructor Injection:** Không khởi tạo database session hay client bên trong class service. Khai báo dependency qua `__init__` nhận `Protocol`.
  ```python
  from typing import Protocol

  class UserRepositoryProtocol(Protocol):
      async def get_by_id(self, user_id: str) -> UserDomainEntity | None: ...

  class UserService:
      def __init__(self, repo: UserRepositoryProtocol) -> None:
          self._repo = repo  # Decoupled hoàn toàn khỏi SQLAlchemy hay Mongo
  ```
- **FastAPI Factory Injections:** Quản trị injection tại `app/core/deps.py` qua `Depends`:
  ```python
  from fastapi import Depends
  from sqlalchemy.ext.asyncio import AsyncSession

  async def get_user_service(
      session: AsyncSession = Depends(get_db_session)
  ) -> UserService:
      repo = SqlAlchemyUserRepository(session)
      return UserService(repo=repo)
  ```

---

### 1.5 Error Handling & Contextual Defensive Patterns
- **Domain Exceptions vs HTTP Exceptions:** Tầng Service tuyệt đối **không** `raise HTTPException`. Service chỉ raise Domain Exceptions. Tầng Router hoặc Global Exception Handler chịu trách nhiệm map sang HTTP status code tương ứng:
  ```python
  # domain/exceptions.py
  class DomainError(Exception): pass
  class EntityNotFoundError(DomainError): pass
  class BalanceInsufficientError(DomainError): pass

  # main.py (Global Exception Mapper)
  @app.exception_handler(EntityNotFoundError)
  async def entity_not_found_handler(request: Request, exc: EntityNotFoundError):
      return JSONResponse(status_code=404, content={"code": "NOT_FOUND", "message": str(exc)})
  ```
- **Context Preservation:** Khi re-raise exception, luôn bảo tồn traceback bằng `raise NewException(...) from err`.
- **ContextVars cho Distributed Tracing:**
  ```python
  import contextvars
  request_id_ctx: contextvars.ContextVar[str] = contextvars.ContextVar("request_id", default="")
  ```

---

# 2. HIGH-PERFORMANCE DATA: PANDAS & POLARS

### 2.1 Kỷ Luật Tối Thượng: Triệt Tiêu 100% Vòng Lặp `for` & `.iterrows()`
- **CẤM:** Duyệt từng dòng bằng `for idx, row in df.iterrows()` hoặc `for row in df.itertuples()` để tính toán cột hoặc áp dụng điều kiện logic. Chi phí context switch và boxing/unboxing của Python interpreter trên từng dòng phá hủy 99% hiệu năng.
- **THAY THẾ:** 
  1. Vectorized native operations (`df['a'] * df['b']`).
  2. `np.where(condition, x, y)` cho logic nhị phân.
  3. `np.select(conditions, choices, default=default)` cho logic nhiều nhánh.
  4. Chuyển đổi sang `Polars Expressions` khi kích thước dữ liệu vượt quá $10^5$ bản ghi.

---

### 2.2 Polars: Expression-First & LazyFrame Architecture
- **Lazy Execution:** Mọi pipeline biến đổi dữ liệu lớn phải bắt đầu bằng `pl.scan_parquet` hoặc `pl.scan_csv`, tận dụng tối đa Query Optimizer (Predicate Pushdown, Projection Pushdown). Chỉ gọi `.collect()` hoặc `.collect(streaming=True)` ở bước cuối cùng.
  ```python
  import polars as pl

  q = (
      pl.scan_parquet("ticks_data/*.parquet")
      .filter((pl.col("symbol") == "VIC") & (pl.col("volume") > 1000))
      .with_columns(
          (pl.col("price") * pl.col("volume")).alias("notional"),
          pl.col("timestamp").dt.truncate("1m").alias("bar_time")
      )
      .group_by(["symbol", "bar_time"])
      .agg([
          pl.col("price").first().alias("open"),
          pl.col("price").max().alias("high"),
          pl.col("price").min().alias("low"),
          pl.col("price").last().alias("close"),
          pl.col("volume").sum().alias("volume"),
          pl.col("notional").sum().alias("turnover"),
      ])
      .sort("bar_time")
  )
  df_candles = q.collect(streaming=True)
  ```
- **Polars Window Expressions:** Sử dụng `.over()` thay vì groupby-merge lặp lại:
  ```python
  # Tính biến động chuẩn hóa theo từng mã cổ phiếu không cần groupby-join
  pl.col("price") / pl.col("price").mean().over("symbol") - 1.0
  ```
- **Conditional Expressions:**
  ```python
  pl.when(pl.col("spread") > 0.05)
    .then(pl.lit("HIGH_VOL"))
    .when(pl.col("spread") > 0.02)
    .then(pl.lit("MED_VOL"))
    .otherwise(pl.lit("LOW_VOL"))
    .alias("volatility_regime")
  ```

---

### 2.3 Pandas 2.0+ Vectorization & PyArrow Engine
- **PyArrow Backend:** Khi khởi tạo DataFrame hoặc đọc file, sử dụng engine PyArrow để giảm 50-70% RAM và tăng tốc độ xử lý chuỗi:
  ```python
  import pandas as pd
  df = pd.read_parquet("market_depth.parquet", dtype_backend="pyarrow")
  ```
- **Method Chaining & Assign:** Sử dụng `.assign()` và `.pipe()` để tạo pipeline biến đổi liên tục, dễ debug:
  ```python
  clean_df = (
      df.loc[df["volume"] > 0]
      .assign(
          log_return=lambda x: np.log(x["close"] / x["close"].shift(1)),
          vwap=lambda x: (x["turnover"] / x["volume"]).fillna(x["close"])
      )
      .dropna(subset=["log_return"])
  )
  ```
- **Khắc phục triệt để `SettingWithCopyWarning`:**
  - Không bao giờ gán slice theo kiểu `df[df['a'] > 1]['b'] = 10`.
  - Luôn gán tường minh qua `.loc`: `df.loc[df['a'] > 1, 'b'] = 10` hoặc clone tường minh qua `.copy()`.

---

### 2.4 Quản Trị Bộ Nhớ (Memory Footprint Reduction)
- **Downcasting Types:** Không lưu kiểu mặc định 64-bit (`int64`, `float64`) khi giá trị chỉ cần độ rộng nhỏ hơn:
  - Timestamp dạng epoch milliseconds -> `int64`.
  - Số lượng cổ phiếu khớp lệnh (Volume) -> `uint32`.
  - Tỷ lệ %, lợi suất, chỉ số RSI -> `float32`.
  - ID phân loại, mã lệnh, trạng thái -> Chuyển đổi từ `object` (string pointer) sang `category` (Pandas) hoặc `pl.Enum` / `pl.Categorical` (Polars). Giảm đến 90% footprint RAM.

---

### 2.5 Time Series & High-Frequency Tick Data
- **As-Of Merge (Tick Matching):** Nghiêm cấm dùng vòng lặp hoặc query SQL phức tạp để match giá khớp lệnh gần nhất với sổ lệnh (Limit Order Book). Dùng `merge_asof` (Pandas) hoặc `join_asof` (Polars):
  ```python
  # Polars join_asof: Match từng giao dịch (trades) với snapshot gần nhất của Order Book
  matched = trades.join_asof(
      quotes,
      on="timestamp",
      by="symbol",
      strategy="backward",  # Lấy quote trước hoặc bằng thời điểm trade
      tolerance="500ms"     # Độ trễ tối đa cho phép
  )
  ```
- **Storage Standards:** Tuyệt đối không lưu tick/order data bằng CSV. 100% dữ liệu chuỗi thời gian phải lưu dưới dạng **Apache Parquet** nén `zstd` hoặc `snappy`, phân vùng (partition) theo `date` và `symbol`.

---

# 3. FASTAPI: PRODUCTION ASYNC ARCHITECTURE

### 3.1 Async Event Loop & Non-Blocking Concurrency
- **Phân biệt `async def` và `def`:**
  - `async def`: Dành cho các tác vụ I/O non-blocking (asyncpg, httpx, redis.asyncio, aiofiles).
  - `def` (Plain sync): Khi sử dụng thư viện đồng bộ (synchronous SDK, NumPy tính toán nặng, OpenCV, sync database drivers). FastAPI sẽ tự động đưa hàm `def` vào threadpool worker riêng (`anyio.to_thread.run_sync`), tránh chặn Event Loop.
- **TỬ HUYỆT (Fatal Anti-Pattern):** Gọi thư viện chặn đồng bộ (blocking call) bên trong hàm `async def`:
  ```python
  # SAI TỐI KỴ - BLOCK HOÀN TOÀN TẤT CẢ CLIENTS KHÁC:
  @router.get("/bad")
  async def bad_endpoint():
      time.sleep(5)                 # Phá hủy Event Loop
      res = requests.get(url)       # Block luồng đơn của tiến trình

  # ĐÚNG - DÙNG ASYNC NATIVE HOẶC ĐẨY VÀO THREADPOOL:
  @router.get("/good-async")
  async def good_async(client: httpx.AsyncClient = Depends(get_http_client)):
      await asyncio.sleep(5)
      res = await client.get(url)

  @router.get("/good-cpu-bound")
  async def good_cpu(data: list[float]):
      import anyio
      result = await anyio.to_thread.run_sync(heavy_numpy_calculation, data)
      return {"result": result}
  ```

---

### 3.2 Thin Router Design & API Contract Enforcement
- **Độ dài Router:** Handler $\le$ 10 dòng code logic. Router chỉ parse request, gọi service, map response.
- **Contract Khắt Khe:** Mọi endpoint đều phải định nghĩa `response_model`, `status_code`, và OpenAPI tag:
  ```python
  @router.post(
      "/accounts/{account_id}/transfer",
      response_model=TransferResponseDTO,
      status_code=status.HTTP_200_OK,
      summary="Execute balance transfer between two accounts"
  )
  async def transfer_balance(
      account_id: str,
      request: TransferRequestDTO,
      service: AccountService = Depends(get_account_service),
  ) -> TransferResponseDTO:
      transfer = await service.execute_transfer(
          source_id=account_id,
          target_id=request.target_account_id,
          amount=request.amount,
          idempotency_key=request.idempotency_key,
      )
      return TransferResponseDTO.from_domain(transfer)
  ```

---

### 3.3 Schema Validation & Anti-Corruption Layer (ACL)
- **Tách biệt DTO và Domain:** Tuyệt đối không để API Router nhận hoặc trả về trực tiếp SQLAlchemy Model. Cần có:
  1. `RequestDTO` (Input schema)
  2. `ResponseDTO` (Output schema)
  3. `DomainEntity` (Thực thể nội tại tầng Service)
- **Anti-Corruption Layer cho External Integration:** Khi gọi API bên thứ 3 (Payment Gateway, Broker API), không bao giờ trả về `dict` tự do. Phải map ngay sang Pydantic schema hoặc Frozen Dataclass:
  ```python
  @dataclass(frozen=True)
  class PaymentGatewayResult:
      transaction_id: str
      status: Literal["SUCCESS", "FAILED", "PENDING"]
      error_code: str | None = None
  ```

---

### 3.4 Lifespan Management, Middleware & Bulkhead Isolation
- **Lifespan Context Manager:** Cấm dùng `@app.on_event("startup")` (đã deprecated). Quản lý vòng đời tài nguyên (DB Pool, HTTP Client, Cache) tập trung qua `lifespan`:
  ```python
  from contextlib import asynccontextmanager
  from fastapi import FastAPI
  import httpx

  @asynccontextmanager
  async def lifespan(app: FastAPI):
      # Khởi tạo Resource Pools
      app.state.http_client = httpx.AsyncClient(
          timeout=httpx.Timeout(connect=5.0, read=30.0, write=10.0, pool=5.0),
          limits=httpx.Limits(max_connections=100, max_keepalive_connections=20)
      )
      yield
      # Dọn dẹp tài nguyên khi shutdown
      await app.state.http_client.aclose()

  app = FastAPI(lifespan=lifespan)
  ```
- **Bulkhead Pattern cho Outgoing HTTP:** Mỗi nhà cung cấp dịch vụ thứ ba phải sở hữu một instance `httpx.AsyncClient` độc lập với pool limit riêng biệt. Sự cố nghẽn mạng từ Provider A không được phép làm cạn kiệt connection pool của Provider B.

---

# 4. MODERN WEB: NEXT.JS 15+ / REACT 19

### 4.1 Server Components (RSC) vs Client Components Boundary
- **Quy tắc Mặc định (Server First):** Tất cả components trong thư mục `app/` mặc định là React Server Components (RSC).
  - RSC dùng cho: Fetching dữ liệu trực tiếp từ DB/API, bảo vệ token/secret keys, giảm thiểu bundle size client (0kb client JS).
- **Client Components (`'use client'`):** Chỉ khai báo `'use client'` tại **lá thấp nhất (leaf components)** của cây DOM có tính tương tác:
  - Lắng nghe sự kiện người dùng (`onClick`, `onChange`, `onSubmit`).
  - Dùng React Hooks (`useState`, `useEffect`, `useReducer`, custom client hooks).
  - Dùng Web APIs (`localStorage`, `navigator`, `window`).
- **Interleaving Pattern (Ghép lồng không gây biến đổi):** Khi Server Component cần render bên trong Client Component, truyền dưới dạng `children` prop để giữ nguyên khả năng thực thi phía server:
  ```tsx
  // ClientWrapper.tsx ('use client')
  export function ModalWrapper({ children }: { children: React.ReactNode }) {
    const [open, setOpen] = useState(false);
    return <div>{open && <div className="modal">{children}</div>}</div>;
  }

  // Page.tsx (Server Component)
  export default async function Page() {
    const serverData = await db.fetchCriticalStats();
    return (
      <ModalWrapper>
        <ServerRenderedStats data={serverData} />
      </ModalWrapper>
    );
  }
  ```

---

### 4.2 State Management Hierarchy (URL State, Local State, Zustand, TanStack Query)
1. **URL State (`useSearchParams`, `nuqs`):** Mọi trạng thái có tính chất chia sẻ được (Filters, Sorting, Search Keywords, Tabs, Pagination) phải lưu trực tiếp trên URL.
2. **Ephemeral UI State (`useState`, `useReducer`):** Modal open/close, dropdown toggle, hover states.
3. **Server State (TanStack Query v5 / React Cache):**
   - Không copy dữ liệu server fetch vào Zustand store.
   - Sử dụng **HydrationBoundary** để prefetch trên server và hydrate cache mượt mà sang client:
   ```tsx
   // app/orders/page.tsx (Server Component)
   export default async function OrdersPage() {
     const queryClient = new QueryClient();
     await queryClient.prefetchQuery(ordersQueryOptions());
     return (
       <HydrationBoundary state={dehydrate(queryClient)}>
         <OrdersTableClient />
       </HydrationBoundary>
     );
   }
   ```
4. **Client Global State (Zustand):** Chỉ lưu state thuần túy tương tác client (Shopping cart draft, User UI Preferences, Realtime Audio/WebSocket connection status).
   - Bắt buộc dùng atomic selectors để tránh re-render thừa:
   ```tsx
   // TỐT: Chỉ re-render khi isOpen thay đổi
   const isOpen = useUIStore((state) => state.isSidebarOpen);
   // XẤU: Re-render khi bất kỳ trường nào trong UIStore biến động
   const { isSidebarOpen } = useUIStore();
   ```

---

### 4.3 Rendering Performance, Streaming SSR & Core Web Vitals
- **Streaming với Suspense:** Bọc các phần tử chậm hoặc fetch dữ liệu ngoại vi bằng `<Suspense fallback={<Skeleton />}>` để truyền streaming HTML ngay lập tức về browser mà không bị nghẽn bởi các async call dài:
  ```tsx
  export default function DashboardPage() {
    return (
      <main className="dashboard-grid">
        <FastHeader />
        <Suspense fallback={<MetricsCardSkeleton />}>
          <HeavyAnalyticsServerComponent />
        </Suspense>
      </main>
    );
  }
  ```
- **React 19 Server Actions:**
  - Sử dụng `useActionState` và `useOptimistic` cho các thao tác form mutation nhằm hiển thị kết quả cho người dùng tức thì trước khi network hoàn thành.
  - Luôn revalidate đúng tag bộ nhớ đệm: `revalidateTag("orders")` hoặc `revalidatePath("/dashboard")`.
- **Tối ưu Core Web Vitals:**
  - **LCP:** Preload hero images qua `<Image priority={true} ... />`.
  - **CLS:** Luôn định nghĩa rõ `width` và `height` trên ảnh và dynamic containers.
  - **INP:** Tránh tính toán nặng trên main thread trong lúc dispatch action; sử dụng `useTransition` cho các render không khẩn cấp.

---

# 5. SYSTEMS PROGRAMMING: MODERN C++20 & RUST

### 5.1 C++20: RAII, Smart Pointers & Memory Safety
- **Quy tắc Quản lý Bộ nhớ Tối cao:**
  - **Nghiêm cấm** sử dụng toán tử trần `new` và `delete`.
  - Sử dụng `std::unique_ptr` làm lựa chọn mặc định thể hiện quyền sở hữu duy nhất (Exclusive Ownership). Tạo bằng `std::make_unique<T>()`.
  - Chỉ sử dụng `std::shared_ptr` khi tài nguyên có nhiều chủ sở hữu độc lập, không xác định được thứ tự hủy.
  - Sử dụng `std::weak_ptr` để phá vỡ tham chiếu vòng tròn (Circular References).
- **Rule of Zero / Rule of Five:**
  - Ưu tiên **Rule of Zero:** Thiết kế class sử dụng các container tiêu chuẩn (`std::vector`, `std::string`, `std::unique_ptr`), không tự viết Destructor hay Copy/Move constructors.
  - Nếu phải tự quản trị tài nguyên bậc thấp, phải viết đầy đủ bộ 5 (Rule of Five): Destructor, Copy Constructor, Copy Assignment, Move Constructor, Move Assignment.
- **Truyền Tham Số Hiệu Năng Cao:**
  - Không truyền `const std::string&` cho hàm chỉ đọc chuỗi -> Dùng `std::string_view` (tránh cấp phát bộ nhớ heap).
  - Không truyền raw pointer mảng -> Dùng `std::span<const T>` cho view mảng liên tục.

---

### 5.2 C++20: Concepts, Ranges & Functional Error Handling
- **Concepts & Constraints:** Thay thế hoàn toàn template metaprogramming phức tạp (SFINAE, `std::enable_if`) bằng `concept`:
  ```cpp
  #include <concepts>

  template<typename T>
  concept Numeric = std::integral<T> || std::floating_point<T>;

  template<Numeric T>
  T calculate_momentum(T current_price, T past_price) noexcept {
      return (current_price - past_price) / past_price;
  }
  ```
- **Ranges Pipelines:** Sử dụng views để xử lý dữ liệu lazy không cấp phát trung gian:
  ```cpp
  #include <ranges>
  #include <vector>

  std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  auto even_squares = numbers 
      | std::views::filter([](int n) { return n % 2 == 0; })
      | std::views::transform([](int n) { return n * n; });
  ```
- **Functional Error Handling:**
  - Trong hot path / latency-critical loops: Cấm throw exceptions. Sử dụng `std::optional<T>` hoặc `std::expected<T, E>` (C++23 hoặc thư viện tương đương trên C++20).

---

### 5.3 Rust: Ownership, Borrowing & Zero-Cost Abstractions
- **Mượn (Borrowing) thay vì Clone:**
  - Ưu tiên nhận slice `&str` thay vì `&String`, nhận `&[T]` thay vì `&Vec<T>`.
  - Tránh lạm dụng `.clone()` để làm hài lòng Borrow Checker. Nếu phải dùng `.clone()`, phải có lý do kỹ thuật rõ ràng (chuyển thread hoặc độc lập mutation).
- **Tránh Lạm Dụng `Arc<Mutex<T>>`:**
  - Phân tách cấu trúc dữ liệu theo nguyên tắc Single-Writer, hoặc truyền thông điệp qua channels (`tokio::sync::mpsc`, `crossbeam`) thay vì dùng khóa đồng bộ trên toàn bộ dữ liệu.
- **Newtype Pattern:** Sử dụng tuple struct 1 phần tử để tạo type-safety ở mức compile-time, zero runtime cost:
  ```rust
  #[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
  pub struct OrderId(pub u64);

  #[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
  pub struct AccountId(pub u64);

  // Không thể truyền nhầm AccountId vào hàm yêu cầu OrderId
  fn cancel_order(order_id: OrderId, account: AccountId) { ... }
  ```

---

### 5.4 Rust: Production Error Handling (`thiserror` vs `anyhow`)
- **Triệt tiêu Hoàn toàn Crash Runtime:**
  - **TUYỆT ĐỐI CẤM** gọi `.unwrap()` hoặc `.expect()` trên mã nguồn chạy production (ngoại trừ các test case hoặc bất biến lúc khởi tạo ứng dụng đã được chứng minh an toàn).
  - Sử dụng toán tử `?` để truyền lỗi lên tầng trên.
- **Phân tách Rõ Ràng Phạm Vi Xử Lý Lỗi:**
  - **Tầng Thư viện / Domain Core:** Dùng `thiserror` định nghĩa enum lỗi tường minh, chi tiết:
    ```rust
    use thiserror::Error;

    #[derive(Error, Debug)]
    pub enum OrderBookError {
        #[error("Insufficient liquidity for order {order_id:?}")]
        InsufficientLiquidity { order_id: u64 },
        #[error("Invalid price point: {0}")]
        InvalidPrice(f64),
        #[error("I/O error while persisting book: {0}")]
        PersistenceError(#[from] std::io::Error),
    }
    ```
  - **Tầng Application / CLI / Entrypoint:** Dùng `anyhow::Result<T>` và `.context()` để thu thập toàn bộ vết ngữ cảnh lỗi khi gọi các subsystem:
    ```rust
    use anyhow::{Context, Result};

    fn boot_engine(config_path: &str) -> Result<()> {
        let raw = std::fs::read_to_string(config_path)
            .with_context(|| format!("Failed to read config file from {}", config_path))?;
        Ok(())
    }
    ```

---

### 5.5 Rust: Concurrency & Async Runtime (Tokio)
- **Cấm Giữ Mutex Guard Qua `.await` Point:**
  - Giữ `std::sync::MutexGuard` qua điểm đình chỉ `.await` sẽ gây lỗi compile (`!Send`) hoặc deadlock threadpool.
  - Giải pháp: Rút ngắn scope của lock bằng khối block `{ ... }` hoặc sử dụng `tokio::sync::Mutex` khi thực sự bắt buộc.
- **Xử lý Tác vụ Nặng CPU hoặc I/O Đồng Bộ:**
  - Tuyệt đối không chạy thuật toán mã hóa nặng hoặc gọi blocking file I/O trong async task. Sử dụng `tokio::task::spawn_blocking`:
  ```rust
  let processed = tokio::task::spawn_blocking(move || {
      heavy_compression_algorithm(&raw_data)
  }).await?;
  ```
- **Structured Concurrency & Graceful Cancellation:**
  - Sử dụng `tokio::select!` để xử lý đồng thời timeout, event trigger và tín hiệu graceful shutdown:
  ```rust
  tokio::select! {
      res = worker.run() => {
          if let Err(e) = res { tracing::error!("Worker error: {:?}", e); }
      }
      _ = tokio::signal::ctrl_c() => {
          tracing::info!("Shutdown signal received. Cleaning up worker tasks...");
          worker.shutdown().await;
      }
  }
  ```

---
*Tài liệu kỹ thuật được thiết lập cho môi trường lập trình tối ưu hóa cao độ, phục vụ trực tiếp cho AI Coding Agents và các kỹ sư hệ thống cao cấp.*
