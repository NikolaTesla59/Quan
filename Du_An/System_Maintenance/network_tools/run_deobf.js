const fs = require('fs');

function deobfuscateFile(filePath, outPath) {
    let code = fs.readFileSync(filePath, 'utf8');
    
    // Find decoder function name
    let fnMatches = [...code.matchAll(/function (a0_0x[a-f0-9]+)\(/g)];
    if (!fnMatches.length) return;
    let decoderName = fnMatches[0][1];
    let arrayFnName = fnMatches[fnMatches.length - 1][1];
    
    let decoderDef = code.slice(code.indexOf('function ' + decoderName), code.indexOf('(function('));
    let shuffleDef = code.slice(code.indexOf('(function('), code.indexOf(',((('));
    if (!shuffleDef || shuffleDef.length > 5000) {
        shuffleDef = code.slice(code.indexOf('(function('), code.indexOf(');const '));
    }
    let arrayDef = code.slice(code.lastIndexOf('function ' + arrayFnName));
    
    let setup = decoderDef + "\n" + shuffleDef + "\n" + arrayDef + "\nglobal.decoder = " + decoderName + ";";
    eval(setup);
    
    let dict = {};
    for (let i = 0x50; i < 0x400; i++) {
        try {
            let val = global.decoder(i);
            if (val !== undefined && typeof val === 'string') {
                dict[i] = val;
            }
        } catch(e) {}
    }
    
    for (let [i, val] of Object.entries(dict)) {
        let hex = '0x' + Number(i).toString(16);
        code = code.split(decoderName + '(' + hex + ')').join(JSON.stringify(val));
        code = code.split(decoderName + '(' + i + ')').join(JSON.stringify(val));
    }
    
    fs.writeFileSync(outPath, code);
    console.log("Wrote", outPath, "with", Object.keys(dict).length, "strings decoded");
}

try {
    deobfuscateFile('C:\\Users\\Admin\\Downloads\\95GG_PRO\\core\\validator.js', 'C:\\Users\\Admin\\Downloads\\95GG_PRO\\core\\validator.deobf.js');
} catch(e) { console.error("validator err:", e); }

try {
    deobfuscateFile('C:\\Users\\Admin\\Downloads\\95GG_PRO\\ui\\controller.js', 'C:\\Users\\Admin\\Downloads\\95GG_PRO\\ui\\controller.deobf.js');
} catch(e) { console.error("controller err:", e); }

try {
    deobfuscateFile('C:\\Users\\Admin\\Downloads\\95GG_PRO\\core\\engine.js', 'C:\\Users\\Admin\\Downloads\\95GG_PRO\\core\\engine.deobf.js');
} catch(e) { console.error("engine err:", e); }
