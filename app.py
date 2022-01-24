from flask import Flask, render_template, request, jsonify, json
from wtforms import StringField, Form
from wtforms.validators import DataRequired, Length
from faker import Faker 

app = Flask(__name__)
fake = Faker()
 
class SearchForm(Form): #create form
    query = StringField('Query', validators=[DataRequired(),Length(max=40)],render_kw={"placeholder": "query"})

def FakeAddress():
    name = [fake.name() for _ in range(100) ]
    address = [fake.address() for _ in range(100) ]
    text = [fake.text() for _ in range(100) ]
    text2 = ['A.NET', 'A#A', 'sharpA-0', 'SystemA+', 'A', 'plusABAPABCABC', 'ALGOLACCAccent', 'Rational', 'SynergyAce', 'DASL', 'Distributed', 'Application', 'Specification', 'LanguageAction!ActionScriptActorAdaAdenine', 'HaystackAdvPLAgdaAgilent', 'VEE', 'Keysight', 'VEEAgoraAIMMSAldorAlefALFALGOL', '58ALGOL', '60ALGOL', '68ALGOL', 'WAlice', 'Alice', 'MLAlma-0AmbientTalkAmiga', 'EAMOS', 'AMOS', 'BASICAMPLAnalitikAngelScriptApache', 'Pig', 'latinApex', 'Salesforce.com,', 'IncAPLApp', 'Inventor', 'for', "Android's", 'visual', 'block', 'language', 'MIT', 'App', 'InventorAppleScriptAPTArcARexxArgusAssembly', 'language', 'ASMAutoItAutoLISP', '', 'Visual', 'LISPAverestAWKAxumBBBabbageBallerinaBashBASICBatch', 'file', 'WindowsMS-DOSbc', 'basic', 'calculatorBCPLBeanShellBertrandBETABLISSBlocklyBlooPBooBoomerangBosqueBucketCC', '–', 'ISOIEC', '9899C--', 'C', 'minus', 'minusC++', 'C', 'plus', 'plus', '–', 'ISOIEC', '14882C*C#', 'C', 'sharp', '–', 'ISOIEC', '23270CALCaché', 'ObjectScriptC', 'Shell', 'cshCamlCayenne', 'Lennart', 'AugustssonCDuceCecilCESIL', 'Computer', 'Education', 'in', 'Schools', 'Instruction', 'LanguageCéuCeylonCFEngineCg', 'High-Level', 'ShaderShading', 'Language', '[HLSL]ChChapel', 'Cascade', 'High', 'Productivity', 'LanguageCharmCHILLCHIP-8ChucKCilk', 'also', 'Cilk++', 'and', 'Cilk', 'plusControl', 'LanguageClaireClarionCleanClipperCLIPSCLISTClojureCLUCMS-2COBOL', '–', 'ISOIEC', '1989CobolScript', '–', 'COBOL', 'Scripting', 'languageCobraCoffeeScriptColdFusionCOMALCOMITCommon', 'Intermediate', 'Language', 'CILCommon', 'Lisp', 'also', 'known', 'as', 'CLCOMPASSComponent', 'PascalConstraint', 'Handling', 'Rules', 'CHRCOMTRANCoolCoqCoral', '66CorVisionCOWSELCPLCryptolCrystalCsoundCuneiformCurlCurryCybilCycloneCypher', 'Query', 'LanguageCythonCEEMACDDDartDarwinDataFlexDatalogDATATRIEVEdBasedcDCL', 'DIGITAL', 'Command', 'LanguageDelphiDinkCDIBOLDogDracoDRAKONDylanDYNAMODAX', 'Data', 'Analysis', 'ExpressionsEEEaseEasy', 'PLIEASYTRIEVE', 'PLUSeCECMAScriptEdinburgh', 'IMPEGLEiffelELANElixirElmEmacs', 'LispEmeraldEpigramEPL', 'Easy', 'Programming', 'LanguageEPL', 'Eltron', 'Programming', 'LanguageErlangesEscherESPOLEsterelEtoysEuclidEulerEuphoriaEusLisp', 'Robot', 'Programming', 'LanguageCMS', 'EXEC', 'EXECEXEC', '2Executable', 'UMLEzhilFFF#', 'F', 'sharpF*FactorFantomFAUSTFFPfishFjölnirFLFlagShipFlavorsFlexFlixFlooPFLOW-MATIC', 'B0FOCAL', 'Formulating', 'On-Line', 'Calculations', 'in', 'Algebraic', 'LanguageFOrmula', 'CALculatorFOCUSFOILFORMAC', 'FORMula', 'MAnipulation', 'Compiler@FormulaForthFortran', '–', 'ISOIEC', '1539FortressFPFoxBaseFoxProFranz', 'LispFutharkF-ScriptGGame', 'Maker', 'Language', 'Scripting', 'languageGameMonkey', 'ScriptGAMS', 'General', 'Algebraic', 'Modeling', 'SystemGAPG-codeGDScript', 'GodotGenieGDL', 'Geometric', 'Description', 'LanguageGEORGEGLSL', 'OpenGL', 'Shading', 'LanguageGNU', 'EGNU', 'Guile', 'GNU', 'Ubiquitous', 'Intelligent', 'Language', 'for', 'ExtensionsGoGo!GOAL', 'Game', 'Oriented', 'Assembly', 'LispGödelGoloGOM', 'Good', 'Old', 'MadGoogle', 'Apps', 'ScriptGosuGOTRAN', 'IBM', '1620GPSS', 'General', 'Purpose', 'Simulation', 'SystemGraphTalk', 'Computer', 'Sciences', 'CorporationGRASSGrasshopperGroovy', 'Apache', 'GroovyHHackHAGGISHALSHalide', 'programming', 'languageHamilton', 'C', 'shellHarbourHartmann', 'pipelinesHaskellHaxeHermesHigh', 'Level', 'Assembly', 'HLAHLSLHollywoodHolyC', 'TempleOSHopHopscotchHopeHumeHyperTalkIIoIconIBM', 'Basic', 'assembly', 'languageIBM', 'HAScriptIBM', 'Informix-4GLIBM', 'RPGIDLIdrisInformISLISPJJJ#', 'J', 'sharpJ++', 'J', 'plus', 'plusJADEJaiJALJanus', 'concurrent', 'constraint', 'programming', 'languageJanus', 'time-reversible', 'computing', 'programming', 'languageJASSJavaJavaFX', 'ScriptJavaScriptJessJCLJEANJoin', 'JavaJOSSJouleJOVIALJoyJScriptJScript', '.NETJuliaJythonKKKaleidoscopeKarelKEEKixtartKlerer-May', 'SystemKIF', 'Knowledge', 'Interchange', 'FormatKojoKotlinKRCKRLKRL', 'KUKA', 'Robot', 'LanguageKRYPTONKornShell', 'kshKoduKv', 'KivyLLabVIEWLadderLANSALassoLavaLC-3LeanLegoscriptLexicoLILLilyPondLimboLimnorLINCLingoLINQLISLISALanguage', 'HLisp', '–', 'ISOIEC', '13816Lite-CLitheLittle', 'bLLLLogoLogtalkLotusScriptLPCLSELSLLiveCodeLiveScriptLuaLucidLustreLYaPASLynxMM', 'Formula', 'languageM2001M4M#Machine', 'codeMAD', 'Michigan', 'Algorithm', 'DecoderMADIMagikMagmaMániMapleMAPPER', 'now', 'part', 'of', 'BISMARK-IV', 'now', 'VISION:BUILDERMaryMATLABMASM', 'Microsoft', 'Assembly', 'x86MATH-MATICMaude', 'systemMaxima', 'see', 'also', 'MacsymaMax', 'Max', 'Msp', '–', 'Graphical', 'Programming', 'EnvironmentMaxScript', 'internal', 'language', '3D', 'Studio', 'MaxMaya', 'MELMDLMercuryMesaMHEG-5', 'Interactive', 'TV', 'programming', 'languageMicrocodeMicroScriptMicrosoft', 'Power', 'FxMIISMilk', 'programming', 'languageMIMICMirahMirandaMIVA', 'ScriptMLModel', '204ModelicaModulaModula-2Modula-3MoholMOOMortranMouseMPDMSLMUMPSMuPADMutanMystic', 'Programming', 'Language', 'MPLNNASMNapier88NekoNemerleNESLNet.DataNetLogoNetRexxNewLISPNEWPNewspeakNewtonScriptNialNickle', 'NITINNimNix', 'Systems', 'configuration', 'languageNPLNot', 'eXactly', 'C', 'NXCNot', 'Quite', 'C', 'NQCNSISNuNWScriptNXT-GOo:XMLOakOberonOBJ2Object', 'LispObjectLOGOObject', 'REXXObject', 'PascalObjective-CObjective-JObliqOCamloccamoccam-πOctaveOmniMarkOpaOpalOpen', 'Programming', 'Language', 'OPLOpenCLOpenEdge', 'Advanced', 'Business', 'Language', 'ABLOpenVeraOPS5OptimJOrcORCAModula-2OrielOrwellOxygeneOzPPP4P′′ParaSailPARIGPPascal', '–', 'ISO', '7185Pascal', 'ScriptPCASTLPCFPEARLPeopleCodePerlPDLPharoPHPPicoPicolispPictPikePILOTPipelinesPizzaPL-11PL0PLBPLCPLI', '–', 'ISO', '6160PLMPLPPLSPLSQLPL360PLANCPlankalkülPlannerPLEXPLEXILPlusPOP-11POP-2PostScriptPortablEPOV-Ray', 'SDLPowerhousePowerBuilder', '–', '4GL', 'GUI', 'application', 'generator', 'from', 'SybasePowerShellPPLProcessingProcessing.jsPrographProject', 'VeronaPrologPROMALPromelaPROSE', 'modeling', 'languagePROTELProvideXPro*CPurePure', 'DataPureScriptPythonQQ', 'programming', 'language', 'from', 'Kx', 'SystemsQ#', 'Microsoft', 'programming', 'languageQalbQuantum', 'Computation', 'LanguageQtScriptQuakeCQPL.QLRRR++RacketRakuRAPIDRapiraRatfivRatforrcReasonREBOLRedRedcodeREFALREXXROOPRPGRPLRSLRTL2RubyRustSSS2S3S-LangS-PLUSSA-CSabreTalkSAILSAKOSASSASLSatherSawzallScalaSchemeScilabScratchScript.NETSedSeed7SelfSenseTalkSequenceLSerpentSETLShort', 'CodeSIMPOLSIGNALSiMPLESIMSCRIPTSimulaSimulinkSISALSLIPSMALLSmalltalkSMLStrongtalkSnap!SNOBOL', 'SPITBOLSnowballSOLSoliditySOPHAEROSSourceSPARKSpeakeasySpeedcodeSPINSPkSPSSQLSQRSqueakSquirrelSRSSLStarlogoStrandStataStateflowSubtextSBLSuperColliderSuperplanSuperTalkSwift', 'Apple', 'programming', 'languageSwift', 'parallel', 'scripting', 'languageSYMPLSystemVerilogTTTACLTACPOLTADS', 'Text', 'Adventure', 'Development', 'SystemTALTclTeaTECO', 'Text', 'Editor', 'and', 'CorrectorTELCOMPTeXTEX', 'Text', 'Executive', 'Programming', 'LanguageTIETMG', 'TransMo', 'Griffer,', 'compiler-compilerTomToiTopspeed', 'ClarionTPU', 'Text', 'Processing', 'UtilityTracTTMT-SQL', 'Transact-SQLTranscript', 'LiveCodeTTCN', 'Tree', 'and', 'Tabular', 'Combined', 'NotationTuringTUTOR', 'PLATO', 'Author', 'LanguageTXLTypeScriptTynkerUUbercodeUCSD', 'PascalUmpleUniconUnifaceUNITYUnrealScriptVValaVerilogVHDLVim', 'scriptViper', 'EthereumEther', 'ETHVisual', 'DataFlexVisual', 'DialogScriptVisual', 'FoxProVisual', 'J++', 'Visual', 'J', 'plus', 'plusVisual', 'LISPVisual', 'ObjectsVisual', 'PrologWWATFIV,', 'WATFOR', 'WATerloo', 'FORtran', 'IVWebAssemblyWebDNAWhileyWinbatchWolfram', 'LanguageWyvernXX++', 'X', 'plus', 'plusMicrosoft', 'Dynamics', 'AXX10xBase++', 'xBase', 'plus', 'plusXBLXC', 'targets', 'XMOS', 'architecturexHarbourXXojoXOTclXodXPLXPL0XQueryXSBXSharp', 'XSLTXtendYYorickYQLYoixZZ', 'notationZ', 'shellZebra,', 'ZPL,', 'ZPL2ZenoZetaLispZigZOPLZPLZ++']
    list = name+address+text+text2

    return list
  
@app.route('/')
def index():
    form = SearchForm(request.form)
    return render_template('index.html', form=form)

@app.route('/generate_data')
def generate_data():
    list = FakeAddress()
    list2 = []
    for i in list:
        a = dict(address=i)
        list2.append(a)

    return jsonify(list2)
 
@app.route('/process', methods=['POST'])
def process():
    country = request.form['country']
    if country:
        return jsonify({'query':country})
    return jsonify({'error': 'missing data..'})

if __name__ == '__main__':
    app.run()

