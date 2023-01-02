import pandas as pd
import efinance as ef

zhongzitou = [
    '873122',  # 中纺标
    '000151',  # 中成股份
    '300374',  # 中铁装配
    '002116',  # 中国海诚
    '603860',  # 中公高科
    '000736',  # 中交地产
    '600138',  # 中青旅
    '301215',  # 中汽股份
    '600730',  # 中国高科
    '300847',  # 中船汉光
    '301175',  # 中科环保
    '300678',  # 中科信息
    '688119',  # 中钢洛耐
    '601858',  # 中国科传
    '600056',  # 中国医药
    '000798',  # 中水渔业
    '600339',  # 中油工程
    '002423',  # 中粮资本
    '301058',  # 中粮科工
    '688297',  # 中无人机
    '600328',  # 中盐化工
    '300140',  # 中环装备
    '600916',  # 中国黄金
    '000970',  # 中科三环
    '600158',  # 中体产业
    '002057',  # 中钢天源
    '600705',  # 中航产融
    '000617',  # 中油资本
    '600536',  # 中国软件
    '000928',  # 中钢国际
    '003009',  # 中天火箭
    '000831',  # 中国稀土
    '603126',  # 中材节能
    '601186',  # 中国铁建
    '600938',  # 中国海油
    '001213',  # 中铁特货
    '600026',  # 中远海能
    '002401',  # 中远海科
    '300788',  # 中信出版
    '600977',  # 中国电影
    '600050',  # 中国联通
    '601600',  # 中国铝业
    '601868',  # 中国能建
    '600088',  # 中视传媒
    '000519',  # 中兵红箭
    '600428',  # 中远海特
    '600941',  # 中国移动
    '688295',  # 中复神鹰
    '000777',  # 中核科技
    '000927',  # 中国铁物
    '601949',  # 中国出版
    '601068',  # 中铝国际
    '000099',  # 中信海直
    '000066',  # 中国长城
    '000881',  # 中广核技
    '300962',  # 中金辐照
    '300425',  # 中建环能
    '000758',  # 中色股份
    '601117',  # 中国化学
    '002051',  # 中工国际
    '688128',  # 中国电研
    '601669',  # 中国电建
    '002189',  # 中光学
    '600150',  # 中国船舶
    '600787',  # 中储股份
    '601800',  # 中国交建
    '601390',  # 中国中铁
    '688009',  # 中国通号
    '603927',  # 中科软
    '000657',  # 中钨高新
    '600765',  # 中航重机
    '600072',  # 中船科技
    '601728',  # 中国电信
    '688568',  # 中科星图
    '000930',  # 中粮科技
    '300527',  # 中船应急
    '600038',  # 中直股份
    '600195',  # 中牧股份
    '600528',  # 中铁工业
    '600500',  # 中化国际
    '600737',  # 中粮糖业
    '600970',  # 中材国际
    '600007',  # 中国国贸
    '601618',  # 中国中冶
    '600118',  # 中国卫星
    '601919',  # 中远海控
    '002013',  # 中航机电
    '601611',  # 中国核建
    '603019',  # 中科曙光
    '003031',  # 中瓷电子
    '601888',  # 中国中免
    '601598',  # 中国外运
    '600176',  # 中国巨石
    '600685',  # 中船防务
    '600760',  # 中航沈飞
    '000768',  # 中航西飞
    '601866',  # 中远海发
    '002080',  # 中材科技
    '000717',  # 中南股份
    '601668',  # 中国建筑

]

laolongtou = [
    '000948',  # 南天信息
    '002603',  # 以岭药业
    '001338',  # 永顺泰
    '002528',  # 英飞拓
    '002077',  # 大港股份
    '000721',  # 西安饮食
    '603029',  # 天鹅股份
    '000617',  # 中油资本
    '000736',  # 中交地产
    '002150',  # 通润装备
    '000815',  # 美利云
    '600050',  # 中国联通
    '002728',  # 特一药业
    '000032',  # 深桑达Ａ
    '002317',  # 众生药业
    '003005',  # 竞业达
    '002093',  # 国脉科技
    '601800',  # 中国交建
    '003023',  # 彩虹集团
    '600536',  # 中国软件
]

position = [
    '512660',  # 军工ETF
    '600941',  # 中国移动
    '002657',  # 中科金财
    '159841',  # 证券ETF
    '600056',  # 中国医药
    '603650',  # 彤程新材
    '000888',  # 峨眉山Ａ
    '002728',  # 特一药业
    '003023',  # 彩虹集团
    '300847',  # 中船汉光
]
etf = ['510050',  # 上证50ETF
       '588090',  # 科创板ETF
       '510060',  # 央企ETF
       '512880',  # 证券ETF
       '512660',  # 军工ETF
       '512480',  # 半导体ETF
       '516160',  # 新能源ETF
       '561910',  # 电池ETF
       '159857',  # 光伏ETF
       '512010',  # 医药ETF
       '512690',  # 酒ETF
       '516110',  # 汽车ETF
       '562510',  # 旅游ETF
       '159915',  # 创业板ETF
       '159959',  # 央企ETF
       '159841',  # 证券ETF
       '159875',  # 新能源ETF
       '159755',  # 电池ETF
       '159929',  # 医药ETF
       '513550',  # 港股通50ETF
       '513090',  # 香港证券ETF
       '513700',  # 香港医药ETF
       '517200',  # 互联网ETF
       '513590',  # 香港消费ETF
       '511380',  # 可转债ETF
       '159636',  # 港股通科技30ETF
       '159776',  # 港股通医药ETF
       '159607',  # 中概互联网ETF
       '159985',  # 豆粕ETF
       '159735',  # 港股消费ETF
       '159615',  # 生物科技ETF港股
       '513600',  # 恒生指数ETF
       '513050',  # 中概互联网ETF
       '159792',  # 港股通互联网ETF
       '513330',  # 恒生互联网ETF

       ]

us_stock = [
'TCOA_WS',#Trajectory Alpha Acquisition Co
'SPKBW',#Silver Spike Acquisition Corp I
'MLAIW',#McLaren Technology Acquisition
'DRAYW',#Macondray Capital Acquisition C
'ALORW',#ALSP Orchid Acquisition Corp I
'POWRW',#Powered Brands Wt
'MURFW',#Murphy Canyon Acquisition Corp
'XPON',#Expion360 Inc
'CCVI_WS',#Churchill Capital Corp VI Wt
'VBOCW',#Viscogliosi Brothers Acquisitio
'SWVLW',#Swvl Holdings Corp Wt
'PLMIW',#Plum Acquisition Corp I Wt
'PDOT_WS',#Peridot Acquisition Corp II Wt
'OPAD_WS',#Offerpad Solutions Inc Wt
'LVRAW',#Levere Holdings Corp Wt
'LIBYW',#Liberty Resources Acquisition C
'KERNW',#Akerna Corp Wt
'IVCAW',#Investcorp India Acquisition Co
'IRNT_WS',#IronNet Inc Wt
'CXAC_WS',#C5 Acquisition Corp Wt
'BSAQ_WS',#黑桃亚洲(权证)
'BRKHW',#BurTech Acquisition Corp Wt
'BBLGW',#Bone Biologics Corp Wt
'ARRWW',#Arrowroot Acquisition Corp Wt
'APGB_WS',#Apollo Strategic Growth Capital
'ACBAW',#Ace Global Business Acquisition
'RENEW',#Cartesian Growth Corp II Wt
'LCAHW',#Landcadia Holdings IV Inc Wt
'XPAXW',#XPAC Acquisition Corp Wt
'BLNGW',#Belong Acquisition Corp Wt
'ARIZR',#Arisz Acquisition Corp Rt
'RAMMW',#Aries I Acquisition Corp Wt
'CITEW',#Cartica Acquisition Corp Wt
'CIFRW',#Cipher Mining Inc Wt
'UPH_WS',#UpHealth Inc Wt
'SWSSW',#Springwater Special Situations
'SHFSW',#SHF Holdings Inc Wt
'NVSAW',#New Vista Acquisition Corp Wt
'KTTAW',#Pasithea Therapeutics Corp Wt
'KALWW',#Kalera plc Wt
'JSPRW',#Jasper Therapeutics Inc Wt
'GAMCW',#Golden Arrow Merger Corp Wt
'FTPAW',#FTAC Parnassus Acquisition Corp
'BRDS_WS',#Bird Global Inc Wt
'BNIXW',#Bannix Acquisition Corp Wt
'BBAI_WS',#BigBear.ai Holdings Inc Wt
'APACW',#StoneBridge Acquisition Corp Wt
'APE',#AMC院线(优先股)
'WAVD',#WaveDancer Inc
'IMBIL',#iMedia Brands Inc Note
'PFDRW',#Pathfinder Acquisition Corp Wt
'HUDAR',#Hudson Acquisition I Corp Rt
'COEPW',#Coeptis Therapeutics Holdings I
'SOUNW',#SoundHound AI Inc Wt
'ELYS',#Elys Game Technology Corp
'JFBRW',#Jeffs’ Brands Ltd Wt
'MTACW',#MedTech Acquisition Corp Wt
'LTCHW',#Latch Inc Wt
'LIDRW',#AEye Inc Wt
'HLGN_WS',#Heliogen Inc Wt
'CNDB_WS',#Concord Acquisition Corp III Wt
'BREZR',#Breeze Holdings Acquisition Cor
'CETXP',#Cemtrex Inc Series 1 Pfd
'HSCSW',#Heart Test Laboratories Inc Wt
'PHGE_U',#BiomX Inc Unit Cons of 1 Sh + 1
'ZEV_WS',#Lightning eMotors Inc Wt
'RMGCW',#RMG Acquisition Corp III Wt
'RGTIW',#Rigetti Computing Inc Wt
'FHLTW',#Future Health ESG Corp Wt
'DAVEW',#Dave Inc Wt
'BYTSW',#BYTE Acquisition Corp Wt
'BWCAW',#Blue Whale Acquisition Corp I W
'BOAC_WS',#Bluescape Opportunities Acquisi
'ADVWW',#Advantage Solutions Inc Wt
'MGAM',#Mobile Global Esports Inc
'ARBK',#Argo Blockchain Plc ADR
'RNERW',#Mount Rainier Acquisition Corp
'OCX',#Oncocyte Corp
'LUCYW',#Innovative Eyewear Inc Wt-A
'VLTA_WS',#Volta Inc Wt
'CCV_WS',#Churchill Capital Corp V Wt
'BFAC_WS',#Battery Future Acquisition Corp
'UTAAW',#UTA Acquisition Corp Wt
'MKFG_WS',#Markforged Holding Corp Wt
'NH',#NantHealth Inc
'ZFOXW',#ZeroFox Holdings Inc Wt
'AUROW',#Aurora Innovation Inc Wt
'IMBI',#iMedia Brands Inc
'APTX',#Aptinyx Inc
'ROSS_WS',#Ross Acquisition Corp II Wt
'RELIW',#Reliance Global Group Inc Wt-A
'RBT_WS',#Rubicon Technologies Inc Wt
'PPHPW',#PHP Ventures Acquisition Corp W
'MEACW',#Mercury Ecommerce Acquisition C
'HYMCL',#Hycroft Mining Holding Corp Wt
'CFFEW',#CF Acquisition Corp VIII Wt
'AVACW',#Avalon Acquisition Inc Wt
'FLJ',#FLJ Group Ltd ADR
'WULF',#TeraWulf Inc
'FRXB_WS',#Forest Road Acquisition Corp II
'BMTX_WS',#BM Technologies Inc Wt
'VORBW',#Virgin Orbit Holdings Inc Wt
'PRDS',#Pardes Biosciences Inc
'TGR_WS',#Kimbell Tiger Acquisition Corp
'CORZ',#Core Scientific Inc
'CCM',#泰和诚医疗
'DBVT',#DBV Technologies SA ADR
'ALVOW',#Alvotech Wt
'DS_B',#Drive Shack Inc Series B Pfd
'OTLK',#Outlook Therapeutics Inc
'MTR',#Mesa Royalty Trust
'SES_WS',#SES AI Corp Wt
'ARBEW',#Arbe Robotics Ltd Wt
'ORIC',#Oric Pharmaceuticals Inc
'WHLRD',#Wheeler Real Estate Investment
'DCRDW',#Decarbonization Plus Acquisitio
'VISL',#Vislink技术
'SKGRW',#SK Growth Opportunities Corp Wt
'NETC_WS',#Nabors Energy Transition Corp W
'MNTSW',#Momentus Inc Wt
'LOCL_WS',#Local Bounti Corpo Wt
'IVCBW',#Investcorp Europe Acquisition C
'EBACW',#European Biotech Acquisition Co
'DNZ_WS',#D and Z Media Acquisition Corp
'CPTNW',#Cepton Inc Wt
'FREQ',#Frequency Therapeutics Inc
'SLNHP',#Soluna Holdings Inc Series A Pf
'TSP',#图森未来
'ROCGW',#Roth CH Acquisition IV Co Wt
'AREB',#American Rebel Holdings Inc
'IMRN',#免疫子制药
'SISI',#尚高生命科学
'HPKEW',#HighPeak Energy Inc Wt
'CLINR',#Clean Earth Acquisitions Corp R
'GLBLW',#Cartesian Growth Corp Wt
'ORIAW',#Orion Biotech Opportunities Cor
'HYZNW',#Hyzon Motors Inc Wt
'CONXW',#CONX Corp Wt
'AQMS',#Aqua Metals Inc
'REKR',#Rekor Systems Inc
'VLN_WS',#Valens Semiconductor Ltd Wt
'BAOS',#宝盛
'ACON',#Aclarion Inc
'DS_C',#Drive Shack Inc Series C Pfd
'JSPR',#Jasper Therapeutics Inc-A
'ANVS',#Annovis Bio Inc
'VIEWW',#View Inc Wt
'OTRKP',#Ontrak Inc Series A Pfd
'MSDAW',#MSD Acquisition Corp Wt
'MPACW',#Model Performance Acquisition C
'HYMCW',#Hycroft Mining Holding Corp Wt
'GWIIW',#Good Works II Acquisition Corp
'FURY',#Fury Gold Mines Ltd
'BKKT_WS',#Bakkt Holdings Inc Wt
'ASNS',#Actelis Networks Inc
'AGBAW',#AGBA Group Holding Ltd Wt
'ISO',#IsoPlexis Corp
'LGVN',#Longeveron Inc-A
'ADERW',#26 Capital Acquisition Corp Wt
'EVLVW',#Evolv Technologies Holdings Inc
'AMCIW',#AMCI Acquisition Corp II Wt
'MSOX',#AdvisorShares MSOS 2x Daily ETF
'HNRG',#Hallador Energy Co
'QBTS_WS',#D-Wave Quantum Inc Wt
'DAVE',#Dave Inc-A
'BTWNW',#Bridgetown Holdings Ltd Wt
'BSGAR',#Blue Safari Group Acquisition C
'AFTR_WS',#AfterNext HealthTech Acquisitio
'SRZN',#Surrozen Inc
'ENSV',#Enservco Corp
'CVM',#CEL-SCI Corp
'LGMK',#LogicMark Inc
'DTRTW',#DTRT Health Acquisition Corp Wt
'PHCF',#普惠财富
'WESTW',#Westrock Coffee Co Wt
'XLO',#Xilio Therapeutics Inc
'HLGN',#Heliogen Inc
'ZIVO',#Zivo Bioscience Inc
'NFNT_WS',#Infinite Acquisition Corp Wt
'ISPOW',#Inspirato Inc Wt
'BWACW',#Better World Acquisition Corp W
'APCA_WS',#AP收购(权证)
'AHRNW',#Ahren Acquisition Corp Wt
'ADCT',#ADC Therapeutics SA
'AMV',#Atlis Motor Vehicles Inc-A
'BMTX',#BM Technologies Inc
'NOTV',#Inotiv Inc
'CACO',#Caravelle International Group
'NINE',#Nine Energy Service Inc
'KA',#Kineta Inc
'VIVE',#Viveve Medical Inc
'OSA',#ProSomnus Inc
'WKSPW',#Worksport Ltd Wt
'LEV_WS',#The Lion Electric Co Wt
'DRCTW',#Direct Digital Holdings Inc Wt
'KCGI_WS',#Kensington Capital Acquisition
'BANFP',#BancFirst Corp Pfd
'NVCN',#Neovasc Inc
'CNTG',#Centogene NV
'LITM',#Snow Lake Resources Ltd
'GVP',#GSE Systems Inc
'EDSA',#Edesa Biotech Inc
'LASE',#Laser Photonics Corp
'ICVX',#Icosavax Inc
'TBLTW',#ToughBuilt Industries Inc Wt-A
'SNPX',#Synaptogenix Inc
'MCAER',#Mountain Crest Acquisition Corp
'CELUW',#Celularity Inc Wt
'AVCTW',#American Virtual Cloud Technolo
'RMED',#Ra Medical Systems Inc
'COEP',#Coeptis Therapeutics Holdings I
'ANTX',#AN2 Therapeutics Inc
'SEED',#奥瑞金种业
'VEV',#Vicinity Motor Corp
'NXLIW',#Nexalin Technology Inc Wt
'FNGR',#FingerMotion Inc
'OKYO',#OKYO Pharma Ltd ADR
'WETG',#悦商集团
'LVO',#LiveOne Inc
'MINDP',#MIND Technology Inc Series A Pf
'GPRK',#GeoPark Ltd
'VINC',#Vincerx Pharma Inc
'TDW_WS_B',#Tidewater Inc Wt_B
'VLD_WS',#Velo3D Inc Wt
'MCACR',#Monterey Capital Acquisition Co
'LVOXW',#LiveVox Holdings Inc Wt
'FRBNW',#Forbion European Acquisition Co
'EUDAW',#EUDA Health Holdings Ltd Wt
'DCFCW',#Tritium DCFC Ltd Wt
'CETX',#Cemtrex Inc
'BCEL',#Atreca Inc-A
'VIGL',#Vigil Neuroscience Inc
'NRGU',#MicroSectors U.S. Big Oil Index
'DRTT',#DIRTT Environmental Solutions L
'DLPN',#Dolphin Entertainment Inc
'AMPX',#Amprius Technologies Inc
'NISN',#宁圣国际
'RNWWW',#ReNew Energy Global plc Wt
'CJJD',#九洲大药房
'PGY',#Pagaya Technologies Ltd-A
'VALU',#Value Line Inc
'ARBKL',#Argo Blockchain Plc Notes
'SBET',#SharpLink Gaming Ltd
'MHLA',#Maiden Holdings Ltd Notes
'FLNT',#Fluent Inc
'ICLK',#爱点击
'FZT_WS',#FAST Acquisition Corp II Wt
'APM',#知临集团
'OUST_WS',#Ouster Inc Wt
'LSEAW',#Landsea Homes Corp Wt
'HGEN',#Humanigen Inc
'RENT',#Rent the Runway Inc-A
'YTEN',#Yield10 Bioscience Inc
'GLBZ',#格伦伯尼万通金控
'OILU',#MicroSectors Oil & Gas Exp. & P
'WDH',#水滴
'CDTX',#Cidara Therapeutics Inc
'BEEMW',#Beam Global Wt
'SURF',#Surface Oncology Inc
'SST_WS',#System1 Inc Wt
'FREEW',#Whole Earth Brands Inc Wt
'AUD',#Audacy Inc
'KLXE',#KLX Energy Services Holdings In
'PMTS',#CPI Card Group Inc
'ACOR',#阿索尔达治疗
'IFRX',#InflaRx NV
'WHLRP',#Wheeler Real Estate Investment
'CBAY',#CymaBay Therapeutics Inc
'UAVS',#AgEagle天线系统
'LXEH',#丽翔教育
'PROF',#Profound Medical Corp
'ANGI',#Angi Inc-A
'BPT',#BPT信托
'CYT',#Cyteir Therapeutics Inc
'GB',#Global Blue Group Holding AG
'AEHL',#羚羊控股
'NMTC',#NeuroOne Medical Technologies C
'GOSS',#Gossamer Bio Inc
'BYFC',#百老汇金融
'PCCT',#Perception Capital Corp II-A
'VERB',#Verb Technology Co Inc
'SWVL',#Swvl Holdings Corp-A
'NXPLW',#NextPlat Corp Wt
'IINNW',#Inspira Technologies Oxy B.H.N.
'IINN',#Inspira Technologies Oxy B.H.N.
'NEXA',#Nexa Resources SA
'TDW_WS',#Tidewater Inc Wt
'WHLR',#Wheeler Real Estate Investment
'CTM',#Castellum Inc
'SBOW',#SilverBow Resources Inc
'TOI',#The Oncology Institute Inc
'IPA',#Immunoprecise Antibodies Ltd
'ASTLW',#Algoma Steel Group Inc Wt
'NVIV',#InVivo Therapeutics Holdings Co
'SMID',#Smith-Midland Corp
'AKLI',#Akili Inc
'IPX',#IperionX Ltd ADR
'PBT',#帕米亚盆地皇室信托
'TOIIW',#The Oncology Institute Inc Wt
'NCPLW',#Netcapital Inc Wt
'GREEL',#Greenidge Generation Holdings I
'ALXO',#ALX Oncology Holdings Inc
'INTR',#Inter & Co Inc-A
'SZZLW',#Sizzle Acquisition Corp Wt
'FRZA',#Forza X1 Inc
'CRMT',#美国汽车行
'NEPT',#海王星科技
'LIDR',#AEye Inc-A
'IPDN',#Professional Diversity Network
'PLAG',#美国绿星球
'MSOS',#AdvisorShares Pure US Cannabis
'WORX',#SCWorx Corp
'MJXL',#ETFMG 2X Daily Alternative Harv
'AZYO',#Aziyo Biologics Inc-A
'PRPO',#Precipio Inc
'CYCN',#Cyclerion Therapeutics Inc
'ACDC',#ProFrac Holding Corp-A
'AMPY',#Amplify Energy Corp
'VIST',#Vista Energy SAB de CV ADR
'CAAS',#中汽系统
'GUSH',#二倍做多每日标普油气出口与生产
'AUMN',#黄金矿业
'WEST',#Westrock Coffee Co
'SI_A',#Silvergate Capital Corp Series
'GRABW',#Grab Holdings Ltd Wt
'SGA',#Saga Communications Inc-A
'ONG',#Direxion Daily Oil Services Bul
'VWEWW',#Vintage Wine Estates Inc Wt
'GMGI',#Golden Matrix Group Inc
'CODI',#Compass Group Diversified Holdi
'AGIL',#AgileThought Inc-A
'CDZI',#加的斯
'GOGO',#Gogo Inc
'VOC',#VOC Energy Trust
'HYPR',#Hyperfine Inc-A
'VERO',#Venus Concept Inc
'TMPO',#Tempo Automation Holdings Inc
'TMKRW',#Tastemaker Acquisition Corp Wt
'RKLY',#Rockley Photonics Holdings Ltd
'PIIIW',#P3 Health Partners Inc Wt
'LAB',#Standard BioTools Inc
'GB_WS',#Global Blue Group Holding AG Wt
'CELGr',#Celgene Corp CVR
'LABD',#三倍做空生物技术ETF-Direxion
'DYAI',#Dyadic International Inc
'XPL',#Solitario Zinc Corp
'CRT',#CRT信托
'TOP',#中阳金融集团
'OPAD',#Offerpad Solutions Inc-A
'GWAV',#Greenwave Technology Solutions
'VAL_WS',#Valaris Ltd Wt
'RIGL',#Rigel Pharmaceuticals Inc
'NBR',#纳伯斯工业
'SOND',#Sonder Holdings Inc
'FATH',#Fathom Digital Manufacturing Co
'USAS',#Americas Gold and Silver Corp
'NCTY',#第九城市
'DNAY',#Codex DNA Inc
'SNFCA',#Security National Financial Cor
'GRAB',#Grab Holdings Ltd-A
'OPHC',#合宜银行控股
'GLP',#全球合伙
'SRGA',#Surgalign Holdings Inc
'HOWL',#Werewolf Therapeutics Inc
'GANX',#Gain Therapeutics Inc
'CRCT',#Cricut Inc-A
'BIG',#必乐透
'BORR',#Borr Drilling Ltd
'SVT',#Servotronics Inc
'USEA',#United Maritime Corp
'SYTA',#Siyata Mobile Inc
'SFT',#Shift Technologies Inc-A
'PASG',#Passage BIO Inc
'NWTNW',#NWTN Inc Wt
'NAMSW',#NewAmsterdam Pharma Co NV Wt
'LBBBR',#Lakeshore Acquisition II Corp R
'BLDEW',#Blade Air Mobility Inc Wt
'BIOR',#Biora Therapeutics Inc
'AZUL',#Azul SA ADR
'TDW',#潮水海运
'MEXX',#Direxion Daily MSCI Mexico Bull
'AREC',#American Resources Corp-A
'QUAD',#Quad/Graphics Inc-A
'RSLS',#ReShape Lifesciences Inc
'ONCT',#Oncternal Therapeutics Inc
'MSPR',#MSP Recovery Inc-A
'BPTH',#Bio-Path Holdings Inc
'TWI',#泰坦国际
'DCTH',#迪卡斯
'FRLN',#Freeline Therapeutics Holdings
'GTX',#Garrett Motion Inc
'AUST',#Austin Gold Corp
'BHVN',#Biohaven Ltd
'TDW_WS_A',#Tidewater Inc Wt-A
'RGTI',#Rigetti Computing Inc
'WEED',#Roundhill Cannabis ETF
'VS',#Versus Systems Inc
'NTZ',#纳图兹家具
'HALL',#标志金融服务
'HLX',#螺旋能源
'REI',#Ring Energy Inc
'ERX',#二倍做多能源ETF-Direxion
'SVIIR',#Spring Valley Acquisition Corp
'AUGX',#Augmedix Inc
'ESTE',#Earthstone Energy Inc-A
'RVSN',#Rail Vision Ltd
'DIG',#二倍做多油气ETF-ProShares
'INZY',#Inozyme Pharma Inc
'DK',#Delek US Holdings Inc
'GNFT',#Genfit SA ADR
'PYR',#PyroGenesis Canada Inc
'IHT',#InnSuites Hospitality Trust
'ABVC',#ABVC BioPharma Inc
'USAU',#美国黄金
'GTXAP',#Garrett Motion Inc Series A Pfd
'MVO',#MV Oil Trust
'PSDN',#AdvisorShares Poseidon Dynamic
'BFIN',#班克金融
'SLNH',#Soluna Holdings Inc
'PRTY',#Party City Holdco Inc
'NESRW',#National Energy Services Reunit
'MDRR',#Medalist Diversified REIT Inc
'ICCM',#IceCure Medical Ltd
'GNS',#Genius Group Ltd
'AVTE',#Aerovate Therapeutics Inc
'TKLF',#Yoshitsu Co Ltd ADR
'EFSH',#1847 Holdings LLC
'GRAY',#Graybug Vision Inc
'PR',#Permian Resources Corp-A
'INDO',#Indonesia Energy Corp Ltd
'CPSS',#Consumer Portfolio Services Inc
'ICAD',#iCAD Inc
'VNOM',#Viper Energy Partners LP
'PRME',#Prime Medicine Inc
'ROCC',#Ranger Oil Corp-A
'RNW',#ReNew Energy Global plc-A
'BRCC',#BRC Inc-A
'WMC',#Western Asset Mortgage Capital
'SBEV_WS',#Splash Beverage Group Inc Wt
'REE',#REE Automotive Ltd-A
'MKFG',#Markforged Holding Corp
'GRNQ',#绿专资本
'UCL',#优克联
'TRVN',#Trevena Inc
'SKIL',#Skillsoft Corp II-A
'DLA',#Delta Apparel Inc
'IMMP',#Immutep Ltd ADR
'PLBY',#PLBY Group Inc
'PYXS',#Pyxis Oncology Inc
'TMQ',#Trilogy Metals Inc
'GNSS',#Genasys Inc
'APA',#阿帕奇石油
'KALA',#卡拉制药
'CELZ',#Creative Medical Technology Hol
'FNA',#Paragon 28 Inc
'DAKT',#达科电子
'DRQ',#德久普
'PBF',#PBF Energy Inc-A
'PBR',#巴西石油
'CVE_WS',#Cenovus Energy Inc Wt
'TEO',#阿根廷电信
'ATIF',#阿提夫控股
'MSC',#新濠影汇
'CVI',#CVR能源
'RONI_WS',#Rice Acquisition Corp II Wt
'QMCO',#昆腾
'METX',#美联国际教育
'DSS',#DSS Inc
'CLSD',#Clearside Biomedical Inc
'AHPI',#联合保健产品
'LBRT',#Liberty Energy Inc-A
'CPG',#Crescent Point Energy Corp
'BNRG',#Brenmiller Energy Ltd
'INTT',#inTEST Corp
'IRIX',#艾里德克斯
'TALO',#Talos Energy Inc
'CMPR',#Cimpress plc
'USIO',#Usio Inc
'EDTK',#王道科技
'CLRB',#Cellectar Biosciences Inc
'OXY_WS',#西方石油(权证)
'RWLK',#ReWalk Robotics Ltd
'NXL',#Nexalin Technology Inc
'OII',#国际海洋工程
'PPSI',#先驱电气
'PBR_A',#巴西石油-优先股
'LDI',#loanDepot Inc-A
'DRS',#Leonardo DRS Inc
'SNCR',#Synchronoss Technologies Inc
'HIBB',#希贝特
'CIVI',#Civitas Resources Inc
'BOOM',#DMC Global Inc
'HROW',#Harrow Health Inc
'LOVE',#The Lovesac Co
'IREN',#Iris Energy Ltd
'EVLO',#Evelo Biosciences Inc
'NEX',#NexTier Oilfield Solutions Inc
'ATUS',#阿尔蒂斯美国
'VCSA',#Vacasa Inc-A
'SVFD',#Save Foods Inc
'PHGE',#BiomX Inc
'ERYP',#ERYTECH Pharma SA ADR
'DXF',#敦信金融
'CNEY',#中北能
'AVYA',#Avaya控股
'PTEN',#Patterson-UTI Energy Inc
'NKLA',#Nikola Corp
'DXLG',#Destination XL Group Inc
'AZ',#A2Z Smart Technologies Corp
'PLCE',#The Children's Place Inc
'QRTEA',#Qurate Retail Inc-A
'BLZE',#Backblaze Inc-A
'ZIMV',#ZimVie Inc
'CMPO',#CompoSecure Inc-A
'CEPU',#Central Puerto SA ADR
'KMX',#车美仕
'RHE',#Regional Health Properties Inc
'IKNA',#Ikena Oncology Inc
'AGAE',#Allied Gaming & Entertainment I
'CACC',#Credit Acceptance Corp
'CVEO',#Civeo Corp
'ERF',#艾诺加能源
'INVO',#INVO BioScience Inc
'DOMA',#Doma Holdings Inc
'TELZ',#Tellurian Inc Notes
'ANEB',#Anebulo Pharmaceuticals Inc
'PCTTW',#PureCycle Technologies Inc Wt
'EKSO',#Ekso Bionics Holdings Inc
'PGM',#iPath Series B Bloomberg Platin
'GMBLP',#Esports Entertainment Group Inc
'PET',#Wag! Group Co
'TA',#TravelCenters of America Inc
'MOGU',#蘑菇街
'MDWD',#MediWound Ltd
'BGI',#Birks Group Inc-A
'CHRD',#Chord Energy Corp
'TOVX',#Theriva Biologics Inc
'LTRY',#Lottery.com Inc
'IMCC',#IM Cannabis Corp
'EOSEW',#Eos Energy Enterprises Inc Wt
'EFTR',#eFFECTOR Therapeutics Inc
'DUOT',#Duos Technologies Group Inc
'HP',#赫尔默里奇&佩恩
'NOG',#Northern Oil and Gas Inc
'NRP',#Natural Resource Partners LP
'GLSI',#Greenwich LifeSciences Inc
'OBE',#Obsidian Energy Ltd
'BGS',#B&G食品
'AFIB',#Acutus Medical Inc
'KLTR',#Kaltura Inc
'GOL',#勒莫国航
'CLIR',#ClearSign Technologies Corp
'VALN',#Valneva SE ADR
'IE',#Ivanhoe Electric Inc
'AKBA',#Akebia Therapeutics Inc
'MJUS',#ETFMG U.S. Alternative Harvest
'XPOF',#Xponential Fitness Inc-A
'SUPV',#Grupo Supervielle SA ADR
'MIMO',#Airspan Networks Holdings Inc
'PSNL',#Personalis Inc
'PAR',#PAR Technology Corp
'TC',#团车
'EC',#哥伦比亚国家石油
'RPHM',#Reneo Pharmaceuticals Inc
'ACCD',#Accolade Inc
'THM',#International Tower Hill Mines
'STSA',#Satsuma Pharmaceuticals Inc
'PRAX',#Praxis Precision Medicines Inc
'NBSE',#NeuBase Therapeutics Inc
'DHC',#Diversified Healthcare Trust
'RYAM',#Rayonier Advanced Materials Inc
'ASTS',#AST SpaceMobile Inc-A
'TELA',#TELA Bio Inc
'NVCT',#Nuvectis Pharma Inc
'MESA',#Mesa Air Group Inc
'HES',#赫斯
'STIX',#Semantix Inc-A
'UCO',#二倍做多原油ETF-ProShares
'RETL',#Direxion Daily Retail Bull 3X S
'TTT',#ProShares UltraPro Short 20 Yea
'PUMP',#ProPetro Holding Corp
'NOTE',#FiscalNote Holdings Inc-A
'GBR',#New Concept Energy Inc
'CNQ',#加拿大自然资源
'PALL',#钯金ETF-ETFS
'ASTR',#Astra Space Inc-A
'HPK',#HighPeak Energy Inc
'CVE',#Cenovus能源
'MGY',#Magnolia Oil & Gas Corp-A
'PLTM',#GraniteShares Platinum Shares E
'SFIX',#Stitch Fix Inc-A
'BEDU',#博实乐
'UGA',#美国汽油基金
'EGY',#瓦可能源
'CSAN',#Cosan SA ADR
'PARR',#Par Pacific Holdings Inc
'VLNS',#The Valens Co Inc
'PLSE',#Pulse Biosciences Inc
'IMTE',#Integrated Media Technology Ltd
'UBR',#ProShares Ultra MSCI Brazil Cap
'TSHA',#Taysha Gene Therapies Inc
'RZLT',#Rezolute Inc
'PW',#Power REIT
'NFGC',#New Found Gold Corp
'BBU',#Brookfield Business Partners LP
'PPLT',#铂金ETF-ETFS
'OMAB',#墨西哥北方中心机场
'OVV',#Ovintiv Inc
'ORLA',#Orla Mining Ltd
'RIG',#越洋钻探
'UTSI',#UT斯达康
'DMS',#Digital Media Solutions Inc-A
'ENLC',#EnLink Midstream LLC
'VKTX',#Viking Therapeutics Inc
'LGTOW',#Legato Merger Corp II Wt
'XYF',#小赢科技
'DMLP',#多尔切斯特
'PDCE',#PDC Energy Inc
'SLGC',#SomaLogic Inc
'SDRL',#Seadrill Ltd
'VLD',#Velo3D Inc
'SANW',#S&W Seed Co
'TMV',#三倍做空20年+国债ETF-Direxion
'ARCO',#Arcos Dorados Holdings Inc-A
'VRME',#VerifyMe Inc
'CRGY',#Crescent Energy Co-A
'PCYG',#Park City Group Inc
'NXC',#Nuveen California Select Tax-Fr
'PLG',#Platinum Group Metals Ltd
'ACP',#abrdn Income Credit Strategies
'TLIS',#Talis Biomedical Corp
'PYPD',#PolyPid Ltd
'PME',#平潭海洋实业
'NBRV',#Nabriva Therapeutics plc
'III',#信息服务
'GROV',#Grove Collaborative Holdings In
'CLPS',#华钦科技
'ASRT',#Assertio Holdings Inc
'AMPE',#安皮奥制药
'BWBBP',#Bridgewater Bancshares Inc Seri
'SMTI',#Sanara MedTech Inc
'COP',#康菲石油
'PSCE',#Invesco S&P SmallCap Energy ETF
'OCC',#Optical Cable Corp
'PFMT',#Performant Financial Corp
'NETI',#Eneti Inc
'USM',#美国无线电话
'CRK',#康斯托克能源
'CNSP',#CNS Pharmaceuticals Inc
'CPE',#卡隆石油
'CORR',#CorEnergy Infrastructure Trust
'TNGX',#Tango Therapeutics Inc
'BBUC',#Brookfield Business Corp-A
'PVL',#Permianville Royalty Trust
'NTCO',#Natura &Co Holding SA ADR
'AMBP_WS',#Ardagh Metal Packaging SA Wt
'ACXP',#Acurx Pharmaceuticals Inc
'ARIS',#Aris Water Solutions Inc-A
'EBON',#亿邦国际
'AR',#Antero Resources Corp
'JFBR',#Jeffs’ Brands Ltd
'AIH',#医美国际
'ASTL',#Algoma Steel Group Inc
'XELB',#Xcel Brands Inc
'CFMS',#Conformis Inc
'BRFS',#巴西食品
'AGM_E',#Federal Agricultural Mortgage C
'EPM',#Evolution Petroleum Corp
'ALLT',#艾奥特通讯
'THRD',#Third Harmonic Bio Inc
'MTDR',#Matador Resources Co
'CTO_A',#CTO Realty Growth Inc Series A
'XES',#油气设服ETF-SPDR S&P
'IMRA',#IMARA Inc
'VAPO',#Vapotherm Inc
'NOPE',#Noble Absolute Return ETF
'CAAP',#Corporacion America Airports SA
'TCBP',#TC BioPharm (Holdings) plc ADR
'VET',#朱砂能源
'ONFO',#Onfolio Holdings Inc
'OG',#洋葱
'LYLT',#Loyalty Ventures Inc
'IKT',#Inhibikase Therapeutics Inc
'EQRXW',#EQRx Inc Wt
'TTP',#Tortoise Pipeline & Energy Fund
'VTRU',#Vitru Ltd
'HAL',#哈里伯顿
'CRC',#加州资源
'PXD',#先锋自然资源
'SM',#SM Energy Co
'PXE',#Invesco Dynamic Energy Explorat
'TSAT',#Telesat Corp
'OPOF',#Old Point Financial Corp
'KOS',#Kosmos Energy Ltd
'ARDS',#Aridis Pharmaceuticals Inc
'ACP_A',#abrdn Income Credit Strategies
'SCVL',#Shoe Carnival Inc
'ROOT',#Root Inc-A
'TDS',#电话数据系统
'GBTG',#Global Business Travel Group In
'EVTV',#Envirotech Vehicles Inc
'SNES',#SenesTech Inc
'GLNG',#Golar LNG Ltd
'MNRL',#Brigham Minerals Inc-A
'VIRI',#Virios Therapeutics Inc
'QRTEB',#Qurate Retail Inc-B
'MTNB',#Matinas BioPharma Holdings Inc
'LYRA',#Lyra Therapeutics Inc
'JOB',#GEE Group Inc
'IOR',#Income Opportunity Realty Inves
'HYMC',#Hycroft Mining Holding Corp-A
'GRIL',#Muscle Maker Inc
'ELEV',#Elevation Oncology Inc
'WTI',#W&T海底钻探
'DVN',#戴文能源
'ATLCP',#Atlanticus Holdings Corp Series
'SGC',#Superior Group of Companies Inc
'VLO',#瓦莱罗能源
'BBWI',#Bath & Body Works Inc
'GNTA',#Genenta Science SpA ADR
'STR',#Sitio Royalties Corp-A
'CHKEL',#Chesapeake Energy Corp Wt
'DJCO',#每日期刊
'RRC',#山脉资源
'ETD',#伊森艾伦室内装饰
'BRZU',#二倍做多巴西ETF-Direxion
'NA',#豪微
'DTST',#Data Storage Corp
'SCTL',#Societal CDMO Inc
'TTI',#脂鲤技术
'RES',#RPC Inc
'STNE',#StoneCo Ltd-A
'DUO',#房多多
'DTLA_',#Brookfield DTLA Fund Office Tru
'FTXN',#First Trust Nasdaq Oil & Gas ET
'AIU',#Meta Data Ltd ADR
'FNWD',#Finward Bancorp
'PFIX',#Simplify Interest Rate Hedge ET
'TROX',#Tronox Holdings plc
'DEN',#丹博里原油
'VHI',#瓦利化工
'XOP',#油气开采ETF-SPDR S&P
'DO',#戴蒙德海底钻探
'CC',#The Chemours Co
'VVPR',#VivoPower International PLC
'SPRB',#Spruce Biosciences Inc
'OSG',#Overseas Shipholding Group Inc-
'INFI',#Infinity Pharmaceuticals Inc
'DSP',#Viant Technology Inc-A
'SEAS',#海洋世界娱乐
'AUVIP',#Applied UV Inc Series A Pfd
'NML',#Neuberger Berman MLP and Energy
'PK',#Park Hotels & Resorts Inc
'ANF',#阿贝克隆比&费奇
'KSS',#柯尔百货
'CONL',#GraniteShares 1.5x Long COIN Da
'BSM',#Black Stone Minerals LP
'VSCO',#Victoria’s Secret & Co
'MUR',#墨菲石油
'UNIT',#Uniti Group Inc
'ENG',#ENGlobal Corp
'DRUG',#Bright Minds Biosciences Inc
'AHT_I',#Ashford Hospitality Trust Inc S
'CRMD',#CorMedix Inc
'PRT',#PermRock Royalty Trust
'SHFS',#SHF Holdings Inc-A
'LSXMB',#Liberty Media Corp Liberty Siri
'OIH',#油服ETF-VanEck Vectors
'BURL',#伯灵顿百货
'BDSX',#Biodesix Inc
'MEC',#Mayville Engineering Co Inc
'IEO',#iShares U.S. Oil & Gas Explorat
'JWN',#诺德斯特龙
'TRGP',#Targa Resources Corp
'PAGP',#Plains GP Holdings LP-A
'SWN',#西南能源
'CRD_A',#克劳福德-A
'FCG',#天然气ETF-First Trust
'CHK',#切萨皮克能源
'TV',#墨西哥电视
'ZEST',#Ecoark Holdings Inc
'RTL',#The Necessity Retail REIT Inc-A
'RKDA',#阿凯迪亚生物科学
'NOV',#NOV Inc
'NNAVW',#NextNav Inc Wt
'ICMB',#Investcorp Credit Management BD
'GGAL',#加利西亚金融
'XP',#XP Inc-A
'CAR',#安飞士
'WTTR',#Select Energy Services Inc-A
'BCLI',#Brainstorm Cell Therapeutics In
'ASTSW',#AST SpaceMobile Inc Wt
'IEZ',#iShares U.S. Oil Equipment & Se
'SD',#SandRidge Energy Inc
'VTEX',#VTEX-A
'SHIP',#Seanergy Maritime Holdings Corp
'SOI',#Solaris Oilfield Infrastructure
'CIB',#哥伦比亚银行
'DINO',#HF Sinclair Corp
'CMT',#Core Molding Technologies Inc
'PDS',#Precision Drilling Corp
'OIS',#Oil States International Inc
'CWK',#Cushman & Wakefield plc
'CENQU',#CENAQ Energy Corp Unit Cons of
'BHR',#Braemar Hotels & Resorts Inc
'EEIQ',#EpicQuest Education Group Inter
'SU',#森科能源
'VAL',#Valaris Ltd
'PANL',#Pangaea Logistics Solutions Ltd
'NAOV',#NanoVibronix Inc
'INBS',#Intelligent Bio Solutions Inc
'GOEV',#Canoo Inc
'BHIL_WS',#Benson Hill Inc Wt
'ATOS',#Atossa Therapeutics Inc
'BOOT',#Boot Barn Holdings Inc
'BCAN',#BYND Cannasoft Enterprises Inc
'HTZ',#赫兹租车
'DY',#戴康工业
'XXII',#22nd Century Group Inc
'TAIT',#Taitron Components Inc-A
'FUN',#雪松娱乐
'NS',#纽星能源
'TCRT',#Alaunos Therapeutics Inc
'SCWO',#374Water Inc
'HUMAW',#Humacyte Inc Wt
'CLBTW',#Cellebrite DI Ltd Wt
'BXC',#布鲁林克斯
'ZUMZ',#Zumiez Inc
'SGHC',#Super Group (SGHC) Ltd
'JOE',#圣乔
'USDP',#USD Partners LP
'OXY',#西方石油
'XTLB',#Xtl生物制药
'VLN',#Valens Semiconductor Ltd
'PXJ',#Invesco Dynamic Oil & Gas Servi
'ZEUS',#Olympic Steel Inc
'PXI',#Invesco DWA Energy Momentum ETF
'BIRD',#Allbirds Inc-A
'OSTK',#Overstock.com Inc
'EQT',#EQT能源
'DPSI',#DecisionPoint Systems Inc
'GPOR',#格尔夫波特能源
'UUU',#Universal Security Instruments
'ANY',#Sphere 3D Corp
'WOOF',#Petco Health and Wellness Co In
'PEB',#Pebblebrook Hotel Trust
'SILX',#ETFMG Prime 2x Daily Junior Sil
'BGR',#BlackRock Energy and Resources
'ARDX',#Ardelyx Inc
'RYE',#Invesco S&P 500 Equal Weight En
'GMDA',#Gamida Cell Ltd
'PAYX',#沛齐
'EOG',#EOG能源
'ANIX',#Anixa Biosciences Inc
'PIRS',#Pieris Pharmaceuticals Inc
'FPAY',#FlexShopper Inc
'EP',#Empire Petroleum Corp
'CEM',#ClearBridge MLP and Midstream F
'AXR',#安美瑞普
'PSX',#Phillips 66
'GALT',#Galectin Therapeutics Inc
'KNOP',#KNOT Offshore Partners LP
'PHX',#PHX矿物
'LIFE',#aTyr Pharma Inc
'EXPR',#Express Inc
'XOMA',#标记临床研究
'WFRD',#威德福国际
'PRGO',#培瑞克
'RC_C',#Ready Capital Corp Series C Pfd
'BAK',#Braskem SA ADR Pfd
'CCU',#智利CCU
'WLMS',#Williams Industrial Services Gr
'VANI',#Vivani Medical Inc
'NRXPW',#NRX Pharmaceuticals Inc Wt
'MRM',#MEDIROM Healthcare Technologies
'BATL',#Battalion Oil Corp
'ACR',#ACRES Commercial Realty Corp
'LAD',#利西亚车行
'SPPP',#Sprott Physical Platinum & Pall
'NE',#Noble Corp plc-A
'CDR_B',#Cedar Realty Trust Inc Series B
'TNL',#Travel + Leisure Co
'PAXS',#PIMCO Access Income Fund
'LFVN',#LifeVantage Corp
'BRF',#巴西小型股ETF-VanEck Vectors
'VRM',#Vroom Inc
'ORGNW',#Origin Materials Inc Wt
'GNE',#Genie Energy Ltd-B
'VDE',#能源指数ETF-Vanguard
'COHN',#Cohen & Co Inc
'NEXT',#NextDecade Corp
'VSAT',#卫讯公司
'LOB',#Live Oak Bancshares Inc
'LTRPA',#Liberty TripAdvisor Holdings In
'ICCH',#ICC Holdings Inc
'ASO',#Academy Sports and Outdoors Inc
'FEIM',#高频电子
'UTME',#联代科技
'RRH',#Advocate Rising Rate Hedge ETF
'MSGE',#Madison Square Garden Entertain
'MPACR',#Model Performance Acquisition C
'CING',#Cingulate Inc
'AWH',#Aspira Women’s Health Inc
'UTSL',#Direxion Daily Utilities Bull 3
'FENY',#Fidelity MSCI Energy Index ETF
'LXU',#LSB Industries Inc
'ASPI',#ASP Isotopes Inc
'NDLS',#Noodles & Co
'SBS',#Companhia de Saneamento Basico
'XLE',#能源ETF-SPDR
'RNGR',#Ranger Energy Services Inc-A
'GHRS',#GH Research PLC
'TCI',#Transcontinental Realty Investo
'PAA',#Plains All American Pipeline LP
'KNTK',#Kinetik Holdings Inc-A
'HTOOW',#Fusion Fuel Green PLC Wt
'IMV',#IMV Inc
'EVOK',#Evoke Pharma Inc
'CGBD',#Carlyle Secured Lending Inc
'REPX',#Riley Exploration Permian Inc
'PCG_G',#Pacific Gas and Electric Co Pfd
'BCX',#BlackRock Resources & Commoditi
'FXN',#First Trust Energy AlphaDEX Fun
'TGS',#Transportadora de Gas del Sur S
'FANG',#Diamondback Energy Inc
'TNP',#Tsakos Energy Navigation Ltd
'WES',#Western Midstream Partners LP
'KMF',#Kayne Anderson Midstream/Energy
'IMO',#帝国石油
'SLB',#斯伦贝谢
'MDWT',#Midwest Holding Inc
'ETRN',#Equitrans Midstream Corp
'MPC',#马拉松原油
'FTEK',#燃料技术
'CHTR',#特许通讯
'ACIW',#ACI环球
'SOUN',#SoundHound AI Inc-A
'DBTX',#Decibel Therapeutics Inc
'CDZIP',#Cadiz Inc Series A Pfd
'TRMD',#TORM plc-A
'CVX',#雪佛龙
'SCLX',#Scilex Holding Co
'CMPOW',#CompoSecure Inc Wt
'TBT',#二倍做空20年+国债ETF-ProShares
'SQFT',#Presidio Property Trust Inc-A
'HUN',#亨斯曼材料
'BRFH',#Barfresh Food Group Inc
'BIS',#二倍做空NASDAQ生物技术ProShares
'RICK',#RCI Hospitality Holdings Inc
'FPL',#First Trust New Opportunities M
'HGBL',#Heritage Global Inc
'PHG',#飞利浦
'HBI',#哈尼斯品牌服装
'CHB',#Global X China Biotech Innovati
'IYE',#iShares U.S. Energy ETF
'STCN',#Steel Connect Inc
'IVVD',#Invivyd
'FRG',#Franchise Group Inc
'CHX',#ChampionX Corp
'QUIK',#快辑半导体
'MDV',#Modiv Inc-C
'MG',#Mistras Group Inc
'KSCP',#Knightscope Inc-A
'AENZ',#Aenza SAA ADR
'CURO',#Curo集团控股
'SANG',#Sangoma Technologies Corp
'BW',#Babcock & Wilcox
'FLYU',#MicroSectors Travel 3X Leverage
'PAGS',#PagSeguro Digital Ltd-A
'HHC',#The Howard Hughes Corp
'TRVG',#trivago NV ADR
'ATCO_I',#Atlas Corp Series I Pfd
'MAA_I',#MAA房产信托(优先股)
'EPIX',#ESSA Pharma Inc
'CWH',#露营世界控股
'KYN',#Kayne Anderson MLP/Midstream In
'DLTH',#Duluth Holdings Inc-B
'NOVN',#Novan Inc
'BNO',#美国布伦特原油基金
'CNX',#康索尔能源
'EMO',#ClearBridge Energy Midstream Op
'EWZS',#巴西小型股ETF-iShares MSCI
'TRX',#TRX Gold Corp
'PULM',#Pulmatrix Inc
'PIK',#Kidpik Corp
'CDAK',#Codiak BioSciences Inc
'TITN',#Titan Machinery Inc
'DWMC',#AdvisorShares Dorsey Wright Mic
'TS',#泰纳瑞斯钢铁
'ASPN',#Aspen Aerogels Inc
'BMA',#Banco Macro SA ADR
'DRLL',#Strive U.S. Energy ETF
'SLNG',#Stabilis Solutions Inc
'BKTI',#BK Technologies Corp
'EPR_C',#EPR Properties Series C Pfd
'LAKE',#雷克兰工业
'EVI',#EnviroStar Inc
'CIG',#Cemig ADR Pfd
'GFF',#格里丰
'MBI',#MBIA Inc
'QTT',#趣头条
'MTEM',#Molecular Templates Inc
'EOSE',#Eos Energy Enterprises Inc-A
'CHNR',#中国天然资源
'NDP',#Tortoise Energy Independence Fu
'PTGX',#Protagonist Therapeutics Inc
'GEO',#GEO惩教集团
'CMPX',#Compass Therapeutics Inc
'NXE',#NexGen Energy Ltd
'MMP',#麦哲伦油气
'GPRE',#绿色平原能源
'TZOO',#旅行动物园
'WHD',#Cactus Inc-A
'ALIM',#Alimera Sciences Inc
'MAG',#MAG Silver Corp
'STER',#Sterling Check Corp
'BWMN',#Bowman Consulting Group Ltd
'CSPI',#CSP Inc
'PEO',#Adams Natural Resources Fund
'SNBR',#Sleep Number Corp
'ITCB',#Itau Corpbanca ADR
'KRO',#康诺斯全球
'CTRA',#Coterra Energy Inc
'SSL',#南非萨索尔
'NWSA',#新闻集团-A
'OI',#欧文斯伊利诺斯玻璃
'IGE',#iShares North American Natural
'IBCP',#独立银行(密歇根州)
'SLCA',#US Silica Holdings Inc
'SBH',#莎莉美容
'AGYS',#诶吉利斯
'TELL',#Tellurian Inc
'IGT',#国际游戏科技
'BBBY',#3B家居
'HBM',#Hudbay Minerals Inc
'BDCX',#ETRACS Quarterly Pay 1.5x Lever
'ZDGE',#Zedge Inc-B
'WHF',#WhiteHorse Finance Inc
'TKC',#土耳其移动通信
'NAUT',#Nautilus Biotechnology Inc
'APRE',#Aprea Therapeutics Inc
'AIM',#AIM ImmunoTech Inc
'HDSN',#哈德森科技
'MRO',#马拉松石油
'ENIC',#Enel Chile SA ADR
'EE',#Excelerate Energy Inc-A
'UEC',#Uranium Energy Corp
'NGL',#NGL Energy Partners LP
'FORD',#福沃德工业
'EFXT',#Enerflex Ltd
'ARCC',#阿瑞斯资本
'BRTX',#BioRestorative Therapies Inc
'STKS',#The ONE Group Hospitality Inc
'CALA',#Calithera Biosciences Inc
'NMIH',#NMI Holdings Inc-A
'FEI',#First Trust MLP and Energy Inco
'YJ',#云集
'SVRA',#Savara Inc
'CDXC',#ChromaDex Corp
'SATS',#回声星通信
'AM',#Antero Midstream Corp
'UNFI',#联合天然食品
'TLF',#Tandy Leather Factory Inc
'WW',#慧俪轻体
'ECCX',#Eagle Point Credit Co Inc Notes
'CMRE',#Costamare Inc
'AQNU',#Algonquin Power & Utilities Cor
'XPRO',#Expro Group Holdings NV
'CLB',#Core Laboratories NV
'SLS',#SEELAS Life Sciences Group Inc
'OLMA',#Olema Pharmaceuticals Inc
'IOBT',#IO Biotech Inc
'NWS',#新闻集团-B
'DAIO',#Data I/O Corp
'TIGO',#米雷康姆国际通信
'HCKT',#哈克特集团
'VSTA',#Vasta Platform Ltd-A
'SNAX',#Stryve Foods Inc-A
'MBIO',#野马生物
'LIQT',#LiqTech International Inc
'FRGE',#Forge Global Holdings Inc
'EVGN',#Evogene Ltd
'CNSL',#联合通讯
'ADES',#Advanced Emissions Solutions In
'IBKR',#盈透证券
'INNV',#InnovAge Holding Corp
'DSGN',#Design Therapeutics Inc
'NCSM',#NCS Multistage Holdings Inc
'MEG',#Montrose Environmental Group In
'FCEL',#燃料电池能源
'BLBD',#Blue Bird Corp
'GNRC',#Generac Holdings Inc
'DAC',#达那俄斯
'ALVO',#Alvotech
'VAXX',#Vaxxinity Inc-A
'TGB',#Taseko Mines Ltd
'CX',#西麦斯
'DSGR',#Distribution Solutions Group In
'IXC',#全球能源ETF-iShares
'SUN',#Sunoco LP
'SGU',#Star Group LP
'XOM',#埃克森美孚
'ACRV',#Acrivon Therapeutics Inc
'KEP',#韩国电力
'SVIX',#VS Trust -1x Short VIX Futures
'QUBT',#Quantum Computing Inc
'CHNA',#Loncar China BioPharma ETF
'CCEL',#Cryo-Cell International Inc
'YI',#1药网
'TRP',#TC Energy Corp
'FARM',#Farmer Bros Co
'KEX',#卡比海运
'SLNA',#Selina Hospitality Plc
'BKR',#Baker Hughes Co-A
'KTOS',#克瑞拓斯安全防卫
'CMMB',#Chemomab Therapeutics Ltd ADR
'ALGT',#忠实航空
'HUDI',#华迪国际
'COIN',#Coinbase Global Inc-A
'YPF',#阿根廷YPF
'FIVE',#Five Below Inc
'BKE',#巴克尔
'AQN',#Algonquin Power & Utilities Cor
'TGNA',#TEGNA Inc
'DRN',#三倍做多房地产ETF-Direxion
'DSX',#黛安娜船舶
'MUSA',#Murphy USA Inc
'LBRDA',#Liberty Broadband Corp-A
'ZTEK',#Zentek Ltd
'VHC',#VirnetX Holding Corp
'NSTC_U',#Northern Star Investment Corp I
'MHLD',#Maiden Holdings Ltd
'DGHI',#Digihost Technology Inc
'AHG',#Akso Health Group ADR
'GES',#Guess Inc
'IPHA',#Innate Pharma SA ADR
'BKCC',#黑石资本投资
'CIM_C',#Chimera Investment Corp Series
'LBRDK',#Liberty Broadband Corp-C
'LILM',#Lilium NV-A
'GIGM',#和信超媒体
'NRGX',#PIMCO Energy and Tactical Credi
'UE',#Urban Edge Properties
'RLJ',#RLJ住房信托
'RFACU',#RF Acquisition Corp Unit Cons o
'KRP',#Kimbell Royalty Partners LP
'IMPPP',#Imperial Petroleum Inc Series A
'PSNY',#极星汽车
'MCB',#Metropolitan Bank Holding Corp
'NPFD',#Nuveen Variable Rate Preferred
'EQS',#Equus Total Return Inc
'CVRX',#CVRx Inc
'LMST',#Limestone Bancorp Inc
'ELDN',#Eledon Pharmaceuticals Inc
'DBE',#Invesco DB Energy Fund
'DPG',#Duff & Phelps Utility and Infra
'NCA',#Nuveen California Municipal Val
'PIXY',#兼职精灵
'VBIV',#VBI Vaccines Inc
'NXTC',#NextCure Inc
'LABP',#Landos Biopharma Inc
'IVC',#英伐凯
'GDOT',#Green Dot Corp-A
'KSET',#KraneShares Global Carbon Offse
'CHMI',#Cherry Hill Mortgage Investment
'AROC',#Archrock Inc
'KFS',#汇富金融服务
'SMR_WS',#NuScale Power Corp Wt
'MNTK',#Montauk Renewables Inc
'PDLB',#Ponce Financial Group Inc
'MFIC',#MidCap Financial Investment Cor
'SIG',#西格内特珠宝
'AMLP',#Alerian MLP ETF
'GPS',#盖普
'SNDL',#SNDL Inc
'XPEL',#XPEL Inc
'NSTD_U',#Northern Star Investment Corp I
'DBO',#原油ETF-PowerShares
'ZIP',#ZipRecruiter Inc-A
'CALM',#Cal-Maine Foods Inc
'PBI_B',#Pitney Bowes Inc Notes
'OVLY',#橡木谷银行
'PTRS',#Partners Bancorp
'CMCT',#Creative Media & Community Trus
'MPAA',#Motorcar Parts of America Inc
'EGO',#埃尔拉多黄金
'UGP',#Ultrapar Participacoes SA ADR
'DWSN',#道森地探
'CIDM',#Cinedigm Corp-A
'ADAG',#天演药业
'SMHB',#ETRACS Monthly Pay 2x Leveraged
'PETS',#PetMed Express Inc
'SB',#Safe Bulkers Inc
'MARPS',#海洋石油信托
'ARCH',#Arch Resources Inc-A
'UONEK',#Urban One Inc-D
'BRN',#Barnwell Industries Inc
'WDS',#Woodside Energy Group Ltd ADR
'NMG',#Nouveau Monde Graphite Inc
'VTRS',#Viatris Inc
'MLP',#毛伊岛菠萝食品
'HGLB',#Highland Global Allocation Fund
'TCRR',#TCR2 Therapeutics Inc
'ATMP',#iPath Select MLP ETN
'OILK',#ProShares K-1 Free Crude Oil St
'TROO',#盟军集团
'NVGS',#Navigator Holdings Ltd
'NLSP',#NLS Pharmaceutics Ltd
'HSKA',#赫斯卡医疗
'AVNT',#Avient Corp
'SFL',#SFL Corp Ltd
'NVEE',#NV5 Global Inc
'USO',#美国原油基金
'BGSF',#BGSF Inc
'XFOR',#X4制药
'NLTX',#Neoleukin Therapeutics Inc
'MIND',#MIND Technology Inc
'HCI',#HCI集团
'SRV',#The Cushing MLP Total Return Fu
'LYTS',#LSI Industries Inc
'USL',#美国原油基金(近12月合约平均)
'AMJ',#JP Morgan Alerian MLP Index ETN
'HIE',#Miller/Howard High Income Equit
'RM',#Regional Management Corp
'FTI',#TechnipFMC plc
'AMZA',#InfraCap MLP ETF
'AVA',#阿维斯塔
'CHEF',#The Chefs' Warehouse Inc
'NR',#新园能源
'CEIX',#CONSOL Energy Inc
'SPWH',#Sportsman’s Warehouse Holdings
'KFRC',#K力
'XFLT',#XAI Octagon Floating Rate & Alt
'ETON',#Eton Pharmaceuticals Inc
'HESM',#Hess Midstream LP-A
'TCON',#TRACON Pharmaceuticals Inc
'ENZ',#恩佐生化
'DBRG_I',#DigitalBridge Group Inc Series
'USAI',#Pacer American Energy Independe
'RACY',#Relativity Acquisition Corp-A
'PBA',#Pembina Pipeline Corp
'ISPC',#iSpecimen Inc
'AMZU',#Direxion Daily AMZN Bull 1.5X S
'MLPX',#Global X MLP & Energy Infrastru
'BCRX',#BioCryst Pharmaceuticals Inc
'ATEX',#Anterix Inc
'MATX',#美森
'SMLP',#Summit Midstream Partners LP
'GER',#Goldman Sachs MLP and Energy Re
'AGRO',#Adecoagro SA
'RDIB',#Reading International Inc-B
'EBR',#巴西电力ADR
'WMB',#威廉姆斯
'TESS',#特斯科技术
'SND',#Smart Sand Inc
'GPN',#环汇
'BNRE',#Brookfield Reinsurance Ltd-A
'TPB',#Turning Point Brands Inc
'NHTC',#然健环球
'BRY',#Berry Corp (bry)
'GRRR',#大猩猩科技
'NBCM',#Neuberger Berman Commodity Stra
'LNG',#Cheniere Energy Inc
'UMI',#USCF Midstream Energy Income Fu
'USAC',#USA Compression Partners LP
'LD',#铅ETN-iPath
'DDS',#狄乐百货
'DXPE',#DXP Enterprises Inc
'HSII',#海德思哲
'GSL',#环球租船
'IPAR',#依特香水
'UPW',#ProShares Ultra Utilities
'BALY',#Bally's Corp
'POWL',#Powell Industries Inc
'VBNK',#VersaBank
'FMX',#Fomento Económico Mexicano SAB
'INN',#Summit Hotel Properties Inc
'DISH',#DISH Network Corp-A
'AVD',#美国先锋
'OKE',#欧尼克
'EXPE',#亿客行
'NTG',#Tortoise Midstream Energy Fund
'ILF',#拉美40ETF-iShares
'KMI',#金德摩根
'JUN_U',#Juniper II Corp Unit Cons of 1
'RMAX',#RE/MAX Holdings Inc-A
'MLPA',#Global X MLP ETF
'BRLT',#Brilliant Earth Group Inc-A
'ISDR',#Issuer Direct Corp
'PAYA',#Paya Holdings Inc
'FSK',#FS KKR Capital Corp
'MATV',#Mativ Inc
'EWW',#墨西哥ETF-iShares MSCI
'UMDD',#UltraPro MidCap400
'FLBR',#Franklin FTSE Brazil ETF
'TFINP',#Triumph Financial Inc Series C
'FREE',#Whole Earth Brands Inc
'SAR',#Saratoga Investment Corp
'FMS',#费森尤斯医疗
'MSGS',#麦迪逊广场花园体育
'BOWL',#Bowlero Corp-A
'PEB_G',#Pebblebrook Hotel Trust Series
'KFY',#光辉国际
'ELAT',#Elanco Animal Health Inc Equity
'GMVDW',#G Medical Innovations Holdings
'GEF',#格瑞夫-A
'CNNB',#Cincinnati Bancorp Inc
'GCT',#大健云仓
'HEES',#HE设备服务
'NFE',#New Fortress Energy Inc-A
'SPTN',#SpartanNash Co
'AMOT',#Allied Motion Technologies Inc
'VAC',#万豪度假环球
'BIAF',#bioAffinity Technologies Inc
'TAST',#Carrols Restaurant Group Inc
'FILL',#iShares MSCI Global Energy Prod
'SEB',#Seaboard Corp
'ATSG',#美国航空运输服务
'LPLA',#LPL Financial Holdings Inc
'IQ',#爱奇艺
'DS_D',#Drive Shack Inc Series D Pfd
'AQST',#Aquestive Therapeutics Inc
'ACB',#Aurora Cannabis
'SAH',#索尼克汽车
'NURO',#NeuroMetrix Inc
'NS_A',#NuStar Energy LP Series A Pfd
'NEON',#Neonode Inc
'CTSO',#CytoSorbents Corp
'BHM',#Bluerock Homes Trust Inc-A
'OMC',#宏盟集团
'GGLL',#Direxion Daily GOOGL Bull 1.5X
'RWAY',#Runway Growth Finance Corp
'KAMN',#Kaman Corp
'FCAP',#第一资本
'AMUB',#ETRACS Alerian MLP Index ETN Se
'AMRC',#阿梅雷斯克
'TSLQ',#AXS TSLA Bear Daily ETF
'SLGCW',#SomaLogic Inc Wt
'LPTX',#Leap Therapeutics Inc
'FV',#First Trust Dorsey Wright Focus
'IMKTA',#英格尔斯超市
'KOLD',#二倍做空天然气ETF-ProShares
'NSP',#Insperity Inc
'RDI',#Reading International Inc-A
'HT',#HT基金
'AMTR',#ETRACS Alerian Midstream Energy
'EPR',#EPR不动产
'AGS',#PlayAGS Inc
'KAR',#KAR车行
'TPYP',#Tortoise North American Pipelin
'ATAT',#亚朵
'GTE',#Gran Tierra Energy Inc
'LPI',#Laredo Petroleum Inc
'REX',#REX American Resources Corp
'FRAF',#富兰克林金融服务
'OIL',#原油ETF-iPath GSCI
'GSP',#iPath S&P GSCI Total Return Ind
'ONEW',#OneWater Marine Inc-A
'LCII',#LCI Industries
'FEN',#First Trust Energy Income and G
'EVC',#超视野传播
'FLXS',#弗莱克斯蒂尔工业
'NFG',#National Fuel Gas Co
'SEAT',#Vivid Seats Inc-A
'QD',#趣店
'CARV',#卡弗储蓄
'BN',#布鲁克菲尔德
'CGAU',#Centerra Gold Inc
'JBK',#Corporate Backed Trust Certific
'IAUX',#i-80 Gold Corp
'FA',#First Advantage Corp
'CHMI_A',#Cherry Hill Mortgage Investment
'NANR',#SPDR S&P North American Natural
'TRIP',#猫途鹰
'AKO_B',#Embotelladora Andina SA ADR-B
'RCEL',#AVITA Medical Inc
'HEP',#霍利能源
'PMM',#Putnam Managed Municipal Income
'GEHI',#Gravitas Education Holdings Inc
'FLLA',#Franklin FTSE Latin America ETF
'PCQ',#PIMCO California Municipal Inco
'ZUO',#祖睿
'GXO',#GXO Logistics Inc
'JHX',#詹姆斯哈迪
'TBLT',#ToughBuilt Industries Inc
'GTES',#Gates Industrial Corp plc
'SEDA_U',#SDCL EDGE Acquisition Corp Unit
'FLMX',#Franklin FTSE Mexico ETF
'GSBD',#Goldman Sachs BDC Inc
'HPI',#John Hancock Preferred Income F
'DFEN',#Direxion Daily Aerospace & Defe
'ITUB',#艾涛巴西联合银行
'IMOS',#南茂科技
'KIND',#Nextdoor Holdings Inc-A
'FIF',#First Trust Energy Infrastructu
'BBD',#布拉德斯科银行-优先股
'TGAN',#Transphorm Inc
'DKL',#Delek Logistics Partners LP
'UFAB',#Unique Fabricating Inc
'UAMY',#United States Antimony Corp
'SCOBU',#ScION Tech Growth II Unit Cons
'GGROW',#Gogoro Inc Wt
'ERNA',#Eterna Therapeutics Inc
'CHRA',#Charah Solutions Inc
'AINC',#Ashford Inc
'SDEI',#Sound Equity Income ETF
'IRS',#IRSA Inversiones y Representaci
'PYPS',#AXS 1.5X PYPL Bear Daily ETF
'DKS',#迪克体育用品
'MMI',#马库斯米利查普
'TSLX',#Sixth Street专业贷款
'NWN',#西北天然气
'TLYS',#Tilly’s Inc-A
'ASR',#Grupo Aeroportuario del Sureste
'TNK',#Teekay Tankers Ltd-A
'CMBM',#Cambium Networks Corp
'MFIN',#Medallion Financial Corp
'VIV',#保罗迪圣电讯
'AREN',#The Arena Group Holdings Inc
'ENFR',#Alerian Energy Infrastructure E
'GLOP',#GasLog Partners LP
'CBD',#Companhia Brasileira de Distrib
'EWZ',#巴西ETF-iShares MSCI
'VMD',#Viemed Healthcare Inc
'KRON',#Kronos Bio Inc
'FRD',#Friedman Industries Inc
'KOF',#可口可乐凡萨瓶装
'AN',#车之国
'BXSL',#Blackstone Secured Lending Fund
'VNTR',#Venator Materials PLC
'TCPC',#BlackRock TCP Capital Corp
'SPCB',#SuperCom Ltd
'IDW',#IDW Media Holdings Inc-B
'HOUR',#Hour Loop Inc
'EBET',#EBET Inc
'CBIO',#Catalyst Biosciences Inc
'ALPP',#Alpine 4 Holdings Inc-A
'LPG',#Dorian LPG Ltd
'NRGV',#Energy Vault Holdings Inc
'UCC',#ProShares Ultra Consumer Servic
'NCV',#Virtus Convertible & Income Fun
'NGMS',#NeoGames SA
'RGC',#脑再生科技
'LYB',#利安德巴塞尔工业
'PLBC',#Plumas Bancorp
'CEN',#Center Coast Brookfield MLP & E
'CODA',#科达章鱼集团
'TSLI',#GraniteShares 1x Short TSLA Dai
'OXLC',#Oxford Lane Capital Corp.
'WANT',#Direxion Daily Consumer Discret
'AMR',#Alpha Metallurgical Resources I
'SHO',#Sunstone Hotel Investors Inc
'URNM',#Sprott Uranium Miners ETF
'HTLFP',#Heartland Financial USA Inc Ser
'AKRO',#Akero Therapeutics Inc
'GBDC',#Golub Capital BDC Inc
'KRT',#Karat Packaging Inc
'SESN',#Sesen Bio Inc
'RCLF',#Rosecliff Acquisition Corp I-A
'PSNYW',#极星汽车(权证)
'HRI',#Herc Holdings Inc
'FOUR',#Shift4 Payments Inc-A
'AAC_WS',#Ares Acquisition Corp Wt
'AIR',#AAR CORP
'QVAL',#Alpha Architect U.S. Quantitati
'LTRN',#Lantern Pharma Inc
'BKNG',#Booking Holdings
'TPL',#Texas Pacific Land Corp
'LFMD',#LifeMD Inc
'RHI',#罗致恒富
'VTOL',#Bristow Group Inc
'GDEN',#黄金娱乐
'NDIV',#Amplify Natural Resources Divid
'OLN',#欧林
'PHI',#菲律宾长途电话
'NYC',#New York City REIT Inc-A
'CTLP',#Cantaloupe Inc
'BBDO',#布拉德斯科银行
'BASE',#Couchbase Inc
'CSWI',#CSW Industrials Inc
'CLDT',#Chatham Lodging信托
'RLTY',#Cohen & Steers Real Estate Oppo
'SONX',#Sonendo Inc
'AMND',#UBS AG ETRACS Alerian Midstream
'MAIN',#Main Street Capital Corp
'GGN',#GAMCO Global Gold, Natural Reso
'KMET',#KraneShares Trust KraneShares E
'WMK',#韦斯市场
'SXTC',#苏轩堂
'TCBK',#TriCo Bancshares
'ORMP',#Oramed Pharmaceuticals Inc
'OPY',#奥本海默控股
'UPWK',#Upwork Inc
'WCC',#西科国际
'GBNH',#Greenbrook TMS Inc
'FRBK',#共和国第一万通金控
'CWBC',#西部社区银行
'LGO',#Largo Inc
'QMOM',#Alpha Architect U.S. Quantitati
'TRS',#瑞奇包装系统
'KARO',#Karooooo Ltd
'TFIN',#Triumph Financial Inc
'TPOR',#Direxion Daily Transportation B
'UFI',#仪化宇辉
'AMBP',#Ardagh Metal Packaging SA
'BRDG',#Bridge Investment Group Holding
'AGTI',#Agiliti Inc
'JMSB',#John Marshall Bancorp Inc
'LRFC',#Logan Ridge Finance Corp
'EINC',#VanEck Energy Income ETF
'GXG',#哥伦比亚ETF-Global X MSCI
'MIDU',#Direxion Mid Cap Bull 3X Shares
'CTRN',#Citi Trends Inc
'INFU',#InfuSystem Holdings Inc
'ALLY',#Ally Financial Inc
'PAG',#潘世奇汽车
'ELAN',#Elanco Animal Health Inc
'WEX',#WEX Inc
'ARTNA',#自流资源
'MLPB',#ETRACS Alerian MLP Infrastructu
'VLRS',#Volaris航空
'TCBI',#Texas Capital Bancshares Inc
'BG',#邦吉
'FLT',#FleetCor Technologies Inc
'WSM',#Williams-Sonoma Inc
'DOZR',#Direxion Daily US Infrastructur
'INT',#全球燃料服务
'VNT',#Vontier Corp
'MSN',#Emerson Radio Corp
'KZIA',#Kazia Therapeutics Ltd ADR
'DOGZ',#多尼斯
'BIOC',#Biocept Inc
'MAN',#万宝盛华
'TSCO',#拖拉机供应
'PBI',#必能宝
'CPS',#Cooper-Standard Holdings Inc
'DORM',#Dorman Products Inc
'SCE_G',#SCE Trust II Pfd
'GSIT',#广船国际技术
'OXSQG',#Oxford Square Capital Corp Note
'MIR_WS',#Mirion Technologies Inc Wt
'JFIN',#嘉银金科
'HCDIP',#Harbor Custom Development Inc S
'CHRB',#Charah Solutions Inc Notes
'OZK',#欧扎克银行
'PAC',#太平洋航空
'JNUG',#二倍做多小金矿指数ETF-Direxion
'DUSL',#Direxion Daily Industrials Bull
'FPA',#First Trust Asia Pacific Ex-Jap
'ONTF',#ON24 Inc
'FLZA',#Franklin FTSE South Africa ETF
'LNC',#林肯国民
'IPG',#埃培智
'MOV',#摩凡陀
'CEQP_',#Crestwood Equity Partners LP Pf
'VCXB_U',#10X Capital Venture Acquisition
'XRT',#零售ETF-SPDR
'COMT',#iShares GSCI Commodity Dynamic
'PFLT',#PennantPark Floating Rate Capit
'PDO',#PIMCO Dynamic Income Opportunit
'LEV_WS_A',#The Lion Electric Co Wt
'FBIO',#Fortress Biotech Inc
'POR',#波特兰通用电气
'SCX',#施泰力
'PFSW',#PFSweb Inc
'OLLI',#Ollie's Bargain Outlet Holdings
'AGNCL',#AGNC Investment Corp Series G P
'HZO',#海上麦斯服务
'TYG',#Tortoise Energy Infrastructure
'AGD',#abrdn Global Dynamic Dividend F
'CCRV',#iShares Commodity Curve Carry S
'SOPA',#Society Pass Inc
'GSG',#大宗商品指数ETF-iShares GSCI
'SHEL',#壳牌
'DWEQ',#AdvisorShares Dorsey Wright Alp
'E',#埃尼石油
'DBC',#大宗商品ETF-PowerShares
'DNOW',#NOW Inc
'OLPX',#Olaplex Holdings Inc
'PFHD',#Professional Holding Corp-A
'SIFY',#Sify Technologies Ltd ADR
'SHPW',#Shapeways Holdings Inc
'MFG',#瑞穗金融
'CRI',#卡特
'AMPG',#AmpliTech Group Inc
'ADXN',#Addex Therapeutics Ltd ADR
'CCJ',#卡梅科
'NMFC',#New Mountain Finance Corp
'ABEV',#Ambev SA ADR
'LYG',#劳埃德银行(US ADR)
'NCNO',#nCino Inc
'WRK',#WestRock Co
'CFFI',#C&F金融
'MBTC',#Nocturne Acquisition Corp
'BYSI',#万春医药
'HST',#HOST酒店及度假村
'GLAD',#格拉德斯通资本
'ENVA',#易诺华国际
'PDBC',#Invesco Optimum Yield Diversifi
'NWLI',#国家西方人寿保险
'KURE',#KraneShares MSCI All China Heal
'URA',#铀矿ETF-Global X
'ICCC',#伊芙美尔医疗
'SR',#Spire Inc
'MTZ',#MasTec Inc
'FDBC',#Fidelity D & D Bancorp Inc
'PZZA',#棒约翰
'ARLP',#Alliance Resource Partners LP
'FDMT',#4D Molecular Therapeutics Inc
'AHT',#阿什福德信托
'TW',#Tradeweb Markets Inc-A
'CLAYU',#Chavant Capital Acquisition Cor
'RIDE',#Lordstown Motors Corp-A
'MCHX',#Marchex Inc-B
'HZN',#Horizon Global Corp
'GOVX',#GeoVax Labs Inc
'APPH',#AppHarvest Inc
'AFRIW',#Forafric Global PLC Wt
'LNW',#Light & Wonder Inc
'USCI',#United States Commodity Index F
'FL',#富乐客
'HFFG',#HF Foods Group Inc
'NZF',#Nuveen Municipal Credit Income
'EVRI',#Everi Holdings Inc
'RFIL',#RF Industries Ltd
'RUSHA',#Rush Enterprises Inc-A
'LUV',#西南航空
'FSCO',#FS Credit Opportunities Corp
'CATO',#加图商场
'KIM',#金克地产
'SMFG',#三井住友金融
'ARGT',#阿根廷ETF-Global X MSCI
'TSLS',#Direxion Daily TSLA Bear 1X Sha
'ALPS',#Alpine Summit Energy Partners I
'SIX',#六旗娱乐
'DBRG_J',#DigitalBridge Group Inc Series
'JO',#咖啡豆ETN-iPath
'GOOG',#谷歌-C
'CHUY',#Chuy’s Holdings Inc
'BLRX',#BioLineRx Ltd ADR
'ARQQW',#Arqit Quantum Inc Wt
'BDCZ',#ETRACS MVIS Business Developmen
'FORTY',#配方系统
'HGV',#希尔顿度假酒店
'DD',#陶氏杜邦
'CGC',#Canopy Growth Corp
'RNLX',#Renalytix plc ADR
'FRBA',#First Bank
'BWEN',#Broadwind Inc
'ACIU',#AC Immune SA
'BP',#英国石油(US)
'AMZN',#亚马逊
'ANPC',#安派科
'CHIS',#Global X MSCI China Consumer St
'KBAL',#Kimball International Inc-B
'YANG',#三倍做空FTSE中国ETF-Direxion
'ASIX',#AdvanSix Inc
'APLE',#Apple Hospitality REIT Inc
'DRH',#DiamondRock Hospitality Co
'CMP',#罗盘矿物
'SFET',#Safe-T Group Ltd ADR
'LOOP',#Loop Industries Inc
'MTCH',#Match Group Inc
'THS',#树屋食品
'SARK',#AXS Short Innovation Daily ETF
'RQI',#Cohen & Steers Quality Income R
'INFL',#Horizon Kinetics Inflation Bene
'FGM',#First Trust Germany AlphaDEX Fu
'PCT',#PureCycle Technologies Inc
'OEC',#Orion Engineered Carbons SA
'NESR',#全国能源统一服务
'BRSH',#Bruush Oral Care Inc
'GUNR',#全球上游自然资源ETF-FlexShares
'NJR',#新泽西能源
'PTNR',#Partner Communications Co Ltd A
'LWAY',#来福威食品
'ITI',#Iteris Inc
'TURN',#180 Degree Capital Corp
'MNSBP',#MainStreet Bancshares Inc Serie
'GIFI',#Gulf Island Fabrication Inc
'MPLX',#MPLX LP
'PFO',#Flaherty & Crumrine Preferred a
'EVR',#Evercore Inc-A
'MP',#MP Materials Corp-A
'FBMS',#第一银行(密西西比州)
'GEVO',#Gevo Inc
'SDCI',#USCF SummerHaven Dynamic Commod
'YTRA',#Yatra Online Inc
'MH_C',#Maiden Holdings Ltd Series C Pf
'CUBE',#CubeSmart
'ENB',#恩桥
'MYTE',#MYT Netherlands Parent BV ADR
'WLFC',#威利斯融资租赁
'SLRX',#Salarius Pharmaceuticals Inc
'OHAA',#Opy Acquisition Corp I-A
'LPTH',#LightPath Technologies Inc-A
'LINK',#互联电子
'BTCY',#Biotricity Inc
'ALDX',#Aldeyra Therapeutics Inc
'COPX',#铜矿ETF-Global X
'WLK',#Westlake Corp
'MNM',#Direxion Daily Metal Miners Bul
'TTE',#TotalEnergies SE ADR
'MUFG',#三菱日联金融
'TBBK',#The Bancorp Inc
'EQRR',#ProShares Equities for Rising R
'ROSS_U',#Ross Acquisition Corp II Unit C
'AMOV',#美洲移动
'WAFU',#华富教育
'IVH',#Ivy High Income Opportunities F
'ASA',#ASA Gold and Precious Metals Li
'CMS',#CMS能源
'LCUT',#美国生牌
'YOLO',#AdvisorShares Pure Cannabis ETF
'AIZ',#安信龙保险
'GOOGL',#谷歌-A
'ALG',#阿拉莫
'SBCF',#Seacoast Banking Corp of Florid
'BSBR',#桑坦德银行巴西分行
'SVM',#希尔威金属矿业
'SAFT',#Safety Insurance Group Inc
'DRD',#DRDGOLD Ltd ADR
'NATR',#天然阳光产品
'FCRD',#First Eagle Alternative Capital
'EUDA',#EUDA Health Holdings Ltd
'SMTC',#先科电子
'VBTX',#Veritex Holdings Inc
'NCR',#NCR Corp
'DWAT',#Arrow Investments Trust Arrow D
'VOYA',#Voya Financial Inc
'SA',#Seabridge Gold Inc
'TNYA',#Tenaya Therapeutics Inc
'CTOS',#Custom Truck One Source Inc
'KRNT',#Kornit Digital Ltd
'FRGAP',#Franchise Group Inc Series A Pf
'GTN',#格雷电视
'RATE',#Global X Interest Rate Hedge ET
'ZLAB',#再鼎医药
'NETL',#NETLease Corporate Real Estate
'WOW',#WideOpenWest Inc
'QCRH',#QCR Holdings Inc
'ABG',#阿斯伯里汽车集团
'AGQ',#二倍做多白银ETF-ProShares
'TTC',#托罗配件
'HCCI',#Heritage-Crystal Clean Inc
'UTL',#Unitil Corp
'AEM',#伊格尔矿业
'BTO',#John Hancock Financial Opportun
'LFUS',#美国力特保险丝
'CASS',#卡斯信息系统
'TBI',#TrueBlue Inc
'RELI',#Reliance Global Group Inc
'PLYA',#海滩酒店度假
'FUNC',#马里兰第一联合
'XOMAO',#标记临床研究(优先股)
'COKE',#可口可乐装瓶
'MJ',#ETFMG Alternative Harvest ETF
'VLGEA',#Village Super Market Inc-A
'BERY',#Berry Global Group Inc
'ICFI',#ICF International Inc
'OXBR',#Oxbridge Re Holdings Ltd
'NECB',#东北社区银行
'BFS',#Saul Centers Inc
'SYLD',#Cambria Shareholder Yield ETF
'AVAV',#AeroVironment Inc
'DFRA',#Donoghue Forlines Yield Enhance
'WU',#西联汇款
'PRI',#Primerica Inc
'QNCX',#Quince Therapeutics Inc
'IAF',#abrdn Australia Equity Fund Inc
'DTM',#DT Midstream Inc
'CNTX',#Context Therapeutics Inc
'BIOL',#BIOLASE Inc
'PLL',#Piedmont Lithium Inc
'SHO_I',#Sunstone Hotel Investors Inc Se
'WD',#Walker & Dunlop Inc
'FAS',#三倍做多金融ETF-Direxion
'ARTW',#Art’s-Way Manufacturing Co Inc
'MFD',#Macquarie/First Trust Global In
'REFI',#Chicago Atlantic Real Estate Fi
'NWPX',#西北管道
'HSON',#Hudson Global Inc
'PALI',#Palisade Bio Inc
'CMCM',#猎豹移动
'CCBG',#Capital City Bank Group Inc
'PBDC',#Putnam BDC Income ETF
'BC',#布朗斯威克
'BIZD',#VanEck BDC Income ETF
'MCFT',#MasterCraft Boat Holdings Inc
'VNM',#越南ETF-VanEck Vectors
'CID',#VictoryShares International Hig
'NRT',#北欧皇家石油信托
'FSFG',#第一储蓄金融
'MOXC',#魔线
'STKL',#SunOpta Inc
'CNTY',#世纪赌场
'HTOO',#Fusion Fuel Green PLC-A
'RUTH',#鲁斯集团
'HAP',#VanEck Natural Resources ETF
'PEG',#公共服务企业
'HTD',#John Hancock Tax-Advantaged Div
'NEOV',#NeoVolta Inc
'NOA',#North American Construction Gro
'GSAT',#全球星
'AMX',#美洲移动
'EZA',#南非ETF-iShares MSCI
'SAL',#Salisbury Bancorp Inc
'CGO',#Calamos Global Total Return Fun
'CSTE',#Caesarstone Ltd
'EXP',#Eagle Materials Inc
'KBWR',#Invesco KBW Regional Banking ET
'SWEB',#AXS Short China Internet ETF
'CTS',#CTS Corp
'BGH',#Barings Global Short Duration H
'GCC',#WisdomTree Continuous Commodity
'RCB',#Ready Capital Corp Notes
'PEB_H',#Pebblebrook Hotel Trust Series
'WTFCP',#Wintrust Financial Corp Series
'MBWM',#莫肯特尔银行
'URE',#二倍做多房地产ETF-ProShares
'IMUX',#Immunic Inc
'MT',#安赛乐米塔尔
'WVE',#Wave Life Sciences Ltd
'ASTE',#Astec Industries Inc
'MU',#美光科技
'FG',#F&G Annuities & Life Inc
'GPP',#Green Plains Partners LP
'GCMG',#GCM Grosvenor Inc-A
'CMND',#Clearmind Medicine Inc
'CIG_C',#Cemig ADR
'ABCB',#Ameris Bancorp
'XSVM',#Invesco S&P SmallCap Value with
'DIS',#迪士尼
'CBOE',#芝加哥期权交易所
'CWT',#California Water Service Group
'ZYXI',#Zynex Inc
'SVC',#Service Properties Trust
'UYM',#二倍做多基础材料ETF-ProShares
'CBSE',#Changebridge Capital Sustainabl
'GAM',#General American Investors Co I
'XHR',#Xenia Hotels & Resorts Inc
'ITRG',#Integra Resources Corp
'FLME_WS',#Flame Acquisition Corp Wt
'BW_A',#Babcock & Wilcox Series A Pfd
'CQP',#Cheniere Energy Partners LP
'PPC',#Pilgrim's Pride Corp
'CINT',#CI&T Inc-A
'ENTG',#英特格
'OMEX',#奥德赛海洋勘探
'DTE',#DTE能源
'RBBN',#Ribbon Communications Inc
'CVGI',#商用汽车
'ACTG',#阿卡西亚
'COFS',#ChoiceOne Financial Services In
'RAAX',#VanEck Inflation Allocation ETF
'OUT',#OUTFRONT Media Inc
'CIZN',#市民金融控股
'BV',#BrightView Holdings Inc
'AWP',#abrdn Global Premier Properties
'UDOW',#三倍做多道指ETF-ProShares
'DPST',#Direxion Daily Regional Banks B
'MXF',#墨西哥基金
'SXC',#SunCoke Energy Inc
'SAND',#沙尘暴黄金
'EIPX',#FT Energy Income Partners Strat
'AXS',#埃克斯资本
'MTCN',#ArcelorMittal Notes
'WKME',#WalkMe Ltd
'LMFA',#LM Funding America Inc
'AP',#安博科-匹兹堡
'O',#Realty Income Corp
'NVDS',#AXS 1.25X NVDA Bear Daily ETF
'PSTL',#Postal Realty Trust Inc-A
'SPXL',#Direxion Daily S&P 500 Bull 3X
'UPRO',#三倍做多标普500ETF-ProShares
'KELYA',#凯利服务-A
'CKX',#CKX Lands Inc
'BANC',#Banc of California Inc
'WH',#温德姆酒店及度假村
'HMST',#HomeStreet Inc
'OP',#OceanPal Inc
'KCAL',#Subversive Food Security ETF
'PINC',#Premier Inc-A
'SVXY',#做空恐慌指数期货短期合约ETF
'USOI',#Credit Suisse X-Links Crude Oil
'RXO',#RXO Inc
'FIZZ',#National Beverage Corp
'KAI',#凯登纸业
'BLW',#BlackRock Limited Duration Inco
'AWF',#AllianceBernstein Global High I
'SUM',#Summit Materials Inc-A
'ESI',#Element Solutions Inc
'GCO',#格涅斯科
'ATNI',#大西洋电讯网络国际
'TAOP',#淘屏
'SSY',#SunLink Health Systems Inc
'EIG',#Employers Holdings Inc
'YETI',#YETI Holdings Inc
'VGR',#Vector Group Ltd
'OLP',#One Liberty Properties Inc
'PMN',#ProMIS Neurosciences Inc
'GPI',#汽车一组
'ACRE',#阿瑞斯商业地产
'FLSP',#Franklin Systematic Style Premi
'BVH',#Bluegreen Vacations Holding Cor
'PFX',#PhenixFIN Corp
'BTU',#皮博迪能源
'SNT',#Senstar Technologies Ltd
'EPSN',#Epsilon Energy Ltd
'ENVX',#Enovix Corp
'NTR',#Nutrien Ltd
'SCM',#Stellus Capital Investment Corp
'HDLB',#ETRACS Monthly Pay 2xLeveraged
'PGC',#皮帕克格拉德斯通金融
'TSE',#Trinseo PLC
'WWD',#伍德沃德
'SNDA',#Sonida Senior Living Inc
'SMSI',#Smith Micro Software Inc
'HNI',#HNI Corp
'PFGC',#Performance Food Group Co
'VMAR',#Vision Marine Technologies Inc
'CDLX',#Cardlytics Inc
'ASH',#亚什兰
'UVV',#环球烟草
'SRTS',#Sensus Healthcare Inc
'CGRN',#Capstone Green Energy Corp
'TGN',#AXS Brendan Wood TopGun Index E
'WWW',#沃尔弗林集团
'RLI',#RLI保险
'CNO',#康塞科
'ODFL',#Old Dominion Freight Line Inc
'KMT',#肯纳金属
'FPH',#五点控股
'TCN',#Tricon Residential Inc
'EZPW',#艾茨克普
'GL',#环球人寿
'MGU',#Macquarie Global Infrastructure
'SURE',#AdvisorShares Insider Advantage
'CARE',#Carter Bankshares Inc
'SP',#SP Plus Corp
'AGR',#Avangrid Inc
'WHR',#惠而浦
'CPER',#United States Copper Index Fund
'ORCC',#Owl Rock Capital Corp
'VIAO',#伟亚光电
'SHPH',#Shuttle Pharmaceuticals Holding
'NWTN',#NWTN Inc
'NHICU',#NewHold Investment Corp II Unit
'HEPS',#D-MARKET Electronic Services &
'FE',#第一能源
'PFSI',#PennyMac Financial Services Inc
'TFC_I',#Truist Financial Corp Series I
'DBI',#Designer Brands Inc-A
'IVRA',#Invesco Real Assets ESG ETF
'CBLS',#Changebridge Capital Long/Short
'AGNCM',#AGNC Investment Corp Series D P
'DOX',#Amdocs Ltd
'LILAK',#Liberty Latin America Ltd-C
'DALT',#Anfield Capital Diversified Alt
'HTY',#John Hancock Tax-Advantaged Glo
'VAMO',#Cambria ETF Trust Cambria Value
'SJW',#SJW Group
'CRAK',#VanEck Oil Refiners ETF
'GRVY',#Gravity Co Ltd ADR
'EVEN',#Direxion Daily S&P 500 Equal We
'KW',#Kennedy-Wilson Holdings Inc
'LCNB',#LCNB Corp
'BPOP',#大众银行(波多黎各)
'VPC',#Virtus Private Credit Strategy
'IFS',#Intercorp Financial Services In
'XOMAP',#标记临床研究(优先股)
'UNM',#尤纳姆
'VATE',#INNOVATE Corp
'VICI',#VICI Properties Inc
'UFCS',#联合火险
'CSGS',#CSG系统国际
'TBF',#做空20年+国债ETF-ProShares
'STRL',#Sterling Infrastructure Inc
'FBP',#第一万能金控
'MMLP',#Martin Midstream Partners LP
'BOC',#波士顿奥马哈
'EXLS',#伊克赛尔服务控股
'MKL',#Markel Corp
'RHP',#Ryman Hospitality Properties In
'AVUV',#Avantis U.S. Small Cap Value ET
'RDIV',#Invesco S&P Ultra Dividend Reve
'SLGN',#西尔格控股
'INSE',#Inspired Entertainment Inc
'FLL',#Full House Resorts Inc
'WY',#惠好
'CENX',#世纪铝业
'UA',#安德玛-C
'ASB_F',#Associated Banc-Corp Series F P
'KR',#克罗格
'CE',#塞拉尼斯
'BDJ',#BlackRock Enhanced Equity Divid
'DDIV',#First Trust Dorsey Wright Momen
'TGLS',#Tecnoglass Inc
'COWZ',#Pacer US Cash Cows 100 ETF
'JCSE',#佳益净科
'EB',#Eventbrite Inc-A
'BBAR',#Banco BBVA Argentina SA ADR
'GEF_B',#格瑞夫-B
'LESL',#Leslie's Inc
'EDTX',#EdtechX Holdings Acquisition Co
'NVX',#NOVONIX Ltd ADR
'RCLFU',#Rosecliff Acquisition Corp I Un
'NNBR',#NN Inc
'M',#梅西百货
'HTZWW',#赫兹租车(权证)
'EPD',#Enterprise Products Partners LP
'IGF',#全球基础设施ETF-iShares
'TPTA',#Terra Property Trust Inc Notes
'BYTE',#Roundhill IO Digital Infrastruc
'XMVM',#Invesco S&P MidCap Value with M
'MYRG',#MYR Group Inc
'GTY',#Getty Realty Corp
'BCM',#iPath Pure Beta Broad Commodity
'BAL',#棉花ETN-iPath
'GRES',#IQ ARB Global Resources ETF
'ARCB',#ArcBest Corp
'ASGN',#盎塞
'RIBT',#RiceBran Technologies
'GT',#固特异轮胎橡胶
'AWYX',#ETFMG 2X Daily Travel Tech ETF
'SO',#南方电力
'CECO',#CECO环保
'PWSC',#PowerSchool Holdings Inc-A
'IDA',#IDACORP Inc
'SRCL',#消毒循环
'ANDE',#安德森斯
'BSVN',#Bank7 Corp
'TJX',#The TJX Companies Inc
'DOW',#陶氏
'RZC',#Reinsurance Group of America In
'PVH',#PVH Corp
'DEA',#Easterly Government Properties
'WSR',#Whitestone REIT
'LOW',#劳氏
'XRTX',#XORTX Therapeutics Inc
'URGN',#乌龙制药
'ALR',#AlerisLife Inc
'ORFN',#Constrained Capital ESG Orphans
'TRTX_C',#TPG RE Finance Trust Inc Series
'CIM_A',#Chimera Investment Corp Series
'DVLU',#First Trust Dorsey Wright Momen
'GME',#游戏驿站
'IRDM',#铱星通讯
'GNR',#SPDR S&P Global Natural Resourc
'SLNO',#Soleno Therapeutics Inc
'RILYK',#B. Riley Financial Inc Notes
'TFSL',#TFS Financial Corp
'LSI',#Life Storage Inc
'XNCR',#Xencor Inc
'VST',#Vistra Corp
'EEX',#Emerald Holding Inc
'ENZL',#新西兰ETF-iShares MSCI
'VRAI',#Virtus Real Asset Income ETF
'GRZZ',#Grizzle Growth ETF
'IPDP',#Dividend Performers ETF
'FMNB',#Farmers National Banc Corp
'MVV',#ProShares Ultra MidCap400
'TLK',#印尼电信
'HWM',#Howmet Aerospace Inc
'EWH',#香港ETF-iShares MSCI
'DOLE',#都乐
'AKR',#阿卡迪亚不动产信托
'TSBK',#Timberland Bancorp Inc
'VVR',#Invesco Senior Income Trust
'DMRC',#数字标识
'OSBC',#Old Second Bancorp Inc
'MLKN',#MillerKnoll Inc
'COMB',#GraniteShares Bloomberg Commodi
'RRR',#Red Rock Resorts Inc-A
'COF',#第一资本金融
'MTX',#Minerals Technologies Inc
'FMC',#FMC Corp
'MGRB',#Affiliated Managers Group Inc N
'ATR',#AptarGroup Inc
'RIV',#RiverNorth Opportunities Fund
'REVG',#REV Group Inc
'EYE',#National Vision Holdings Inc
'ROST',#罗斯百货
'VRTS',#维德思投资
'CRD_B',#克劳福德-B
'AATC',#Autoscope Technologies Corp
'ADC',#艾格里不动产
'SPG',#西蒙地产
'BUL',#Pacer US Cash Cows Growth ETF
'MTB_H',#M&T Bank Corp Series H Pfd
'GBLI',#Global Indemnity Group LLC-A
'UGI',#UGI公用事业
'DNP',#DNP Select Income Fund
'DLTR',#美元树
'ORN',#Orion Group Holdings Inc
'DMAT',#Global X Disruptive Materials E
'BC_C',#Brunswick Corp Notes
'MCW',#Mister Car Wash Inc
'AEE',#阿曼瑞恩
'FTRI',#First Trust Indxx Global Natura
'BKU',#BankUnited Inc
'RPM',#RPM International Inc
'GDXU',#MicroSectors Gold Miners 3X Lev
'GOGL',#Golden Ocean Group Ltd
'NXST',#Nexstar Media Group Inc
'PUI',#Invesco DWA Utilities Momentum
'NTB',#毕达菲尔特银行
'GRU',#ELEMENTS Linked to the MLCX Gra
'DRH_A',#DiamondRock Hospitality Co Seri
'EWA',#澳大利亚ETF-iShares MSCI
'USEG',#美国能源
'MDJH',#明大嘉和
'LEG',#礼恩派
'FNF',#富达国民金融
'UUUU',#Energy Fuels Inc
'FOVL',#iShares Focused Value Factor ET
'PTVE',#Pactiv Evergreen Inc
'ES',#能源方案
'SLVP',#iShares MSCI Global Silver Mine
'EMIF',#新兴市场基础设施ETF-iShares
'SPVM',#Invesco S&P 500 Value with Mome
'CBRE',#世邦魏理仕
'EWM',#马来西亚ETF-iShares MSCI
'CIO_A',#City Office REIT Inc Series A P
'CTMX',#CytomX Therapeutics Inc
'AES',#爱依斯电力
'SNLN',#Highland/iBoxx Senior Loan ETF
'KTB',#Kontoor Brands Inc
'PIT',#VanEck Commodity Strategy ETF
'HOFT',#胡克家具
'FFBW',#FFBW Inc
'ESS',#埃塞克斯信托
'BCS',#巴克莱
'BIOTU',#Biotech Acquisition Co Unit Con
'ABR_F',#Arbor Realty Trust Inc Series F
'WPRT',#西港燃料
'LUCY',#Innovative Eyewear Inc
'LND',#BrasilAgro – Companhia Brasile
'HQY',#HealthEquity Inc
'AMTX',#Aemetis Inc
'UXI',#ProShares Ultra Industrials
'GO',#Grocery Outlet Holding Corp
'LZB',#La-Z-Boy Inc
'RZV',#Invesco S&P SmallCap 600 Pure V
'TRTY',#Cambria Trinity ETF
'DSU',#BlackRock Debt Strategies Fund
'OSCV',#Opus Small Cap Value ETF
'PEB_F',#Pebblebrook Hotel Trust Series
'AEP',#美国电力
'BCO',#布林克
'LNN',#Lindsay Corp
'GVLU',#Gotham 1000 Value ETF
'CGTX',#Cognition Therapeutics Inc
'PCH',#PotlatchDeltic Corp
'AVY',#艾利丹尼森
'KEQU',#基瓦尼科技
'XEL',#埃克西尔能源
'CMDY',#iShares Bloomberg Roll Select C
'IBTX',#Independent Bank Group Inc
'NAPA',#Duckhorn Portfolio Inc
'STRM',#Streamline Health Solutions Inc
'SCS',#Steelcase Inc-A
'RLY',#SPDR SSgA Multi Asset Real Retu
'PPBT',#Purple Biotech Ltd ADR
'REXR',#Rexford Industrial Realty Inc
'CXW',#CoreCivic Inc
'UBA',#Urstadt Biddle Properties Inc-A
'PRK',#Park National Corp
'FELE',#富兰克林电子
'ARCE',#Arco Platform Ltd-A
'DALN',#DallasNews Corp-A
'FTS',#Fortis Inc
'CTA',#Simplify Managed Futures Strate
'EVV',#Eaton Vance Limited Duration In
'TGT',#塔吉特
'AZEK',#The AZEK Co Inc-A
'FGBI',#First Guaranty Bancshares Inc
'RNST',#Renasant Corp
'FUND',#Sprott Focus Trust
'CORR_A',#CorEnergy Infrastructure Trust
'ET',#能源转换
'SYF',#Synchrony Financial
'OFS',#OFS Capital Corp
'HYLN',#Hyliion Holdings Corp
'HLN',#Haleon plc ADR
'ACHL',#Achilles Therapeutics plc ADR
'EWC',#加拿大ETF-iShares MSCI
'ERH',#Allspring Utilities and High In
'BRX',#Brixmor Property Group Inc
'WSO',#华斯科
'TPX',#泰普尔丝涟
'API',#声网
'HTIA',#Healthcare Trust Inc Series A P
'FRGI',#Fiesta Restaurant Group Inc
'CAL',#Caleres Inc
'AFG',#美国金融
'BRK_B',#伯克希尔哈撒韦-B
'CNHI',#CNH Industrial NV
'CNP',#中点能源
'ECVT',#Ecovyst Inc
'EPP',#太平洋除日本ETF-iShares MSCI
'UBS',#瑞银集团
'DXYN',#迪克希
'BUI',#BlackRock Utilities, Infrastruc
'FR',#第一工业地产信托
'CIGI',#高力国际集团
'PRIM',#Primoris Services Corp
'GRFS',#基立福
'EMLP',#First Trust North American Ener
'AAN',#The Aaron’s Co Inc
'UNF',#第一联合
'HPP_C',#Hudson Pacific Properties Inc S
'TYO',#Direxion Daily 7-10 Year Treasu
'EEFT',#嘉银通
'PEX',#ProShares Global Listed Private
'FISI',#Financial Institutions Inc
'URI',#联合租赁
'WTV',#WisdomTree U.S. Value Fund
'BLDG',#Cambria Global Real Estate ETF
'CIR',#Circor国际
'TRU',#TransUnion
'MNPR',#Monopar Therapeutics Inc
'ITRM',#Iterum Therapeutics plc
'HTCR',#HeartCore Enterprises Inc
'DLNG',#Dynagas LNG Partners LP
'PPL',#PPL能源
'FET',#Forum Energy Technologies Inc
'BKH',#黑山
'SCL',#史提宾
'LXFR',#Luxfer Holdings PLC
'PICK',#iShares MSCI Global Select Meta
'PHVS',#Pharvaris NV
'SILJ',#ETFMG Prime Junior Silver Miner
'STLA',#Stellantis集团
'PSMT',#普尔斯玛特
'EXC',#爱克斯龙电力
'ARGD',#Argo Group International Holdin
'MBOX',#Freedom Day Dividend ETF
'PNW',#品尼高西方资本
'STNG',#Scorpio Tankers Inc
'FTXR',#First Trust Nasdaq Transportati
'WATT',#Energous Corp
'WPC',#W. P. Carey Inc
'ADNT',#Adient plc
'CCNE',#CNB金融
'TRV',#旅行者保险
'AIG',#美国国际集团
'CNS',#科恩-斯蒂尔斯金融
'DSPC',#AXS De-SPAC ETF
'PAM',#Pampa Energia SA ADR
'DOMH',#Dominari Holdings Inc
'ACHV',#Achieve Life Sciences Inc
'WFG',#West Fraser Timber Co Ltd
'TOUR',#途牛
'GMOM',#Cambria Global Momentum ETF
'FBL',#GraniteShares 1.5x Long META Da
'RBLX',#Roblox Corp-A
'CMCO',#哥伦布-麦金农
'ADM',#阿彻丹尼尔斯米德兰
'URTY',#ProShares UltraPro Russell2000
'EDF',#Virtus Stone Harbor Emerging Ma
'FTGC',#First Trust Global Tactical Com
'TNA',#三倍做多小型股ETF-Direxion
'NEE_R',#NextEra Energy Inc Corporate Un
'DJCB',#ETRACS Bloomberg Commodity Inde
'GDO',#Western Asset Global Corporate
'ALGM',#Allegro MicroSystems Inc
'TWN',#The Taiwan Fund
'BNS',#加拿大丰业银行
'DES',#WisdomTree U.S. SmallCap Divide
'SCHW',#嘉信理财
'BBAX',#JPMorgan BetaBuilders Developed
'TEX',#特雷克斯
'ATH_C',#Athene Holding Ltd Series C Pfd
'KNX',#Knight-Swift Transportation Hol
'PIO',#Invesco Global Water ETF
'ERJ',#巴西航空工业
'PLYM',#普利茅斯工业房地产信托
'JQC',#Nuveen Credit Strategies Income
'BIP',#布鲁克菲尔德公共建设
'SASR',#Sandy Spring Bancorp Inc
'NYT',#纽约时报
'AAL',#美国航空
'FLAU',#Franklin FTSE Australia ETF
'AOS',#A.O.史密斯
'CHCT',#Community Healthcare Trust Inc
'SBEV',#Splash Beverage Group Inc
'PRLD',#Prelude Therapeutics Inc
'NM',#Navios Maritime Holdings Inc
'AHHX',#Adaptive High Income ETF
'CVY',#Invesco Zacks Multi-Asset Incom
'IGMS',#IGM Biosciences Inc
'VRTV',#Veritiv Corp
'HE',#夏威夷电力
'VVV',#胜牌
'RJF',#瑞杰金融
'FLCA',#Franklin FTSE Canada ETF
'VSTO',#Vista Outdoor Inc
'OMF',#OneMain Holdings Inc
'CG',#凯雷集团
'ORLY',#奥莱利
'UYG',#二倍做多金融ETF-ProShares
'LW',#蓝威斯顿控股
'LPX',#路易斯安那太平洋
'NXRT',#NexPoint Residential Trust Inc
'AFL',#美国家庭人寿保险
'CNBS',#Amplify Seymour Cannabis ETF
'CTA_A',#E. I. du Pont de Nemours and Co
'DXC',#DXC Technology Co
'GAIN',#格拉德斯通投资
'OCSL',#Oaktree Specialty Lending Corp
'AFK',#非洲指数ETF-VanEck Vectors
'AMOM',#QRAFT AI-Enhanced U.S. Large Ca
'AEG',#荷兰全球保险
'FBRT',#Franklin BSP Realty Trust Inc
'XOUT',#GraniteShares XOUT U.S. Large C
'AXP',#美国运通
'VIRC',#Virco Mfg Corp
'RRAC_U',#Rigel Resource Acquisition Corp
'CFFN',#国会联邦金融
'MUA',#BlackRock MuniAssets Fund
'NURE',#Nuveen Short-Term REIT ETF
'FCNCA',#第一公民银行股份-A
'CZR',#凯撒娱乐
'INLX',#Intellinetics Inc
'FNX',#First Trust Mid Cap Core AlphaD
'ISD',#PGIM High Yield Bond Fund
'MGEE',#MGE Energy Inc
'PNRG',#PrimeEnergy Corp
'GNK',#根科船务贸易
'ACT',#Enact Holdings Inc
'NHS',#Neuberger Berman High Yield Str
'BCD',#Abrdn Bloomberg All Commodity L
'PECO',#Phillips Edison & Co Inc
'FPF',#First Trust Intermediate Durati
'PEBO',#Peoples Bancorp Inc
'TRI',#汤森路透
'WEAT',#小麦ETF-Teucrium
'LTH',#Life Time Group Holdings Inc
'RDN',#Radian Group Inc
'NILE_D',#BitNile Holdings Inc Series D P
'GMET',#VanEck Green Metals ETF
'TY',#Tri Continental Corporation
'RSF',#RiverNorth Capital and Income F
'EVRG',#Evergy
'VIRT',#Virtu Financial Inc-A
'EPRT',#Essential Properties Realty Tru
'USVT',#US Value ETF
'MBUU',#Malibu Boats Inc-A
'TNON',#Tenon Medical Inc
'OBNK',#Origin Bancorp Inc
'JJE',#iPath Series B Bloomberg Energy
'IOSP',#英诺斯派材料
'JEF',#Jefferies Financial Group Inc
'SPMO',#Invesco S&P 500 Momentum ETF
'TMST',#TimkenSteel Corp
'HCSG',#医疗保健服务
'TRST',#TrustCo Bank Corp NY
'LQDT',#Liquidity Services Inc
'UCIB',#ETRACS CMCI Total Return ETN Se
'PII',#北极星
'L',#洛斯保险
'BRC',#布雷迪
'SITE',#SiteOne Landscape Supply Inc
'GDMN',#WisdomTree Efficient Gold Plus
'CPSI',#Computer Programs and Systems I
'ICAP',#InfraCap Equity Income Fund ETF
'NSIT',#Insight Enterprises Inc
'GNW',#Genworth金融
'PSA',#大众仓储
'NG',#NOVAGOLD Resources Inc
'AROW',#箭牌金融
'ONTO',#Onto Innovation Inc
'GERM',#ETFMG Treatments, Testing and A
'HYT',#BlackRock Corporate High Yield
'FAX',#abrdn Asia-Pacific Income Fund
'ROIC',#Retail Opportunity Investments
'MSBI',#Midland States Bancorp Inc
'XSMO',#Invesco S&P SmallCap Momentum E
'MDIV',#First Trust Multi-Asset Diversi
'FCX',#自由港麦克莫兰
'COOK',#Traeger Inc
'SPUU',#Direxion Daily S&P 500 Bull 2X
'ESGS',#Columbia U.S. ESG Equity Income
'OGE',#OGE Energy Corp
'AL',#航空租赁
'RWJ',#Invesco S&P SmallCap 600 Revenu
'SOHO',#Sotherly Hotels Inc
'DEEP',#Roundhill Acquirers Deep Value
'NSA',#National Storage Affiliates Tru
'UZF',#US Cellular Corp Note
'FCA',#First Trust China AlphaDEX Fund
'XMMO',#Invesco S&P MidCap Momentum ETF
'FLHK',#Franklin FTSE Hong Kong ETF
'OB',#Outbrain Inc
'DOOR',#美森特
'TOLZ',#ProShares DJ Brookfield Global
'ECLN',#First Trust EIP Carbon Impact E
'EVTC',#Evertec Inc
'PSEC',#普罗斯佩克特资本
'BJRI',#BJ’s Restaurants Inc
'PWR',#广达服务
'DLX',#豪华
'MSEX',#米德尔赛克斯水务公司
'WT',#WisdomTree Inc
'SYY',#西斯科
'CCK',#皇冠控股
'DGICA',#多尼戈尔股份-A
'FOF',#Cohen & Steers Closed-End Oppor
'NWE',#NorthWestern Corp
'TRTX',#TPG房地产金融信托
'HELE',#海伦特洛伊家电
'WBIY',#WBI Power Factor High Dividend
'INDB',#美国独立银行
'UFPT',#UFP Technologies Inc
'OOTO',#Direxion Daily Travel & Vacatio
'RGCO',#RGC Resources Inc
'GPMT_A',#Granite Point Mortgage Trust In
'REMX',#稀土战略原料ETF-VanEck Vectors
'SAMT',#Strategas Macro Thematic Opport
'AVIE',#Avantis Inflation Focused Equit
'ISDX',#Invesco RAFI Strategic Develope
'PPT',#Putnam Premier Income Trust
'MXE',#The Mexico Equity and Income Fu
'VFVA',#Vanguard U.S. Value Factor ETF
'FXU',#First Trust Utilities AlphaDEX
'PDP',#Invesco DWA Momentum ETF
'APAM',#Artisan Partners Asset Manageme
'FCTR',#First Trust Lunt U.S. Factor Ro
'OFG',#OFG Bancorp
'HOTL',#Kelly Hotel & Lodging Sector ET
'GLRY',#Inspire Faithward Mid Cap Momen
'AZO',#汽车地带
'DRI',#达登饭店
'FLNG',#FLEX LNG Ltd
'RPG',#Invesco S&P 500 Pure Growth ETF
'FIX',#Comfort Systems USA Inc
'XRAY',#登士柏
'DJP',#大宗商品ETN-iPath
'SSO',#二倍做多标普500ETF-ProShares
'JPC',#Nuveen Preferred & Income Oppor
'XTN',#SPDR S&P Transportation ETF
'AEO',#美鹰傲飞
'FDL',#First Trust Morningstar ETF
'TGH',#Textainer Group Holdings Ltd
'DIVZ',#TrueShares Low Volatility Equit
'FNCB',#FNCB Bancorp Inc
'WSC',#WillScot Mobile Mini Holdings C
'TRHC',#Tabula Rasa HealthCare Inc
'BBY',#百思买
'XCOR',#FundX ETF
'MHK',#莫霍克工业
'PSCU',#Invesco S&P SmallCap Utilities
'ADT',#ADT Inc
'BCIM',#abrdn Bloomberg Industrial Meta
'RPT',#RPT Realty
'RWK',#Invesco S&P MidCap 400 Revenue
'CW',#寇蒂斯莱特
'IDU',#iShares U.S. Utilities ETF
'MITT_B',#AG Mortgage Investment Trust In
'JJC',#铜ETN-iPath
'SLVM',#Sylvamo Corp
'ESEA',#Euroseas Ltd
'AIHS',#森淼科技
'PLNT',#Planet Fitness Inc-A
'NNN',#National Retail Properties Inc
'GLPI',#Gaming and Leisure Properties I
'BWNB',#Babcock & Wilcox Enterprises In
'JBLU',#捷蓝航空
'EDI',#Virtus Stone Harbor Emerging Ma
'SNA',#实耐宝
'RYI',#Ryerson Holding Corp
'ICL',#ICL Group Ltd
'AMH',#American Homes 4 Rent-A
'WERN',#沃纳企业
'PVBC',#Provident Bancorp Inc (MD)
'GEL',#Genesis Energy LP
'NUGT',#二倍做多金矿指数ETF-Direxion
'ARC',#美国图文
'BRKL',#布鲁克赖恩银行
'MTUM',#iShares Edge MSCI USA Momentum
'SIL',#Global X Silver Miners ETF
'LYFT',#Lyft Inc-A
'GII',#SPDR S&P Global Infrastructure
'AMTB',#Amerant Bancorp Inc-A
'BWA',#博格华纳
'FOX',#福克斯-B
'PID',#Invesco International Dividend
'IPKW',#Invesco International BuyBack A
'PATI',#Patriot Transportation Holding
'DMA',#Destra Multi-Alternative Fund
'SFNC',#Simmons First National Corp
'ONB',#Old National Bancorp
'SCCF',#Sachem Capital Corp Notes
'ARNC',#Arconic Corp
'EBF',#恩尼斯
'TRC',#Tejon Ranch Co
'HAYW',#Hayward Holdings Inc
'FRT',#FRT信托
'WMPN',#William Penn Bancorp
'STRR',#Star Equity Holdings Inc
'DXGE',#WisdomTree Germany Hedged Equit
'CLM',#Cornerstone Strategic Value Fun
'MAT',#美泰
'CPK',#切萨皮克气业
'BIDS',#Amplify Digital & Online Tradin
'PNNT',#PennantPark Investment Corp
'TDS_U',#Telephone and Data Systems Inc
'RKLB',#Rocket Lab USA Inc-A
'SPDV',#AAM S&P 500 High Dividend Value
'CSB',#VictoryShares US Small Cap High
'RFG',#Invesco S&P MidCap 400 Pure Gro
'INTZ',#Intrusion Inc
'JLL',#仲量联行
'BBSI',#巴瑞特商业服务
'SON',#Sonoco Products Co
'UMBF',#UMB金融
'HIPS',#GraniteShares HIPS US High Inco
'FTDS',#First Trust Dividend Strength E
'ICNC_U',#Iconic Sports Acquisition Corp
'FLN',#First Trust Latin America Alpha
'COOP',#Mr. Cooper Group Inc
'PST',#ProShares UltraShort Lehman 7-1
'MRIN',#Marin Software Inc
'DIV',#Global X Super Dividend ETF
'GDXJ',#金矿小型股ETF-VanEck Vectors
'NEE_Q',#NextEra Energy Inc Units
'MLNK',#MeridianLink Inc
'ODP',#欧迪办公
'CM',#加拿大帝国商业银行
'NMRD',#Nemaura Medical Inc
'LFT',#Lument Finance Trust Inc
'SKT',#Tanger Factory Outlet Centers I
'NI',#尼索思
'GABC',#德美银行
'EDIV',#SPDR S&P Emerging Markets Divid
'DHS',#WisdomTree U.S. High Dividend F
'SBGI',#辛克莱广播
'LILA',#Liberty Latin America Ltd-A
'CBU',#Community Bank System Inc
'DON',#WisdomTree U.S. MidCap Dividend
'EIX',#爱迪生国际
'SBRA',#Sabra Health Care REIT Inc
'ONEY',#SPDR Russell 1000 Yield Focus E
'SKM',#韩国SK电信
'SEV',#Sono Group NV
'AESR',#Anfield U.S. Equity Sector Rota
'NTST',#NetSTREIT Corp
'PHK',#PIMCO High Income Fund
'UTG',#Reaves Utility Income Fund
'OGN',#Organon & Co
'FBNC',#第一银行(卡罗莱纳州)
'BRSP',#BrightSpire Capital Inc-A
'GPK',#Graphic Packaging Holding Co
'CTAS',#信达思
'CARG',#CarGurus Inc-A
'ISCF',#iShares Edge MSCI Multifactor I
'SYNH',#Syneos Health Inc-A
'SGDJ',#Sprott Junior Gold Miners ETF
'CPT',#卡姆登物业信托
'NAVI',#Navient Corp
'BHP',#必和必拓(US ADR)
'APRN',#蓝围裙
'ECL',#艺康
'ESGR',#恩斯塔
'CB',#安达保险
'EZM',#WisdomTree U.S. MidCap Fund
'PMCB',#PharmaCyte Biotech Inc
'LSAF',#LeaderShares AlphaFactor US Cor
'TRNO',#Terreno Realty Corp
'CTR',#ClearBridge MLP and Midstream T
'AHH',#Armada Hoffler Properties Inc
'OWL',#Blue Owl Capital Inc-A
'HDV',#iShares Core High Dividend ETF
'BFOR',#Barron’s 400 ETF
'PRMW',#Primo Water Corp
'NMM',#Navios Maritime Partners LP
'FUTY',#Fidelity MSCI Utilities Index E
'AWR',#美洲国家水务
'CLBK',#Columbia Financial Inc
'UAA',#安德玛-A
'QQC',#Simplify Growth Equity Plus Con
'AMD',#超威半导体
'BKSC',#南卡罗来纳银行
'IX',#欧力士
'CELH',#燃力士控股
'CLH',#Clean Harbors Inc
'OPAL',#OPAL Fuels Inc-A
'ERIC',#爱立信
'MERC',#美世国际
'ICOW',#Pacer Developed Markets Interna
'RNSC',#Small Cap US Equity Select ETF
'RSG',#共和废品处理
'CWST',#Casella Waste Systems Inc-A
'XLU',#公用事业ETF-SPDR
'GTLS_B',#查特工业(优先股)
'HPF',#John Hancock Preferred Income F
'BRK_A',#伯克希尔哈撒韦-A
'SDHY',#PGIM Short Duration High Yield
'AMG',#AMG资管
'HERD',#Pacer Cash Cows Fund of Funds E
'IFRA',#iShares U.S. Infrastructure ETF
'CGNX',#康耐视
'CBT',#卡博特
'BKI',#Black Knight Inc
'YPS',#Arrow Reverse Cap 500 ETF
'HR',#医疗保健房地产信托
'DUK',#杜克能源
'RTM',#Invesco S&P 500 Equal Weight Ma
'SFM',#Sprouts Farmers Market Inc
'NLR',#核能ETF-VanEck Vectors
'WRLD',#环球验收
'IAA',#IAA Inc
'CCI',#冠城
'RYU',#Invesco S&P 500 Equal Weight Ut
'WABC',#西美银行
'IIM',#Invesco Value Municipal Income
'QDIV',#Global X S&P 500 Quality Divide
'HOLI',#和利时自动化
'WBS',#韦伯斯特金融
'MGMT',#Ballast Small/Mid Cap ETF
'CLLS',#Cellectis SA ADR
'HVAL',#ALPS Hillman Active Value ETF
'SPVU',#Invesco S&P 500 Enhanced Value
'EWRE',#Invesco S&P 500 Equal Weight Re
'R',#莱德系统
'PKG',#美国包装
'XSLV',#Invesco S&P SmallCap Low Volati
'SLAB',#芯科实验室
'FNTC',#Direxion Daily FinTech Bull 2X
'DLR',#数字房地产信托
'PSCD',#Invesco S&P SmallCap Consumer D
'BANR',#邦纳
'NMRK',#Newmark Group Inc-A
'MOB',#Mobilicom Ltd ADR
'MLTX',#MoonLake Immunotherapeutics-A
'INOD',#Innodata Inc
'CTSH',#高知特
'WSBC',#韦斯银行
'EVX',#VanEck Environmental Services E
'VFMF',#Vanguard U.S. Multifactor ETF
'HBAN',#亨廷顿银行
'ONEO',#SPDR Russell 1000 Momentum Focu
'DGP',#二倍做多黄金ETN-DB
'MSB',#美莎比信托
'MBINN',#Merchants Bancorp Series C Pfd
'TRTN_B',#Triton International Ltd Series
'MO',#奥驰亚集团
'MIXT',#MiX Telematics Ltd ADR
'NEU',#NewMarket Corp
'ALK',#阿拉斯加航空
'JHAA',#Nuveen High Income 2023 Target
'FUL',#富乐
'ATI',#阿勒格尼技术
'EWMC',#Invesco S&P MidCap 400 Equal We
'DTIL',#Precision BioSciences Inc
'CHCI',#康斯托克控股
'BON',#天美生物
'IEUS',#iShares MSCI Europe Small-Cap E
'OHI',#Omega Healthcare Investors Inc
'NEE',#新纪元能源
'HIG',#哈特福德金融
'PPI',#AXS Astoria Inflation Sensitive
'UHAL_B',#U-Haul Holding Co-N
'NS_C',#NuStar Energy LP Series C Pfd
'DVY',#股息指数ETF-iShares
'WSFS',#WSFS金融
'DDM',#二倍做多道指ETF-ProShares
'FEMS',#First Trust Emerging Markets Sm
'SEE',#希悦尔
'DIAX',#Nuveen Dow 30SM Dynamic Overwri
'VPU',#公用事业指数ETF-Vanguard
'AEPPZ',#American Electric Power Co Inc
'DFAT',#Dimensional U.S. Targeted Value
'OMFL',#Invesco Russell 1000 Dynamic Mu
'PWS',#Pacer WealthShield ETF
'REGL',#ProShares S&P MidCap 400 Divide
'ISTR',#Investar Holding Corp
'PSR',#Invesco Active U.S. Real Estate
'TCBX',#Third Coast Bancshares Inc
'DBB',#基础金属ETF-PowerShares
'CAT',#卡特彼勒
'VNO_O',#Vornado Realty Trust Series O P
'SLP',#Simulations Plus Inc
'THRY',#Thryv Holdings Inc
'CRNC',#Cerence Inc
'LKQ',#LKQ Corp
'IEDI',#iShares U.S. Consumer Focused E
'SMIG',#AAM Bahl & Gaynor Small/Mid Cap
'HROWL',#Harrow Health Inc Notes
'CNDT',#Conduent Inc
'BEN',#富兰克林资源
'PSCM',#Invesco S&P SmallCap Materials
'HGER',#Harbor All-Weather Inflation Fo
'EATZ',#AdvisorShares Restaurant ETF
'ELP',#Companhia Paranaense de Energia
'DB',#德意志银行
'VLT',#Invesco High Income Trust II
'CALF',#Pacer US Small Cap Cash Cows 10
'DGRS',#WisdomTree U.S. SmallCap Qualit
'EGBN',#伊格尔合众银行
'RVT',#Royce Value Trust
'RPV',#Invesco S&P 500 Pure Value ETF
'XLC',#The Communication Services Sele
'DSMC',#Distillate Small/Mid Cash Flow
'REIT',#ALPS Active REIT ETF
'DWCR',#Arrow Investments Trust Arrow D
'TRIB',#Trinity Biotech plc ADR
'BYD',#博伊德赌场
'EMN',#伊士曼化工
'JJN',#镍ETN-iPath
'CCOI',#Cogent通信
'NFBK',#Northfield Bancorp Inc
'CRF',#Cornerstone Total Return Fund
'BOAT',#SonicShares Global Shipping ETF
'LNT',#美国联合能源
'TPHD',#Timothy Plan High Dividend Stoc
'LOGI',#罗技
'PYZ',#Invesco DWA Basic Materials Mom
'VCTR',#Victory Capital Holdings Inc-A
'CNA',#CNA金融
'MOG_A',#穆格-A
'ESGRP',#Enstar Group Ltd Series D Pfd
'G',#简柏特
'NPK',#National Presto Industries Inc
'LUMN',#Lumen Technologies Inc
'BLMN',#Bloomin’ Brands Inc
'AMNB',#美国国家银行
'GOEX',#Global X Gold Explorers ETF
'RMR',#The RMR Group Inc-A
'PEAK',#Healthpeak Properties Inc
'FYT',#First Trust Small Cap Value Alp
'AGNCP',#AGNC Investment Corp Series F P
'IVCBU',#Investcorp Europe Acquisition C
'OC',#欧文斯科宁
'JJA',#iPath Series B Bloomberg Agricu
'JJM',#工业金属ETN-iPath
'B',#巴恩斯
'IMCR',#Immunocore Holdings plc ADR
'ISSC',#创新软件
'MFC',#宏利金融
'DGS',#WisdomTree Emerging Markets Sma
'PAX',#Patria Investments Ltd-A
'MFGP',#微焦点国际
'XMLV',#Invesco S&P MidCap Low Volatili
'IGD',#Voya Global Equity Dividend and
'SWX',#Southwest Gas Holdings Inc
'PSB_Z',#PS Business Parks Inc Series Z
'COLD',#Americold Realty Trust Inc
'WPM',#惠顿贵金属
'EWO',#奥地利ETF-iShares MSCI
'ERC',#Allspring Multi-Sector Income F
'TAP',#摩森康胜-B
'BAP',#Credicorp Ltd
'VALQ',#American Century STOXX U.S. Qua
'SMP',#Standard Motor Products Inc
'AESC',#爱依斯电力(普通单位)
'VBR',#Vanguard Small-Cap Value ETF
'DFLV',#Dimensional US Large Cap Value
'RNR_G',#RenaissanceRe Holdings Ltd Seri
'CAC',#卡姆登国家银行
'IIPR',#Innovative Industrial Propertie
'THG',#汉诺威保险
'KTH',#Structured Products Corp CorTS
'KLAC',#科磊
'OMFS',#Invesco Russell 2000 Dynamic Mu
'PNFP',#Pinnacle Financial Partners Inc
'HUBG',#枢纽集团
'AILV',#Alpha Intelligent - Large Cap V
'INVH',#Invitation Homes Inc
'UTES',#Virtus Reaves Utilities ETF
'SIRE',#Sisecam Resources LP
'MNDO',#思维终端科技
'EVEX',#Eve Holding Inc
'FCPT',#Four Corners Property Trust Inc
'KALU',#凯撒铝业
'CFR',#库伦佛寺银行
'AGX',#Argan Inc
'PACK',#Ranpak Holdings Corp-A
'FBIZ',#第一商业金融服务
'IROQ',#IF Bancorp Inc
'TPHE',#Timothy Plan High Dividend Stoc
'THO',#索尔工业
'SYRS',#Syros Pharmaceuticals Inc
'BSIG',#BrightSphere Investment Group I
'RGLD',#皇家黄金
'FTLS',#First Trust Long/Short Equity
'FINW',#FinWise Bancorp
'BALL',#鲍尔包装
'ATO',#Atmos Energy Corp
'WM',#美国废物管理
'WTM',#白山保险集团
'NRO',#Neuberger Berman Real Estate Se
'AEZS',#依特钠
'JRE',#Janus Henderson U.S. Real Estat
'DFUV',#Dimensional US Marketwide Value
'JYNT',#The Joint Corp
'FEP',#First Trust Europe AlphaDEX Fun
'DFSV',#Dimensional US Small Cap Value
'GNTX',#真泰克
'PIM',#Putnam Master Intermediate Inco
'NWG',#NatWest Group plc ADR
'ILAG',#Intelligent Living Application
'CF',#CF实业
'FBCV',#Fidelity Blue Chip Value ETF
'PSCC',#Invesco S&P SmallCap Consumer S
'ELD',#新兴市场地方债ETF-WisdomTree
'FCN',#FTI咨询
'ESNT',#Essent Group Ltd
'EAD',#Allspring Income Opportunities
'STBA',#S&T Bancorp Inc
'DEM',#新兴市场高股息ETF-WisdomTree
'MEOH',#梅赛尼斯
'DXR',#Daxor Corp
'AGOX',#Adaptive Alpha Opportunities ET
'WEC',#WEC能源
'SVAL',#iShares US Small Cap Value Fact
'BVXV',#Biondvax制药
'FNV',#Franco-Nevada Corp
'TFPM',#Triple Flag Precious Metals Cor
'KMED',#KraneShares Emerging Markets He
'DUOL',#多邻国
'STXV',#Strive 1000 Value ETF
'EDD',#Morgan Stanley Emerging Markets
'AGO',#保证担保
'SHBI',#Shore Bancshares Inc
'TCFC',#The Community Financial Corp
'PYPT',#AXS 1.5X PYPL Bull Daily ETF
'FISV',#费哲金融服务
'PEY',#Invesco High Yield Equity Divid
'MAR',#万豪国际
'RCKY',#Rocky Brands Inc
'WCN',#Waste Connections Inc
'MOLN',#Molecular Partners AG ADR
'CNTA',#Centessa Pharmaceuticals Plc AD
'TECK',#泰克资源
'GILT',#吉来特卫星网络
'WTMF',#WisdomTree Managed Futures Stra
'DUSA',#Davis Select U.S. Equity ETF
'UVE',#万全保险
'SOL',#瑞能新能源
'XSHD',#Invesco S&P SmallCap High Divid
'HLIO',#Helios Technologies Inc
'XSHQ',#Invesco S&P SmallCap Quality ET
'ASAN',#Asana Inc-A
'FWRD',#福沃运输
'CMCSA',#康卡斯特
'ICR_A',#InPoint Commercial Real Estate
'PEZ',#Invesco DWA Consumer Cyclicals
'DLB',#杜比实验室
'YELP',#Yelp Inc
'PSCF',#Invesco S&P SmallCap Financials
'FEX',#First Trust Large Cap Core Alph
'RESI',#Kelly Residential & Apartment R
'HTH',#希尔托普控股
'AMRX',#Amneal Pharmaceuticals Inc-A
'SPYD',#SPDR Portfolio S&P 500 High Div
'LSAT',#LeaderShares AlphaFactor Tactic
'MOS',#美盛
'MAA',#MAA房产信托
'AX',#Axos Financial Inc
'WTFCM',#Wintrust Financial Corp Series
'FFBC',#第一金融银行
'NUVA',#纽瓦索器材
'PRU',#保德信金融
'EEMD',#AAM S&P Emerging Markets High D
'DISV',#Dimensional International Small
'RA',#Brookfield Real Assets Income F
'SFBS',#ServisFirst Bancshares Inc
'SNPO',#Snap One Holdings Corp
'CVV',#CVD设备
'JPSE',#JPMorgan Diversified Return U.S
'GRC',#The Gorman-Rupp Co
'MRTN',#马尔登运输
'CVCO',#卡寇工业
'VRNT',#Verint Systems Inc
'VALE',#淡水河谷
'FRPH',#FRP Holdings Inc
'RVLV',#Revolve Group Inc-A
'FDEU',#First Trust Dynamic Europe Equi
'CTRE',#CareTrust REIT Inc
'ASET',#FlexShares Real Assets Allocati
'BMO',#蒙特利尔银行
'SDOG',#ALPS Sector Dividend Dogs ETF
'CSX',#CSX运输
'DFAR',#Dimensional US Real Estate ETF
'SFYX',#SoFi Next 500 ETF
'GPC',#通用配件
'PEB_E',#Pebblebrook Hotel Trust Series
'PBP',#Invesco S&P 500 BuyWrite ETF
'GSBC',#南方万通金控
'AVLV',#Avantis U.S. Large Cap Value ET
'FITE',#SPDR S&P Kensho Future Security
'EQRX',#EQRx Inc
'BWFG',#Bankwell Financial Group Inc
'TD',#道明银行
'SYNA',#Synaptics Inc
'CADE',#Cadence Bank
'BC_B',#Brunswick Corp Notes
'ICF',#房地产信托ETF-iShares
'FPRO',#Fidelity Real Estate Investment
'FCBC',#第一社区银行股份
'XLRE',#房地产ETF-SPDR
'NIE',#Virtus Equity & Convertible Inc
'FRME',#第一招商股份
'CRBG',#Corebridge Financial Inc
'VONV',#Vanguard Russell 1000 Value ETF
'SEDA',#SDCL EDGE Acquisition Corp-A
'FSMO',#Fidelity Small-Mid Cap Opportun
'FLQM',#Franklin U.S. Mid Cap Multifact
'GLTR',#abrdn Physical Precious Metals
'GM',#通用汽车
'USRT',#iShares Core U.S. REIT ETF
'CRTO',#科韬
'FTQI',#First Trust Nasdaq BuyWrite Inc
'QVMM',#Invesco S&P MidCap 400 QVM Mult
'VJET',#维捷
'HCOM',#Hartford Schroders Commodity St
'GRCL',#亘喜生物
'FTK',#Flotek工业
'BLD',#TopBuild Corp
'CUBI',#Customers Bancorp Inc
'JNPR',#瞻博网络
'SMLF',#iShares Edge MSCI Multifactor U
'FLFVU',#Feutune Light Acquisition Corp
'VNQ',#房地产信托指数ETF-Vanguard
'UTF',#Cohen & Steers Infrastructure F
'MPTI',#M-tron Industries Inc
'BLX',#拉丁美洲出口银行
'REET',#iShares Trust iShares Global RE
'ACA',#Arcosa Inc
'SWK',#史丹利百得
'PBJ',#食品饮料ETF-PowerShares
'WTS',#沃茨水工业
'SSRM',#SSR Mining Inc
'CRH',#CRH水泥(ADR)
'FXZ',#First Trust Materials AlphaDEX
'EIGR',#Eiger BioPharmaceuticals Inc
'EGIS',#2ndVote Society Defended ETF
'BCSF',#Bain Capital Specialty Finance
'ATXG',#盈喜集团
'HAS',#孩之宝
'HOMB',#Home BancShares Inc
'CPRT',#科帕特
'BIOX',#Bioceres Crop Solutions Corp
'ROCAU',#ROC Energy Acquisition Corp Uni
'PKBK',#帕克合众银行
'JPRE',#JPMorgan Realty Income ETF
'CHIH',#Global X MSCI China Health Care
'KRNY',#卡尼金融储蓄
'UIS',#优利系统
'CAKE',#起司工坊
'BBCA',#JPMorgan BetaBuilders Canada ET
'SBSI',#Southside Bancshares Inc
'LXP',#LXP Industrial Trust
'JPS',#Nuveen Preferred & Income Secur
'PLUS',#正羽科技
'VLY',#硅谷国家银行
'DWAW',#AdvisorShares Dorsey Wright FSM
'JJG',#iPath Series B Bloomberg Grains
'AMT',#美国电塔
'RFV',#Invesco S&P MidCap 400 Pure Val
'UTRN',#Vesper U.S. Large Cap Short-Ter
'CDC',#VictoryShares US EQ Income Enha
'LTL',#ProShares Ultra Telecommunicati
'TCX',#Tucows Inc
'CFA',#VictoryShares US 500 Volatility
'PATK',#Patrick Industries Inc
'TEVA',#梯瓦制药
'QARP',#Xtrackers Russell 1000 US Quali
'PKE',#帕克航空航天
'CUZ',#卡津斯不动产
'AER',#AerCap飞机租赁
'UWM',#二倍做多罗素2000ETF-ProShares
'FITB',#五三银行
'SXT',#Sensient Technologies Corp
'PSCI',#Invesco S&P SmallCap Industrial
'IP',#国际纸业
'AUSF',#Global X Adaptive U.S. Factor E
'DFE',#欧洲小型红利股ETF-WisdomTree
'GSHD',#Goosehead Insurance Inc-A
'ABM',#ABM工业
'HEWC',#iShares Currency Hedged MSCI Ca
'HAUS',#Residential REIT Income ETF
'FNB_E',#F.N.B. Corp Series E Pfd
'MPWR',#Monolithic Power Systems Inc
'VLU',#SPDR S&P 1500 Value Tilt ETF
'AVAL',#Grupo Aval Acciones y Valores S
'PFL',#PIMCO Income Strategy Fund
'PINE',#Alpine Income Property Trust In
'FM',#前沿市场100ETF-iShares MSCI
'VICE',#AdvisorShares Vice ETF
'SBAC',#SBA通信-A
'ALEX',#亚历山大&鲍德温
'ESAB',#ESAB Corp
'WTW',#Willis Towers Watson PLC
'FNDA',#Schwab Fundamental U.S. Small C
'URG',#Ur-能源
'NGG',#英国国家电网
'MRC',#MRC Global Inc
'FXD',#可选消费ETF-FirstTrust AlphaDEX
'QABA',#First Trust NASDAQ ABA Communit
'FLR',#福陆
'TMP',#Tompkins Financial Corp
'PRGS',#Progress Software Corp
'HOPE',#Hope Bancorp Inc
'JPUS',#JPMorgan Diversified Return U.S
'IYR',#美国房地产ETF-iShares
'SHYD',#VanEck ETF Trust VanEck Short H
'COST',#开市客
'UDR',#UDR不动产信托
'STAG',#STAG Industrial Inc
'HAFC',#韩美金融
'SLYV',#SPDR S&P 600 Small Cap Value ET
'FDM',#First Trust DJ Select MicroCap
'DERM',#Journey Medical Corp
'DBEH',#iMGP DBi Hedge Strategy ETF
'RBLD',#First Trust Alerian U.S. NextGe
'FOXA',#福克斯-A
'FNY',#First Trust Mid Cap Growth Alph
'UZE',#US Cellular Corp Notes
'FTXG',#First Trust Nasdaq Food & Bever
'MBCC',#Monarch Blue Chips Core ETF
'DX',#德尼克斯投资
'BANX',#ArrowMark金融
'GIII',#G-III Apparel Group Ltd
'SMLV',#SPDR SSGA US Small Cap Low Vola
'JBT',#约翰宾技术
'BYRE',#Principal Real Estate Active Op
'JPME',#JPMorgan Diversified Return U.S
'RNP',#Cohen & Steers REIT and Preferr
'SCI',#Service Corp International
'VFMO',#Vanguard U.S. Momentum Factor E
'EWCO',#Invesco S&P 500 Equal Weight Co
'RTH',#零售ETF-VanEck Vectors
'ALCO',#阿里科
'CFO',#VictoryShares US 500 Enhanced V
'STVN',#Stevanato Group SpA
'OCFC',#OceanFirst Financial Corp
'ENV',#Envestnet Inc
'PSC',#Principal U.S. Small-Cap Multi-
'AAP',#Advance Auto Parts Inc
'EQNR',#Equinor ASA ADR
'KBUY',#KraneShares CICC China Consumer
'AWI',#阿姆斯特朗
'FBZ',#First Trust Brazil AlphaDEX Fun
'ACGL',#艾奇资本
'IVAL',#Alpha Architect International Q
'DVYA',#iShares Asia /Pacific Dividend
'TRMK',#Trustmark Corp
'RWR',#SPDR Dow Jones REIT ETF
'MCBS',#MetroCity Bankshares Inc
'IWS',#罗素中型价值股ETF-iShares
'ELME',#Elme Communities Trust
'BQ',#波奇宠物
'VMOT',#Alpha Architect Value Momentum
'SIVR',#Aberdeen Standard Physical Silv
'FXP',#二倍做空FTSE中国50指数ETF
'TRTN',#Triton International Ltd
'FEMB',#First Trust Emerging Markets Lo
'GREI',#Goldman Sachs Future Real Estat
'SUI',#Sun Communities Inc
'BFH',#Bread Financial Holdings Inc
'FCPI',#Fidelity Stocks for Inflation E
'EQTY',#Kovitz Core Equity ETF
'WELL',#Welltower Inc
'BY',#署名银行
'LARK',#兰德马克银行
'EDOG',#ALPS Emerging Sector Dividend D
'NSC',#诺福克南方
'JXI',#全球公用事业ETF-iShares
'SCHH',#Schwab U.S. REIT ETF
'KSCD',#KFA Small Cap Quality Dividend
'SGRP',#SPAR Group Inc
'GTIM',#恋上餐厅
'THD',#泰国ETF-iShares MSCI
'LMT',#洛克希德马丁
'ISCV',#iShares Morningstar Small-Cap V
'PRF',#Invesco FTSE RAFI US 1000 ETF
'FVC',#First Trust Dorsey Wright Dynam
'CBSH',#科默斯银行
'ELV',#Elevance Health Inc
'PY',#Principal Shareholder Yield Ind
'CSF',#VictoryShares US Discovery Enha
'FYLD',#Cambria Foreign Shareholder Yie
'AGNCO',#AGNC Investment Corp Series E P
'FLQS',#Franklin U.S. Small Cap Multifa
'OGS',#ONE Gas Inc
'JJT',#锡ETN-iPath
'HAIN',#海恩时富
'NVQ',#QRAFT AI-Enhanced U.S. Next Val
'FTA',#First Trust Large Cap Value Alp
'EVMT',#Invesco Electric Vehicle Metals
'AIF',#Apollo Tactical Income Fund
'HD',#家得宝
'KOP',#科佩斯控股
'ABEQ',#Absolute Select Value ETF
'BLHY',#Virtus Newfleet High Yield Bond
'SMOT',#VanEck Morningstar SMID Moat ET
'BBRE',#JPMorgan BetaBuilders MSCI US R
'IAK',#iShares U.S. Insurance ETF
'FAD',#First Trust Multi Cap Growth Al
'SPHD',#Invesco S&P 500 High Dividend L
'SEIM',#SEI Enhanced U.S. Large Cap Mom
'AAM_B',#Apollo Asset Management Inc Ser
'AVIV',#Avantis International Large Cap
'PM',#菲利普莫里斯国际
'DG',#达乐
'LGI',#Lazard Global Total Return and
'COE',#51Talk
'NMR',#野村控股
'CVLY',#科多勒斯谷万通金控
'DYNF',#BlackRock U.S. Equity Factor Ro
'FNK',#First Trust Mid Cap Value Alpha
'PVAL',#Putnam Focused Large Cap Value
'CUBS',#Asian Growth Cubs ETF
'LBAY',#Leatherback Long/Short Alternat
'RH',#RH
'VTWV',#Vanguard Russell 2000 Value ETF
'MYNA',#Mynaric AG ADR
'IAG',#IAMGOLD Corp
'BPYPN',#Brookfield Property Partners LP
'APWC',#亚太电线电缆
'IFGL',#iShares International Developed
'FHI',#联邦投资
'RINF',#ProShares Inflation Expectation
'J',#Jacobs Solutions Inc
'SMDV',#ProShares Russell 2000 Dividend
'CRESY',#Cresud ADR
'USB',#美国合众银行
'KBWY',#高股息房地产信托ETF-PowerShares
'FCCO',#第一社区(南卡州)
'SRC',#Spirit Realty Capital Inc
'BMRA',#Biomerica Inc
'CTVA',#Corteva Inc
'WIRE',#Encore Wire Corp
'ROSC',#Hartford Multifactor Small Cap
'FRDM',#Freedom 100 Emerging Markets ET
'CTLT',#Catalent Inc
'YOSH',#Yoshiharu Global Co-A
'NCPL',#Netcapital Inc
'MDYG',#SPDR S&P 400 Mid Cap Growth ETF
'CEG',#Constellation Energy Corp
'SPNE',#海脊控股
'RBB',#RBB银行
'VOX',#电信业指数ETF-Vanguard
'DLY',#DoubleLine Yield Opportunities
'BPYPO',#Brookfield Property Partners LP
'FREL',#Fidelity MSCI Real Estate Index
'ION',#ProShares S&P Global Core Batte
'DEUS',#Xtrackers Russell US Multifacto
'VNMC',#Natixis Vaughan Nelson Mid Cap
'CPB',#金宝汤
'ABR',#阿伯房地产信托
'FXG',#日常消费ETF-FirstTrust AlphaDEX
'ITW',#伊利诺伊机械
'DESP',#Despegar.com Corp
'AMCI',#AMCI Acquisition Corp II-A
'VIOV',#Vanguard S&P Small-Cap 600 Valu
'MCN',#Madison Covered Call & Equity S
'ISVL',#iShares Trust iShares Internati
'CZA',#Invesco Zacks Mid-Cap ETF
'ESLT',#埃尔比特系统
'MEGI',#MainStay CBRE Global Infrastruc
'PRFZ',#Invesco FTSE RAFI US 1500 Small
'EPHE',#菲律宾ETF-iShares MSCI
'CSD',#Invesco S&P Spin-Off ETF
'IYT',#道琼斯运输业指数ETF-iShares
'FLS',#福斯
'FUNL',#CornerCap Fundametrics Large-Ca
'TAC',#TransAlta Corp
'TRTN_D',#Triton International Ltd Series
'EMD',#Western Asset Emerging Markets
'U',#Unity Software Inc
'SEIV',#SEI Enhanced U.S. Large Cap Val
'TPC',#Tutor Perini Corp
'RTX',#雷神技术
'USLB',#Invesco Russell 1000 Low Beta E
'SBI',#Western Asset Intermediate Muni
'ARE',#亚历山大房地产
'UNH',#联合健康
'USMF',#WisdomTree U.S. Multifactor Fun
'NHC',#National HealthCare Corp
'CPLP',#Capital Product Partners LP
'KWR',#奎克化学
'AVUS',#Avantis U.S. Equity ETF
'AA',#美国铝业
'PAHC',#美国辉宝
'MMD',#MainStay MacKay DefinedTerm Mun
'YORW',#约克自来水
'RDOG',#ALPS REIT Dividend Dogs ETF
'UPS',#联合包裹服务
'EDEN',#MSCI丹麦ETF-iShares
'SOYB',#大豆ETF-Teucrium
'CRIT',#Optica Rare Earths & Critical M
'FRI',#房地产信托指数ETF-First Trust
'SXI',#Standex International Corp
'PBDM',#Invesco PureBeta FTSE Developed
'SBFG',#SB Financial Group Inc
'AMSF',#AMERISAFE Inc
'KNW',#Know Labs Inc
'BVS',#Bioventus Inc-A
'MOO',#农业ETF-VanEck Vectors
'CMA',#联信银行
'DVAL',#BrandywineGLOBAL – Dynamic US
'PEJ',#休闲娱乐ETF-PowerShares
'OCAXU',#OCA Acquisition Corp Unit Cons
'SYBT',#Stock Yards Bancorp Inc
'AIVL',#WisdomTree U.S. AI Enhanced Val
'KBR',#KBR科技
'NWBI',#Northwest Bancshares Inc
'ORI',#Old Republic International Corp
'PPTY',#U.S. Diversified Real Estate ET
'JOET',#Virtus Terranova U.S. Quality M
'CMRA',#Comera Life Sciences Holdings I
'MSM',#MSC Industrial Direct Co Inc-A
'XUSP',#Innovator Uncapped Accelerated
'FC',#富兰克林柯维
'BUFG',#FT Cboe Vest Buffered Allocatio
'MAC',#马塞里奇房产
'META',#Meta Platforms Inc-A
'HRT',#HireRight Holdings Corp
'HMC',#本田汽车
'CRNX',#Crinetics Pharmaceuticals Inc
'IPAY',#移动支付ETF-PureFunds ISE
'IVEG',#iShares Emergent Food and AgTec
'EYLD',#Cambria ETF Trust Cambria Emerg
'WTRG',#Essential Utilities Inc
'SPRE',#SP Funds S&P Global REIT Sharia
'CENQ',#CENAQ Energy Corp-A
'FDVV',#Fidelity High Dividend ETF
'DLR_L',#Digital Realty Trust Inc Series
'AFYA',#Afya Ltd-A
'CRAI',#CRA国际
'USEQ',#Invesco Russell 1000 Enhanced E
'VOE',#Vanguard Mid-Cap Value ETF
'GNL',#Global Net Lease Inc
'ONEV',#SPDR Russell 1000 Low Volatilit
'FXR',#First Trust Industrials AlphaDE
'DTD',#WisdomTree U.S. Total Dividend
'FBGX',#FI Enhanced Large Cap Growth ET
'NETZ',#Engine No. 1 Transform Climate
'WMS',#Advanced Drainage Systems Inc
'RS',#Reliance Steel & Aluminum Co
'TAK',#武田制药
'IWIN',#Amplify Inflation Fighter ETF
'IGTR',#Innovator Gradient Tactical Rot
'EFX',#艾可菲
'AZZ',#AZZ Inc
'FMAT',#Fidelity MSCI Materials Index E
'NU',#Nu Holdings Ltd-A
'AFTY',#Pacer CSOP FTSE China A50 ETF
'PKX',#浦项钢铁
'OMI',#欧麦斯-麦能医疗
'BTHM',#BlackRock Future U.S. Themes ET
'AMID',#Argent Mid Cap ETF
'NOM',#Nuveen Missouri Quality Municip
'FGD',#First Trust DJ Global Select Di
'XDJL',#Innovator U.S. Equity Accelerat
'NWL',#纽威品牌
'MPRO',#Monarch ProCap ETF
'FYBR',#前线通信
'HYXU',#iShares International High Yiel
'PAK',#巴基斯坦ETF-Global X MSCI
'ARL',#美国房地产投资
'DTRE',#First Trust Alerian Disruptive
'IJS',#iShares S&P Small-Cap 600 Value
'SPXT',#ProShares S&P 500 Ex-Technology
'VAW',#Vanguard Materials ETF
'PPHP',#PHP Ventures Acquisition Corp-A
'VYM',#高股息指数ETF-Vanguard
'GYLD',#Arrow Dow Jones Global Yield ET
'TSN',#泰森食品
'OUSM',#ALPS O'Shares U.S. Small-Cap Qu
'CSTM',#Constellium SE-A
'WPP',#WPP集团(US ADR)
'VGI',#Virtus Global Multi-Sector Inco
'BTI',#英美烟草
'BFC',#Bank First Corp
'DXJ',#日本证券汇率对冲ETF-WisdomTree
'EQL',#ALPS Equal Sector Weight ETF
'TEQI',#T. Rowe Price Equity Income ETF
'BX',#黑石集团
'MMS',#马克西姆斯
'AME',#阿美特克
'HIBL',#Direxion Daily S&P 500 High Bet
'AOD',#abrdn Total Dynamic Dividend Fu
'SIXS',#ETC 6 Meridian Small Cap Equity
'SCCG',#Sachem Capital Corp Notes
'MDV_A',#Modiv Inc Series A Pfd
'AVDV',#Avantis International Small Cap
'GOODO',#格拉德斯通商业(优先股)
'GDIV',#Harbor Dividend Growth Leaders
'DFNL',#Davis Select Financial ETF
'PCF',#High Income Securities Fund
'LECO',#林肯电气
'SJT',#San Juan Basin Royalty Trust
'DFS',#探索金融服务
'PLM',#PolyMet Mining Corp
'FTCH',#Farfetch Ltd-A
'MDY',#标普中型股400ETF-SPDR
'SCHL',#学乐教育
'TSME',#Thrivent Small-Mid Cap ESG ETF
'TTAI',#FCF International Quality ETF
'BROG',#Brooge Energy Ltd
'TROW',#普信集团
'SRVR',#Pacer Data & Infrastructure Rea
'IDMO',#Invesco S&P International Devel
'TBLA',#Taboola.com Ltd
'ELS',#宜居生活资产信托
'INFA',#Informatica Inc-A
'UBP_K',#Urstadt Biddle Properties Inc S
'EFSC',#Enterprise Financial Services C
'IJT',#iShares S&P Small-Cap 600 Growt
'FIG',#Simplify Macro Strategy ETF
'RY',#加拿大皇家银行
'KO',#可口可乐
'FXA',#澳元ETF-CurrencyShares
'RTLPO',#The Necessity Retail REIT Inc S
'TMFM',#Motley Fool Mid-Cap Growth ETF
'CSWC',#西南资本
'XDOC',#Innovator U.S. Equity Accelerat
'TKR',#铁姆肯
'SRHQ',#SRH U.S. Quality ETF
'FNDX',#Schwab Fundamental U.S. Large C
'XME',#金属采矿ETF-SPDR
'YCS',#二倍做空日元ETF-ProShares
'SMMV',#iShares Trust ETF
'EQAL',#Invesco Russell 1000 Equal Weig
'APO',#阿波罗全球管理
'HOV',#霍夫纳尼安
'SWAG',#Stran & Co Inc
'NCRA',#Nocera Inc
'IDE',#Voya Infrastructure, Industrial
'CLNE',#Clean Energy Fuels Corp
'SNPD',#Xtrackers S&P ESG Dividend Aris
'EGP',#EastGroup Properties Inc
'REZ',#住宅房产信托ETF-iShares
'JHSC',#John Hancock Multifactor Small
'GFL',#GFL Environmental Inc
'TWO',#Two Harbors Investment Corp
'FCOM',#Fidelity MSCI Communication Ser
'FDT',#First Trust Developed Markets E
'BULZ',#MicroSectors FANG & Innovation
'JAVA',#JPMorgan Active Value ETF
'FNDB',#Schwab Fundamental U.S. Broad M
'USVM',#VictoryShares US Small Mid Cap
'BEDZ',#AdvisorShares Hotel ETF
'RFFC',#RiverFront Dynamic US Flex-Cap
'THRX',#Theseus Pharmaceuticals Inc
'DFAC',#Dimensional U.S. Core Equity 2
'MGV',#Vanguard Mega Cap Value ETF
'MTW',#马尼托沃克
'ADP',#自动数据处理
'NUMV',#Nuveen ESG Mid-Cap Value ETF
'PSP',#全球私募股权基金ETF-PowerShares
'NTRS',#北方信托
'SSPY',#Syntax Stratified LargeCap ETF
'VIOO',#Vanguard S&P Small-Cap 600 ETF
'LGL',#The LGL Group Inc
'DOV',#都福
'PWB',#Invesco Dynamic Large Cap Growt
'QDYN',#FlexShares Quality Dynamic Inde
'PRIF_G',#Priority Income Fund Inc Series
'XMHQ',#Invesco S&P MidCap Quality ETF
'PSMG',#Invesco Growth Multi-Asset Allo
'MIDE',#Xtrackers S&P MidCap 400 ESG ET
'HBIO',#哈佛生物科学
'SLV',#白银ETF-iShares
'BBW',#Build-A-Bear Workshop Inc
'WFC',#富国银行
'TGH_B',#Textainer Group Holdings Ltd Se
'NEM',#纽蒙特
'QVMS',#Invesco S&P SmallCap 600 QVM Mu
'PNBK',#爱国者国家银行
'ULH',#环球物流控股
'FLYW',#Flywire Corp
'LRCX',#拉姆研究
'SKYH',#Sky Harbour Group Corp-A
'ALRS',#Alerus Financial Corp
'CHDN',#Churchill Downs Inc
'HON',#霍尼韦尔(US)
'BOKF',#博克金融
'AVRE',#Avantis Real Estate ETF
'BCI',#Abrdn Bloomberg All Commodity S
'CMLS',#Cumulus Media Inc-A
'UGIC',#UGI Corp Corporate Units
'RWL',#Invesco S&P 500 Revenue ETF
'SPMD',#SPDR Portfolio S&P 400 Mid Cap
'SMLR',#Semler Scientific Inc
'IPI',#Intrepid Potash Inc
'SRET',#Global X SuperDividend REIT ETF
'PCAR',#帕卡
'SLM',#学贷美
'DLN',#WisdomTree U.S. LargeCap Divide
'FAF',#第一美国
'MSA',#MSA Safety Inc
'PRN',#Invesco DWA Industrials Momentu
'FRTX',#Fresh Tracks Therapeutics Inc
'FCT',#First Trust Senior Floating Rat
'FEUZ',#First Trust Eurozone AlphaDEX E
'AVB',#艾芙隆海湾社区
'DAL',#达美航空
'DCGO',#DocGo Inc
'KBWD',#Invesco KBW High Dividend Yield
'VONE',#Vanguard Russell 1000 ETF
'DTH',#WisdomTree International High D
'NKTX',#Nkarta Inc
'DOL',#WisdomTree International LargeC
'MMTM',#SPDR S&P 1500 Momentum Tilt ETF
'HUSV',#First Trust Horizon Managed Vol
'MGA',#麦格纳国际
'DFIV',#Dimensional International Value
'DFAS',#Dimensional U.S. Small Cap ETF
'ORC',#Orchid Island Capital Inc
'USFD',#美国食品控股
'FRO',#Frontline Ltd
'CGABL',#Carlyle Group Inc Notes
'ED',#爱迪生联合电气
'ORA',#奥玛特科技
'KIO',#KKR Income Opportunities Fund
'FLO',#花苑食品
'TPVG',#TriplePoint Venture Growth BDC
'TNET',#TriNet Group Inc
'IBOC',#国际银行
'TMDV',#ProShares Russell U.S. Dividend
'AY',#Atlantica Sustainable Infrastru
'PACW',#PacWest Bancorp
'OVS',#Overlay Shares Small Cap Equity
'AFMC',#First Trust Active Factor Mid C
'MIN',#MFS Intermediate Income Trust
'SPXV',#ProShares S&P 500 Ex-Health Car
'SNPV',#Xtrackers S&P ESG Value ETF
'XRLV',#Invesco S&P 500 ex-Rate Sensiti
'HKND',#Humankind US Stock ETF
'PBPB',#Potbelly Corp
'FSS',#联邦信号
'TPZ',#Tortoise Power and Energy Infra
'SIXA',#ETC 6 Meridian Mega Cap Equity
'ENR',#劲量控股
'TPLE',#Timothy Plan US Large/Mid Cap C
'IJK',#标普中型成长股400ETF-iShares
'XDSQ',#Innovator ETFs Trust Innovator
'ALTL',#Pacer Lunt Large Cap Alternator
'AWK',#美国水业
'MDYV',#SPDR S&P 400 Mid Cap Value ETF
'RYN',#雷欧尼尔
'UJB',#ProShares Ultra High Yield ETF
'ESIX',#SPDR S&P SmallCap 600 ESG ETF
'ILCV',#iShares Morningstar Value ETF
'LVOX',#LiveVox Holdings Inc-A
'PUK',#英国保诚
'NLY',#Annaly Capital Management Inc
'PALC',#Pacer Lunt Large Cap Multi-Fact
'DLS',#WisdomTree International SmallC
'ACI',#艾伯森
'EWUS',#iShares MSCI United Kingdom Sma
'WKLY',#SoFi Weekly Dividend ETF
'PERF',#玩美
'TAGS',#Teucrium Agricultural Fund ETV
'IMTM',#iShares Edge MSCI Intl Momentum
'FXO',#First Trust Financials AlphaDEX
'SDY',#红利股ETF-SPDR S&P
'USLM',#United States Lime & Minerals I
'BLNG',#Belong Acquisition Corp-A
'HSMV',#First Trust Horizon Managed Vol
'IRT',#Independence Realty Trust Inc
'EQR',#公平住屋
'K',#家乐氏
'RIO',#力拓(US)
'VSMV',#VictoryShares US Multi-Factor M
'OPINL',#Office Properties Income Trust
'MLM',#马丁-玛丽埃塔材料
'RYJ',#Invesco Raymond James SB-1 Equi
'HNDL',#Strategy Shares Nasdaq 7HANDL I
'RDVI',#FT Cboe Vest Rising Dividend Ac
'SENEA',#Seneca Foods Corp-A
'HYLS',#First Trust Tactical High Yield
'BCC',#Boise Cascade Co
'ORAN',#法国电信
'SPHQ',#Invesco S&P 500 Quality ETF
'CHH',#精选国际酒店
'LLY',#礼来
'CATH',#Global X S&P 500 Catholic Value
'PKW',#Invesco BuyBack Achievers ETF
'ITA',#美国航天国防ETF-iShares
'VFQY',#Vanguard U.S. Quality Factor ET
'DDLS',#WisdomTree Dynamic Currency Hed
'FFIV',#F5
'IJH',#标普中型股ETF-iShares
'SPSM',#SPDR Portfolio S&P 600 Small Ca
'UBFO',#联合安全银行
'FDD',#First Trust Dow Jones STOXX Sel
'IWD',#罗素1000价值股ETF-iShares
'CLW',#克利尔沃特纸业
'PAMC',#Pacer Lunt MidCap Multi-Factor
'RCD',#Invesco S&P 500 Equal Weight Co
'NXG',#NXG NextGen Infrastructure Inco
'SCHV',#Schwab U.S. Large-Cap Value ETF
'EELV',#Invesco S&P Emerging Markets Lo
'SMLE',#Xtrackers S&P SmallCap 600 ESG
'EXFY',#Expensify Inc-A
'AAIC',#阿灵顿资产投资
'DFGR',#Dimensional Global Real Estate
'JETS',#航空ETF-US Global
'WBIG',#WBI BullBear Yield 3000 ETF
'PFEL',#AXS 2X PFE Bull Daily ETF
'EURN',#Euronav NV
'LEAD',#Reality Shares DIVCON Leaders D
'DXJS',#WisdomTree Japan Hedged SmallCa
'CDR_C',#Cedar Realty Trust Inc Series C
'GDDY',#GoDaddy Inc-A
'VMI',#维蒙特工业
'SPBC',#Simplify U.S. Equity PLUS GBTC
'HFXI',#IQ FTSE International Equity Cu
'AMYT',#Amryt Pharma plc ADR
'NDSN',#诺信
'PXF',#Invesco FTSE RAFI Developed Mar
'TWNK',#Hostess Brands Inc-A
'LHX',#L3Harris Technologies Inc
'FTVIU',#FinTech Acquisition Corp VI Uni
'SMR',#NuScale Power Corp-A
'EVOJ',#Evo Acquisition Corp-A
'FINX',#Global X FinTech ETF
'NFRA',#FlexShares STOXX Global Broad I
'BIT',#BlackRock Multi-Sector Income T
'RFDA',#RiverFront Dynamic US Dividend
'KLCD',#KFA Large Cap Quality Dividend
'GCOW',#Pacer Global Cash Cows Dividend
'CLAS',#Class Acceleration Corp-A
'ALL',#好事达保险
'HXL',#赫氏
'HWKN',#霍金斯材料
'CP',#加拿大太平洋铁路
'BANF',#BancFirst银行
'SDVY',#First Trust SMID Cap Rising Div
'GRPN',#Groupon Inc-A
'XLB',#基础材料ETF-SPDR
'AXON',#Axon Enterprise Inc
'DKRB',#Subversive Decarbonization ETF
'CPA',#科帕控股
'JRI',#Nuveen Real Asset Income and Gr
'PCG',#太平洋煤气电力
'FLQL',#Franklin U.S. Large Cap Multifa
'DEW',#WisdomTree Global High Dividend
'USA',#Liberty All-Star Equity Fund
'HEQ',#John Hancock Hedged Equity & In
'IUS',#Invesco RAFI Strategic US ETF
'HVT',#哈弗蒂家具
'AVGE',#Avantis All Equity Markets ETF
'VIAV',#Viavi Solutions Inc
'GQRE',#FlexShares Global Quality Real
'JHMM',#John Hancock Multifactor Mid Ca
'JJS',#软商品ETN-iPath
'IUSV',#iShares Core S&P U.S. Value ETF
'RWAYL',#Runway Growth Finance Corp Note
'WAT',#沃特世
'SNY',#赛诺菲
'PDCO',#帕特森
'CGDV',#Capital Group Dividend Value ET
'XLY',#可选消费ETF-SPDR
'CINF',#辛辛那提金融
'IVOV',#Vanguard S&P Mid-Cap 400 Value
'DVOL',#First Trust Dorsey Wright Momen
'ARR',#Armour住宅房产
'IWX',#iShares Russell Top 200 Value E
'WDIV',#SPDR S&P Global Dividend
'RMM',#RiverNorth Managed Duration Mun
'PPG',#PPG工业
'VTV',#价值股指数ETF-Vanguard
'SCD',#LMP Capital and Income Fund
'ESACU',#ESGEN Acquisition Corp Unit Con
'KOIN',#Capital Link Global Fintech Lea
'CUBB',#Customers Bancorp Inc Notes
'GSMG',#耀世星辉
'EOD',#Allspring Global Dividend Oppor
'IYZ',#美国电信ETF-iShares
'GDE',#WisdomTree Efficient Gold Plus
'ARMK',#Aramark
'SPYI',#NEOS S&P 500 High Income ETF
'FVD',#First Trust VL Dividend
'FPAG',#FPA Global Equity ETF
'MGNX',#MacroGenics Inc
'MCD',#麦当劳
'PTMC',#Pacer Trendpilot US Mid Cap ETF
'CNI',#加拿大国家铁路
'CVCY',#中央谷地
'FLLV',#Franklin U.S. Low Volatility ET
'TIMB',#TIM SA ADR
'AHH_A',#Armada Hoffler Properties Inc S
'ABR_E',#Arbor Realty Trust Inc Series E
'CSA',#VictoryShares US Small Cap Vola
'SFY',#SoFi Select 500 ETF
'XJH',#iShares ESG Screened S&P Mid-Ca
'POST',#Post Holdings Inc
'SPLV',#标普500低波幅ETF-PowerShares
'MXI',#iShares Global Materials ETF
'GSPY',#Gotham Enhanced 500 ETF
'VYMI',#Vanguard International High Div
'VFH',#金融指数ETF-Vanguard
'VMC',#火神材料
'FDV',#Federated Hermes U.S. Strategic
'SLY',#SPDR S&P 600 Small Cap ETF
'BITS',#Global X Blockchain & Bitcoin S
'IHG',#洲际酒店(US)
'DTSS',#数海信息
'TIPD',#Direxion Daily TIPS Bear 2X Sha
'PYPL',#PayPal Holdings Inc
'CHRW',#罗宾逊全球物流
'DHT',#DHT控股
'IVOO',#Vanguard S&P Mid-Cap 400 ETF
'DIVO',#Amplify CWP Enhanced Dividend I
'SZNE',#Pacer CFRA-Stovall Equal Weight
'SIXL',#ETC 6 Meridian Low Beta Equity
'RNMC',#Mid Cap US Equity Select ETF
'AMCR',#Amcor plc
'ARCK',#Arbor Rapha Capital Bioholdings
'LNKB',#LINKBANCORP Inc
'GRTX',#Galera Therapeutics Inc
'GREK',#希腊ETF-Global X MSCI
'IUSS',#Invesco RAFI Strategic US Small
'SCHD',#美元红利股ETF-Schwab
'XJR',#iShares ESG Screened S&P Small-
'BBMC',#JPMorgan BetaBuilders U.S. Mid
'AMBC',#Ambac Financial Group Inc
'RDVY',#First Trust Rising Dividend Ach
'SIGI',#Selective Insurance Group Inc
'AQGX',#AI Quality Growth ETF
'GWW',#固安捷
'ASB',#Associated Banc-Corp
'RF',#地区金融
'XPO',#XPO
'TILL',#Teucrium Agricultural Strategy
'REXR_C',#Rexford Industrial Realty Inc S
'VNAM',#Global X MSCI Vietnam ETF
'RECS',#Columbia Research Enhanced Core
'IMCV',#iShares Morningstar Mid-Cap Val
'MDB',#MongoDB Inc-A
'XTJA',#Innovator U.S. Equity Accelerat
'CPF',#中央太平洋银行
'ETJ',#Eaton Vance Risk-Managed Divers
'BBLU',#EA Bridgeway Blue Chip ETF
'IYM',#美国基础材料ETF-iShares
'UFPI',#UFP Industries Inc
'UCBI',#美国社区银行
'NAN',#Nuveen New York Quality Municip
'OPI',#Office Properties Income Trust
'KIE',#保险ETF-SPDR S&P
'HYGH',#iShares Interest Rate Hedged Hi
'SMDY',#Syntax Stratified MidCap ETF
'RGI',#Invesco S&P 500 Equal Weight In
'SBR',#Sabine Royalty Trust
'OFC',#Corporate Office Properties Tru
'LCLG',#Logan Capital Broad Innovative
'IOVA',#Iovance Biotherapeutics Inc
'IJR',#标普小型股ETF-iShares
'MEDP',#Medpace Holdings Inc
'PSL',#Invesco DWA Consumer Staples Mo
'KRE',#区域银行ETF-SPDR S&P
'DBJP',#Xtrackers MSCI Japan Hedged Equ
'SMBC',#Southern Missouri Bancorp Inc
'PLRG',#Principal U.S. Large-Cap Adapti
'FID',#First Trust S&P International D
'VCR',#可选消费指数ETF-Vanguard
'RITA',#ETFB Green SRI REITs ETF
'FLIC',#长岛第一国民银行
'VIOG',#Vanguard S&P Small-Cap 600 Grow
'MFUS',#PIMCO RAFI Dynamic Multi-Factor
'SOFI',#SoFi Technologies Inc
'METC',#Ramaco Resources Inc
'MET',#大都会人寿
'JMEE',#JPMorgan Market Expansion Enhan
'QVML',#Invesco S&P 500 QVM Multi-facto
'MWA',#Mueller Water Products Inc
'KF',#The Korea Fund
'CLRO',#ClearOne通讯
'AFGB',#American Financial Group Inc De
'AIT',#应用工业技术
'PGR',#前进保险
'IYC',#iShares U.S. Consumer Discretio
'CIEN',#Ciena科技
'WEN',#云狄斯快餐
'AFT',#Apollo Senior Floating Rate Fun
'NDVG',#Nuveen Dividend Growth ETF
'NSL',#Nuveen Senior Income Fund
'H',#凯悦酒店
'FDLS',#Inspire Fidelis Multi Factor ET
'NOK',#诺基亚
'THLV',#THOR Low Volatility ETF
'SBT',#Sterling Bancorp Inc
'IRWD',#Ironwood Pharmaceuticals Inc-A
'EMFM',#Global X MSCI Next Emerging & F
'SLF',#永明金融
'AFLG',#First Trust Active Factor Large
'WMG',#华纳音乐
'IDVO',#Amplify International Enhanced
'DMAC',#DiaMedica Therapeutics Inc
'ULVM',#VictoryShares US Value Momentum
'PJT',#PJT Partners Inc-A
'ETR',#安特吉
'VRSK',#Verisk分析
'FIDI',#Fidelity International High Div
'VTNR',#顶点能源
'FPI',#农田合伙基金
'ESG',#FlexShares STOXX US ESG Impact
'XFLT_A',#XAI Octagon Floating Rate & Alt
'QVOY',#Q3 All-Season Active Rotation E
'PRIF_K',#Priority Income Fund Inc Series
'PEP',#百事
'RIET',#Hoya Capital High Dividend Yiel
'XTJL',#Innovator U.S. Equity Accelerat
'HONE',#HarborOne Bancorp Inc
'PRAY',#FIS Biblically Responsible Risk
'NRIM',#Northrim BanCorp Inc
'DIVB',#iShares Core Dividend ETF
'KEY',#KeyCorp
'NOBL',#ProShares S&P 500 Dividend Aris
'LAMR',#拉马尔户外广告
'WRB',#WR柏克利
'SELV',#SEI Enhanced Low Volatility U.S
'ROUS',#Hartford Multifactor U.S. Equit
'BLES',#Inspire Global Hope ETF
'LRGF',#iShares Edge MSCI Multifactor U
'SIGIP',#Selective Insurance Group Inc S
'ADTN',#亚川
'SBLK',#Star Bulk Carriers Corp
'RSP',#标普500等权ETF-Guggenheim
'BFST',#Business First Bancshares Inc
'ASYS',#Amtech Systems Inc
'NOC',#诺斯罗普-格鲁曼(US)
'EWSC',#Invesco S&P SmallCap 600 Equal
'NWFL',#Norwood Financial Corp
'MISL',#First Trust Indxx Aerospace & D
'BCE',#加拿大贝尔
'RPRX',#Royalty Pharma plc-A
'KBWP',#Invesco KBW Property & Casualty
'DGT',#SPDR Global Dow ETF
'FLIY',#Franklin FTSE Italy ETF
'IAI',#iShares U.S. Broker-Dealers & S
'LGLV',#SPDR SSGA US Large Cap Low Vola
'RE',#艾弗再保险
'GS_D',#The Goldman Sachs Group Inc Ser
'MEI',#Methode Electronics Inc
'MGRC',#McGrath RentCorp
'IVAC',#因特瓦克
'UZD',#US Cellular Corp Notes
'VNO_L',#Vornado Realty Trust Series L P
'EWI',#意大利ETF-iShares MSCI
'BKGI',#BNY Mellon Global Infrastructur
'SII',#Sprott Inc.
'OSK',#Oshkosh Corp
'VOOV',#Vanguard S&P 500 Value ETF
'WOMN',#Impact Shares YWCA Women’s Emp
'GDV',#The Gabelli Dividend & Income T
'PFM',#Invesco Dividend Achievers ETF
'FLV',#American Century Focused Large
'UNG',#美国天然气基金
'GUSA',#Goldman Sachs MarketBeta U.S. 1
'NVT',#nVent Electric plc
'FCO',#abrdn Global Income Fund Inc
'IJJ',#iShares S&P Mid-Cap 400 Value E
'DWUS',#AdvisorShares Dorsey Wright FSM
'KVLE',#KFA Value Line Dynamic Core Equ
'TPLC',#Timothy Plan US Large/Mid Cap C
'KBE',#银行ETF-SPDR S&P
'EPS',#WisdomTree U.S. LargeCap Fund
'NSA_A',#National Storage Affiliates Tru
'SIZE',#iShares Edge MSCI USA Size Fact
'GLOP_A',#GasLog Partners LP Series A Pfd
'CGUS',#Capital Group Core Equity ETF
'TPSC',#Timothy Plan US Small Cap Core
'SCHY',#Schwab International Dividend E
'IMFL',#Invesco International Developed
'SCHM',#Schwab U.S. Mid Cap ETF
'IYJ',#iShares U.S. Industrials ETF
'CMSA',#CMS Energy Corp Notes
'INDS',#Pacer Industrial Real Estate ET
'GFLU',#GFL Environmental Inc Equity Un
'GEw',#通用电气(US) WI
'BKMC',#BNY Mellon US Mid Cap Core Equi
'SELF',#Global Self Storage Inc
'CSM',#ProShares Large Cap Core Plus
'SPLG',#SPDR Portfolio S&P 500 ETF
'JGH',#Nuveen Global High Income Fund
'HYFM',#Hydrofarm Holdings Group Inc
'EYEN',#Eyenovia Inc
'ECF_A',#Ellsworth Growth and Income Fun
'CODI_A',#Compass Group Diversified Holdi
'ARMR',#Armor US Equity Index ETF
'PHO',#水资源ETF-PowerShares
'ARES',#Ares Management Corp-A
'ACSI',#American Customer Satisfaction
'SNX',#新聚思
'DGRO',#iShares Core Dividend Growth ET
'YXI',#做空FTSE中国50ETF-ProShares
'IWN',#罗素2000价值股ETF-iShares
'ASHR',#沪深300ETF-德银嘉实
'CGW',#Invesco S&P Global Water Index
'HWC',#汉考克惠特尼
'OAK_A',#Oaktree Capital Group LLC Serie
'CSV',#Carriage Services Inc
'SPYV',#SPDR Portfolio S&P 500 Value ET
'MTG',#MGIC Investment Corp
'OTTR',#奥特泰尔
'HDIV',#QRAFT AI-Enhanced U.S. High Div
'GLRE',#绿光资本
'LAZ',#Lazard Ltd-A
'XTL',#SPDR S&P Telecom ETF
'LII',#雷诺士
'EFC',#Ellington投资
'EWU',#英国ETF-iShares MSCI
'HYIN',#WisdomTree Alternative Income F
'CRUZ',#Defiance Hotel, Airline, and Cr
'MIR',#Mirion Technologies Inc-A
'CLMT',#卡路美
'JEPI',#JPMorgan Equity Premium Income
'SIXH',#ETC 6 Meridian Hedged Equity In
'FDIS',#Fidelity MSCI Consumer Discreti
'AWAY',#ETFMG Travel Tech ETF
'OVL',#Overlay Shares Large Cap Equity
'TSPA',#T. Rowe Price U.S. Equity Resea
'RILYP',#B. Riley Financial Inc Series A
'IVE',#标普500价值股ETF-iShares
'BLCO',#Bausch + Lomb Corp
'ADIV',#SmartETFs Asia Pacific Dividend
'KREF',#KKR Real Estate Finance Trust I
'FIVA',#Fidelity International Value Fa
'BWG',#BrandywineGLOBAL Global Income
'IYF',#美国金融ETF-iShares
'DIM',#WisdomTree International MidCap
'SDIV',#Global X SuperDividend ETF
'PDT',#John Hancock Premium Dividend F
'IEP',#伊坎企业
'RILYO',#B. Riley Financial Inc Notes
'BAFN',#BayFirst Financial Corp
'JUST',#Goldman Sachs JUST U.S. Large C
'MBIN',#Merchants Bancorp
'THR',#Thermon Group Holdings Inc
'NEE_P',#NextEra Energy Inc Corporate Un
'YUMY',#VanEck Future of Food ETF
'C',#花旗集团
'WKHS',#Workhorse Group Inc
'VFMV',#Vanguard U.S. Minimum Volatilit
'NORW',#挪威ETF-Global X MSCI
'SMG',#The Scotts Miracle-Gro Co
'IWR',#罗素中型股ETF-iShares
'IXP',#全球电信ETF-iShares
'EHC',#Encompass Health Corp
'XDAP',#Innovator U.S. Equity Accelerat
'CRPT',#First Trust SkyBridge Crypto In
'BBDC',#Barings BDC Inc
'AGMH',#安高盟
'MA',#万事达
'FDLO',#Fidelity Low Volatility Factor
'BELFB',#Bel Fuse Inc-B
'FNLC',#第一银行(缅因州)
'CFG_E',#Citizens Financial Group Inc Se
'JVAL',#JPMorgan U.S. Value Factor ETF
'CASY',#Casey’s General Stores Inc
'RWX',#国际除美国房地产ETF-SPDR
'VERA',#Vera Therapeutics Inc-A
'DALS',#DA32 Life Science Tech Acquisit
'PJAN',#Innovator U.S. Equity Power Buf
'VO',#Vanguard Mid-Cap ETF
'EQWL',#Invesco S&P 100 Equal Weight ET
'STZ',#星座品牌-A
'TXRH',#德州公路酒吧
'AAPD',#Direxion Daily AAPL Bear 1X Sha
'HEWU',#iShares Currency Hedged MSCI Un
'AADR',#AdvisorShares Dorsey Wright ADR
'TRN',#Trinity Industries Inc
'DWLD',#Davis Select Worldwide ETF
'CGV',#Conductor Global Equity Value E
'COTY',#科蒂
'QDEF',#FlexShares Quality Dividend Def
'AVSC',#Avantis U.S Small Cap Equity ET
'FIBK',#First Interstate BancSystem Inc
'NSTB',#Northern Star Investment Corp I
'ENSG',#恩赛因
'JXN',#Jackson Financial Inc-A
'BJ',#BJ批发俱乐部
'EFIV',#SPDR S&P 500 ESG ETF
'WLTG',#WealthTrust DBS Long Term Growt
'GGG',#固瑞克
'AVT',#安富利
'TILT',#FlexShares Mornigstar US Market
'IVZ',#景顺
'ETB',#Eaton Vance Tax-Managed Buy-Wri
'IGBH',#iShares Interest Rate Hedged Lo
'AIN',#奥尔巴尼国际
'BGY',#BlackRock Enhanced Internationa
'YALL',#God Bless America ETF
'LKFN',#莱克兰金融
'DDT',#Dillard's Inc Pfd of Dillard's
'UNP',#联合太平洋
'CDL',#VictoryShares US Large Cap High
'PAAS',#泛美白银
'HT_E',#HT基金(优先股)
'STX',#希捷科技
'JUSA',#JPMorgan ActiveBuilders U.S. La
'PWV',#Invesco Dynamic Large Cap Value
'GVA',#花岗岩建筑
'CUT',#MSCI全球林木ETF-Guggenheim
'GLOB',#Globant SA
'GTN_A',#格雷电视-A
'SPYX',#SPDR S&P 500 Fossil Fuel Reserv
'IPGP',#IPG光电
'JQUA',#JPMorgan U.S. Quality Factor ET
'HNW',#Pioneer Diversified High Income
'SPTM',#SPDR Portfolio S&P 1500 Composi
'HBNC',#哈里逊合众银行
'REG',#Regency Centers Corp
'BLOK',#Amplify Transformational Data S
'NS_B',#NuStar Energy LP Series B Pfd
'SPNS',#Sapiens International Corp NV
'DBS',#Invesco DB Silver Fund
'XLI',#工业ETF-SPDR
'ILCB',#iShares Morningstar U.S. Equity
'EFAS',#Global X MSCI SuperDividend EAF
'IWB',#罗素1000ETF-iShares
'EES',#WisdomTree U.S. SmallCap Fund
'POWW',#AMMO Inc
'HIL',#希尔国际管理
'QDF',#FlexShares Quality Dividend Ind
'RYF',#Invesco S&P 500 Equal Weight Fi
'PPH',#VanEck Pharmaceutical ETF
'TMKRU',#Tastemaker Acquisition Corp Uni
'SITC',#SITE Centers Corp
'FHB',#First Hawaiian Inc
'ROKT',#SPDR S&P Kensho Final Frontiers
'YYY',#高收益封基ETF-YieldShares
'KGHG',#KraneShares Global Carbon Trans
'ESRT',#Empire State Realty Trust Inc-A
'DSTL',#Distillate U.S. Fundamental Sta
'RUSHB',#Rush Enterprises Inc-B
'QUAL',#iShares Edge MSCI USA Quality F
'BWAQU',#Blue World Acquisition Corp Uni
'CRBN',#iShares MSCI ACWI Low Carbon Ta
'KRMD',#KORU Medical Systems Inc
'IVLC',#Invesco US Large Cap Core ESG E
'HCMA',#HCM Acquisition Corp-A
'OALC',#OneAscent Large Cap Core ETF
'FLRG',#Fidelity U.S. Multifactor ETF
'CHSCO',#CHS Inc Class B Pfd
'HTLF',#哈特兰金融
'RESP',#WisdomTree U.S. ESG Fund
'GSEW',#Goldman Sachs Equal Weight U.S.
'RCL',#皇家加勒比邮轮
'JMOM',#JPMorgan U.S. Momentum Factor E
'TG',#特里迪加
'FAB',#First Trust Multi Cap Value Alp
'FTXO',#First Trust Nasdaq Bank ETF
'FNDF',#Schwab Fundamental Internationa
'VLUE',#iShares Edge MSCI USA Value Fac
'SPXN',#ProShares S&P 500 Ex-Financials
'HYI',#Western Asset High Yield Define
'FBIN',#Fortune Brands Innovations Inc
'ESGA',#American Century Sustainable Eq
'SCHB',#美国全市场ETF-Schwab
'SPCMU',#Sound Point Acquisition Corp I
'EMDV',#ProShares MSCI Emerging Markets
'DMDV',#AAM S&P Developed Markets High
'FSV',#FirstService Corp
'BECN',#Beacon Roofing Supply Inc
'FTGS',#First Trust Growth Strength ETF
'MFDX',#PIMCO RAFI Dynamic Multi-Factor
'FDUS',#Fidus Investment Corp
'LADR',#Ladder Capital Corp-A
'LCF',#Touchstone US Large Cap Focused
'GOAU',#U.S. Global GO GOLD and Preciou
'GLO',#Clough Global Opportunities Fun
'FUE',#ELEMENTS Linked to the MLCX Bio
'SNPE',#Xtrackers S&P 500 ESG ETF
'ITOT',#iShares Core S&P Total U.S. Sto
'AQUA',#Evoqua Water Technologies Corp
'DDWM',#WisdomTree Dynamic Currency Hed
'WTFC',#信达金融
'GGAAU',#Genesis Growth Tech Acquisition
'MELI',#MercadoLibre Inc
'FCF',#第一联邦金融
'RL',#拉夫劳伦
'RVP',#Retractable Technologies Inc
'PESI',#佩尔马福克斯环境服务
'STRV',#Strive 500 ETF
'GSLC',#Goldman Sachs ActiveBeta U.S. L
'VUSE',#Vident Core US Equity ETF
'PDBA',#Invesco Agriculture Commodity S
'SHE',#SPDR MSCI USA Gender Diversity
'HEAR',#乌龟海岸
'AQWA',#Global X Clean Water ETF
'AEHR',#Aehr Test Systems
'SPY',#标普500ETF-SPDR
'TFII',#TFI International Inc
'TRNS',#Transcat Inc
'IXG',#全球金融ETF-iShares
'UHAL',#U-Haul Holding Co
'COO',#库珀医疗
'AFSM',#First Trust Active Factor Small
'ACVF',#American Conservative Values ET
'DECK',#德克斯户外
'FEUS',#FlexShares ESG & Climate US Lar
'ADBE',#奥多比
'NBHC',#National Bank Holdings Corp-A
'KOKU',#Xtrackers MSCI Kokusai Equity E
'IQSM',#IQ Candriam ESG U.S. Mid Cap Eq
'TOK',#iShares MSCI Kokusai ETF
'ENOR',#iShares MSCI Norway ETF
'IFF',#国际香料香精
'ARW',#艾睿电子
'BKLC',#BNY Mellon US Large Cap Core Eq
'DAR',#美国达尔令国际
'ACWF',#iShares Edge MSCI Multifactor G
'GLW',#康宁
'CHAU',#二倍做多沪深300ETF-Direxion
'PFI',#Invesco DWA Financial Momentum
'FLGB',#Franklin FTSE United Kingdom ET
'CIM_B',#Chimera Investment Corp Series
'KXI',#全球日常消费ETF-iShares
'KT',#韩国电信
'ESGU',#iShares ESG MSCI USA ETF
'EXR',#Extra Space Storage Inc
'LCTU',#BlackRock U.S. Carbon Transitio
'SHW',#宣伟
'UDIV',#Franklin U.S. Core Dividend Til
'GTLB',#Gitlab Inc-A
'UAV',#AdvisorShares Drone Technology
'TEF',#西班牙电信
'SWKH',#SWK Holdings Corp
'PBSM',#Invesco PureBeta MSCI USA Small
'KROP',#Global X AgTech & Food Innovati
'SLYG',#SPDR S&P 600 Small Cap Growth E
'UTHR',#联合治疗
'BRNY',#Burney U.S. Factor Rotation ETF
'DCOM',#迪募社区银行
'REVS',#Columbia Research Enhanced Valu
'AIRT',#Air T Inc
'WRAP',#Wrap Technologies Inc
'VSH',#威世科技
'CVR',#Chicago Rivet & Machine Co
'JCTR',#JPMorgan Carbon Transition U.S.
'IGA',#Voya Global Advantage and Premi
'ABB',#阿西布朗勃法瑞
'PFG',#信安金融
'TTWO',#Take-Two Interactive Software I
'BSL',#Blackstone/GSO Senior Floating
'FDTS',#First Trust Developed Markets e
'BUSE',#First Busey Corp
'AGNC',#AGNC Investment Corp
'ZWS',#Zurn Elkay Water Solutions Corp
'XAR',#SPDR S&P Aerospace & Defense ET
'XLF',#金融ETF-SPDR
'YLDE',#ClearBridge Dividend Strategy E
'RUFF',#Alpha Dog ETF
'GTLS',#查特工业
'JZRO',#Janus Henderson Net Zero Transi
'PIE',#Invesco DWA Emerging Markets Mo
'JJP',#iPath Series B Bloomberg Precio
'EMCF',#恩克莱尔金融
'SJM',#JM斯马克
'IVLU',#iShares Edge MSCI Intl Value Fa
'FDMO',#Fidelity Momentum Factor ETF
'UGL',#二倍做多黄金ETF-ProShares
'VOO',#标普500ETF-Vanguard
'DBJA',#Innovator Double Stacker 9 Buff
'NUSC',#Nuveen ESG Small-Cap ETF
'DIVD',#Altrius Global Dividend ETF
'VEEE',#Twin Vee PowerCats Co
'UMH',#UMH Properties Inc
'KKR',#KKR & Co Inc
'RVRB',#Reverb ETF
'MRK',#默沙东
'SHOO',#史蒂夫·马登
'IGRO',#iShares International Dividend
'SCHX',#Schwab U.S. Large-Cap ETF
'DFUS',#Dimensional U.S. Equity ETF
'OPP',#RiverNorth/DoubleLine Strategic
'AIRC',#Apartment Income REIT Corp
'DCI',#唐纳森
'RSPE',#Invesco ESG S&P 500 Equal Weigh
'BGX',#Blackstone/GSO Long-Short Credi
'STN',#斯坦泰克
'JHDV',#John Hancock U.S. High Dividend
'DBRG_H',#DigitalBridge Group Inc Series
'XBAP',#Innovator U.S. Equity Accelerat
'VNSE',#Natixis Vaughan Nelson Select E
'ACIO',#Aptus Collared Income Opportuni
'TR',#Tootsie Roll Industries Inc
'HAPI',#Harbor Corporate Culture ETF
'MDLZ',#亿滋国际
'DVND',#Touchstone Dividend Select ETF
'DEEF',#Xtrackers FTSE Developed ex US
'SKY',#Skyline Champion Corp
'WAL',#阿莱恩斯西部银行
'WLDR',#Affinity World Leaders Equity E
'EWGS',#iShares MSCI Germany Small-Cap
'BUYW',#Main BuyWrite ETF
'IDV',#国际红利股ETF-iShares
'VTI',#全市场指数ETF-Vanguard
'WTRE',#WisdomTree New Economy Real Est
'HDEF',#Xtrackers MSCI EAFE High Divide
'RNDM',#Developed International Equity
'RHTX',#RH Tactical Outlook ETF
'SUPL',#ProShares Supply Chain Logistic
'KNG',#Cboe Vest S&P 500 Dividend Aris
'IMCB',#iShares Morningstar Mid-Cap ETF
'DBA',#农产品ETF-PowerShares
'BJAN',#Innovator U.S. Equity Buffer ET
'IBM',#IBM国际商业机器(US)
'IWV',#罗素3000ETF-iShares
'WTT',#Wireless Telecom Group Inc
'SSLY',#Syntax Stratified SmallCap ETF
'EFV',#iShares MSCI EAFE Value ETF
'MHNC',#Maiden Holdings North America L
'NUDV',#Nuveen ESG Dividend ETF
'DCP',#DCP Midstream LP
'VOTE',#Engine No. 1 Transform 500 ETF
'JANZ',#TrueShares Structured Outcome (
'FSMD',#Fidelity Small-Mid Factor ETF
'LYFE',#2ndVote Life Neutral Plus ETF
'SVOL',#Simplify Volatility Premium ETF
'GUT',#The Gabelli Utility Trust
'USPX',#Franklin U.S. Equity Index ETF
'TDVG',#T. Rowe Price Dividend Growth E
'BHLB',#Berkshire Hills Bancorp Inc
'EBLU',#Ecofin Global Water ESG Fund
'IPAC',#iShares Core MSCI Pacific ETF
'VV',#Vanguard Large-Cap ETF
'BSTP',#Innovator Buffer Step-Up Strate
'NGVT',#Ingevity Corp
'PIPR',#Piper Sandler Co
'QLC',#FlexShares US Quality Large Cap
'JVA',#Coffee Holding Co Inc
'APG',#APi Group Corp
'ACCO',#爱可品牌
'MILN',#Global X Millennial Consumer ET
'JHG',#骏利亨德森集团
'DFIC',#Dimensional International Core
'DAN',#达纳
'ACR_D',#ACRES Commercial Realty Corp Se
'IR',#英格索兰
'CCOR',#Core Alternative ETF
'IVSG',#Invesco Select Growth ETF
'WEA',#Western Asset Premier Bond Fund
'QLV',#FlexShares US Quality Low Volat
'GOOD',#格拉德斯通商业
'SUBS',#Fount Subscription Economy ETF
'BRMK',#Broadmark Realty Capital Inc
'EUSA',#iShares MSCI USA Equal Weighted
'LSTR',#莱帝运输
'FYLG',#Global X Financials Covered Cal
'IBA',#Industrias Bachoco SAB de CV AD
'CROX',#卡骆驰
'VB',#小型股指数ETF-Vanguard
'GVIP',#Goldman Sachs Hedge Industry VI
'VOOG',#Vanguard S&P 500 Growth ETF
'HOMZ',#Hoya Capital Housing ETF
'BDEC',#Innovator U.S. Equity Buffer ET
'SAA',#ProShares Ultra SmallCap600
'RING',#iShares MSCI Global Gold Miners
'AUY',#Yamana Gold Inc
'CSR',#Centerspace
'UAN',#CVR Partners LP
'VIS',#工业指数ETF-Vanguard
'TISI',#Team Inc
'LTHM',#Livent Corp
'VDNI',#V-Shares US Leadership Diversit
'AKAM',#阿卡迈
'BCML',#BayCom Corp
'UPV',#ProShares Ultra FTSE Europe
'QRFT',#QRAFT AI-Enhanced U.S. Large Ca
'GD',#通用动力
'FLJH',#Franklin FTSE Japan Hedged ETF
'BNKU',#MicroSectors U.S. Big Banks Ind
'HMN',#霍勒斯曼恩
'CHE',#Chemed Corp
'MDU',#MDU Resources Group Inc
'BCTXW',#BriaCell Therapeutics Corp Wt
'ASPY',#ASYMshares ASYMmetric S&P 500 E
'VIG',#股利增长指数ETF-Vanguard
'SMMD',#iShares Russell 2500 ETF
'AEIS',#先进能源工业
'IMOM',#Alpha Architect International Q
'SHYF',#The Shyft Group Inc
'AIVI',#WisdomTree International AI Enh
'IGR',#CBRE Global Real Estate Income
'CAPE',#DoubleLine Shiller CAPE U.S. Eq
'USMV',#美国最小波幅ETF-iShares
'NULV',#Nuveen ESG Large-Cap Value ETF
'JOUT',#约翰逊户外
'PSMO',#Pacer Swan SOS Moderate (Octobe
'KRG',#凯特地产信托
'VEL',#Velocity Financial Inc
'IQIN',#IQ 500 International ETF
'IVOG',#Vanguard S&P Mid-Cap 400 Growth
'QSR',#餐饮品牌国际
'WNEB',#Western New England Bancorp Inc
'PRG',#PROG Holdings Inc
'IIVIP',#Coherent Corp Series A Pfd
'PSTP',#Innovator Power Buffer Step-Up
'PAVE',#Global X U.S. Infrastructure De
'HIO',#Western Asset High Income Oppor
'DFSU',#Dimensional US Sustainability C
'SSUS',#Day Hagan/Ned Davis Research Sm
'FSM',#Fortuna Silver Mines Inc
'MGC',#Vanguard Mega Cap ETF
'EDOW',#First Trust Dow 30 Equal Weight
'IDHD',#Invesco S&P International Devel
'TER',#泰瑞达
'STWD',#Starwood Property Trust Inc
'CEFS',#Saba Closed-End Funds ETF
'SBUX',#星巴克
'XLP',#日常消费ETF-SPDR
'JBHT',#JB亨特运输服务
'NSPL',#NightShares 500 1x/1.5x ETF
'DFAU',#Dimensional US Core Equity Mark
'VOT',#Vanguard Mid-Cap Growth ETF
'GOLD',#巴里克黄金
'APRZ',#TrueShares Structured Outcome (
'THFF',#First Financial Corp
'IVV',#标普500ETF-iShares
'PSMM',#Invesco Moderately Conservative
'HSBC',#汇丰控股
'AAM_A',#Apollo Asset Management Inc Ser
'RITM_C',#Rithm Capital Corp Series C Pfd
'GLOV',#Goldman Sachs ActiveBeta World
'HJEN',#Direxion Hydrogen ETF
'OEF',#标普100ETF-iShares
'BAPR',#Innovator U.S. Equity Buffer ET
'IUSA',#Amberwave Invest USA JSG Fund
'FNDC',#Schwab Fundamental Internationa
'EME',#埃姆科
'SIRI',#天狼星XM
'DFIS',#Dimensional International Small
'IYY',#iShares Dow Jones U.S. ETF
'IYK',#iShares U.S. Consumer Staples E
'FIDU',#Fidelity MSCI Industrials Index
'VDC',#日常消费指数ETF-Vanguard
'TCMD',#Tactile Systems Technology Inc
'IWL',#iShares Russell Top 200 ETF
'APRT',#AllianzIM U.S. Large Cap Buffer
'FMAR',#FT Cboe Vest U.S. Equity Buffer
'VEGI',#全球农业生产商ETF-iShares MSCI
'IVW',#标普500成长股ETF-iShares
'CZWI',#Citizens Community Bancorp Inc
'TTGT',#TechTarget Inc
'IDOG',#ALPS International Sector Divid
'BRO',#布朗保险
'FIS',#富达国民信息服务
'GLBLU',#Cartesian Growth Corp Unit Cons
'XBJL',#Innovator U.S. Equity Accelerat
'LIN',#Linde plc
'PCGU',#Pacific Gas and Electric Co Equ
'FFEB',#FT Cboe Vest U.S. Equity Buffer
'EFC_A',#Ellington Financial Inc Series
'TTAC',#FCF US Quality ETF
'MTN',#Vail Resorts Inc
'VTR',#芬塔公司
'FFHG',#FormulaFolios Hedged Growth ETF
'NIMC',#NiSource Inc Series A Corporate
'SNRH',#Senior Connect Acquisition Corp
'SAEF',#Schwab Ariel ESG ETF
'BNOV',#Innovator U.S. Equity Buffer ET
'LVHI',#Franklin International Low Vola
'FNCL',#Fidelity MSCI Financials Index
'DIA',#道琼斯工业ETF-SPDR
'NOW',#现在服务公司
'URTH',#iShares MSCI World ETF
'EWK',#比利时ETF-iShares MSCI
'GVAL',#Cambria Global Value ETF
'SOVO',#Sovos Brands Inc
'SRG',#Seritage Growth Properties-A
'SAFE',#Safehold Inc
'FDRR',#Fidelity Dividend ETF for Risin
'RODE',#Hartford Multifactor Diversifie
'ZTS',#硕腾
'BIBL',#Inspire 100 ETF
'SAM',#波士顿啤酒
'ACN',#埃森哲
'SDEM',#Global X MSCI SuperDividend Eme
'DECT',#AllianzIM U.S. Large Cap Buffer
'QWLD',#SPDR MSCI World StrategicFactor
'JRO',#Nuveen Floating Rate Income Opp
'ESP',#Espey Mfg & Electronics Corp
'IQSU',#IQ Candriam ESG U.S. Large Cap
'BBVA',#西班牙毕尔巴鄂比斯开银行(ADR)
'JRNY',#ALPS Global Travel Beneficiarie
'HEI_A',#海科航空-A
'TY_',#Tri-Continental Corp Pfd
'RBA',#里奇兄弟拍卖
'VEA',#Vanguard FTSE Developed Markets
'NSTS',#NSTS Bancorp Inc
'ALOT',#AstroNova Inc
'FCAX_U',#Fortress Capital Acquisition Co
'JRSH',#Jerash Holdings (US) Inc
'GEOS',#Geospace Technologies Corp
'PNOV',#Innovator U.S. Equity Power Buf
'FSST',#Fidelity Sustainable U.S. Equit
'BIP_B',#布鲁克菲尔德公共建设(优先股)
'SSTK',#Shutterstock Inc
'BETZ',#Roundhill Sports Betting & iGam
'FORH',#Formidable ETF
'LCAAU',#L Catterton Asia Acquisition Co
'LGACU',#Lazard Growth Acquisition Corp
'PWC',#Invesco Dynamic Market ETF
'TBX',#ProShares Short 7 10 Year Treas
'BATRK',#Liberty Media Corp Liberty Brav
'QLYS',#科力斯
'FACT_U',#Freedom Acquisition I Corp Unit
'D',#道明尼能源
'MGPI',#MGP Ingredients Inc
'SQ',#Block Inc-A
'WEBR',#Weber Inc-A
'REFR',#Research Frontiers Inc
'PSLV',#Sprott Physical Silver Trust
'KNSW_U',#KnightSwan Acquisition Corp Uni
'PRNT',#The 3D Printing ETF
'JHMD',#John Hancock Multifactor Develo
'WBA',#沃尔格林-联合博姿
'EPU',#秘鲁ETF-iShares MSCI
'SPYG',#SPDR Portfolio S&P 500 Growth E
'AVAC',#Avalon Acquisition Inc-A
'VWID',#Virtus WMC International Divide
'EZJ',#ProShares Ultra MSCI Japan
'SECT',#Main Sector Rotation ETF
'NRDY',#Nerdy Inc-A
'HBCP',#Home Bancor Inc
'MCK',#麦克森
'STXK',#Strive 2000 ETF
'RAYD',#Rayliant Quantitative Developed
'BKSE',#BNY Mellon US Small Cap Core Eq
'QUS',#SPDR MSCI USA StrategicFactors
'KSA',#沙特阿拉伯ETF-iShares MSCI
'MURF',#Murphy Canyon Acquisition Corp-
'APACU',#StoneBridge Acquisition Corp Un
'AVDE',#Avantis International Equity ET
'EDZ',#三倍做空新兴市场ETF-Direxion
'SOR',#Source Capital
'CLSA',#Cabana Target Leading Sector Ag
'USSG',#Xtrackers MSCI USA ESG Leaders
'DSI',#iShares MSCI KLD 400 Social ETF
'SCHK',#Schwab 1000 Index ETF
'RFDI',#First Trust RiverFront Dynamic
'EFO',#ProShares Ultra MSCI EAFE
'WFCF',#Where Food Comes From Inc
'IDLV',#Invesco S&P International Devel
'LGSTU',#Semper Paratus Acquisition Corp
'CMCL',#喀里多尼亚矿业(US)
'SAIA',#Saia Inc
'BMRC',#马林银行
'AFCG',#AFC Gamma Inc
'SIVB',#硅谷银行
'FIVR',#STRATEGY SHARES NASDAQ 5 HANDL
'PERI',#Perion Network Ltd
'JHML',#John Hancock Multifactor Large
'BDN',#布兰迪维因房地产信托
'TXT',#德事隆
'QGRO',#American Century STOXX U.S. Qua
'HRL',#荷美尔食品
'XHYE',#BondBloxx USD High Yield Bond E
'PZC',#PIMCO California Municipal Inco
'ODV',#Osisko Development Corp
'SPXE',#ProShares S&P 500 Ex-Energy ETF
'EMR',#艾默生电气
'XTR',#Global X S&P 500 Tail Risk ETF
'CAMP',#CalAmp Corp
'TLTD',#FlexShares Morningstar Develope
'DSOC',#Innovator Double Stacker ETF –
'BKLN',#高级银团贷款ETF-PowerShares
'UIVM',#VictoryShares International Val
'QLD',#二倍做多纳斯达克100ETF
'KGC',#金罗斯黄金
'EFNL',#芬兰ETF-iShares MSCI
'MITT_A',#AG Mortgage Investment Trust In
'SNPG',#Xtrackers S&P 500 Growth ESG ET
'EWS',#新加坡ETF-iShares MSCI
'FAPR',#FT Cboe Vest U.S. Equity Buffer
'SCHC',#Schwab International Small-Cap
'PSMB',#Invesco Balanced Multi-Asset Al
'UEVM',#VictoryShares Emerging Markets
'MCR',#MFS Charter Income Trust
'DFAI',#Dimensional International Core
'FSEP',#FT Cboe Vest U.S. Equity Buffer
'GCI',#甘尼特
'BCPC',#拜切
'FND',#Floor & Decor Holdings Inc-A
'BFIT',#Global X Health & Wellness ETF
'ROOF',#IQ CBRE NextGen Real Estate ETF
'CHMI_B',#Cherry Hill Mortgage Investment
'AYI',#Acuity Brands Inc
'BSEA',#ETFMG Breakwave Sea Decarboniza
'TMFE',#Motley Fool Capital Efficiency
'WSBF',#沃特财务
'XYLG',#Global X S&P 500 Covered Call &
'SMPL',#易美味
'GJH',#STRATS Trust For United States
'ETI_',#Entergy Texas Inc Series A Pfd
'JPM',#摩根大通
'EQC',#Equity Commonwealth
'TUGN',#STF Tactical Growth & Income ET
'NKEQ',#AXS 2X NKE Bear Daily ETF
'TPIF',#Timothy Plan International ETF
'ASHS',#中证500ETF-德银嘉实
'ONBPO',#Old National Bancorp Series A P
'MSI',#摩托罗拉解决方案
'PNC',#PNC金融服务集团
'PIZ',#Invesco DWA Developed Markets M
'THYF',#T. Rowe Price U.S. High Yield E
'CSML',#IQ Chaikin U.S. Small Cap ETF
'SHUS',#Syntax Stratified U.S. Total Ma
'SPDW',#SPDR Portfolio Developed World
'SCHA',#Schwab U.S. Small-Cap ETF
'GRNT',#Granite Ridge Resources Inc
'ESGG',#FlexShares STOXX Global ESG Sel
'BAH',#博思艾伦
'MOFG',#MidWestOne Financial Group Inc
'BSET',#巴西特家具
'JSTC',#Adasina Social Justice All Cap
'IYG',#iShares U.S. Financial Services
'BTAL',#AGFiQ U.S. Market Neutral Anti-
'CTBB',#Qwest Corp Notes
'BAUG',#Innovator U.S. Equity Buffer ET
'FMBH',#First Mid Bancshares Inc
'EEV',#ProShares UltraShort MSCI Emerg
'QEFA',#SPDR MSCI EAFE StrategicFactors
'HAWX',#iShares Currency Hedged MSCI AC
'RCI',#罗杰斯通信
'SPMV',#Invesco S&P 500 Minimum Varianc
'BEP_A',#Brookfield Renewable Partners L
'FIW',#First Trust Water ETF
'DEF',#Invesco Defensive Equity ETF
'MDT',#美敦力
'NULC',#Nuveen ESG Large-Cap ETF
'FLSA',#Franklin FTSE Saudi Arabia ETF
'FCEF',#First Trust CEF Income Opportun
'VT',#世界全市场指数ETF-Vanguard
'NSPI',#Nationwide S&P 500 Risk-Managed
'HSCZ',#iShares Currency Hedged MSCI EA
'SANM',#新美亚电子
'IWY',#iShares Russell Top 200 Growth
'ITT',#ITT Inc
'VIDI',#Vident International Equity Fun
'EWBC',#华美
'DGRW',#WisdomTree U.S. Quality Dividen
'TSJA',#Innovator Triple Stacker ETF -
'ETHO',#Etho Climate Leadership U.S. ET
'MCBC',#Macatawa Bank Corp
'IEV',#欧洲ETF-iShares
'QCON',#American Century Quality Conver
'PEXL',#Pacer US Export Leaders ETF
'EFRA',#iShares Environmental Infrastru
'VSLU',#Applied Finance Valuation Large
'MAXI',#Simplify Bitcoin Strategy PLUS
'INTC',#英特尔
'GSUS',#Goldman Sachs MarketBeta U.S. E
'SSD',#Simpson Manufacturing Co Inc
'LEA',#李尔
'GAMB',#Gamb
'DGL',#Invesco DB Gold Fund
'ACWI',#全球ETF-iShares MSCI
'CVBF',#CVB金融
'DNOV',#FT Cboe Vest U.S. Equity Deep B
'BJUN',#Innovator U.S. Equity Buffer ET
'DHR',#丹纳赫
'TU',#泰勒斯
'AEL',#美国股票投资寿险
'UVSP',#宾夕法尼亚裕益银行
'ZTR',#Virtus Total Return Fund
'XLG',#Invesco S&P 500 Top 50 ETF
'SPUC',#Simplify US Equity PLUS Upside
'AMN',#AMN医疗服务
'IWM',#罗素2000ETF-iShares
'LBAI',#拉扎德银行
'ARGO',#阿尔戈国际控股
'OSCR',#Oscar Health Inc-A
'CHSCM',#CHS Inc Class B Series 3 Pfd
'PAYC',#Paycom Software Inc
'HII',#亨廷顿英戈尔斯工业
'TSOC',#Innovator Triple Stacker ETF –
'OAIM',#OneAscent International Equity
'STCE',#Schwab Crypto Thematic ETF
'FEDM',#FlexShares ESG & Climate Develo
'TMFS',#Motley Fool Small-Cap Growth ET
'OXLCP',#Oxford Lane Capital Corp Series
'SPGM',#SPDR Portfolio MSCI Global Stoc
'SRE',#桑普拉能源
'PPA',#Invesco Aerospace & Defense ETF
'CEF',#Sprott Physical Gold and Silver
'RISR',#FolioBeyond Rising Rates ETF
'CEFD',#ETRACS Monthly Pay 1.5X Leverag
'FMIL',#Fidelity New Millennium ETF
'DCP_C',#DCP Midstream LP Series C Pfd
'ITAN',#Sparkline Intangible Value ETF
'RHS',#Invesco S&P 500 Equal Weight Co
'DVA',#达维塔保健
'BECO',#BlackRock Future Climate and Su
'MMT',#MFS Multimarket Income Trust
'DHF',#BNY Mellon High Yield Strategie
'INTF',#iShares Edge MSCI Multifactor I
'GOF',#Guggenheim Strategic Opportunit
'FSD',#First Trust High Income Long/Sh
'ABNB',#爱彼迎
'RGR',#斯特姆-鲁格
'EUSC',#WisdomTree Europe Hedged SmallC
'PTA',#Cohen & Steers Tax-Advantaged P
'CLRG',#IQ Chaikin U.S. Large Cap ETF
'ORCL',#甲骨文
'AVK',#Advent Convertible and Income F
'CET',#Central Securities Corporation
'INGR',#宜瑞安
'IRBA',#iMGP RBA Responsible Global All
'SLGL',#Sol-Gel Technologies Ltd
'KOCG',#FIS Knights of Columbus Global
'COMP',#Compass Inc-A
'MNST',#怪物饮料
'JPIN',#JPMorgan Diversified Return Int
'DBP',#Invesco DB Precious Metals Fund
'FSTA',#Fidelity MSCI Consumer Staples
'NAMS',#NewAmsterdam Pharma Co NV
'GIB',#CGI Inc
'RODM',#Hartford Multifactor Developed
'HYGI',#iShares Inflation Hedged High Y
'IEUR',#iShares Core MSCI Europe ETF
'RWO',#全球房地产ETF-SPDR
'FDEC',#FT Cboe Vest U.S. Equity Buffer
'SYK',#史赛克
'SGDM',#Sprott Gold Miners ETF
'GLYC',#GlycoMimetics Inc
'COM',#Direxion Auspice Broad Commodit
'F',#福特汽车
'ETN',#伊顿
'FMF',#First Trust Managed Futures Str
'ESMV',#iShares ESG MSCI USA Min Vol Fa
'NACP',#Impact Shares NAACP Minority Em
'PCEF',#高收益封基ETF-PowerShares
'NVBT',#AllianzIM U.S. Large Cap Buffer
'NIM',#Nuveen Select Maturities Munici
'BLCN',#Reality Shares Nasdaq NexGen Ec
'BH',#Biglari Holdings Inc-B
'SUSL',#iShares ESG MSCI USA Leaders ET
'SNV',#西诺乌斯金融
'JIRE',#JPMorgan International Research
'BDC',#百通公司
'AVSU',#Avantis Responsible U.S. Equity
'SUSA',#iShares MSCI USA ESG Select ETF
'JSML',#Janus Henderson Small Cap Growt
'TMFG',#Motley Fool Global Opportunitie
'BMAR',#Innovator U.S. Equity Buffer ET
'ABC',#美源伯根
'AFRM',#Affirm Holdings Inc-A
'DGX',#奎斯特诊疗
'JANT',#AllianzIM U.S. Large Cap Buffer
'RESD',#WisdomTree International ESG Fu
'DBOC',#Innovator Double Stacker 9 Buff
'TANNI',#TravelCenters of America Inc No
'ON',#安森美半导体
'HYZD',#零久期高收益债ETF-WisdomTree
'FVAL',#Fidelity Value Factor ETF
'OUSA',#ALPS O'Shares U.S. Quality Divi
'SCHF',#Schwab International Equity ETF
'FYC',#First Trust Small Cap Growth Al
'AUGZ',#TrueShares Structured Outcome (
'ALB',#美国雅保
'ZIONL',#Zions Bancorp NA Notes
'BKIE',#BNY Mellon International Equity
'YJUN',#FT Cboe Vest International Equi
'CGXU',#Capital Group International Foc
'KCE',#SPDR S&P Capital Markets ETF
'ZECP',#Zacks Earnings Consistent Portf
'IQLT',#iShares Edge MSCI Intl Quality
'LGND',#Ligand Pharmaceuticals Inc
'PSFJ',#Pacer Swan SOS Flex (July) ETF
'BHF',#Brighthouse Financial Inc
'STXD',#Strive 1000 Dividend Growth ETF
'KFFB',#肯塔基第一银行
'DBEF',#Xtrackers MSCI EAFE Hedged Equi
'BA',#波音
'SXUS',#Janus Henderson International S
'XCEM',#Columbia EM Core ex-China ETF
'MNP',#Western Asset Municipal Partner
'HEI',#海科航空
'RHRX',#RH Tactical Rotation ETF
'BATRA',#Liberty Media Corp Liberty Brav
'SLRC',#SLR Investment Corp
'TPG',#TPG Inc-A
'NXTG',#First Trust Indxx NextG ETF
'AVSD',#Avantis Responsible Internation
'UONE',#Urban One Inc-A
'QINT',#American Century Quality Divers
'UVDV',#UVA Dividend Value ETF
'SEA',#U.S. Global Sea to Sky Cargo ET
'MAS',#马斯可木业
'IGI',#Western Asset Investment Grade
'NVST',#Envista Holdings Corp
'INC',#VanEck Dynamic High Income ETF
'FWRG',#First Watch Restaurant Group In
'LJAQ',#LightJump Acquisition Corp
'HYS',#PIMCO 0-5 Year High Yield Corpo
'PFS',#Provident Financial Services In
'LBTYA',#自由全球-A
'PBUS',#Invesco PureBeta MSCI USA ETF
'MS_A',#Morgan Stanley Series A Pfd
'NZAC',#SPDR MSCI ACWI Climate Paris Al
'RTYD',#Simplify US Small Cap PLUS Down
'FDEM',#Fidelity Emerging Markets Multi
'DCF',#BNY Mellon Alcentra Global Cred
'CEQP',#Crestwood Equity Partners LP
'AMPH',#Amphastar Pharmaceuticals Inc
'ISCB',#iShares Morningstar Small-Cap E
'SRG_A',#Seritage Growth Properties Seri
'GHI',#Greystone Housing Impact Invest
'SMCP',#AlphaMark Actively Managed Smal
'RDMX',#SPDR Bloomberg SASB Developed M
'PSFO',#Pacer Swan SOS Flex (October) E
'MMX',#Maverix Metals Inc
'KKR_C',#KKR & Co Inc Series C Pfd
'HUBB',#哈勃集团
'FDWM',#Fidelity Women's Leadership ETF
'ISZE',#iShares Edge MSCI Intl Size Fac
'SNDR',#Schneider National Inc-B
'DHIL',#Diamond Hill Investment Group I
'VOXR',#Vox Royalty Corp
'DUHP',#Dimensional US High Profitabili
'IQDY',#FlexShares International Qualit
'SF',#Stifel Financial Corp
'BUD',#百威英博
'DIP',#BTD Capital Fund
'PKB',#Invesco Dynamic Building & Cons
'VEGN',#US Vegan Climate ETF
'BLDR',#Builders FirstSource Inc
'AOMR',#Angel Oak Mortgage Inc
'PFBC',#保富银行
'DJIA',#Global X Dow 30 Covered Call ET
'HEWJ',#iShares Currency Hedged MSCI Ja
'EIRL',#爱尔兰ETF-iShares MSCI
'OPPX',#Corbett Road Tactical Opportuni
'FTCS',#First Trust Capital Strength ET
'FDEV',#Fidelity Targeted International
'ADX',#Adams Diversified Equity Fund
'UL',#联合利华(英国)
'RDWR',#Radware Ltd
'CNOB',#ConnectOne Bancorp Inc
'HPP',#Hudson Pacific Properties Inc
'PSFM',#Pacer Swan SOS Flex (April) ETF
'SHG',#新韩金融
'ESGD',#iShares ESG MSCI EAFE ETF
'LSXMK',#Liberty Media Corp Liberty Siri
'FFIC',#法拉盛金融
'FMCX',#FMC Excelsior Focus Equity ETF
'VNRX',#VolitionRx Ltd
'JULZ',#TrueShares Structured Outcome (
'DMCY',#Democracy International Fund
'LSXMA',#Liberty Media Corp Liberty Siri
'TLTE',#FlexShares Morningstar Emerging
'JPEM',#JPMorgan Diversified Return Eme
'ET_E',#Energy Transfer LP Series E Pfd
'AYX',#Alteryx Inc-A
'HYRM',#Xtrackers Risk Managed USD High
'NICE',#NICE Ltd ADR
'BUFR',#FT Cboe Vest Fund of Buffer ETF
'FNDE',#Schwab Fundamental Emerging Mar
'UBCB',#UBC Algorithmic Fundamentals ET
'BSJO',#Invesco BulletShares 2024 High
'SDGA',#Impact Shares Sustainable Devel
'IAT',#iShares U.S. Regional Banks ETF
'DURA',#VanEck Durable High Dividend ET
'ROL',#Rollins Inc
'DLNG_A',#Dynagas LNG Partners LP Series
'JHI',#John Hancock Investors Trust
'GECCM',#Great Elm Capital Corp Notes
'UOCT',#Innovator U.S. Equity Ultra Buf
'CEV',#Eaton Vance California Municipa
'BKCI',#BNY Mellon Concentrated Interna
'FALN',#iShares Fallen Angels USD Bond
'CDAY',#Ceridian HCM Holding Inc
'HSY',#好时
'ASG',#Liberty All-Star Growth Fund
'FTC',#First Trust Large Cap Growth Al
'UNTY',#联合银行
'VIGI',#Vanguard International Dividend
'CHKP',#Check Point Software Technologi
'CHS',#Chico’s FAS Inc
'OUNZ',#VanEck Merk Gold Trust
'VSDA',#VictoryShares Dividend Accelera
'BFEB',#Innovator U.S. Equity Buffer ET
'KJAN',#Innovator U.S. Small Cap Power
'DBL',#DoubleLine Opportunistic Credit
'HYDW',#Xtrackers Low Beta High Yield B
'CDX',#Simplify High Yield PLUS Credit
'MANH',#曼哈顿联合软件
'SLDP',#Solid Power Inc
'IBHF',#iShares iBonds 2026 Term High Y
'HIGH',#Simplify Enhanced Income ETF
'CMRE_C',#Costamare Inc Pfd-C
'RDFI',#Rareview Dynamic Fixed Income E
'TDV',#ProShares S&P Technology Divide
'SENT',#AdvisorShares Alpha DNA Equity
'NDJI',#Nationwide Dow Jones Risk-Manag
'BAD',#B.A.D. ETF
'TEI',#Templeton Emerging Markets Inco
'PICC',#Pivotal Investment Corp III-A
'GNT',#GAMCO Natural Resources, Gold &
'SCCC',#Sachem Capital Corp Notes
'EUFN',#欧洲金融ETF-iShares MSCI
'CSTR',#CapStar Financial Holdings Inc
'PSCQ',#Pacer Swan SOS Conservative (Oc
'INTE',#Integral Acquisition Corp 1-A
'CPARU',#Catalyst Partners Acquisition C
'GK',#AdvisorShares Gerber Kawasaki E
'NVBW',#AllianzIM U.S. Large Cap Buffer
'KAIIU',#Kismet Acquisition Two Corp Uni
'BLUA_U',#BlueRiver Acquisition Corp Unit
'PTEU',#Pacer Trendpilot European Index
'SQEW',#LeaderShares Equity Skew ETF
'GLST',#Global Star Acquisition Inc-A
'CSTA_U',#Constellation Acquisition Corp
'HIW',#海伍兹物业
'ESML',#iShares ESG MSCI USA Small-Cap
'EOI',#Eaton Vance Enhanced Equity Inc
'CHCO',#城市控股
'UBSI',#联合银行
'BSJT',#Invesco BulletShares 2029 High
'EQIX',#易昆尼克斯
'VOD',#沃达丰(US)
'FGRO',#Fidelity Growth Opportunities E
'KHC',#卡夫亨氏
'MFA_C',#MFA Financial Inc Series C Pfd
'FOXW',#FoxWayne Enterprises Acquisitio
'BYNO',#byNordic Acquisition Corp-A
'BMAQ',#Blockchain Moon Acquisition Cor
'SPYC',#Simplify US Equity PLUS Convexi
'SFLR',#Innovator Equity Managed Floor
'SIVBP',#SVB Financial Group Series A Pf
'PENN',#PENN Entertainment Inc
'VPN',#Global X Data Center REITs & Di
'HIX',#Western Asset High Income Fund
'WEBS',#Direxion Daily Dow Jones Intern
'MBCN',#米德尔菲尔德银行
'SGHL',#Signal Hill Acquisition Corp-A
'IPVF',#InterPrivate III Financial Part
'OCAX',#OCA Acquisition Corp-A
'RYLG',#Global X Russell 2000 Covered C
'GRX',#The Gabelli Healthcare & Wellne
'IUSG',#iShares Core S&P U.S. Growth ET
'NUHY',#Nuveen ESG High Yield Corporate
'DCO',#杜科蒙
'GIA',#GigCapital5 Inc
'DIVS',#SmartETFs Dividend Builder ETF
'FLBL',#Franklin Senior Loan ETF
'IOO',#iShares Global 100 ETF
'AMAX',#RH Hedged Multi-Asset Income ET
'CLAY',#Chavant Capital Acquisition Cor
'TCHP',#T. Rowe Price Blue Chip Growth
'MTA',#Metalla Royalty & Streaming Ltd
'JGGCU',#Jaguar Global Growth Corp I Uni
'BPYPP',#Brookfield Property Partners LP
'WAB',#美国西屋制动
'XBOC',#Innovator U.S. Equity Accelerat
'HAYN',#海恩斯国际
'LCTD',#BlackRock World ex U.S. Carbon
'HLT',#希尔顿酒店
'VPL',#亚太ETF-Vanguard FTSE
'WNC',#WABASH国立
'KFYP',#KraneShares CICC China Leaders
'XVV',#iShares ESG Screened S&P 500 ET
'HOG',#哈雷戴维森
'FFA',#First Trust Enhanced Equity Inc
'CITE',#Cartica Acquisition Corp-A
'CVT',#Cvent Holding Corp
'XLSR',#SPDR SSGA US Sector Rotation ET
'CIK',#Credit Suisse Asset Management
'SBNYP',#Signature Bank Series A Pfd
'WRB_H',#W. R. Berkley Corp Debentures
'TT',#特灵科技
'GAST',#Gabelli Automation ETF
'BSJS',#Invesco BulletShares 2028 High
'EXPD',#康捷国际物流
'TEAF',#Ecofin Sustainable and Social I
'HLI',#华利安
'PGZ',#Principal Real Estate Income Fu
'GDX',#金矿ETF-VanEck Vectors
'BITO',#ProShares Bitcoin Strategy ETF
'ECCV',#Eagle Point Credit Co Inc Notes
'BK',#纽约梅隆银行
'NAPR',#Innovator Growth-100 Power Buff
'FTSL',#First Trust Senior Loan Fund ET
'GSIE',#Goldman Sachs ActiveBeta Intern
'BBUS',#JPMorgan BetaBuilders U.S. Equi
'EMGC',#Emerge EMPWR Sustainable Select
'HTGC',#海格投资
'FMAG',#Fidelity Magellan ETF
'BOCT',#Innovator U.S. Equity Buffer ET
'SCSC',#ScanSource Inc
'GTR',#WisdomTree Target Range Fund
'WNS',#WNS控股
'ECNS',#iShares MSCI China Small-Cap ET
'JKHY',#杰克亨利
'FBCG',#Fidelity Blue Chip Growth ETF
'BOH',#夏威夷银行
'XYLD',#Global X S&P 500 Covered Call E
'IHD',#Voya Emerging Markets High Divi
'FAUG',#FT Cboe Vest U.S. Equity Buffer
'DWMF',#WisdomTree International Multif
'MGNI',#Magnite Inc
'KBWB',#Invesco KBW Bank ETF
'JEQ',#abrdn Japan Equity Fund Inc
'EVF',#Eaton Vance Senior Income Trust
'NODK',#NI Holdings Inc
'CSL',#卡莱尔伙伴
'V',#维萨
'DEMZ',#Democratic Large Cap Core ETF
'ESGY',#American Century Sustainable Gr
'HPQ',#惠普
'QLVD',#FlexShares Developed Markets ex
'CWI',#SPDR MSCI ACWI ex-US ETF
'PLDR',#Putnam Sustainable Leaders ETF
'ITRN',#Ituran Location and Control Ltd
'ECOZ',#TrueShares ESG Active Opportuni
'LRN',#Stride Inc
'GWRS',#Global Water Resources Inc
'ROP',#儒博实业
'IEFA',#iShares Core MSCI EAFE ETF
'DJUN',#FT Cboe Vest U.S. Equity Deep B
'NUMG',#Nuveen ESG Mid-Cap Growth ETF
'FVCB',#FVCBankcorp Inc
'LDOS',#Leidos Holdings Inc
'DWX',#SPDR S&P International Dividend
'CBRL',#CB乡村店
'BYRN',#Byrna Technologies Inc
'XDEC',#FT Cboe Vest U.S. Equity Enhanc
'ECAT',#BlackRock ESG Capital Allocatio
'SIHY',#Harbor Scientific Alpha High-Yi
'PJUN',#Innovator U.S. Equity Power Buf
'PRQR',#ProQR Therapeutics NV
'CNMD',#CONMED Corp
'SRCE',#1st Source Corp
'GJP',#STRATS Trust For Dominion Resou
'YMAR',#FT Cboe Vest International Equi
'HLAL',#Wahed FTSE USA Shariah ETF
'ABR_D',#Arbor Realty Trust Inc Series D
'BSJU',#Invesco BulletShares 2030 High
'MOTE',#VanEck Morningstar ESG Moat ETF
'LSEA',#Landsea Homes Corp-A
'PFE',#辉瑞
'ERM',#EquityCompass Risk Manager ETF
'EVH',#Evolent Health Inc-A
'BOUT',#Innovator IBD Breakout Opportun
'IBP',#Installed Building Products Inc
'ALIT',#Alight Inc-A
'ANGL',#堕落天使高收益债ETF
'GLCN',#VanEck China Growth Leaders ETF
'UDEC',#Innovator U.S. Equity Ultra Buf
'EXI',#全球工业ETF-iShares
'PJUL',#Innovator U.S. Equity Power Buf
'ESGV',#Vanguard ESG U.S. Stock ETF
'TFC_O',#Truist Financial Corp Series O
'IQSI',#IQ Candriam ESG International E
'IBHI',#iShares iBonds 2029 Term High Y
'FSP',#Franklin Street Properties Corp
'BHV',#BlackRock Virginia Municipal Bo
'IDHQ',#Invesco S&P International Devel
'FICO',#Fair Isaac Corp
'IWF',#罗素1000成长股ETF-iShares
'SPGP',#Invesco S&P 500 GARP ETF
'NSS',#NuStar Logistics LP Notes
'TDSE',#Cabana Target Drawdown 16 ETF
'DIHP',#Dimensional International High
'VSS',#全球除美国小型股指数ETF
'BCAT',#BlackRock Capital Allocation Tr
'DWM',#WisdomTree International Equity
'VOXX',#奥迪富斯
'NEWT',#Newtek Business Services Corp
'SHEN',#Shenandoah Telecommunications C
'FJUN',#FT Cboe Vest U.S. Equity Buffer
'JHID',#John Hancock International High
'EFR',#Eaton Vance Senior Floating-Rat
'FMAO',#Farmers & Merchants Bancorp Inc
'NDAQ',#纳斯达克
'WBIL',#WBI BullBear Quality 3000 ETF
'GGZ',#The Gabelli Global Small and Mi
'HYUP',#Xtrackers High Beta High Yield
'QSPT',#FT Cboe Vest Nasdaq-100 Buffer
'XBB',#BondBloxx BB-Rated USD High Yie
'STXG',#Strive 1000 Growth ETF
'IDEV',#iShares Core MSCI International
'PSCJ',#Pacer Swan SOS Conservative (Ju
'PRIF_H',#Priority Income Fund Inc Series
'BUFD',#FT Cboe Vest Fund of Deep Buffe
'BEPC',#Brookfield Renewable Corp-A
'XBTF',#VanEck Bitcoin Strategy ETF
'VTWO',#Vanguard Russell 2000 ETF
'SCZ',#小型股ETF-iShares MSCI EAFE
'SLG',#SL Green Realty Corp
'RFEM',#First Trust RiverFront Dynamic
'OCTT',#AllianzIM U.S. Large Cap Buffer
'DBV',#G10外汇利差ETF-PowerShares
'OPBK',#OP Bancorp
'DAUG',#FT Cboe Vest U.S. Equity Deep B
'TUR',#土耳其ETF-iShares MSCI
'RITM',#Rithm Capital Corp
'NJUL',#Innovator Growth-100 Power Buff
'DMAY',#FT Cboe Vest U.S. Equity Deep B
'IAU',#黄金ETF-iShares
'SJIJ',#South Jersey Industries Inc Not
'IGHG',#ProShares Investment Grade-Inte
'ZION',#齐昂银行
'JOAN',#JOANN Inc
'FWONK',#Liberty Media Corp Liberty Form
'AXTA',#Axalta涂层系统
'GRP_U',#Granite Real Estate Investment
'TMUS',#T-Mobile US Inc
'NIB',#可可ETN-iPath
'ARQT',#Arcutis Biotherapeutics Inc
'EFA',#EAFE指数ETF-iShares MSCI
'OAIE',#Optimize AI Smart Sentiment Eve
'PSA_S',#Public Storage Series S Pfd
'SGOL',#Aberdeen Standard Physical Gold
'GLDD',#Great Lakes Dredge & Dock Corp
'GGT',#The Gabelli Multimedia Trust
'STEP',#StepStone Group Inc-A
'EXPO',#毅博
'PHB',#高收益垃圾公司债ETF-PowerShares
'AGM_F',#Federal Agricultural Mortgage C
'HYGV',#FlexShares High Yield Value-Sco
'PMT_B',#PennyMac Mortgage Investment Tr
'GATX',#GATX Corp
'GSSC',#Goldman Sachs Access U.S. Small
'ACTV',#LeaderShares Activist Leaders E
'LC',#LendingClub Corp
'EYPT',#EyePoint Pharmaceuticals Inc
'BBSC',#JPMorgan BetaBuilders U.S. Smal
'AHT_F',#Ashford Hospitality Trust Inc S
'BDX',#碧迪医疗
'ROM',#ProShares Ultra Technology
'PZA',#Invesco National AMT-Free Munic
'IXUS',#iShares Core MSCI Total Interna
'FUSB',#First US Bancshares Inc
'LEXI',#Alexis Practical Tactical ETF
'ASC',#Ardmore Shipping Corp
'SWBI',#Smith & Wesson Brands Inc
'PHD',#Pioneer Floating Rate Trust
'QDPL',#Pacer Metaurus US Large Cap Div
'IQV',#艾昆纬
'CHIE',#中国能源指数ETF-Global X
'JANW',#AllianzIM U.S. Large Cap Buffer
'PLAY',#Dave & Buster's Entertainment I
'DJD',#Invesco Dow Jones Industrial Av
'HTFB',#Horizon Technology Finance Corp
'STLG',#iShares Factors US Growth Style
'GWX',#SPDR S&P International SmallCap
'MOTG',#VanEck Morningstar Global Wide
'CR',#Crane Holdings Co
'PSEP',#Innovator U.S. Equity Power Buf
'GDV_H',#The Gabelli Dividend & Income T
'CORN',#玉米ETF-Teucrium
'OSS',#One Stop Systems Inc
'JSD',#Nuveen Short Duration Credit Op
'TYRA',#Tyra Biosciences Inc
'ICE',#洲际交易所
'VNQI',#全球除美国房地产指数ETF
'EFAD',#ProShares Trust ProShares MSCI
'ARDC',#Ares Dynamic Credit Allocation
'WINA',#威玛克
'XRMI',#Global X S&P 500 Risk Managed I
'PAI',#Western Asset Investment Grade
'ICD',#Independence Contract Drilling
'EGAN',#eGain Corp
'DEO',#帝亚吉欧(US ADR)
'QJUN',#FT Cboe Vest Nasdaq-100 Buffer
'FNOV',#FT Cboe Vest U.S. Equity Buffer
'CSCO',#思科
'BAR',#GraniteShares Gold Trust
'EMMF',#WisdomTree Emerging Markets Mul
'ISMD',#Inspire Small/Mid Cap ETF
'LEGH',#Legacy Housing Corp
'AAAU',#Goldman Sachs Physical Gold ETF
'IJUL',#Innovator International Develop
'FJAN',#FT Cboe Vest U.S. Equity Buffer
'MODL',#VictoryShares WestEnd U.S. Sect
'AOR',#iShares Core Growth Allocation
'GIC',#Global Industrial Co
'ENFN',#Enfusion Inc-A
'JULW',#AllianzIM U.S. Large Cap Buffer
'CLSE',#Convergence Long/Short Equity E
'IWP',#罗素中型成长股ETF-iShares
'FEM',#First Trust Emerging Markets Al
'TIG',#Trean Insurance Group Inc
'BLI',#Berkeley Lights Inc
'RSEE',#Rareview Systematic Equity ETF
'NEE_N',#NextEra Energy Inc Series N Deb
'IAUM',#iShares Gold Trust Micro ETF
'PRIF_J',#Priority Income Fund Inc Series
'DFHY',#Donoghue Forlines Tactical High
'GGT_E',#The Gabelli Multimedia Trust In
'FXC',#加元ETF-CurrencyShares
'OXSQ',#Oxford Square Capital Corp
'XCLR',#Global X S&P 500 Collar 95-110
'JBSS',#John B. Sanfilippo & Son Inc
'FSYD',#Fidelity Sustainable High Yield
'VUG',#成长股指数ETF-Vanguard
'ZIONP',#Zions Bancorp NA Series A Pfd
'IFED',#ETRACS IFED Invest with the Fed
'VXF',#Vanguard Extended Market ETF
'CHGX',#AXS Change Finance ESG ETF
'XTOC',#Innovator U.S. Equity Accelerat
'CHIX',#中国金融指数ETF-Global X
'NZUS',#SPDR MSCI USA Climate Paris Ali
'QQMG',#Invesco ESG NASDAQ 100 ETF
'BGLD',#FT Cboe Vest Gold Strategy Quar
'ATVI',#动视暴雪
'ARKX',#ARK Space Exploration & Innovat
'ENS',#艾诺斯
'PSMR',#Pacer Swan SOS Moderate (April)
'BEPI',#Brookfield BRP Holdings (Canada
'HYGW',#iShares Trust iShares High Yiel
'ASHX',#Xtrackers MSCI China A Inclusio
'ILCG',#iShares Morningstar Growth ETF
'LYEL',#Lyell Immunopharma Inc
'EQUL',#IQ Engender Equality ETF
'SCCO',#南方铜业
'FTXH',#First Trust Nasdaq Pharmaceutic
'FTV',#Fortive Corp
'DECW',#AllianzIM U.S. Large Cap Buffer
'XJUN',#FT Cboe Vest U.S. Equity Enhanc
'USNZ',#Xtrackers Net Zero Pathway Pari
'BWXT',#BWX Technologies Inc
'YEXT',#Yext Inc
'FFSG',#FormulaFolios Smart Growth ETF
'EPOW',#晖阳新能源
'DFAX',#Dimensional World ex U.S. Core
'PTNQ',#Pacer Trendpilot 100 ETF
'RGP',#Resources Connection Inc
'DJUL',#FT Cboe Vest U.S. Equity Deep B
'NREF_A',#NexPoint Real Estate Finance In
'IBHG',#iShares iBonds 2027 Term High Y
'FTF',#Franklin Limited Duration Incom
'VGK',#欧洲ETF-Vanguard FTSE
'MOAT',#VanEck Morningstar Wide Moat ET
'MSCI',#明晟
'BJUL',#Innovator U.S. Equity Buffer ET
'GOODN',#格拉德斯通商业(优先股)
'LEVI',#李维斯
'CMG',#墨式烧烤
'MRVL',#迈威尔科技
'CS',#瑞士信贷
'RNDV',#US Equity Dividend Select ETF
'PB',#Prosperity Bancshares Inc
'SITC_A',#SITE Centers Corp Class A Pfd
'NIC',#Nicolet Bankshares Inc
'PSET',#Principal Price Setters Index E
'PSFF',#Pacer Swan SOS Fund of Funds ET
'FJUL',#FT Cboe Vest U.S. Equity Buffer
'KBA',#KraneShares Bosera MSCI China A
'MVRL',#ETRACS Monthly Pay 1.5X Leverag
'GS_A',#The Goldman Sachs Group Inc Ser
'ESE',#ESCO科技
'EQC_D',#Equity Commonwealth Series D Pf
'OVLH',#Overlay Shares Hedged Large Cap
'NUO',#Nuveen Ohio Quality Municipal I
'RFEU',#First Trust RiverFront Dynamic
'GSID',#Goldman Sachs MarketBeta Intern
'IMNM',#Immunome Inc
'AERC',#AeroClean Technologies Inc
'PCSB',#PCSB Financial Corp
'ARBE',#Arbe Robotics Ltd
'KAPR',#Innovator U.S. Small Cap Power
'SCPL',#SciPlay Corp-A
'SPEU',#SPDR Portfolio Europe ETF
'SSXU',#Day Hagan/Ned Davis Research Sm
'QMAR',#FT Cboe Vest Nasdaq-100 Buffer
'VWE',#Vintage Wine Estates Inc
'FLHY',#Franklin High Yield Corporate E
'BSJP',#Invesco BulletShares 2025 High
'EQH',#安盛公平控股
'NAT',#Nordic American Tankers Ltd
'CSSEN',#Chicken Soup for the Soul Enter
'IBHH',#iShares iBonds 2028 Term High Y
'OCIO',#ClearShares OCIO ETF
'GHC',#格雷厄姆控股
'EASG',#Xtrackers MSCI EAFE ESG Leaders
'XHB',#家园建设ETF-SPDR S&P
'LVHD',#Franklin U.S. Low Volatility Hi
'VRT',#Vertiv Holdings Co-A
'XB',#BondBloxx B-Rated USD High Yiel
'DBX',#Dropbox Inc-A
'MSD',#Morgan Stanley Emerging Markets
'XPND',#First Trust Expanded Technology
'MAGA',#Point Bridge America First ETF
'UJUL',#Innovator U.S. Equity Ultra Buf
'BMAY',#Innovator U.S. Equity Buffer ET
'JOF',#Japan Smaller Capitalization Fu
'CBAN',#科勒尼
'IQDE',#FlexShares International Qualit
'SIXJ',#AllianzIM U.S. Large Cap 6 Mont
'LETB',#AdvisorShares Let Bob AI Powere
'EFAX',#SPDR MSCI EAFE Fossil Fuel Rese
'OCEN',#IQ Clean Oceans ETF
'ROG',#罗杰斯
'CI',#信诺
'PLD',#安博
'JNK',#高收益债ETF-SPDR
'IVT',#InvenTrust Properties Corp
'BRT',#BRT房地产信托
'JSMD',#Janus Henderson Small/Mid Cap G
'SPXC',#SPX Technologies Inc
'THY',#Toews Agility Shares Dynamic Ta
'PHT',#Pioneer High Income Trust
'FITBP',#Fifth Third Bancorp Series A Pf
'UMAY',#Innovator U.S. Equity Ultra Buf
'TFX',#泰利福
'QTJL',#Innovator Growth Accelerated Pl
'PDN',#Invesco FTSE RAFI Developed Mar
'ILPT',#工业物流房地产信托
'HPX',#HPX Corp Unit Cons-A
'USMC',#Principal U.S. Mega-Cap Multi-F
'HCVI',#Hennessy Capital Investment Cor
'STEL',#Stellar Bancorp Inc
'CATC',#Cambridge Bancorp
'OSI',#Osiris Acquisition Corp-A
'BTF',#Valkyrie Bitcoin Strategy ETF
'FIVG',#Defiance Next Gen Connectivity
'EGPT',#埃及ETF-VanEck Vectors
'BALT',#Innovator Defined Wealth Shield
'SLI',#Standard Lithium Ltd
'HYB',#The New America High Income Fun
'GSEU',#Goldman Sachs ActiveBeta Europe
'OBOR',#KraneShares MSCI One Belt One R
'AHYB',#American Century Select High Yi
'ACAH',#Atlantic Coastal Acquisition Co
'ROK',#罗克韦尔自动化
'TNC',#坦能
'BKHY',#BNY Mellon High Yield Beta ETF
'DIVI',#Franklin International Core Div
'COWG',#Pacer US Large Cap Cash Cows Gr
'SSP',#The E.W. Scripps Co-A
'BSJN',#Invesco BulletShares 2023 High
'FWONA',#Liberty Media Corp Liberty Form
'GLD',#黄金ETF-SPDR
'CDAQU',#Compass Digital Acquisition Cor
'FRXB_U',#Forest Road Acquisition Corp II
'HUM',#哈门那
'TWNI',#Tailwind International Acquisit
'VTHR',#Vanguard Russell 3000 ETF
'ISAA',#Iron Spark I Inc-A
'NVSAU',#New Vista Acquisition Corp Unit
'NVSA',#New Vista Acquisition Corp-A
'ATMVU',#AlphaVest Acquisition Corp Unit
'SVFA',#SVF Investment Corp-A
'PORT_U',#Southport Acquisition Corp Unit
'SGII',#Seaport Global Acquisition II C
'DFND',#Reality Shares DIVCON Dividend
'TRIS',#Tristar Acquisition I Corp-A
'HUDAU',#Hudson Acquisition I Corp Unit
'HMAC',#Hainan Manaslu Acquisition Corp
'MGK',#Vanguard Mega Cap Growth ETF
'PGAL',#葡萄牙ETF-Global X MSCI
'BRAC',#Broad Capital Acquisition Corp
'QTJA',#Innovator Growth Accelerated Pl
'TMKR',#Tastemaker Acquisition Corp-A
'INCY',#因塞特医疗
'DBAW',#Xtrackers MSCI All World ex US
'DSEP',#FT Cboe Vest U.S. Equity Deep B
'WINN',#Harbor Long-Term Growers ETF
'MBLY',#Mobileye Global Inc-A
'ADRT',#Ault Disruptive Technologies Co
'GDNR',#Gardiner Healthcare Acquisition
'EURL',#Direxion Daily FTSE Europe Bull
'HYLB',#Xtrackers USD High Yield Corpor
'FAN',#First Trust Global Wind Energy
'HEFA',#iShares Currency Hedged MSCI EA
'PNR',#滨特尔
'EBC',#Eastern Bankshares Inc
'APAC',#StoneBridge Acquisition Corp-A
'COCO',#The Vita Coco Co Inc
'FNVT',#Finnovate Acquisition Corp-A
'DECA',#Denali Capital Acquisition Corp
'FQAL',#Fidelity Quality Factor ETF
'OOMA',#Ooma Inc
'NEP',#NextEra Energy Partners LP
'BUFF',#Innovator Laddered Fund of U.S.
'RAD',#来德爱
'IQDF',#FlexShares International Qualit
'ROCGU',#Roth CH Acquisition IV Co Unit
'KJUL',#Innovator U.S. Small Cap Power
'FTHY',#First Trust High Yield Opportun
'VONG',#Vanguard Russell 1000 Growth ET
'SES',#SES AI Corp-A
'OSIS',#OSI Systems Inc
'SILC',#矽晶电信
'HEGD',#Swan Hedged Equity US Large Cap
'WOOD',#全球林木ETF-iShares
'PSMJ',#Pacer Swan SOS Moderate (July)
'DFSI',#Dimensional International Susta
'EAOA',#iShares ESG Aware Aggressive Al
'SCHG',#Schwab U.S. Large-Cap Growth ET
'PNM',#PNM Resources Inc
'RFP',#Resolute Forest Products Inc
'PBL',#PGIM Portfolio Ballast ETF
'SJNK',#短期高收益债ETF-SPDR
'SSB',#South State Corp
'UAL',#联合航空
'LSCC',#莱迪思半导体
'SGG',#白糖ETN-iPath
'ZBRA',#斑马技术
'VICR',#Vicor Corp
'PAPR',#Innovator U.S. Equity Power Buf
'ACR_C',#ACRES Commercial Realty Corp Se
'ACWX',#全球除美国ETF-iShares MSCI
'APTV',#Aptiv PLC
'TMO',#赛默飞世尔科技
'HAUZ',#Xtrackers International Real Es
'TQQQ',#三倍做多纳斯达克100ETF
'FMAY',#FT Cboe Vest U.S. Equity Buffer
'ESGN',#Columbia International ESG Equi
'ALSN',#艾里逊变速箱
'UNVR',#Univar Solutions Inc
'NVO',#诺和诺德
'AOA',#iShares Core Aggressive Allocat
'EQX',#Equinox Gold Corp
'EWG',#德国ETF-iShares MSCI
'PFEB',#Innovator U.S. Equity Power Buf
'GLU',#The Gabelli Global Utility and
'THRM',#Gentherm Inc
'GHYB',#Goldman Sachs Access High Yield
'PG',#宝洁
'GABF',#Gabelli Financial Services Oppo
'PBS',#Invesco Dynamic Media ETF
'PLAT',#WisdomTree Modern Tech Platform
'HIDE',#Alpha Architect High Inflation
'BBIN',#JPMorgan BetaBuilders Internati
'GIS',#通用磨坊
'YALA',#雅乐科技
'BTG',#B2Gold Corp
'OTIS',#Otis Worldwide Corp
'GLDM',#SPDR Gold MiniShares Trust
'PFN',#PIMCO Income Strategy Fund II
'JPT',#Nuveen Preferred and Income Fun
'PFXNZ',#PhenixFIN Corp Notes
'IMCG',#iShares Morningstar Mid-Cap Gro
'FTAG',#First Trust Indxx Global Agricu
'IGM',#iShares Expanded Tech Sector ET
'GLP_B',#Global Partners LP Series B Pfd
'C_J',#Citigroup Inc Series J Pfd
'SESG',#Sprott ESG Gold ETF
'BHK',#BlackRock Core Bond Trust
'MOTI',#VanEck Morningstar Internationa
'SEIQ',#SEI Enhanced U.S. Large Cap Qua
'KOCT',#Innovator U.S. Small Cap Power
'HYDR',#Global X Hydrogen ETF
'STNC',#Hennessy Stance ESG Large Cap E
'EARN',#Ellington Residential Mortgage
'NUEM',#Nuveen ESG Emerging Markets Equ
'BAC_E',#Bank of America Corp Series E P
'EQBK',#Equity Bancshares Inc-A
'CMS_C',#CMS Energy Corp Series C Pfd
'WASH',#华盛顿信托银行
'FOCT',#FT Cboe Vest U.S. Equity Buffer
'SPUS',#SP Funds S&P 500 Sharia Industr
'IQHI',#IQ MacKay ESG High Income ETF
'IT',#加特纳
'JIDA',#JPMorgan ActiveBuilders Interna
'ULE',#二倍做多欧元ETF-ProShares
'FHYS',#Federated Hermes Short Duration
'BUFT',#FT Cboe Vest Buffered Allocatio
'WFHY',#WisdomTree U.S. High Yield Corp
'CIM_D',#Chimera Investment Corp Series
'EP_C',#El Paso Energy Capital Trust I
'RYT',#标普500科技股等权ETF-Guggenheim
'CEFA',#Global X S&P Catholic Values De
'ASEA',#东南亚ETF-Global X
'RNLC',#Large Cap US Equity Select ETF
'STGF',#Merk Stagflation ETF
'CHD',#丘奇&德怀特
'PDEC',#Innovator U.S. Equity Power Buf
'ACGLN',#Arch Capital Group Ltd Series G
'ECH',#MSCI智利ETF-iShares
'CATY',#国泰万通金控
'DIEM',#Franklin Emerging Market Core D
'IWFG',#IQ Winslow Focused Large Cap Gr
'QTAP',#Innovator Growth Accelerated Pl
'SHYG',#iShares 0-5 Year High Yield Cor
'USER',#UserTesting Inc
'TRND',#Pacer Trendpilot Fund of Funds
'JRS',#Nuveen Real Estate Income Fund
'EVOP',#EVO Payments Inc-A
'ZIG',#The Acquirers Fund
'SWZ',#The Swiss Helvetia Fund
'EEMV',#iShares Edge MSCI Min Vol Emerg
'WAFD',#华盛顿联邦储蓄
'JPI',#Nuveen Preferred and Income Ter
'RYLD',#Global X Russell 2000 Covered C
'RZG',#Invesco S&P SmallCap 600 Pure G
'FFTY',#Innovator IBD 50 ETF
'WCC_A',#WESCO International Inc Series
'LBC',#Luther Burbank Corp
'CARR',#Carrier Global Corp
'GRMN',#佳明
'ACWV',#iShares Edge MSCI Min Vol Globa
'IJAN',#Innovator International Develop
'DSL',#DoubleLine Income Solutions Fun
'TMFC',#Motley Fool 100 Index ETF
'TBNK',#Territorial Bancorp Inc
'USXF',#iShares ESG Advanced MSCI USA E
'ATCO',#Atlas Corp
'SRL',#Scully Royalty Ltd
'FLGR',#Franklin FTSE Germany ETF
'HIFS',#欣厄姆银行
'SCHW_J',#The Charles Schwab Corp Series
'SNN',#施乐辉公司
'NJAN',#Innovator Growth-100 Power Buff
'VZ',#威瑞森通讯
'PLMR',#Palomar Holdings Inc
'BRAG',#Bragg Gaming Group Inc
'GAA',#Cambria Global Asset Allocation
'SPE',#Special Opportunities Fund
'IAUF',#iShares Gold Strategy ETF
'AILG',#Alpha Intelligent - Large Cap G
'VNCE',#文斯控股
'GHG',#格林酒店
'VEU',#全球除美国ETF-Vanguard FTSE
'TFC',#Truist Financial Corp
'USHY',#iShares Broad USD High Yield Co
'KORU',#Direxion Daily South Korea Bull
'HDMV',#First Trust Horizon Managed Vol
'UGE',#ProShares Ultra Consumer Goods
'SACC',#Sachem Capital Corp Notes
'IBHC',#iShares iBonds 2023 Term High Y
'FSBC',#Five Star Bancorp
'HYG',#高收益公司债ETF-iShares iBoxx
'PSA_H',#Public Storage Series H PFd
'QGRW',#WisdomTree U.S. Quality Growth
'TWO_A',#Two Harbors Investment Corp Ser
'HPE',#慧与
'HTLD',#哈特兰快递
'HFGO',#Hartford Large Cap Growth ETF
'JNJ',#强生
'NBTB',#NBT Bancorp Inc
'TFC_R',#Truist Financial Corp Series R
'UNOV',#Innovator U.S. Equity Ultra Buf
'ZHDG',#ZEGA Buy and Hedge ETF
'DEX',#Delaware Enhanced Global Divide
'PSFD',#Pacer Swan SOS Flex (January) E
'EQH_A',#Equitable Holdings Inc Series A
'YDEC',#FT Cboe Vest International Equi
'FOSL',#福斯尔
'WRND',#IQ Global Equity R&D Leaders ET
'MKSI',#万机仪器
'HYDB',#iShares Edge High Yield Defensi
'NVG',#Nuveen AMT-Free Municipal Credi
'FDG',#American Century Focused Dynami
'FLEE',#Franklin FTSE Europe ETF
'FGLD',#Franklin Responsibly Sourced Go
'NYCB_U',#NEW YORK COMMUNITY CAPITAL TRUS
'MGIC',#Magic Software Enterprises Ltd
'SPGI',#标普全球
'SCJ',#iShares MSCI Japan Sm Cap
'APT',#Alpha Pro Tech Ltd
'FN',#Fabrinet
'PCM',#PCM Fund
'EVO',#Evotec SE ADR
'DWAS',#Invesco DWA SmallCap Momentum E
'DVYE',#iShares Emerging Markets Divide
'XHYI',#BondBloxx USD High Yield Bond I
'BUZZ',#VanEck Social Sentiment ETF
'JGRO',#JPMorgan Active Growth ETF
'EWD',#瑞典ETF-iShares MSCI
'PTIN',#Pacer Trendpilot International
'BAC',#美国银行
'IETC',#iShares U.S. Tech Independence
'HYBB',#iShares BB Rated Corporate Bond
'SPD',#Simplify US Equity PLUS Downsid
'MRAD',#SmartETFs Advertising & Marketi
'EWY',#韩国ETF-iShares MSCI
'NTSX',#WisdomTree 90/60 U.S. Balanced
'DE',#迪尔
'EWJV',#iShares MSCI Japan Value ETF
'PABU',#iShares Paris-Aligned Climate M
'FOMO',#AXS FOMO ETF
'XCCC',#BondBloxx CCC-Rated USD High Yi
'WLTH',#LifeGoal Wealth Builder ETF
'FLTW',#Franklin FTSE Taiwan ETF
'CORT',#Corcept Therapeutics Inc
'BUYZ',#Franklin Disruptive Commerce ET
'MRCC',#Monroe Capital Corp
'COF_L',#Capital One Financial Corp Seri
'ALTG',#Alta Equipment Group Inc-A
'TFLR',#T. Rowe Price Floating Rate ETF
'QLS',#IQ Hedge Long Short Tracker ETF
'CMI',#康明斯
'CLSM',#Cabana Target Leading Sector Mo
'BCAB',#BioAtla Inc
'VLYPO',#Valley National Bancorp Series
'BCV',#Bancroft Fund
'MHUA',#美华国际医疗
'HTUS',#Hull Tactical US ETF
'KNGS',#UPHOLDINGS Compound Kings ETF
'TEMP',#JPMorgan Climate Change Solutio
'CEW',#新兴市场货币ETF-WisdomTree
'MFV',#MFS Special Value Trust
'HYTR',#CP High Yield Trend ETF
'PMT_A',#PennyMac Mortgage Investment Tr
'MCSE',#Martin Currie Sustainable Inter
'GIM',#Templeton Global Income Fund
'JEMA',#JPMorgan ActiveBuilders Emergin
'ARWR',#Arrowhead Pharmaceuticals Inc
'PFIS',#人民金服
'KRBN',#KraneShares Global Carbon Strat
'TDSD',#Cabana Target Drawdown 13 ETF
'PUTW',#WisdomTree PutWrite Strategy Fu
'NOMD',#Nomad Foods Ltd
'IWO',#罗素2000成长股ETF-iShares
'BAC_P',#Bank of America Corp Series PP
'GATO',#Gatos Silver Inc
'FNB',#F.N.B. Corp
'SQLV',#Royce Quant Small-Cap Quality V
'AMED',#阿米斯医疗
'NYCB',#纽约社区银行
'VXUS',#Vanguard Total International St
'BSJR',#Invesco BulletShares 2027 High
'SMCI',#超微电脑
'AGCO',#爱科集团
'BSEP',#Innovator U.S. Equity Buffer ET
'CNYA',#iShares MSCI China A ETF
'FLEH',#Franklin FTSE Europe Hedged ETF
'WWJD',#Inspire International ETF
'FDP',#戴尔蒙特新鲜制造
'EBR_B',#巴西电力-优先股
'DPZ',#达美乐比萨(US)
'UAUG',#Innovator U.S. Equity Ultra Buf
'IMRX',#Immuneering Corp-A
'UHT',#Universal Health Realty Income
'SLVO',#Credit Suisse X-Links Silver Sh
'QRMI',#Global X NASDAQ 100 Risk Manage
'BIO',#Bio Rad实验室-A
'BKCH',#Global X Blockchain ETF
'USEP',#Innovator U.S. Equity Ultra Buf
'ETX',#Eaton Vance Municipal Income 20
'DINT',#Davis Select International ETF
'BBEU',#JPMorgan BetaBuilders Europe ET
'MSFT',#微软
'AIRR',#First Trust RBA American Indust
'XHYF',#BondBloxx USD High Yield Bond F
'CSII',#Cardiovascular Systems Inc
'DTW',#DTE Energy Co Series E Debentur
'QQJG',#Invesco ESG NASDAQ Next Gen 100
'QQQ',#纳斯达克100ETF-ProShares
'DEHP',#Dimensional Emerging Markets Hi
'IBET',#iBET Sports Betting & Gaming ET
'UJUN',#Innovator U.S. Equity Ultra Buf
'LONZ',#PIMCO Senior Loan Active Exchan
'VSGX',#Vanguard ESG International Stoc
'DFEV',#Dimensional Emerging Markets Va
'OCN',#Ocwen Financial Corp
'IMXI',#国际货币快递
'NTGR',#NETGEAR Inc
'DMXF',#iShares ESG Advanced MSCI EAFE
'SONY',#索尼
'BSJQ',#Invesco BulletShares 2026 High
'USNA',#优莎娜
'NWLG',#Nuveen Winslow Large-Cap Growth
'SEVN',#Seven Hills Realty Trust
'KDP',#Keurig Dr Pepper Inc
'RC_E',#Ready Capital Corp Series E Pfd
'PDM',#Piedmont Office Realty Trust In
'IBHD',#iShares iBonds 2024 Term High Y
'WING',#Wingstop Inc
'BDXB',#Becton Dickinson and Co Series
'BXP',#波士顿地产
'KHYB',#KraneShares Asia Pacific High I
'T',#美国电话电报
'PFFV',#Global X Variable Rate Preferre
'QQQM',#Invesco NASDAQ 100 ETF
'WAFDP',#Washington Federal Inc Series A
'NERD',#Roundhill Video Games ETF
'NMI',#Nuveen Municipal Income Fund
'NUS',#如新集团
'NUSI',#Nationwide Nasdaq-100 Risk-Mana
'OCTW',#AllianzIM U.S. Large Cap Buffer
'WFC_Q',#Wells Fargo & Co Series Q Pfd
'DGII',#美国迪进国际
'HEQT',#Simplify Hedged Equity ETF
'CL',#高露洁
'MDRRP',#Medalist Diversified REIT Inc S
'NYCB_A',#New York Community Bancorp Inc
'SMHI',#SEACOR Marine Holdings Inc
'HEDJ',#欧洲证券汇率对冲ETF-WisdomTree
'MTVR',#Fount Metaverse ETF
'BOE',#BlackRock Enhanced Global Divid
'CBNK',#Capital Bancorp Inc
'INSW',#International Seaways Inc
'IGLD',#FT Cboe Vest Gold Strategy Targ
'TBLD',#Thornburg Income Builder Opport
'SHYL',#Xtrackers Short Duration High Y
'LGH',#HCM Defender 500 Index ETF
'IOCT',#Innovator International Develop
'MMSC',#First Trust Multi-Manager Small
'SPHB',#Invesco S&P 500 High Beta ETF
'BJK',#博彩ETF-VanEck Vectors
'SPR',#Spirit AeroSystems Holdings Inc
'AMSWA',#美国软件
'FFIN',#第一金融银行股份(德克萨斯州)
'ATCOL',#Atlas Corp Notes
'WIZ',#Merlyn.AI Bull-Rider Bear-Fight
'ARGO_A',#Argo Group International Holdin
'OTEX',#Open Text Corp
'MGM',#美高梅
'ADME',#Aptus Drawdown Managed Equity E
'JACK',#Jack in the Box Inc
'CAG',#康尼格拉
'ROAM',#Hartford Multifactor Emerging M
'GURU',#Global X Guru Index ETF
'DOC',#Physicians Realty Trust
'JBGS',#JBG史密斯地产
'APOG',#远地点
'TDG',#TransDigm Group Inc
'NULG',#Nuveen ESG Large-Cap Growth ETF
'HBT',#HBT Financial Inc
'OXSQL',#Oxford Square Capital Corp Note
'SIXO',#AllianzIM U.S. Large Cap 6 Mont
'MOD',#摩丁制造
'PFRL',#PGIM Floating Rate Income ETF
'RNWZ',#TrueShares Eagle Global Renewab
'ORGN',#Origin Materials Inc
'IVDG',#Invesco Focused Discovery Growt
'VCXA',#10X Capital Venture Acquisition
'ACRO',#Acropolis Infrastructure Acquis
'WMT',#沃尔玛
'AJG',#亚瑟加拉格尔
'GECCN',#Great Elm Capital Corp Notes
'BTWNU',#Bridgetown Holdings Ltd Unit Co
'SCRM',#Screaming Eagle Acquisition Cor
'GFOR',#Graf Acquisition Corp IV
'APEN',#Apollo Endosurgery Inc
'TTEK',#德照科技
'CPI',#IQ Real Return ETF
'GIPR',#Generation Income Properties In
'LRND',#IQ U.S. Large Cap R&D Leaders E
'KVSA',#Khosla Ventures Acquisition Co-
'IRAA',#Iris Acquisition Corp-A
'CHMG',#Chemung Financial Corp
'CDAQ',#Compass Digital Acquisition Cor
'POCT',#Innovator U.S. Equity Power Buf
'MTAL',#Metals Acquisition Corp-A
'PUCKU',#Goal Acquisitions Corp Unit Con
'BCH',#智利银行
'YOTA',#Yotta Acquisition Corp
'NKG',#Nuveen Georgia Quality Municipa
'FACA_U',#Figure Acquisition Corp I Unit
'XPDB',#Power & Digital Infrastructure
'WGRO',#WisdomTree U.S. Growth & Moment
'MER_K',#Bank of America Corp Notes
'VLATU',#Valor Latitude Acquisition Corp
'TIOAU',#Tio Tech A Unit Cons of 1 CL A
'EOCW_U',#Elliott Opportunity II Corp Uni
'VTWG',#Vanguard Russell 2000 Growth ET
'RJAC',#Jackson Acquisition Co-A
'IGAC',#IG Acquisition Corp-A
'EACPU',#Edify Acquisition Corp Unit Con
'VBOCU',#Viscogliosi Brothers Acquisitio
'MON',#Monument Circle Acquisition Cor
'WPCB_U',#Warburg Pincus Capital Corp I—
'VPCBU',#VPC Impact Acquisition Holdings
'TBSA',#TB SA Acquisition Corp-A
'PLMIU',#Plum Acquisition Corp I Unit Co
'WPCB',#Warburg Pincus Capital Corp I—
'WPCA',#Warburg Pincus Capital Corp I—
'RKTA',#Rocket Internet Growth Opportun
'PRSRU',#Prospector Capital Corp Unit Co
'TZPS',#TZP Strategies Acquisition Corp
'SLAM',#Slam Corp-A
'ITAQU',#Industrial Tech Acquisitions II
'HHLA_U',#HH&L Acquisition Co Unit Cons o
'HERA',#FTAC Hera Acquisition Corp-A
'BCOR',#Blucora Inc
'TRIS_U',#Tristar Acquisition I Corp Unit
'ROSS',#Ross Acquisition Corp II-A
'TLGA_U',#TLG Acquisition One Corp Unit C
'PACXU',#Pioneer Merger Corp Unit Cons o
'MTRN',#Materion Corp
'GSRMU',#GSR II Meteora Acquisition Corp
'FGMCU',#FG Merger Corp Unit Cons of 1 S
'AAC_U',#Ares Acquisition Corp Unit Cons
'MHN',#BlackRock MuniHoldings New York
'EMCG',#Embrace Change Acquisition Corp
'ASCB',#A SPAC II Acquisition Corp-A
'NETC',#Nabors Energy Transition Corp-A
'KCGI',#Kensington Capital Acquisition
'JATT',#JATT Acquisition Corp-A
'EUM',#ProShares Short MSCI Emerging M
'GSDWU',#Global Systems Dynamics Inc Uni
'DECAU',#Denali Capital Acquisition Corp
'RCS',#PIMCO Strategic Income Fund
'XSEP',#FT Cboe Vest U.S. Equity Enhanc
'EBND',#新兴市场地方债ETF-SPDR
'GTAC',#Global Technology Acquisition C
'DSAQ',#Direct Selling Acquisition Corp
'AVTR',#Avantor Inc
'TKNO',#Alpha Teknova Inc
'TGRW',#T. Rowe Price Growth Stock ETF
'PMF',#PIMCO Municipal Income Fund
'KLDW',#Knowledge Leaders Developed Wor
'SHUA',#SHUAA Partners Acquisition Corp
'PWUP',#PowerUp Acquisition Corp-A
'CENTA',#Central Garden & Pet Co-A
'JEPQ',#JPMorgan Nasdaq Equity Premium
'XDQQ',#Innovator Growth Accelerated ET
'GVCIU',#Green Visor Financial Technolog
'PLAO',#Patria Latin American Opportuni
'CRM',#赛富时
'OXAC',#Oxbridge Acquisition Corp-A
'MCAAU',#Mountain & Co I Acquisition Cor
'GTEK',#Goldman Sachs Future Tech Leade
'PXS',#Pyxis Tankers Inc
'GHYG',#iShares US & Intl High Yield Co
'FBK',#FB Financial Corp
'EWL',#瑞士ETF-iShares MSCI
'ADOC',#Edoc Acquisition Corp-A
'VNO_N',#Vornado Realty Trust Series N P
'IWTR',#iShares MSCI Water Management M
'CGGO',#Capital Group Global Growth Equ
'VIA',#Via Renewables Inc-A
'ACM',#AECOM
'NBH',#Neuberger Berman Municipal Fund
'PSEC_A',#Prospect Capital Corp Series A
'AVNS',#Avanos Medical Inc
'HMNF',#HMN金融
'CCSI',#Consensus Cloud Solutions Inc
'QYLD',#Global X NASDAQ 100 Covered Cal
'GAL',#SPDR SSgA Global Allocation ETF
'HOLX',#豪洛捷
'KWT',#太阳能ETF-VanEck Vectors
'TUG',#STF Tactical Growth ETF
'FRC',#第一共和银行
'CLS',#天弘科技
'DMO',#Western Asset Mortgage Opportun
'CHI',#Calamos Convertible Opportuniti
'TAXF',#American Century Diversified Mu
'FNGU',#MicroSectors FANG Index 3X Leve
'MET_A',#MetLife Inc Series A Pfd
'HL',#赫克拉矿业
'BGT',#BlackRock Floating Rate Income
'FSBW',#FS Bancorp Inc
'SCWX',#SecureWorks Corp-A
'BRKY',#Direxion Breakfast Commodities
'JULT',#AllianzIM U.S. Large Cap Buffer
'SPSC',#SPS Commerce Inc
'GAB',#The Gabelli Equity Trust
'CII',#BlackRock Enhanced Capital and
'CDW',#CDW Corp
'ALTY',#Global X Alternative Income ETF
'TECL',#Direxion Technology Bull 3X Sha
'WEBL',#Direxion Daily Dow Jones Intern
'MANU',#曼联
'PFXF',#VanEck Preferred Securities ex
'POTX',#Global X Cannabis ETF
'PAUG',#Innovator U.S. Equity Power Buf
'CHW',#Calamos Global Dynamic Income F
'FRA',#BlackRock Floating Rate Income
'IGN',#北美多媒体网络ETF-iShares
'XHYT',#BondBloxx USD High Yield Bond T
'BUFB',#Innovator Laddered Allocation B
'ATH_D',#Athene Holding Ltd Series D Pfd
'MFEM',#PIMCO RAFI Dynamic Multi-Factor
'CURE',#三倍做多医疗ETF-Direxion
'FICS',#First Trust International Devel
'AUB',#Atlantic Union Bankshares Corp
'REM',#房地产按揭贷款ETF-iShares
'GLDI',#Credit Suisse X-Links Gold Shar
'OBT',#Orange County Bancorp Inc
'CVS',#西维斯健康
'PXH',#Invesco FTSE RAFI Emerging Mark
'ENOV',#Enovis Corp
'POOL',#Pool Corp
'DAPR',#FT Cboe Vest U.S. Equity Deep B
'QQXT',#First Trust NASDAQ-100 Ex-Techn
'LYV',#Live Nation Entertainment Inc
'GSFP',#Goldman Sachs Future Planet Equ
'QEMM',#SPDR MSCI Emerging Markets Stra
'AQNA',#Algonquin Power & Utilities Cor
'SABR',#Sabre Corp
'TDIV',#First Trust NASDAQ Technology D
'MLVF',#Malvern Bancorp Inc
'ESHY',#Xtrackers J.P. Morgan ESG USD H
'IAPR',#Innovator International Develop
'IHE',#iShares U.S. Pharmaceutical ETF
'IHDG',#WisdomTree International Hedged
'AGM',#联邦农业抵押贷款-C
'IDLB',#Invesco FTSE International Low
'BSMX',#桑坦德银行墨西哥分行
'EWP',#西班牙ETF-iShares MSCI
'COF_J',#Capital One Financial Corp Seri
'OMCL',#Omnicell Inc
'JMM',#Nuveen Multi-Market Income Fund
'BC_A',#Brunswick Corp Notes
'DJAN',#FT Cboe Vest U.S. Equity Deep B
'LQDH',#iShares Interest Rate Hedged Co
'COF_K',#Capital One Financial Corp Seri
'SILV',#SilverCrest Metals Inc
'EMLC',#新兴市场地方货币债ETF
'AAA',#AXS First Priority CLO Bond ETF
'STAR_I',#iStar Inc Series I Pfd
'CALB',#California BanCorp
'FXE',#欧元ETF-CurrencyShares
'ING',#荷兰国际
'HSC',#哈斯科材料
'IQDG',#WisdomTree International Qualit
'ECOW',#Pacer Emerging Markets Cash Cow
'PRH',#Prudential Financial Inc Notes
'KNBE',#KnowBe4 Inc-A
'SMMF',#Summit Financial Group Inc
'SB_D',#Safe Bulkers Inc Series D Pfd
'HYXF',#iShares ESG Advanced High Yield
'FULC',#Fulcrum Therapeutics Inc
'OZ',#Belpointe PREP LLC Unit-A
'RWAYZ',#Runway Growth Finance Corp Note
'DMF',#BNY Mellon Municipal Income
'RJF_A',#瑞杰金融(优先股)
'KEMX',#KraneShares MSCI Emerging Marke
'WRB_G',#W. R. Berkley Corp Debentures
'SSPX',#Janus Henderson U.S. Sustainabl
'GAM_B',#General American Investors Co I
'CMRE_E',#Costamare Inc Pfd-E
'JPHY',#JPMorgan High Yield Research En
'HYLG',#Global X Health Care Covered Ca
'KLIC',#库力索法工业
'OXM',#牛津工业
'PEBK',#北卡罗莱纳国民银行
'LBTYK',#自由全球-C
'NTKI',#Nationwide Russell 2000 Risk-Ma
'GLQ',#Clough Global Equity Fund
'GRBK_A',#Green Brick Partners Inc Series
'APRW',#AllianzIM U.S. Large Cap Buffer
'LOMA',#Loma Negra Compania Industrial
'PNQI',#Invesco NASDAQ Internet ETF
'JIG',#JPMorgan International Growth E
'PSN',#Parsons Corp
'CMBS',#iShares CMBS Bond ETF
'PH',#派克汉尼汾
'FLFR',#Franklin FTSE France ETF
'AAT',#American Assets Trust Inc
'BUFQ',#FT Cboe Vest Fund of Nasdaq-100
'MSTQ',#LHA Market State Tactical Q ETF
'EVCM',#EverCommerce Inc
'EMFQ',#Amplify Emerging Markets FinTec
'HART',#IQ Healthy Hearts ETF
'BWZ',#SPDR Bloomberg Short Term Inter
'MOTO',#SmartETFs Smart Transportation
'AOK',#iShares Core Conservative Alloc
'PTBD',#Pacer Trendpilot US Bond ETF
'A',#安捷伦
'ALL_I',#The Allstate Corp Series I Pfd
'FAST',#快扣
'QQH',#HCM Defender 100 Index ETF
'AON',#怡安保险
'EEMO',#Invesco S&P Emerging Markets Mo
'USAP',#通用不锈钢和合金制品
'QCOM',#高通
'KRMA',#Global X Conscious Companies ET
'ACGLO',#Arch Capital Group Ltd Series F
'RELX',#RELX
'ANSS',#安西斯
'GNTY',#Guaranty Bancshares Inc
'EMP',#Entergy Mississippi LLC Bonds
'VRSN',#威瑞信
'NOCT',#Innovator Growth-100 Power Buff
'RNEM',#Emerging Markets Equity Select
'GEM',#Goldman Sachs ActiveBeta Emergi
'NMK_C',#Niagara Mohawk Power Corp Pfd
'INTU',#财捷
'BME',#BlackRock Health Sciences Trust
'RGA',#美国再保险集团
'UYLD',#Angel Oak UltraShort Income ETF
'ABT',#雅培
'ET_C',#Energy Transfer LP Series C Pfd
'BEPH',#Brookfield BRP Holdings (Canada
'FLSW',#Franklin FTSE Switzerland ETF
'BLKB',#布莱克波特科技
'CHT',#中华电信
'FDX',#联邦快递
'GRID',#First Trust NASDAQ Clean Edge S
'SWKS',#思佳讯
'EOCT',#Innovator Emerging Markets Powe
'RRX',#Regal Rexnord Corp
'IYW',#美国科技ETF-iShares
'EXG',#Eaton Vance Tax-Managed Global
'DUDE',#Merlyn.AI SectorSurfer Momentum
'JBBB',#Janus Henderson B-BBB CLO ETF
'PEPG',#PepGen Inc
'CENT',#Central Garden & Pet Co
'AQNB',#Algonquin Power & Utilities Cor
'SEMR',#SEMrush Holdings Inc-A
'PMAR',#Innovator U.S. Equity Power Buf
'EVT',#Eaton Vance Tax-Advantaged Divi
'NGE',#尼日利亚ETF-Global X MSCI
'DLR_K',#Digital Realty Trust Inc Series
'JJSF',#JJSF食品
'VPG',#Vishay精密集团
'EPAM',#EPAM Systems Inc
'PNI',#PIMCO New York Municipal Income
'PBH',#普雷斯蒂奇
'SIGA',#西佳科技
'GBUY',#Goldman Sachs Future Consumer E
'ETW',#Eaton Vance Tax-Managed Global
'AMH_H',#American Homes 4 Rent Series H
'MPB',#宾州中部银行
'MRGR',#ProShares Merger ETF
'FYX',#First Trust Small Cap Core Alph
'QTUM',#Defiance Quantum ETF
'TACK',#Fairlead Tactical Sector ETF
'PPBI',#太平洋第一合众银行
'OEUR',#ALPS O’Shares Europe Quality D
'NRUC',#National Rural Utilities Cooper
'JHEM',#John Hancock Multifactor Emergi
'FLC',#Flaherty & Crumrine Total Retur
'MDC',#M.D.C. Holdings Inc
'IIIV',#i3 Verticals Inc-A
'EBAY',#易趣
'TYLG',#Global X Information Technology
'HSIC',#亨利香恩服务
'EWT',#台湾ETF-iShares MSCI
'BSMP',#Invesco BulletShares 2025 Munic
'STRA',#斯特雷耶教育
'HTBI',#HomeTrust Bancshares Inc
'SBBA',#Scorpio Tankers Inc Notes
'MMLG',#First Trust Multi-Manager Large
'VRIG',#Invesco Variable Rate Investmen
'FEHY',#FlexShares ESG & Climate High Y
'RNEW',#VanEck Green Infrastructure ETF
'OXLCM',#Oxford Lane Capital Corp Series
'CYB',#人民币ETF-WisdomTree
'PNFPP',#Pinnacle Financial Partners Inc
'IHTA',#Invesco High Income 2024 Target
'GS_K',#The Goldman Sachs Group Inc Ser
'TAFI',#AB Tax-Aware Short Duration Mun
'HNNA',#Hennessy Advisors Inc
'MCY',#默邱利通用
'FLOT',#浮动利率债ETF-iShares
'BUCK',#Simplify Stable Income ETF
'JUCY',#Aptus Enhanced Yield ETF
'NTAP',#美国网存
'DBEU',#Xtrackers MSCI Europe Hedged Eq
'HOM',#LifeGoal Home Down Payment Inve
'IDYA',#IDEAYA生物科学
'NUV',#Nuveen Municipal Value Fund
'ASGI',#abrdn Global Infrastructure Inc
'ARB',#AltShares Merger Arbitrage ETF
'SYNB',#Putnam BioRevolution ETF
'EAOR',#iShares ESG Aware Growth Alloca
'GLP_A',#Global Partners LP Series A Pfd
'NUGO',#Nuveen Growth Opportunities ETF
'GBLD',#Invesco MSCI Green Building ETF
'AMP',#阿默普莱斯金融
'MEM',#Matthews Emerging Markets Equit
'FPEI',#First Trust Institutional Prefe
'TDY',#Teledyne Technologies Inc
'IMGO',#Imago BioSciences Inc
'HBANP',#Huntington Bancshares Inc Serie
'RILYZ',#B. Riley Financial Inc Notes
'ZBH',#捷迈邦美
'XHYD',#BondBloxx USD High Yield Bond C
'NGVC',#Natural Grocers by Vitamin Cott
'TWIN',#双环
'STE',#思泰瑞医疗
'EFAV',#iShares Edge MSCI Min Vol EAFE
'HYBL',#SPDR Blackstone High Income ETF
'UBP',#优士达不动产
'UDN',#做空美元指数ETF-PowerShares
'ITIC',#投资者不动产
'EAFD',#Simplify Developed Ex-US PLUS D
'FDHY',#Fidelity High Yield Factor ETF
'PMAY',#Innovator U.S. Equity Power Buf
'UMAR',#Innovator U.S. Equity Ultra Buf
'WBIF',#WBI BullBear Value 3000 ETF
'SCE_H',#SCE Trust III Pfd
'PAWZ',#ProShares Pet Care ETF
'CBZ',#CBIZ Inc
'ADEA',#Adeia Inc
'FSTR',#LB福斯特
'XLK',#科技ETF-SPDR
'IDME',#International Drawdown Managed
'JELD',#JELD-WEN Holding Inc
'EGF',#BlackRock Enhanced Government F
'FEZ',#欧洲斯托克50ETF-SPDR
'SNSR',#Global X Internet of Things ETF
'BWC',#Blue Whale Acquisition Corp I-A
'CANE',#Teucrium Sugar Fund ETV
'TM',#丰田汽车(US ADR)
'TILE',#Interface Inc
'THCPU',#Thunder Bridge Capital Partners
'MYN',#BlackRock MuniYield New York Qu
'DGNU',#Dragoneer Growth Opportunities
'NXPI',#恩智浦半导体
'LCG',#Sterling Capital Focus Equity E
'FMET',#Fidelity Metaverse ETF
'EZU',#欧元区ETF-iShares MSCI
'TWCB',#Bilander Acquisition Corp-A
'THCP',#Thunder Bridge Capital Partners
'INKM',#SPDR SSGA Income Allocation ETF
'GXII',#GX Acquisition Corp II-A
'FZT',#FAST Acquisition Corp II-A
'CONX',#CONX Corp-A
'PUCK',#Goal Acquisitions Corp
'FMIV',#Forum Merger IV Corp-A
'QFTA_U',#Quantum FinTech Acquisition Cor
'DTOC',#Digital Transformation Opportun
'XPAX',#XPAC Acquisition Corp-A
'TPBA',#TPB Acquisition Corp I-A
'TCOA_U',#Trajectory Alpha Acquisition Co
'GHL',#格林希尔事务所
'TRTL',#TortoiseEcofin Acquisition Corp
'RCAC',#Revelstone Capital Acquisition
'APTM',#Alpha Partners Technology Merge
'WRAC',#Williams Rowland Acquisition Co
'NSTD',#Northern Star Investment Corp I
'NSTC',#Northern Star Investment Corp I
'SECD',#Senior Secured Credit Opportuni
'ZING',#FTAC Zeus Acquisition Corp-A
'MTAC',#MedTech Acquisition Corp-A
'JUGG',#JAWS Juggernaut Acquisition Cor
'EUDV',#ProShares MSCI Europe Dividend
'DNAD',#Social Capital Suvretta Holding
'MITAU',#Coliseum Acquisition Corp Unit
'EOCW',#Elliott Opportunity II Corp-A
'STRE_U',#Supernova Partners Acquisition
'BACA',#Berenson Acquisition Corp I_A
'SPG_J',#Simon Property Group Inc Series
'SAMAU',#Schultze Special Purpose Acquis
'POWRU',#Star Peak Corp II Unit Cons of
'DISAU',#Disruptive Acquisition Corp I U
'CPUH',#Compute Health Acquisition Corp
'APGB',#Apollo Strategic Growth Capital
'STRE',#Supernova Partners Acquisition
'RJAC_U',#Jackson Acquisition Co Unit Con
'POW',#Powered Brands-A
'KAIR',#Kairos Acquisition Corp-A
'KAII',#Kismet Acquisition Two Corp-A
'DISA',#Disruptive Acquisition Corp I-A
'CHAA',#Catcha Investment Corp-A
'AURC',#Aurora Acquisition Corp II-A
'ABGI',#ABG Acquisition Corp I-A
'OPCH',#Option Care Health Inc
'MSDA',#MSD Acquisition Corp-A
'IBER',#Ibere Pharmaceuticals-A
'ENER',#Accretion Acquisition Corp
'PNTM',#Pontem Corp-A
'PDOT',#Peridot Acquisition Corp II-A
'LHC_U',#Leo Holdings Corp II Unit Cons
'GPAC',#Global Partner Acquisition Corp
'BNIX',#Bannix Acquisition Corp
'ANAC_U',#Arctos NorthStar Acquisition Co
'AEACU',#Authentic Equity Acquisition Co
'VII',#7GC & Co Holdings Inc-A
'SVFAU',#SVF Investment Corp Unit Cons o
'SCOB',#ScION Tech Growth II-A
'HHLA',#HH&L Acquisition Co-A
'FTVI',#FinTech Acquisition Corp VI-A
'ANAC',#Arctos NorthStar Acquisition Co
'NDMO',#Nuveen Dynamic Municipal Opport
'FCAX',#Fortress Capital Acquisition Co
'AKIC',#Sports Ventures Acquisition Cor
'MSSA',#Metal Sky Star Acquisition Corp
'PACX',#Pioneer Merger Corp-A
'FATP',#Fat Projects Acquisition Corp-A
'SVII',#Spring Valley Acquisition Corp
'FHLT',#Future Health ESG Corp
'GIAC',#Gesher I Acquisition Corp
'CIIG',#CIIG Capital Partners II Inc-A
'GLLI',#Globalink Investment Inc
'BITE',#Bite Acquisition Corp
'IRRX',#Integrated Rail and Resources A
'ACAB',#Atlantic Coastal Acquisition Co
'HFND',#Unlimited HFND Multi-Strategy R
'DDEC',#FT Cboe Vest U.S. Equity Deep B
'ACAC',#Acri Capital Acquisition Corp-A
'LBBB',#Lakeshore Acquisition II Corp
'BRKH',#BurTech Acquisition Corp-A
'UTAA',#UTA Acquisition Corp-A
'BWAQ',#Blue World Acquisition Corp-A
'BIOSU',#BioPlus Acquisition Corp Unit C
'AIB',#AIB Acquisition Corp-A
'NFNT',#Infinite Acquisition Corp-A
'LIBY',#Liberty Resources Acquisition C
'GIA_U',#GigCapital5 Inc Unit Cons of 1
'GSJY',#Goldman Sachs ActiveBeta Japan
'SHAP_U',#Spree Acquisition Corp 1 Ltd Un
'BIOS',#BioPlus Acquisition Corp-A
'RENE',#Cartesian Growth Corp II-A
'IQMD',#Intelligent Medicine Acquisitio
'LIVB',#LIV Capital Acquisition Corp II
'RCFA',#RCF Acquisition Corp-A
'TGR',#Kimbell Tiger Acquisition Corp-
'VHNA',#Vahanna Tech Edge Acquisition I
'FRBN',#Forbion European Acquisition Co
'ALSA',#Alpha Star Acquisition Corp
'SRLN',#SPDR Blackstone GSO Senior Loan
'CMCA',#Capitalworks Emerging Markets A
'BTZ',#BlackRock Credit Allocation Inc
'LGST',#Semper Paratus Acquisition Corp
'ACDI',#Ascendant Digital Acquisition C
'RENEU',#Cartesian Growth Corp II Unit C
'KACL',#Kairous Acquisition Corp Ltd
'ALSAU',#Alpha Star Acquisition Corp Uni
'VMCA',#Valuence Merger Corp I-A
'CLSC',#Cabana Target Leading Sector Co
'MCAA',#Mountain & Co I Acquisition Cor
'ACAQ',#Athena Consumer Acquisition Cor
'QCLR',#Global X NASDAQ 100 Collar 95-1
'LGTOU',#Legato Merger Corp II Unit Cons
'BSGA',#Blue Safari Group Acquisition C
'DOCT',#FT Cboe Vest U.S. Equity Deep B
'BNFT',#Benefitfocus Inc
'DCRDU',#Decarbonization Plus Acquisitio
'PSCX',#Pacer Swan SOS Conservative (Ja
'EFG',#iShares MSCI EAFE Growth ETF
'FXB',#英镑ETF-CurrencyShares
'MFA',#MFA Financial Inc
'STC',#Stewart Information Services Co
'QPX',#AdvisorShares Q Dynamic Growth
'CASH',#Pathward Financial Inc
'UBP_H',#Urstadt Biddle Properties Inc S
'ESQ',#艾斯奎尔金融控股
'CME',#芝加哥商业交易所
'KEUA',#KraneShares European Carbon All
'WLKP',#Westlake Chemical Partners LP
'DTF',#DTF Tax-Free Income 2028 Term F
'MGI',#速汇金国际
'GAB_H',#The Gabelli Equity Trust Inc Se
'NFLT',#Virtus Newfleet Multi-Sector Bo
'TAYD',#Taylor Devices Inc
'PZT',#Invesco New York AMT-Free Munic
'XHYH',#BondBloxx USD High Yield Bond H
'TDSC',#Cabana Target Drawdown 10 ETF
'AJRD',#Aerojet Rocketdyne Holdings Inc
'SPHY',#SPDR Portfolio High Yield Bond
'RILYM',#B. Riley Financial Inc Notes
'ISEM',#Invesco RAFI Strategic Emerging
'NAZ',#Nuveen Arizona Quality Municipa
'ALGN',#艾利科技
'NAD',#Nuveen Quality Municipal Income
'REMG',#SPDR Bloomberg SASB Emerging Ma
'BSBK',#Bogota Financial Corp
'NMAI',#Nuveen Multi-Asset Income Fund
'BLK',#贝莱德
'SOXX',#半导体ETF-iShares PHLX
'BSCE',#Invesco BulletShares 2023 USD E
'JPXN',#iShares JPX-Nikkei 400 ETF
'ATEC',#阿尔法泰克
'OXSQZ',#Oxford Square Capital Corp Note
'BSMQ',#Invesco BulletShares 2026 Munic
'BSMR',#Invesco BulletShares 2027 Munic
'IWC',#微型股ETF-iShares
'PCN',#PIMCO Corporate & Income Strate
'SF_C',#Stifel Financial Corp Series C
'UCON',#First Trust TCW Unconstrained P
'PWZ',#Invesco California AMT-Free Mun
'NLY_F',#Annaly Capital Management Inc S
'FFTG',#FormulaFolios Tactical Growth E
'OR',#Osisko Gold Royalties Ltd
'CRYP',#AdvisorShares Managed Bitcoin S
'SSG',#ProShares UltraShort Semiconduc
'SAY',#Saratoga Investment Corp Notes
'MORT',#VanEck Mortgage REIT Income ETF
'ALV',#奥托立夫
'FLTR',#VanEck IG Floating Rate ETF
'CSHI',#NEOS Enhanced Income Cash Alter
'RJF_B',#瑞杰金融(优先股)
'FSLD',#Fidelity Sustainable Low Durati
'EPAC',#实用动力
'CLOI',#VanEck CLO ETF
'CUBI_E',#Customers Bancorp Inc Series E
'SPCZ',#RiverNorth Enhanced Pre-Merger
'PSFE',#Paysafe Ltd-A
'MRSK',#Toews Agility Shares Managed Ri
'FINS',#Angel Oak Financial Strategies
'BKES',#BNY Mellon Sustainable Global E
'NUDM',#Nuveen ESG International Develo
'LFG',#Archaea Energy Inc-A
'WLY',#约翰威立国际出版-A
'NID',#Nuveen Intermediate Duration Mu
'MLR',#Miller Industries Inc
'RNRG',#Global X Renewable Energy Produ
'COW',#活禽ETN-iPath
'LSPD',#Lightspeed Commerce Inc
'EA',#艺电
'HEWG',#德国汇率对冲ETF-iShares
'EWJ',#日本ETF-iShares MSCI
'CCEP',#可口可乐欧洲太平洋合伙(US)
'PHYS',#Sprott Physical Gold Trust
'MCI',#Barings Corporate Investors
'CAF',#中国A股指数ETF-摩根士丹利
'TMFX',#Motley Fool Next Index ETF
'LOUP',#Innovator Loup Frontier Tech ET
'QAI',#多策略对冲基金复制ETF-IQ
'HAIL',#SPDR S&P Kensho Smart Mobility
'FFND',#The Future Fund Active ETF
'GGRW',#Gabelli Growth Innovators ETF
'CNXT',#中创100ETF-VanEck Vectors华夏
'CTBI',#大众信托合众银行
'SPH',#Suburban Propane Partners LP
'INSI',#Insight Select Income Fund
'XWEB',#SPDR S&P Internet ETF
'MCRI',#Monarch Casino & Resort Inc
'RTO',#能多洁
'CRL',#查尔斯河
'HAPY',#Harbor Corporate Culture Leader
'EMXC',#iShares MSCI Emerging Markets e
'FCVT',#First Trust SSI Strategic Conve
'NRG',#NRG Energy Inc
'IRBT',#iRobot Corp
'YUM',#百胜餐饮
'JLS',#Nuveen Mortgage and Income Fund
'CWB',#可转债ETF-SPDR
'VRE',#Veris Residential Inc
'COF_N',#Capital One Financial Corp Seri
'TBIL',#US Treasury 3 Month Bill ETF
'IPOS',#Renaissance International IPO E
'BAX',#百特国际
'XHLF',#BondBloxx Bloomberg Six Month T
'BR',#布罗德里奇金融
'XLV',#医疗ETF-SPDR
'LEMB',#新兴市场当地国债ETF-iShares
'BOH_A',#Bank of Hawaii Corp Series A Pf
'POSH',#Poshmark Inc-A
'YSEP',#FT Cboe Vest International Equi
'ISCG',#iShares Morningstar Small-Cap G
'NHI',#National Health Investors Inc
'EQH_C',#Equitable Holdings Inc Series C
'ADI',#亚德诺
'NOVA',#Sunnova Energy International In
'FOCS',#Focus Financial Partners Inc-A
'CWAN',#Clearwater Analytics Holdings I
'TPR',#Tapestry Inc
'PTLC',#Pacer Trendpilot US Large Cap E
'FSIG',#First Trust Limited Duration In
'CMF',#iShares California Muni Bond ET
'PSF',#Cohen & Steers Select Preferred
'FTEC',#Fidelity MSCI Information Techn
'HSRT',#Hartford Short Duration ETF
'LDP',#Cohen & Steers Limited Duration
'GS_C',#The Goldman Sachs Group Inc Ser
'IYLD',#iShares Morningstar Multi-Asset
'COWN',#高宏集团-A
'KRC',#吉劳埃地产
'FPX',#First Trust US Equity Opportuni
'SFYF',#SoFi Social 50 ETF
'FUMB',#First Trust Ultra Short Duratio
'CGGR',#Capital Group Growth ETF
'SOXQ',#Invesco PHLX Semiconductor ETF
'OPNT',#Opiant Pharmaceuticals Inc
'RTAI',#Rareview Tax Advantaged Income
'SUB',#iShares Short-Term National Mun
'EAI',#Entergy Arkansas LLC Bonds 2066
'PLXS',#普雷克萨斯
'ERII',#Energy Recovery Inc
'MKC',#味好美
'AVSE',#Avantis Responsible Emerging Ma
'QQQE',#Direxion NASDAQ-100 Equal Weigh
'NCV_A',#Virtus Convertible & Income Fun
'CEMB',#iShares J.P. Morgan EM Corporat
'OVF',#Overlay Shares Foreign Equity E
'DBEM',#Xtrackers MSCI Emerging Markets
'ALE',#阿里特
'TDSB',#Cabana Target Drawdown 7 ETF
'TDSA',#Cabana Target Drawdown 5 ETF
'HYLV',#IQ S&P High Yield Low Volatilit
'JAMF',#Jamf Holding Corp
'BWEB',#Bitwise Funds Trust Bitwise Web
'BSRR',#塞拉银行
'AOTG',#AOT Growth and Innovation ETF
'BYLD',#iShares Yield Optimized Bond ET
'ET_D',#Energy Transfer LP Series D Pfd
'SOJC',#The Southern Co Series 2017B No
'ESGRO',#Enstar Group Ltd Series E Pfd
'FLRT',#Pacer Pacific Asset Floating Ra
'IXN',#全球科技ETF-iShares
'PSJ',#Invesco Dynamic Software ETF
'VTIP',#Vanguard Short-Term Inflation-P
'HDG',#ProShares Hedge Replication ETF
'ECPG',#安可资本
'MTD',#梅特勒-托利多
'LSST',#Natixis Loomis Sayles Short Dur
'QQQJ',#Invesco NASDAQ Next Gen 100 ETF
'FHN_D',#First Horizon Corp Series D Pfd
'FLJP',#Franklin FTSE Japan ETF
'DALI',#First Trust Dorsey Wright DALI
'FLUD',#Franklin Ultra Short Bond ETF
'FHN',#第一地平线银行
'ENBA',#Enbridge Inc Notes
'BKUI',#BNY Mellon Ultra Short Income E
'NEAR',#iShares Short Maturity Bond ETF
'GHTA',#Goose Hollow Tactical Allocatio
'XC',#WisdomTree Emerging Markets ex-
'ATH_E',#Athene Holding Ltd Series E Pfd
'RXI',#全球可选消费ETF-iShares
'IBMO',#iShares iBonds Dec 2026 Term Mu
'AGNCN',#AGNC Investment Corp Series C P
'TANNZ',#TravelCenters of America Inc No
'MCRO',#IQ Hedge Macro Tracker ETF
'IBMN',#iShares iBonds Dec 2025 Term Mu
'FTXL',#First Trust Nasdaq Semiconducto
'VGT',#信息科技指数ETF-Vanguard
'GIL',#吉登运动服
'EJAN',#Innovator Emerging Markets Powe
'DBGR',#Xtrackers MSCI Germany Hedged E
'IXJ',#全球医疗ETF-iShares
'CCF',#Chase Corp
'SWIR',#Sierra Wireless Inc
'SLX',#钢铁ETF-VanEck Vectors
'TARO',#Taro Pharmaceutical Industries
'QQEW',#First Trust NASDAQ-100 Equal We
'REYN',#Reynolds Consumer Products Inc
'TOWN',#Towne Bank
'ADSK',#欧特克
'KEN',#Kenon Holdings Ltd
'OPER',#ClearShares Ultra-Short Maturit
'AAWW',#阿特拉斯环球航空
'KEYS',#是德科技
'MCHP',#微芯科技
'CFG',#Citizens Financial Group Inc
'ULST',#SPDR SSgA Ultra Short Term Bond
'RYAN',#Ryan Specialty Holdings Inc-A
'TECS',#Direxion Technology Bear 3X Sha
'GE',#通用电气(US)
'BBJP',#JPMorgan BetaBuilders Japan ETF
'ITM',#VanEck ETF Trust VanEck Interme
'VNLA',#Janus Henderson Short Duration
'DFNM',#Dimensional National Municipal
'TBUX',#T. Rowe Price Ultra Short-Term
'USTB',#VictoryShares USAA Core Short-T
'VUSB',#Vanguard Ultra-Short Bond ETF
'RPT_D',#RPT Realty Series D Pfd
'PULS',#PGIM Ultra Short Bond ETF
'GSY',#Invesco Ultra Short Duration ET
'MEAR',#iShares Short Maturity Municipa
'JMUB',#JPMorgan Municipal ETF
'JPST',#JPMorgan Ultra-Short Income ETF
'OBIL',#US Treasury 12 Month Bill ETF
'TFLO',#iShares Treasury Floating Rate
'EGLE',#伊格尔散货航运
'MAXR',#Maxar Technologies Ltd
'WGO',#温尼巴格实业
'FRHC',#Freedom Holding Corp
'PRFT',#The Perficient Inc
'ZD',#Ziff Davis Inc
'WK',#Workiva Inc-A
'COLM',#哥伦比亚户外
'FXL',#First Trust Technology AlphaDEX
'RXL',#二倍做多医疗ETF-ProShares
'BILS',#SPDR Bloomberg 3-12 Month T-Bil
'RBCP',#RBC Bearings Inc Series A Pfd
'FERG',#Ferguson plc
'IHF',#iShares U.S. Health Care Provid
'ZYRX',#中盈瑞信
'ZYNE',#Zynerba Pharmaceuticals Inc
'ZWRKW',#Z-Work Acquisition Corp Wt
'ZWRKU',#Z-Work Acquisition Corp Unit Co
'ZWRK',#Z-Work Acquisition Corp-A
'ZVSAW',#ZyVersa Therapeutics Inc Wt
'ZTOPW',#Zi Toprun Acquisition Corp Wt
'ZTOPU',#Zi Toprun Acquisition Corp Unit
'ZTOP',#Zi Toprun Acquisition Corp
'ZTAQW',#Zimmer Energy Transition Acquis
'ZTAQU',#Zimmer Energy Transition Acquis
'ZT',#Zimmer Energy Transition Acquis
'ZPIN',#智联招聘
'ZOM',#Zomedica Corp
'ZKIN',#正康国际
'ZJYL',#中进医疗
'ZINGW',#FTAC Zeus Acquisition Corp Wt
'ZINGU',#FTAC Zeus Acquisition Corp Unit
'ZGN_WS',#Ermenegildo Zegna NV Wt
'ZGHB',#环保新材
'ZFOX',#ZeroFox Holdings Inc
'ZEPP',#华米科技
'ZCAR',#Defiance Vehicle & Technology I
'YVR',#Liquid Media Group Ltd
'YOTAU',#Yotta Acquisition Corp Unit Con
'YOTAR',#Yotta Acquisition Corp Rt
'YNDX',#Yandex NV-A
'YMAT',#J-Star Holding Co Ltd
'YLD',#Principal Active High Yield ETF
'YKAI',#誉凯健康
'YGF',#燕谷坊
'YEAR',#AB Ultra Short Income ETF
'YCBD',#cbdMD Inc
'YBZN',#优创易泊
'XWEL',#XWELL Inc
'XVOL',#Acruence Active Hedge U.S. Equi
'XTAP',#Innovator U.S. Equity Accelerat
'XSVN',#BondBloxx Bloomberg Seven Year
'XPDBW',#Power & Digital Infrastructure
'XPDBU',#Power & Digital Infrastructure
'XPAXU',#XPAC Acquisition Corp Unit Cons
'XNAV',#FundX Aggressive ETF
'XI',#小i机器人
'XHYC',#BondBloxx USD High Yield Bond C
'XGN',#Exagen Inc
'XFINW',#ExcelFin Acquisition Corp Wt
'XFINU',#ExcelFin Acquisition Corp Unit
'XFIN',#ExcelFin Acquisition Corp-A
'XERS',#Xeris制药
'XELA',#Exela Technologies Inc
'XDJA',#Innovator U.S. Equity Accelerat
'XBJA',#Innovator U.S. Equity Accelerat
'XBIO',#Xenetic Biosciences Inc
'WYTCW',#Wytec International Inc Wt
'WYTC',#Wytec International Inc
'WXT',#物芯控股
'WWACW',#Worldwide Webb Acquisition Corp
'WWACU',#Worldwide Webb Acquisition Corp
'WVVIP',#Willamette Valley Vineyards Inc
'WUBA',#58同城
'WTMAU',#Welsbach Technology Metals Acqu
'WTMA',#Welsbach Technology Metals Acqu
'WTER',#The Alkaline Water Co Inc
'WRNT',#Warrantee Inc ADR
'WRAC_WS',#Williams Rowland Acquisition Co
'WRAC_U',#Williams Rowland Acquisition Co
'WQGA_WS',#World Quantum Growth Acquisitio
'WQGA_U',#World Quantum Growth Acquisitio
'WQGA',#World Quantum Growth Acquisitio
'WPS',#iShares International Developed
'WPCB_WS',#Warburg Pincus Capital Corp I—
'WPCA_WS',#Warburg Pincus Capital Corp I—
'WPCA_U',#Warburg Pincus Capital Corp I—
'WNNR_U',#Andretti Acquisition Corp Unit
'WNNR',#Andretti Acquisition Corp-A
'WNDY',#Global X Wind Energy ETF
'WLYB',#约翰威立国际出版-B
'WLGS',#宏利营造
'WKEY',#WISeKey International Holding A
'WISH',#ContextLogic Inc-A
'WINVW',#WinVest Acquisition Corp Wt
'WINVU',#WinVest Acquisition Corp Unit C
'WINVR',#WinVest Acquisition Corp Rt
'WINV',#WinVest Acquisition Corp
'WINT',#Windtree Therapeutics Inc
'WIL',#iPath Women in Leadership ETN
'WIA',#Western Asset Inflation-Linked
'WHLRL',#Wheeler Real Estate Investment
'WHLM',#Wilhelmina国际
'WF',#韩国友利
'WE_WS',#WeWork Inc Wt
'WEL_WS',#Integrated Wellness Acquisition
'WEL_U',#Integrated Wellness Acquisition
'WEL',#Integrated Wellness Acquisition
'WEJOW',#Wejo Group Ltd Wt
'WEIX',#Dynamic Short Short-Term Volati
'WBIS',#WBI BullBear Trend Switch US 20
'WBIQ',#WBI BullBear Trend Switch US 10
'WBIM',#WBI BullBear Trend Switch US 20
'WBIK',#WBI BullBear Trend Switch US 10
'WBEV',#Winc Inc
'WAVSW',#Western Acquisition Ventures Co
'WAVSU',#Western Acquisition Ventures Co
'WAVS',#Western Acquisition Ventures Co
'WAVC_U',#Waverley Capital Acquisition Co
'WAVC',#Waverley Capital Acquisition Co
'WAL_A',#Western Alliance Bancorp Series
'WALL',#无锡金城幕墙
'WALDW',#Waldencast plc Wt
'WALD',#Waldencast plc-A
'VZLA',#Vizsla Silver Corp
'VYGG_WS',#Vy Global Growth Wt
'VWRM',#Virtus WMC Risk-Managed Alterna
'VVNT',#Vivint Smart Home Inc-A
'VTS',#Vitesse Energy Inc
'VTRO',#Vitro Diagnostics Inc
'VTIQW',#VectoIQ Acquisition Corp II Wt
'VTIQU',#VectoIQ Acquisition Corp II Uni
'VTIQ',#VectoIQ Acquisition Corp II-A
'VTGN',#VistaGen Therapeutics Inc
'VTEC',#Valtech SE-A
'VST_WS_A',#Vistra Corp Wt
'VSSYW',#Versus Systems Inc Wt
'VSSAW',#VIKASA SPAC Series I Acquisitio
'VSSAU',#VIKASA SPAC Series I Acquisitio
'VSSA',#VIKASA SPAC Series I Acquisitio
'VSACW',#Vision Sensing Acquisition Corp
'VSACU',#Vision Sensing Acquisition Corp
'VSAC',#Vision Sensing Acquisition Corp
'VQS',#VIQ Solutions Inc
'VPCBW',#VPC Impact Acquisition Holdings
'VPCB',#VPC Impact Acquisition Holdings
'VNO',#沃那多房产信托
'VMGAW',#VMG Consumer Acquisition Corp W
'VMGAU',#VMG Consumer Acquisition Corp U
'VMGA',#VMG Consumer Acquisition Corp-A
'VMCAW',#Valuence Merger Corp I Wt
'VMAT',#V-Shares MSCI World ESG Materia
'VLDRW',#Velodyne Lidar Inc Wt
'VLAT',#Valor Latitude Acquisition Corp
'VIRS',#Pacer BioThreat Strategy ETF
'VIIAW',#7GC & Co Holdings Inc Wt
'VIIAU',#7GC & Co Holdings Inc Unit Cons
'VHNAW',#Vahanna Tech Edge Acquisition I
'VHNAU',#Vahanna Tech Edge Acquisition I
'VHAQr',#Viveon Health Acquisition Corp
'VHAQ_WS',#Viveon Health Acquisition Corp
'VHAQ_U',#Viveon Health Acquisition Corp
'VGZ',#Vista Gold Corp
'VGFC',#The Very Good Food Co Inc
'VERBW',#Verb Technology Co Inc Wt
'VEON',#VEON Ltd ADR
'VENAW',#Venus Acquisition Corp Wt
'VENAU',#Venus Acquisition Corp Unit Con
'VENAR',#Venus Acquisition Corp Rt
'VEMY',#Virtus Stone Harbor Emerging Ma
'VELOW',#Velocity Acquisition Corp Wt
'VELOU',#Velocity Acquisition Corp Unit
'VELO',#Velocity Acquisition-A
'VDNT',#Verdant Earth Technologies Ltd
'VCXAW',#10X Capital Venture Acquisition
'VCXAU',#10X Capital Venture Acquisition
'VCV',#Invesco California Value Munici
'VCNX',#Vaccinex Inc
'VCLN',#Virtus Duff & Phelps Clean Ener
'VCAP',#Cambria Venture ETF
'VBOC',#Viscogliosi Brothers Acquisitio
'VAQC',#Vector Acquisition Corp II-A
'VACXW',#Vistas Acquisition Co II Inc Wt
'VACXU',#Vistas Acquisition Co II Inc Un
'VACX',#Vistas Acquisition Co II Inc-A
'UWMC_WS',#UWM Holdings Corp Wt
'UTC',#Uranium Trading Corp-A
'USX',#美国xpress企业
'USML',#ETRACS 2x Leveraged MSCI US Min
'USI',#Principal Ultra-Short Active In
'USCTW',#TKB Critical Technologies 1 Wt
'USCT',#TKB Critical Technologies 1-A
'USB_P',#US Bancorp Series K Pfd
'UPWD',#JPMorgan Social Advancement ETF
'UPTDU',#TradeUP Acquisition Corp Unit C
'UPTD',#TradeUP Acquisition Corp
'UNAM',#尤尼柯北美保险
'UKWIU',#UK Wisdom Ltd Unit Cons of 1 CL
'UKWIR',#UK Wisdom Ltd Rt
'UKWI',#UK Wisdom Ltd-A
'UKOMW',#Ucommune International Ltd Wt
'UJAN',#Innovator U.S. Equity Ultra Buf
'UDI',#USCF Dividend Income Fund
'UCTT',#超科林半导体
'UCAR',#优品车
'UBXG',#有家保险
'UBOT',#Direxion Daily Robotics Artific
'UBER',#优步
'UBCP',#联合合众银行(俄亥俄州)
'UAPR',#Innovator U.S. Equity Ultra Buf
'UAE',#阿联酋ETF-iShares MSCI
'TZPSW',#TZP Strategies Acquisition Corp
'TZPSU',#TZP Strategies Acquisition Corp
'TYDE',#Cryptyde Inc
'TWX',#时代华纳
'TWOA',#two-A
'TWNI_U',#Tailwind International Acquisit
'TWND_WS',#Tailwind Acquisition Corp II Wt
'TWND_U',#Tailwind Acquisition Corp II Un
'TWLVW',#Twelve Seas Investment Co II Wt
'TWLVU',#Twelve Seas Investment Co II Un
'TWLV',#Twelve Seas Investment Co II-A
'TWEN',#T20 Holdings Ltd
'TWCGW',#Galliot Acquisition Corp Wt
'TWCGU',#Galliot Acquisition Corp Unit C
'TWCG',#Galliot Acquisition Corp-A
'TWCBW',#Bilander Acquisition Corp Wt
'TUSI',#Touchstone Ultra Short Income E
'TURO',#Turo Inc
'TTSH',#Tile Shop Holdings Inc
'TTNP',#Titan Pharmaceuticals Inc
'TSPQ_U',#TCW Special Purpose Acquisition
'TSPQ',#TCW Special Purpose Acquisition
'TSIBW',#Tishman Speyer Innovation Corp
'TSIBU',#Tishman Speyer Innovation Corp
'TSIB',#Tishman Speyer Innovation Corp
'TRUE',#TrueCar Inc
'TRTL_WS',#TortoiseEcofin Acquisition Corp
'TRTL_U',#TortoiseEcofin Acquisition Corp
'TRQ',#Turquoise Hill Resources Ltd
'TRPXW',#Therapix Biosciences Ltd Wt
'TRPL',#Pacer Metaurus US Large Cap Div
'TRONW',#Corner Growth Acquisition Corp
'TRONU',#Corner Growth Acquisition Corp
'TRON',#Corner Growth Acquisition Corp
'TRIS_WS',#Tristar Acquisition I Corp Wt
'TRFK',#Pacer Data and Digital Revoluti
'TRCA_U',#Twin Ridge Capital Acquisition
'TRCA',#Twin Ridge Capital Acquisition
'TRAQ_WS',#Trine II Acquisition Corp Wt
'TRAQ_U',#Trine II Acquisition Corp Unit
'TRAQ',#Trine II Acquisition Corp-A
'TPET',#Trio Petroleum Corp
'TPBAW',#TPB Acquisition Corp I Wt
'TPBAU',#TPB Acquisition Corp I Unit Con
'TONY',#淘你欢
'TOKE',#Cambria Cannabis ETF
'TOACW',#Talon 1 Acquisition Corp Wt
'TOACU',#Talon 1 Acquisition Corp Unit C
'TOAC',#Talon 1 Acquisition Corp-A
'TO',#Tower One Wireless Corp-A
'TNXP',#Tonix Pharmaceuticals Holding C
'TMTCW',#TMT Acquisition Corp Wt
'TMTCU',#TMT Acquisition Corp Unit Cons
'TMTCR',#TMT Acquisition Corp Rt
'TMTC',#TMT Acquisition Corp
'TMCWW',#TMC the metal company Inc Wt
'TMAC_U',#The Music Acquisition Corp Unit
'TMAC',#The Music Acquisition Corp-A
'TLSA',#Tiziana Life Sciences Ltd
'TLGYU',#TLGY Acquisition Corp Unit Cons
'TLGY',#TLGY Acquisition Corp-A
'TLGA',#TLG Acquisition One Corp-A
'TKAT',#Takung Art Co Ltd
'TIOAW',#Tio Tech A Wt
'TINT',#ProShares Smart Materials ETF
'TIL',#Instil Bio Inc
'THCPW',#Thunder Bridge Capital Partners
'THCHW',#TH International Ltd Wt
'THACW',#Thrive Acquisition Corp Wt
'THACU',#Thrive Acquisition Corp Unit Co
'TGVCW',#TG Venture Acquisition Corp Wt
'TGVCU',#TG Venture Acquisition Corp-A U
'TGVC',#TG Venture Acquisition Corp-A
'TGR_U',#Kimbell Tiger Acquisition Corp
'TGAAW',#Target Global Acquisition I Cor
'TGAAU',#Target Global Acquisition I Cor
'TGAA',#Target Global Acquisition I Cor
'TFCFA',#21世纪福克斯-A
'TFCF',#21世纪福克斯-B
'TETEW',#Technology & Telecommunication
'TETEU',#Technology & Telecommunication
'TETCW',#Tech and Energy Transition Corp
'TETCU',#Tech and Energy Transition Corp
'TENKU',#TenX Keane Acquisition Unit Con
'TENKR',#TenX Keane Acquisition Rt
'TECTP',#Tectonic Financial Inc Series B
'TDTT',#FlexShares iBoxx 3 Year Target
'TDACW',#Translational Development Acqui
'TDACU',#Translational Development Acqui
'TDAC',#Translational Development Acqui
'TCVA',#TCV Acquisition Corp-A
'TCS',#The Container Store Group Inc
'TCBC',#TC Bancshares Inc
'TBSAW',#TB SA Acquisition Corp Wt
'TBSAU',#TB SA Acquisition Corp Unit Con
'TBLAW',#Taboola.com Ltd Wt
'TBCPW',#Thunder Bridge Capital Partners
'TBCPU',#Thunder Bridge Capital Partners
'TAHT',#SynCardia Systems Inc
'SZZLU',#Sizzle Acquisition Corp Unit Co
'SZZL',#Sizzle Acquisition Corp
'SZNZ',#Pacer CFRA-Stovall Small Cap Se
'SZNL',#Pacer CFRA-Stovall Large Cap Se
'SZNG',#Pacer CFRA-Stovall Global Seaso
'SYUS',#Syntax Stratified U.S. Total Ma
'SYTAW',#Siyata Mobile Inc Wt
'SYII',#Syntax Stratified Total Market
'SXQG',#ETC 6 Meridian Quality Growth E
'SWSS',#Springwater Special Situations
'SWETW',#Athlon Acquisition Corp Wt
'SWETU',#Athlon Acquisition Corp Unit Co
'SWET',#Athlon Acquisition Corp-A
'SWCH',#Switch Inc-A
'SWAGW',#Stran & Co Inc Wt
'SVREW',#SaverOne 2014 Ltd Wt
'SVNAW',#7 Acquisition Corp Wt
'SVNAU',#7 Acquisition Corp Unit Cons of
'SVN',#7天连锁
'SVIIW',#Spring Valley Acquisition Corp
'SVIIU',#Spring Valley Acquisition Corp
'SVFB',#SVF Investment Corp 2-A
'SVA',#科兴生物
'SURG',#SurgePays Inc
'SUNFU',#Sunfire Acquisition Corp Ltd Un
'SUNFR',#Sunfire Acquisition Corp Ltd Rt
'SUNF',#Sunfire Acquisition Corp Ltd-A
'SUAC_WS',#ShoulderUp Technology Acquisiti
'SUAC_U',#ShoulderUp Technology Acquisiti
'SUAC',#ShoulderUp Technology Acquisiti
'STWY',#Steinway Musical Instruments Ho
'STTK',#Shattuck Labs Inc
'STSSW',#Sharps Technology Inc Wt
'STR_WS',#Sitio Royalties Corp Wt
'STRY_WS',#Starry Group Holdings Inc Wt
'STRY',#Starry Group Holdings Inc-A
'STRRP',#Star Equity Holdings Inc Series
'STRE_WS',#Supernova Partners Acquisition
'STRCW',#Sarcos Technology and Robotics
'STPZ',#PIMCO 1-5 Year U.S. TIPS Index
'STLV',#iShares Factors US Value Style
'STLRW',#Stellaris Growth Acquisition Co
'STLRU',#Stellaris Growth Acquisition Co
'STLR',#Stellaris Growth Acquisition Co
'STKH',#Steakholder Foods Ltd ADR
'STIXW',#Semantix Inc Wt
'STET_WS',#ST Energy Transition I Ltd Wt
'STET_U',#ST Energy Transition I Ltd Unit
'STET',#ST Energy Transition I Ltd-A
'SSSSL',#SuRo Capital Corp Notes
'SSBI',#Summit State Bank
'SSAAW',#Science Strategic Acquisition C
'SSAAU',#Science Strategic Acquisition C
'SSAA',#Science Strategic Acquisition C
'SRZNW',#Surrozen Inc Wt
'SQFTW',#Presidio Property Trust Inc Wt
'SPXX',#Nuveen S&P 500 Dynamic Overwrit
'SPTKU',#SportsTek Acquisition Corp Unit
'SPTK',#SportsTek Acquisition Corp-A
'SPRU',#Spruce Power Holding Corp
'SPRO',#Spero Therapeutics Inc
'SPRC',#SciSparc Ltd
'SPLP_A',#Steel Partners Holdings LP Seri
'SPKB',#Silver Spike Acquisition Corp I
'SPKAU',#SPK收购(普通单位)
'SPKAR',#SPK收购(权利)
'SPK',#SPK收购
'SPIR_WS',#Spire Global Inc Wt
'SPGS_U',#Simon Property Group Acquisitio
'SPGS',#Simon Property Group Acquisitio
'SPGC',#Sacks Parente Golf Inc
'SPE_C',#Special Opportunities Fund Inc
'SPCMW',#Sound Point Acquisition Corp I
'SPCM',#Sound Point Acquisition Corp I
'SOTK',#Sono-Tek Corp
'SOSHW',#SOS Hydration Inc Wt
'SOSH',#SOS Hydration Inc
'SOLE',#Sole Elite Group Ltd
'SOHON',#Sotherly Hotels Inc Series D Pf
'SODR',#SONDORS Inc
'SNRHU',#Senior Connect Acquisition Corp
'SMSA',#Samsara Vision Inc
'SMIHU',#Summit Healthcare Acquisition C
'SMHJ',#Defiance Indxx Junior Semicondu
'SMFL',#Smart for Life Inc
'SMAPW',#SportsMap Tech Acquisition Corp
'SMAPU',#SportsMap Tech Acquisition Corp
'SLWD',#Sol-Wind Renewable Power LP
'SLVRW',#SILVERspac Inc Wt
'SLVRU',#SILVERspac Inc Unit Cons of 1 C
'SLT_',#Pacer Salt High truBeta US Mark
'SLNAW',#Selina Hospitality Plc Wt
'SLAC_WS',#Social Leverage Acquisition Cor
'SLAC_U',#Social Leverage Acquisition Cor
'SKYD',#UltraShort Nasdaq Cloud Computi
'SKYAW',#Skydeck Acquisition Corp Wt
'SKYAU',#Skydeck Acquisition Corp Unit C
'SKIL_WS',#Skillsoft Corp Wt
'SKGR',#SK Growth Opportunities Corp-A
'SJI',#South Jersey Industries Inc
'SJA',#SolarJuice Co Ltd
'SIOX',#Sio Gene Therapies Inc
'SIO',#Touchstone Strategic Income Opp
'SINA',#新浪
'SIM',#Grupo Simec SAB de CV ADR
'SIERW',#Sierra Lake Acquisition Corp Wt
'SIERU',#Sierra Lake Acquisition Corp Un
'SIER',#Sierra Lake Acquisition Corp-A
'SIEN',#Sientra Inc
'SHUAW',#SHUAA Partners Acquisition Corp
'SHUAU',#SHUAA Partners Acquisition Corp
'SHQAW',#Shelter Acquisition Corp I Wt
'SHQAU',#Shelter Acquisition Corp I Unit
'SHQA',#Shelter Acquisition Corp I-A
'SHPP',#Pacer Industrials and Logistics
'SHDG',#Soundwatch Hedged Equity ETF
'SHCAW',#Spindletop Health Acquisition C
'SHCAU',#Spindletop Health Acquisition C
'SHAP_WS',#Spree Acquisition Corp 1 Ltd Wt
'SHACW',#SCP & CO Healthcare Acquisition
'SHACU',#SCP & CO Healthcare Acquisition
'SHAC',#SCP & CO Healthcare Acquisition
'SGTX',#Sigilon Therapeutics Inc
'SGRP_W',#Sirius International Insurance
'SGOV',#iShares 0-3 Month Treasury Bond
'SGLY',#Singularity Future Technology L
'SGIIW',#Seaport Global Acquisition II C
'SGIIU',#Seaport Global Acquisition II C
'SGHLW',#Signal Hill Acquisition Corp Wt
'SGHLU',#Signal Hill Acquisition Corp Un
'SGHC_WS',#Super Group (SGHC) Ltd Wt
'SGE',#Strong Global Entertainment Inc
'SFRWW',#Appreciate Holdings Inc Wt
'SFBC',#Sound Financial Bancorp Inc
'SEPZ',#Listed Funds Trust TrueShares S
'SENEB',#Seneca Foods Corp-B
'SEDA_WS',#SDCL EDGE Acquisition Corp Wt
'SEATW',#Vivid Seats Inc Wt
'SEAC',#SeaChange International Inc
'SDTR',#Sound Total Return ETF
'SDSI',#American Century Short Duration
'SDGS',#Newday Sustainable Development
'SDFI',#Sound Fixed Income ETF
'SDEE',#Sound Enhanced Equity Income ET
'SDACW',#Sustainable Development Acquisi
'SDACU',#Sustainable Development Acquisi
'SDAC',#Sustainable Development Acquisi
'SCYB_',#Sol Global Investments Corp
'SCYB',#UltraShort Nasdaq Cybersecurity
'SCUA_WS',#Sculptor Acquisition Corp I Wt
'SCUA_U',#Sculptor Acquisition Corp I Uni
'SCRMU',#Screaming Eagle Acquisition Cor
'SCOBW',#ScION Tech Growth II Wt
'SCOAW',#ScION Tech Growth I Wt
'SCOAU',#ScION Tech Growth I Unit Cons o
'SCOA',#ScION Tech Growth I-A
'SCMAW',#Seaport Calibre Materials Acqui
'SCMAU',#Seaport Calibre Materials Acqui
'SCMA',#Seaport Calibre Materials Acqui
'SCLEW',#Broadscale Acquisition Corp Wt
'SCLEU',#Broadscale Acquisition Corp Uni
'SCLE',#Broadscale Acquisition Corp-A
'SCIT',#三彩家
'SCIM',#Global X Scientific Beta Emergi
'SCHE',#Schwab Emerging Markets Equity
'SCDL',#ETRACS 2x Leveraged US Dividend
'SCCI',#Shimmick Construction Co Inc
'SCCB',#Sachem Capital Corp Notes
'SCAQW',#Stratim Cloud Acquisition Corp
'SCAQU',#Stratim Cloud Acquisition Corp
'SB_C',#Safe Bulkers Inc Series C Pfd
'SBUG',#iPath Silver ETN
'SBSW',#Sibanye Stillwater Ltd ADR
'SBND',#Columbia Short Duration Bond ET
'SBII_U',#Sandbridge X2 Corp Unit Cons of
'SBII',#Sandbridge X2 Corp-A
'SBIG',#SpringBig Holdings Inc
'SBFMW',#Sunshine Biopharma Inc Wt
'SAVN',#LifeGoal Conservative Wealth Bu
'SATLW',#Satellogic Inc Wt
'SAMAW',#Schultze Special Purpose Acquis
'SAMA',#Schultze Special Purpose Acquis
'SAITW',#SAI TECH Global Corp Wt
'SAGP',#Strategas Global Policy Opportu
'SAGAU',#Sagaliam Acquisition Corp Unit
'SAGAR',#Sagaliam Acquisition Corp Rt
'SAGA',#Sagaliam Acquisition Corp-A
'SAG',#SAG Holdings Ltd
'SABSW',#SAB Biotherapeutics Inc Wt
'SABS',#SAB Biotherapeutics Inc
'RZB',#Reinsurance Group of America In
'RZA',#Reinsurance Group of America In
'RY_T',#Royal Bank of Canada Series C-2
'RXRE',#Pacer Benchmark Healthcare Real
'RXRAW',#RXR Acquisition Corp Wt
'RXRAU',#RXR Acquisition Corp Unit Cons
'RXRA',#RXR Acquisition Corp-A
'RXD',#ProShares UltraShort Health Car
'RWODW',#Redwoods Acquisition Corp Wt
'RWODU',#Redwoods Acquisition Corp Unit
'RWODR',#Redwoods Acquisition Corp Rt
'RWOD',#Redwoods Acquisition Corp
'RVSB',#Riverview Bancorp Inc
'RVR',#REV Renewables Inc
'RULEWI',#Strategy Shares Drawbridge Dyna
'RUBY',#Rubius Therapeutics Inc
'RTLPP',#The Necessity Retail REIT Inc S
'RSXJ',#俄罗斯小型股ETF-VanEckt Vectors
'RSX',#俄罗斯ETF-VanEck Vectors
'RSVRW',#Reservoir Media Inc Wt
'RSPY',#Revere Sector Opportunity ETF
'RRAC_WS',#Rigel Resource Acquisition Corp
'RPHS',#Regents Park Hedged Market Stra
'ROVR',#Rover Group Inc-A
'ROSEW',#Rose Hill Acquisition Corp Wt
'ROSEU',#Rose Hill Acquisition Corp Unit
'ROSE',#Rose Hill Acquisition Corp-A
'RONI_U',#Rice Acquisition Corp II Unit C
'RODI',#iPath Return on Disability ETN
'ROCLW',#Roth CH Acquisition V Co Wt
'ROCLU',#Roth CH Acquisition V Co Unit C
'ROCL',#Roth CH Acquisition V Co
'ROCI',#ROC ETF
'ROCAR',#ROC Energy Acquisition Corp Rt
'ROAR',#Impact Shares Climate Risk Rein
'RNWK',#RealNetworks Inc
'RNERU',#Mount Rainier Acquisition Corp
'RNER',#Mount Rainier Acquisition Corp
'RNAZ',#TransCode Therapeutics Inc
'RMGCU',#RMG Acquisition Corp III Unit C
'RMGC',#RMG Acquisition Corp III-A
'RMCF',#洛矶山巧克力工厂
'RMBI',#Richmond Mutual Bancorporation
'RLFT',#Relief Therapeutics Holding SA
'RKTA_WS',#Rocket Internet Growth Opportun
'RKTA_U',#Rocket Internet Growth Opportun
'RKLY_WS',#Rockley Photonics Holdings Ltd
'RJAC_WS',#Jackson Acquisition Co Wt
'RILYN',#B. Riley Financial Inc Notes
'RIF',#RMR Real Estate Income Fund
'RHE_A',#Regional Health Properties Inc
'RHCB',#BNY Mellon Responsible Horizons
'RGT',#Royce Global Value Trust
'RGS',#Regis Corp
'RFL',#Rafael Holdings Inc-B
'RFACW',#RF Acquisition Corp Wt
'RFACR',#RF Acquisition Corp Rt
'RFAC',#RF Acquisition Corp-A
'REVHW',#Revolution Healthcare Acquisiti
'REVHU',#Revolution Healthcare Acquisiti
'REVH',#Revolution Healthcare Acquisiti
'REVEW',#Alpine Acquisition Corp Wt
'REVEU',#Alpine Acquisition Corp Unit Co
'REVE',#Alpine Acquisition Corp
'REVBW',#Revelation Biosciences Inc Wt
'REVBU',#Revelation Biosciences Inc Unit
'RETO',#瑞图生态
'RESE',#WisdomTree Emerging Markets ESG
'RELY',#Remitly Global Inc
'REED',#Reed’s Inc
'RDXXW',#Roman DBDR Tech Acquisition Cor
'RDXXU',#Roman DBDR Tech Acquisition Cor
'RDXX',#Roman DBDR Tech Acquisition Cor
'RDW_WS',#Redwire Corp Wt
'RDTXW',#Roman DBDR Tech Acquisition Cor
'RDTXU',#Roman DBDR Tech Acquisition Cor
'RDTX',#Roman DBDR Tech Acquisition Cor
'RDHL',#RedHill Biopharma Ltd ADR
'RCRTW',#Recruiter.com Group Inc Wt
'RCOR_WS',#Renovacor Inc Wt
'RCOR',#Renovacor Inc
'RCLFW',#Rosecliff Acquisition Corp I Wt
'RCFA_WS',#RCF Acquisition Corp Wt
'RCFA_U',#RCF Acquisition Corp Unit Cons
'RCC',#Ready Capital Corp Notes
'RCAT',#Red Cat Holdings Inc
'RCACW',#Revelstone Capital Acquisition
'RCACU',#Revelstone Capital Acquisition
'RBOT_WS',#Vicarious Surgical Inc Wt
'RBKB',#Rhinebeck Bancorp Inc
'RASF',#Real Asset Strategies ETF
'RAND',#兰德资本
'RAM',#Aries I Acquisition Corp-A
'RAFE',#PIMCO RAFI ESG U.S. ETF
'RACYW',#Relativity Acquisition Corp Wt
'RACYU',#Relativity Acquisition Corp Uni
'RACB',#Research Alliance Corp II-A
'QYLG',#Global X Nasdaq 100 Covered Cal
'QUMU',#Qumu Corp
'QULL',#ETRACS 2x Leveraged MSCI US Qua
'QTR',#Global X NASDAQ 100 Tail Risk E
'QTOC',#Innovator Growth Accelerated Pl
'QTEK',#QualTek Services Inc-A
'QSG',#量子之歌
'QQU',#Simplify Growth Equity Plus Ups
'QQCY',#青青草元
'QOMOW',#Qomolangma Acquisition Corp Wt
'QOMOU',#Qomolangma Acquisition Corp Uni
'QOMOR',#Qomolangma Acquisition Corp Rt
'QOMO',#Qomolangma Acquisition Corp
'QIWI',#Qiwi plc ADR
'QHI',#沁弘
'QFTA',#Quantum FinTech Acquisition Cor
'QED',#IQ Hedge Event-Driven Tracker E
'PYT',#PPLUS Trust Certificates Series
'PYPE',#ETRACS NYSE Pickens Core Midstr
'PXUS',#Principal International Adaptiv
'PXSAW',#Pyxis Tankers Inc Wt
'PXSAP',#Pyxis Tankers Inc Series A Pfd
'PWUPU',#PowerUp Acquisition Corp Unit C
'PWM',#盛德财富
'PV_U',#Primavera Capital Acquisition C
'PVI',#Invesco VRDO Tax-Free ETF
'PUYI',#普益财富
'PUCKW',#Goal Acquisitions Corp Wt
'PTY',#PIMCO Corporate & Income Opport
'PTWOW',#Pono Capital Two Inc Wt
'PTWOU',#Pono Capital Two Inc Unit Cons
'PTWO',#Pono Capital Two Inc-A
'PTOCW',#Pine Technology Acquisition Cor
'PTOCU',#Pine Technology Acquisition Cor
'PTOC',#Pine Technology Acquisition Cor
'PTIXW',#Protagenic Therapeutics Inc Wt
'PTICU',#PropTech Investment Corp II Uni
'PTE',#PolarityTE Inc
'PSTV',#Plus Therapeutics Inc
'PSRS',#Pacer CFRA-Stovall Small Cap Se
'PSRL',#Pacer CFRA-Stovall Large Cap Se
'PSRG',#Pacer CFRA-Stovall Global Seaso
'PSRE',#Pacer CFRA-Stovall Equal Weight
'PSPC_WS',#Post Holdings Partnering Corp W
'PSPC_U',#Post Holdings Partnering Corp U
'PSMS',#Pacer Swan SOS Moderate (Septem
'PSMD',#Pacer Swan SOS Moderate (Januar
'PSIT',#PSI International Inc
'PSFS',#Pacer Swan SOS Flex (September)
'PSFE_WS',#Paysafe Ltd Wt
'PSE',#Prime Skyline Ltd
'PSCS',#Pacer Swan SOS Conservative (Se
'PSAGW',#Property Solutions Acquisition
'PSAGU',#Property Solutions Acquisition
'PSAG',#Property Solutions Acquisition
'PRZOW',#ParaZero Technologies Ltd Wt
'PRZO',#ParaZero Technologies Ltd
'PRTC',#PureTech Health PLC ADR
'PRSTW',#Presto Automation Inc Wt
'PRSRW',#Prospector Capital Corp Wt
'PRSR',#Prospector Capital Corp-A
'PRPC_WS',#CC Neuberger Principal Holdings
'PRPC_U',#CC Neuberger Principal Holdings
'PRPC',#CC Neuberger Principal Holdings
'PROQW',#PROTONIQ Acquisition Corp Wt
'PROQU',#PROTONIQ Acquisition Corp Unit
'PROQR',#PROTONIQ Acquisition Corp Rt
'PROQ',#PROTONIQ Acquisition Corp-A
'PRMI',#Priam Properties Inc
'PRLHW',#Pearl Holdings Acquisition Corp
'PRLH',#Pearl Holdings Acquisition Corp
'PRIF_D',#Priority Income Fund Inc Series
'PRHD',#IQ S&P U.S. Preferred Stock Low
'PRENW',#Prenetics Global Ltd Wt
'PREF',#Principal Spectrum Preferred Se
'PRDT_WS',#Peridot Acquisition Corp III Wt
'PRDT_U',#Peridot Acquisition Corp III Un
'PRDT',#Peridot Acquisition Corp III-A
'PRBM_U',#Parabellum Acquisition Corp Uni
'PQIN',#PGIM Quant Solutions Strategic
'PPYAU',#Papaya Growth Opportunity Corp
'PPYA',#Papaya Growth Opportunity Corp
'PPTA',#Perpetua Resources Corp
'PPHPU',#PHP Ventures Acquisition Corp U
'PPHPR',#PHP Ventures Acquisition Corp R
'PORT_WS',#Southport Acquisition Corp Wt
'PORT',#Southport Acquisition Corp-A
'PONOW',#Pono Capital Corp Wt
'PONOU',#Pono Capital Corp Unit Cons of
'POND_U',#Angel Pond Holdings Corp Unit C
'PNTM_U',#Pontem Corp Unit Cons of 1 CL A
'PNACW',#Prime Number Acquisition I Corp
'PNACU',#Prime Number Acquisition I Corp
'PNACR',#Prime Number Acquisition I Corp
'PNAC',#Prime Number Acquisition I Corp
'PMTG',#PIMCO Mortgage Income Trust Inc
'PMGMW',#Priveterra Acquisition Corp Wt
'PMGMU',#Priveterra Acquisition Corp Uni
'PMGM',#Priveterra Acquisition Corp-A
'PMEC',#Primech Holdings Ltd
'PLYM_A',#Plymouth Industrial REIT Inc Se
'PLX',#Protalix BioTherapeutics Inc
'PLTNW',#Plutonian Acquisition Corp Wt
'PLTNU',#Plutonian Acquisition Corp Unit
'PLTNR',#Plutonian Acquisition Corp Rt
'PLTN',#Plutonian Acquisition Corp
'PLTL',#Principal U.S. Small-Cap Adapti
'PLTEU',#Pulte Acquisition Corp Unit Con
'PLMI',#Plum Acquisition Corp I-A
'PLAOW',#Patria Latin American Opportuni
'PLAOU',#Patria Latin American Opportuni
'PKBOW',#Peak Bio Inc Wt
'PJFV',#PGIM Jennison Focused Value ETF
'PJFG',#PGIM Jennison Focused Growth ET
'PIEL',#Pacer International Export Lead
'PICC_U',#Pivotal Investment Corp III Uni
'PIAI_WS',#Prime Impact Acquisition I Wt
'PIAI_U',#Prime Impact Acquisition I Unit
'PIAI',#Prime Impact Acquisition I-A
'PHYT_WS',#Pyrophyte Acquisition Corp Wt
'PHYT_U',#Pyrophyte Acquisition Corp Unit
'PHYT',#Pyrophyte Acquisition Corp-A
'PHUN',#Phunware Inc
'PHIO',#Phio Pharmaceuticals Corp
'PHICW',#Population Health Investment Co
'PHICU',#Population Health Investment Co
'PHIC',#Population Health Investment Co
'PHGE_WS',#BiomX Inc Wt
'PHCC',#Preston Hollow Community Capita
'PGSS_WS',#Pegasus Digital Mobility Acquis
'PGSS_U',#Pegasus Digital Mobility Acquis
'PGSS',#Pegasus Digital Mobility Acquis
'PGRWW',#Progress Acquisition Corp Wt
'PGRWU',#Progress Acquisition Corp Unit
'PGRW',#Progress Acquisition Corp-A
'PGRO',#Putnam Focused Large Cap Growth
'PGRE',#Paramount Group Inc
'PGP',#PIMCO Global StocksPlus & Incom
'PFXNL',#PhenixFIN Corp Notes
'PFTAW',#Portage Fintech Acquisition Cor
'PFTAU',#Portage Fintech Acquisition Cor
'PFTA',#Portage Fintech Acquisition Cor
'PFIN',#P&F Industries Inc-A
'PFFR',#InfraCap REIT Preferred ETF
'PFDRU',#Pathfinder Acquisition Corp Uni
'PFD',#Flaherty & Crumrine Preferred a
'PETWW',#Wag! Group Co Wt
'PETVW',#PetVivo Holdings Inc Wt
'PERF_WS',#玩美(权证)
'PEPLW',#PepperLime Health Acquisition C
'PEPL',#PepperLime Health Acquisition C
'PEP31',#PepsiCo Inc Notes 2031
'PEP27',#PepsiCo Inc Notes 2027
'PEI_D',#Pennsylvania Real Estate Invest
'PEI_C',#Pennsylvania Real Estate Invest
'PEI_B',#Pennsylvania Real Estate Invest
'PEI',#宾夕法尼亚房地产投资信托
'PEGRW',#Project Energy Reimagined Acqui
'PEGRU',#Project Energy Reimagined Acqui
'PEGR',#Project Energy Reimagined Acqui
'PDOT_U',#Peridot Acquisition Corp II Uni
'PDEX',#Pro-Dex Inc
'PCXCW',#Parsec Capital Acquisitions Cor
'PCXCU',#Parsec Capital Acquisitions Cor
'PCX',#Parsec Capital Acquisitions Cor
'PCPC_WS',#Periphas Capital Partnering Cor
'PCPC_U',#Periphas Capital Partnering Cor
'PCPC',#Periphas Capital Partnering Cor
'PCG_I',#Pacific Gas and Electric Co Pfd
'PCG_H',#Pacific Gas and Electric Co Pfd
'PCCTW',#Perception Capital Corp II Wt
'PCCTU',#Perception Capital Corp II Unit
'PC',#松下
'PBUG',#Pacer iPath Gold Trendpilot ETN
'PBTS',#宏桥高科
'PBLA',#Panbela Therapeutics Inc
'PBHC',#Pathfinder Bancorp Inc
'PBFX',#PBF Logistics LP
'PBBK',#PB Bankshares Inc
'PBAXW',#Phoenix Biotech Acquisition Cor
'PBAXU',#Phoenix Biotech Acquisition Cor
'PBAX',#Phoenix Biotech Acquisition Cor
'PAVMZ',#PAVmed Inc Wt
'PANA',#Panacea Acquisition Corp II-A
'PAFOU',#Pacifico Acquisition Corp Unit
'PAFOR',#Pacifico Acquisition Corp Rt
'PAD',#Pacer Benchmark Apartments & Re
'PACXW',#Pioneer Merger Corp Wt
'PACI_WS',#PROOF Acquisition Corp I Wt
'PACI_U',#PROOF Acquisition Corp I Unit C
'PACI',#PROOF Acquisition Corp I-A
'OZON',#Ozon Holdings PLC ADR
'OXUSU',#Oxus Acquisition Corp Unit Cons
'OXUS',#Oxus Acquisition Corp-A
'OXACW',#Oxbridge Acquisition Corp Wt
'OXACU',#Oxbridge Acquisition Corp Unit
'OVID',#Ovid Therapeutics Inc
'OTRK',#Ontrak Inc
'OTMOW',#Otonomo Technologies Ltd Wt
'OTG',#OTG EXP Inc-A
'OTECW',#OceanTech Acquisitions I Corp W
'OTECU',#OceanTech Acquisitions I Corp U
'OTEC',#OceanTech Acquisitions I Corp-A
'OSTRW',#Oyster Enterprises Acquisition
'OSTRU',#Oyster Enterprises Acquisition
'OSTR',#Oyster Enterprises Acquisition
'OSI_WS',#Osiris Acquisition Corp Wt
'OSI_U',#Osiris Acquisition Corp Unit Co
'ORTX',#Orchard Therapeutics plc ADR
'ORIAU',#Orion Biotech Opportunities Cor
'ORIA',#Orion Biotech Opportunities Cor
'ORGO',#Organogenesis Holdings Inc-A
'OQAI',#O'Shares Quality Artificial Int
'OPTN',#OptiNose Inc
'OPP_A',#RiverNorth/DoubleLine Strategic
'OPGN',#OpGen Inc
'OPFI',#OppFi Inc
'OPA_WS',#Magnum Opus Acquisition Ltd Wt
'OPA_U',#Magnum Opus Acquisition Ltd Uni
'OPALW',#OPAL Fuels Inc Wt
'OPA',#Magnum Opus Acquisition Ltd-A
'ONYXW',#Onyx Acquisition Co I Wt
'ONYXU',#Onyx Acquisition Co I Unit Cons
'ONYX',#Onyx Acquisition Co I-A
'ONS_WS',#ONS Acquisition Corp Wt
'ONS_U',#ONS Acquisition Corp Unit Cons
'ONS',#ONS Acquisition Corp-A
'ONOF',#Global X Adaptive U.S. Risk Man
'ONFOW',#Onfolio Holdings Inc Wt
'ONCR',#Oncorus Inc
'OMEG',#Omega Alpha SPAC-A
'OMED',#OptMed Inc
'OLITW',#OmniLit Acquisition Corp Wt
'OISC',#Opus International Small/Mid Ca
'OILS_WS',#Permex Petroleum Corp Wt
'OILS',#Permex Petroleum Corp
'OIIM',#凹凸科技
'OIG',#Orbital Infrastructure Group In
'OHPAW',#Orion Acquisition Corp Wt
'OHPAU',#Orion Acquisition Corp Unit Con
'OHPA',#Orion Acquisition Corp-A
'OHAAW',#Opy Acquisition Corp I Wt
'OHAAU',#Opy Acquisition Corp I Unit Con
'OGRS',#O'Shares U.S. Small Cap Quality
'OGRO',#O'Shares U.S. Large Cap Quality
'OGCP',#Empire State Realty Op LP Serie
'OFSSH',#OFS Capital Corp Notes
'OFED',#Oconee Federal Financial Corp
'OEPWW',#One Equity Partners Open Water
'OEPWU',#One Equity Partners Open Water
'OEPW',#One Equity Partners Open Water
'ODDS',#Pacer BlueStar Digital Entertai
'OCTZ',#TrueShares Structured Outcome (
'OCG',#东方文化
'OCEA',#Ocean Biomedical Inc
'OCCIO',#OFS Credit Co Inc Series C Pfd
'OCCIN',#OFS Credit Co Inc Series E Pfd
'OCCI',#OFS Credit Co Inc
'OCAXW',#OCA Acquisition Corp Wt
'OBSV',#ObsEva SA
'OBOT',#O'Shares Quality Robotics and A
'NZRO',#Strategy Shares Halt Climate Ch
'NYX',#NYIAX Inc
'NYMT',#纽约抵押信托
'NYAX',#Nayax Ltd
'NXTP',#NextPlay Technologies Inc
'NVVEW',#Nuvve Holding Corp Wt
'NVVE',#Nuvve Holding Corp
'NVOS',#Novo Integrated Sciences Inc
'NVNOW',#enVVeno Medical Corp Wt
'NVACW',#NorthView Acquisition Corp Wt
'NVACR',#NorthView Acquisition Corp Rt
'NVAC',#NorthView Acquisition Corp
'NUVB_WS',#Nuvation Bio Inc Wt
'NUBIW',#Nubia Brand International Corp
'NUBIU',#Nubia Brand International Corp
'NUBI',#Nubia Brand International Corp-
'NTZG',#Nuveen Global Net Zero Transiti
'NTRBW',#Nutriband Inc Wt
'NSTD_WS',#Northern Star Investment Corp I
'NSTB_U',#Northern Star Investment Corp I
'NSCS',#Nuveen Small Cap Select ETF
'NRXP',#NRX Pharmaceuticals Inc
'NRSNW',#NeuroSense Therapeutics Ltd Wt
'NRDY_WS',#Nerdy Inc Wt
'NRACW',#Noble Rock Acquisition Corp Wt
'NRAC',#Noble Rock Acquisition Corp-A
'NPABW',#New Providence Acquisition Corp
'NPABU',#New Providence Acquisition Corp
'NPAB',#New Providence Acquisition Corp
'NOVZ',#TrueShares Structured Outcome (
'NOVVW',#Nova Vision Acquisition Corp Wt
'NOVVU',#Nova Vision Acquisition Corp Un
'NOVV',#Nova Vision Acquisition Corp
'NOVSW',#Novusterra Inc Wt
'NOVS',#Novusterra Inc
'NORT',#Nordic Realty Trust Inc
'NOGNW',#Nogin Inc Wt
'NOGN',#Nogin Inc
'NNNL',#Pacer Benchmark Net Lease Real
'NNDM',#Nano Dimension Ltd ADR
'NN',#NextNav Inc
'NM_H',#Navios Maritime Holdings Inc AD
'NM_G',#Navios Maritime Holdings Inc AD
'NMK_B',#Niagara Mohawk Power Corp Pfd
'NIQ',#Nuveen Intermediate Duration Qu
'NILE',#BitNile Holdings Inc
'NHICW',#NewHold Investment Corp II Wt
'NGD',#New Gold Inc
'NGC_WS',#Northern Genesis Acquisition Co
'NGC_U',#Northern Genesis Acquisition Co
'NGC',#Northern Genesis Acquisition Co
'NFYS_WS',#Enphys Acquisition Corp Wt
'NFYS_U',#Enphys Acquisition Corp Unit Co
'NFYS',#Enphys Acquisition Corp-A
'NFTX',#Ultimax Digital Inc
'NFNT_U',#Infinite Acquisition Corp Unit
'NEWTL',#Newtek Business Services Corp N
'NETC_U',#Nabors Energy Transition Corp U
'NEPG',#NEP Group Inc
'NEN',#New England Realty Associates L
'NEATW',#Noble Education Acquisition Cor
'NEATU',#Noble Education Acquisition Cor
'NEATR',#Noble Education Acquisition Cor
'NEAT',#Noble Education Acquisition Cor
'NDAQ29',#Nasdaq Inc Notes 2029
'NDAQ21',#Nasdaq Inc Notes 2021
'NDACW',#NightDragon Acquisition Corp Wt
'NDACU',#NightDragon Acquisition Corp Un
'NDAC',#NightDragon Acquisition Corp-A
'NCZ',#Virtus Convertible & Income Fun
'NCACW',#Newcourt Acquisition Corp Wt
'NCACU',#Newcourt Acquisition Corp Unit
'NCAC',#Newcourt Acquisition Corp-A
'NBTX',#Nanobiotix SA ADR
'NBSTU',#Newbury Street Acquisition Corp
'NBST',#Newbury Street Acquisition Corp
'NBDS',#Neuberger Berman Disrupters ETF
'NBCT',#Neuberger Berman Carbon Transit
'NBCC',#Neuberger Berman Next Generatio
'NAVA',#Nava Health MD Inc
'NAK',#Northern Dynasty Minerals Ltd
'NAACW',#North Atlantic Acquisition Corp
'MYPSW',#PlayStudios Inc Wt
'MYO',#迈欧莫
'MXRXW',#Med-X Inc Wt
'MXRX',#Med-X Inc
'MURFU',#Murphy Canyon Acquisition Corp
'MULN',#Mullen Automotive Inc
'MULG',#Muliang Viagoo Technology Inc
'MUI',#BlackRock Municipal Income Fund
'MTVC_WS',#Motive Capital Corp II Wt
'MTVC_U',#Motive Capital Corp II Unit Con
'MTUL',#ETRACS 2x Leveraged MSCI US Mom
'MTRYW',#Monterey Bio Acquisition Corp W
'MTRYU',#Monterey Bio Acquisition Corp U
'MTRY',#Monterey Bio Acquisition Corp
'MTL_',#Mechel PAO ADR Pfd
'MTL',#车里雅宾斯克钢铁
'MTCR',#Metacrine Inc
'MTC',#海川证券
'MTBCO',#CareCloud Inc Series B Pfd
'MTAL_WS',#Metals Acquisition Corp Wt
'MTAL_U',#Metals Acquisition Corp Unit Co
'MTACU',#MedTech Acquisition Corp Unit C
'MSVB',#Mid-Southern Bancorp Inc
'MSSAW',#Metal Sky Star Acquisition Corp
'MSSAU',#Metal Sky Star Acquisition Corp
'MSPRZ',#MSP Recovery Inc Wt
'MSPRW',#MSP Recovery Inc Wt
'MSMR',#McElhenny Sheffield Managed Ris
'MSFC',#毛氏翡翠
'MSACW',#Medicus Sciences Acquisition Co
'MSAC',#Medicus Sciences Acquisition Co
'MRZM',#Marizyme Inc
'MRDB_WS',#MariaDB plc Wt
'MRAI',#Marpai Inc-A
'MPRAW',#Mercato Partners Acquisition Co
'MPRAU',#Mercato Partners Acquisition Co
'MPRA',#Mercato Partners Acquisition Co
'MPLN_WS',#MultiPlan Corp Wt
'MPACU',#Model Performance Acquisition C
'MOOD',#Relative Sentiment Tactical All
'MONCW',#Monument Circle Acquisition Cor
'MOHR',#Mohr Growth ETF
'MOG_B',#穆格-B
'MOBVW',#Mobiv Acquisition Corp Wt
'MOBVU',#Mobiv Acquisition Corp Unit Con
'MOBV',#Mobiv Acquisition Corp-A
'MOBQW',#Mobiquity Technologies Inc Wt
'MOBBW',#Mobilicom Ltd ADR Wt
'MNX',#MN8 Energy Inc
'MNTV',#Momentive Global Inc
'MNTN_WS',#Everest Consolidator Acquisitio
'MNTN_U',#Everest Consolidator Acquisitio
'MNTN',#Everest Consolidator Acquisitio
'MNBD',#ALPS Intermediate Municipal Bon
'MMSB',#IQ MacKay Multi-Sector Income E
'MMCA',#IQ MacKay California Municipal
'MLSS',#Milestone Scientific Inc
'MLPR',#ETRACS Quarterly Pay 1.5X Lever
'MLAIU',#McLaren Technology Acquisition
'MLAI',#McLaren Technology Acquisition
'MLACW',#Malacca Straits Acquisition Co
'MLACU',#Malacca Straits Acquisition Co
'MLAC',#Malacca Straits Acquisition Co
'MKTW',#MarketWise Inc-A
'MKC_V',#味好美
'MKARW',#Makara Strategic Acquisition Co
'MKARU',#Makara Strategic Acquisition Co
'MKAR',#Makara Strategic Acquisition Co
'MJIN',#ETFMG 2X Daily Inverse Alternat
'MIT_U',#Mason Industrial Technology Inc
'MITT_C',#AG Mortgage Investment Trust In
'MITAW',#Coliseum Acquisition Corp Wts
'MINM',#Minim Inc
'MIMO_WS_C',#Airspan Networks Holdings Inc W
'MIMO_WS_B',#Airspan Networks Holdings Inc W
'MIGI',#Mawson Infrastructure Group Inc
'MIG',#VanEck Moody's Analytics IG Cor
'MH_D',#Maiden Holdings Ltd Series D Pf
'MGTA',#Magenta Therapeutics Inc
'MGLD',#The Marygold Companies Inc
'MGIH',#禧图集团
'MGF',#MFS Government Markets Income T
'MFUL',#Mindful Conservative ETF
'MFM',#MFS Municipal Income Trust
'METXW',#Meten Holding Group Ltd Wt
'METV',#Roundhill Ball Metaverse ETF
'METCL',#Ramaco Resources Inc Note
'MEOAW',#Minority Equality Opportunities
'MEOAU',#Minority Equality Opportunities
'MEOA',#Minority Equality Opportunities
'MELT',#Melt Pharmaceuticals Inc
'MEKA',#MELI Kaszek Pioneer Corp-A
'MEIP',#MEI Pharma Inc
'MEDS',#TRxADE HEALTH INC
'MEACU',#Mercury Ecommerce Acquisition C
'MEAC',#Mercury Ecommerce Acquisition C
'MDLZ45',#Mondelez International Inc Note
'MDLZ35A',#Mondelez International Inc Note
'MDLZ35',#Mondelez International Inc Note
'MDLZ27',#Mondelez International Inc Note
'MDLZ21',#Mondelez International Inc Note
'MDLW',#Medallion Resources Ltd Wt
'MDLSW',#MDNA Life Sciences Inc Wt
'MDLS',#MDNA Life Sciences Inc
'MDL',#Medallion Resources Ltd
'MDGSW',#Medigus Ltd Wt-C
'MDCP',#VictoryShares THB Mid Cap ESG E
'MCLDW',#mCloud Technologies Corp Wt
'MCAGU',#Mountain Crest Acquisition Corp
'MCAGR',#Mountain Crest Acquisition Corp
'MCAFU',#Mountain Crest Acquisition Corp
'MCAFR',#Mountain Crest Acquisition Corp
'MCAEU',#Mountain Crest Acquisition Corp
'MCAE',#Mountain Crest Acquisition Corp
'MCACW',#Monterey Capital Acquisition Co
'MCACU',#Monterey Capital Acquisition Co
'MCAC',#Monterey Capital Acquisition Co
'MCAAW',#Mountain & Co I Acquisition Cor
'MBTCU',#Nocturne Acquisition Corp Unit
'MBSC_WS',#M3-Brigade Acquisition III Corp
'MBSC_U',#M3-Brigade Acquisition III Corp
'MBSC',#M3-Brigade Acquisition III Corp
'MBNKP',#Medallion Bank Series F Pfd
'MBND',#SPDR Nuveen Municipal Bond ETF
'MBBB',#VanEck Moody's Analytics BBB Co
'MBAC_WS',#M3-Brigade Acquisition II Corp
'MBAC_U',#M3-Brigade Acquisition II Corp
'MBAC',#M3-Brigade Acquisition II Corp-
'MAYZ',#TrueShares Structured Outcome (
'MARZ',#TrueShares Structured Outcome (
'MARXW',#Mars Acquisition Corp Wt
'MARXU',#Mars Acquisition Corp Unit Cons
'MARXR',#Mars Acquisition Corp Rt
'MARX',#Mars Acquisition Corp
'MAQCW',#Maquia Capital Acquisition Corp
'MAQCU',#Maquia Capital Acquisition Corp
'MAQC',#Maquia Capital Acquisition Corp
'MAMB',#Monarch Ambassador Income ETF
'MACC_U',#Mission Advancement Corp Unit C
'MACC',#Mission Advancement Corp-A
'MACAU',#Moringa Acquisition Corp Unit e
'MACA',#Moringa Acquisition Corp-A
'MAAX',#VanEck ETF Trust VanEck Muni Al
'LYTWW',#Lytus Technologies Holdings PTV
'LXRX',#莱斯康制药
'LXP_C',#LXP Industrial Trust Series C P
'LVS',#金沙集团
'LVRAU',#Levere Holdings Corp Unit Cons
'LVRA',#Levere Holdings Corp-A
'LVOXU',#LiveVox Holdings Inc Unit Cons
'LVOPP',#LiveOne Inc Series A Pfd
'LVOL',#American Century Low Volatility
'LVLU',#Lulu’s Fashion Lounge Holdings
'LVACW',#LAVA Medtech Acquisition Corp W
'LVACU',#LAVA Medtech Acquisition Corp U
'LVAC',#LAVA Medtech Acquisition Corp-A
'LUNG_',#ProLung Inc
'LTRYW',#Lottery.com Inc Wt
'LTC',#LTC Properties Inc
'LSPRU',#Larkspur Health Acquisition Cor
'LSLT_',#Pacer Salt Low truBeta US Marke
'LSDI',#Lucy Scientific Discovery Inc
'LSBK',#莱克肖尔万通金控
'LRHCW',#La Rosa Holdings Corp Wt
'LRHC',#La Rosa Holdings Corp
'LRE',#Lead Real Estate Co Ltd ADR
'LPCN',#Lipocine Inc
'LOTZW',#CarLotz Inc Wt
'LOTZ',#CarLotz Inc-A
'LOPP',#Gabelli Love Our Planet & Peopl
'LOKM_WS',#Live Oak Mobility Acquisition C
'LOKM_U',#Live Oak Mobility Acquisition C
'LOKM',#Live Oak Mobility Acquisition C
'LOHA',#乐活
'LOCC_WS',#Live Oak Crestview Climate Acqu
'LOCC_U',#Live Oak Crestview Climate Acqu
'LOCC',#Live Oak Crestview Climate Acqu
'LNC_D',#林肯国民(优先股)
'LMNL',#Liminal BioSciences Inc
'LMACW',#Liberty Media Acquisition Corp
'LMACU',#Liberty Media Acquisition Corp
'LMACA',#Liberty Media Acquisition Corp-
'LLAP_WS',#Terran Orbita Corp Wt
'LKCO',#箩筐技术
'LK',#瑞幸咖啡
'LIXTW',#Lixte Biotechnology Holdings In
'LIVBW',#LIV Capital Acquisition Corp II
'LIVBU',#LIV Capital Acquisition Corp II
'LITTW',#Logistics Innovation Technologi
'LITTU',#Logistics Innovation Technologi
'LITT',#Logistics Innovation Technologi
'LIONW',#Lionheart III Corp Wt
'LIONU',#Lionheart III Corp Unit Cons of
'LION',#Lionheart III Corp-A
'LICN',#理臣咨询
'LIBYU',#Liberty Resources Acquisition C
'LIAI',#乐盟互动
'LHDX',#Lucira Health Inc
'LHC',#Leo Holdings Corp II-A
'LHAA',#Lerer Hippeau Acquisition Corp-
'LGV_WS',#Longview Acquisition Corp II Wt
'LGV_U',#Longview Acquisition Corp II Un
'LGVCW',#LAMF Global Ventures Corp I Wt
'LGVC',#LAMF Global Ventures Corp I-A
'LGV',#Longview Acquisition Corp II-A
'LGSTW',#Semper Paratus Acquisition Corp
'LGHLW',#狮子集团控股(权证)
'LGACW',#Lazard Growth Acquisition Corp
'LGAC',#Lazard Growth Acquisition Corp
'LFT_A',#Lument Finance Trust Inc Pfd
'LFLYW',#Leafly Holdings Inc Wt
'LFACW',#LF Capital Acquisition Corp II
'LFACU',#LF Capital Acquisition Corp II
'LFAC',#LF Capital Acquisition Corp II-
'LEGAU',#Lead Edge Growth Opportunities
'LEGA',#Lead Edge Growth Opportunities
'LDSPW',#Sports & Health Tech Acquisitio
'LDSPU',#Sports & Health Tech Acquisitio
'LDSP',#Sports & Health Tech Acquisitio
'LDHAW',#LDH Growth Corp I Wt
'LDHAU',#LDH Growth Corp I Unit Cons of
'LDHA',#LDH Growth Corp I-A
'LCW_WS',#Learn CW Investment Corp Wt
'LCW_U',#Learn CW Investment Corp Unit C
'LCW',#Learn CW Investment Corp-A
'LCR',#Leuthold Core ETF
'LCAHU',#Landcadia Holdings IV Inc Unit
'LCAAW',#L Catterton Asia Acquisition Co
'LCAA',#L Catterton Asia Acquisition Co
'LCA',#Landcadia Holdings IV Inc-A
'LBTYB',#自由全球-B
'LBO',#Cambria Buyout ETF
'LBGJ',#利邦
'LBBBW',#Lakeshore Acquisition II Corp W
'LBBBU',#Lakeshore Acquisition II Corp U
'LBAR',#Leatherback Long/Short Absolute
'LAZYW',#Lazydays Holdings Inc Wt
'LAZR',#Luminar Technologies Inc-A
'LATGW',#LatAmGrowth SPAC Wt
'LATGU',#LatAmGrowth SPAC Unit Cons of 1
'LANV_WS',#复朗集团(权证)
'LAAAU',#Lakeshore Acquisition I Corp Un
'KYCHW',#Keyarch Acquisition Corp Wt
'KYCHU',#Keyarch Acquisition Corp Unit C
'KYCHR',#Keyarch Acquisition Corp Rt
'KYCH',#Keyarch Acquisition Corp-A
'KWESW',#KWESST Micro Systems Inc Wt
'KVSC',#Khosla Ventures Acquisition Co
'KTCC',#Key Tronic Corp
'KSM',#DWS Strategic Municipal Income
'KSICW',#Kadem Sustainable Impact Corp W
'KSICU',#Kadem Sustainable Impact Corp U
'KSI',#Kadem Sustainable Impact Corp-A
'KRNLW',#Kernel Group Holdings Inc Wt
'KRNLU',#Kernel Group Holdings Inc Unit
'KRNL',#Kernel Group Holdings Inc-A
'KRBP',#Kiromic BioPharma Inc
'KPN',#柯普尼
'KPLTW',#Katapult Holdings Inc Wt
'KOOL',#群核科技
'KONG',#Formidable Fortress ETF
'KNSW',#KnightSwan Acquisition Corp-A
'KN',#Knowles Corp
'KLR_WS',#Kaleyra Inc Wt
'KLC',#KinderCare Learning Companies I
'KLAQW',#KL Acquisition Corp Wt
'KLAQU',#KL Acquisition Corp Unit Cons o
'KLAQ',#KL Acquisition Corp-A
'KITTW',#Nauticus Robotics Inc Wt
'KIQ',#Kelso Technologies Inc
'KINZU',#KINS Technology Group Inc Unit
'KEY_L',#KeyCorp Series H Pfd
'KERN',#Akerna Corp
'KELYB',#凯利服务-B
'KDRN',#Kingsbarn Tactical Bond ETF
'KDIV',#KraneShares S&P Pan Asia Divide
'KCGI_U',#Kensington Capital Acquisition
'KCAC',#Kensington Capital Acquisition
'KBNT',#Kubient Inc
'KBND',#KraneShares Bloomberg China Bon
'KANG',#爱康国宾
'KAIRW',#Kairos Acquisition Corp Wt
'KAIRU',#Kairos Acquisition Corp Unit Co
'KAIIW',#Kismet Acquisition Two Corp Wt
'KAHC_WS',#KKR Acquisition Holdings I Corp
'KAHC_U',#KKR Acquisition Holdings I Corp
'KAHC',#KKR Acquisition Holdings I Corp
'KACLW',#Kairous Acquisition Corp Ltd Wt
'KACLU',#Kairous Acquisition Corp Ltd Un
'KACLR',#Kairous Acquisition Corp Ltd Rt
'JZXN',#九紫新能
'JZ',#见知教育
'JYAC',#Jiya Acquisition Corp-A
'JWSM_WS',#Ares Acquisition Corp Wt
'JWSM_U',#Ares Acquisition Corp Unit Cons
'JWACR',#Jupiter Wellness Acquisition Co
'JWAC',#Jupiter Wellness Acquisition Co
'JUPWW',#Jupiter Wellness Inc Wt
'JUN_WS',#Juniper II Corp Wt
'JUNZ',#TrueShares Structured Outcome (
'JUNSW',#Jupiter Neurosciences Inc Wt
'JUNS',#Jupiter Neurosciences Inc
'JUNE',#Junee Ltd
'JUN',#Juniper II Corp-A
'JUGGW',#JAWS Juggernaut Acquisition Cor
'JUGGU',#JAWS Juggernaut Acquisition Cor
'JSKY',#Defiance Junior Cloud Computing
'JR',#锦嵘健康
'JOLT',#Xtrackers Indxx New Energy & En
'JOFFW',#JOFF Fintech Acquisition Corp W
'JOFFU',#JOFF Fintech Acquisition Corp U
'JOFF',#JOFF Fintech Acquisition Corp-A
'JMPW',#跳跃网络
'JMEI',#聚美优品
'JMACW',#Maxpro Capital Acquisition Corp
'JMACU',#Maxpro Capital Acquisition Corp
'JMAC',#Maxpro Capital Acquisition Corp
'JIA',#天鹅到家
'JGGCW',#Jaguar Global Growth Corp I Wt
'JG',#极光
'JFR',#Nuveen Floating Rate Income Fun
'JEMD',#Nuveen Emerging Markets Debt 20
'JCICU',#Jack Creek Investment Corp Unit
'JCIC',#Jack Creek Investment Corp-A
'JBOT',#Defiance Junior Robotics ETF
'JATT_WS',#JATT Acquisition Corp Wt
'JATT_U',#JATT Acquisition Corp Unit Cons
'JAQCW',#Jupiter Acquisition Corp Wt
'JAQCU',#Jupiter Acquisition Corp Unit C
'JAQC',#Jupiter Acquisition Corp-A
'JANA',#嘉纳科技
'IZM',#拍明芯城
'IZEA',#IZEA Worldwide Inc
'IXAQW',#IX Acquisition Corp Wt
'IXAQU',#IX Acquisition Corp Unit Cons o
'IXAQ',#IX Acquisition Corp-A
'IWML',#ETRACS 2x Leveraged US Size Fac
'IWLG',#IQ Winslow Large Cap Growth ETF
'IWFL',#ETRACS 2x Leveraged US Growth F
'IWDL',#ETRACS 2x Leveraged US Value Fa
'IVCPW',#Swiftmerge Acquisition Corp Wt
'IVCPU',#Swiftmerge Acquisition Corp Uni
'IVCP',#Swiftmerge Acquisition Corp-A
'IVCAU',#Investcorp India Acquisition Co
'ITQRW',#Itiquira Acquisition Corp Wt
'ITQRU',#Itiquira Acquisition Corp Unit
'ITQ',#Itiquira Acquisition Corp-A
'ITP',#互联网科技包装
'ITAQW',#Industrial Tech Acquisitions II
'ITAQ',#Industrial Tech Acquisitions II
'ISIG',#Insignia Systems Inc
'ISDB',#Invesco Short Duration Bond ETF
'IRRX_U',#Integrated Rail and Resources A
'IRAAU',#Iris Acquisition Corp Unit Cons
'IQUS',#IQ 500 ETF
'IQMDU',#Intelligent Medicine Acquisitio
'IPVIW',#InterPrivate IV InfraTech Partn
'IPVIU',#InterPrivate IV InfraTech Partn
'IPVI',#InterPrivate IV InfraTech Partn
'IPVF_U',#InterPrivate III Financial Part
'IPVA_U',#InterPrivate II Acquisition Cor
'IPPP',#Preferred-Plus ETF
'IPB',#Merrill Lynch & Co Inc Trust Ce
'IPAXU',#Inflection Point Acquisition Co
'IPAX',#Inflection Point Acquisition Co
'IOACW',#Innovative International Acquis
'IOACU',#Innovative International Acquis
'IOAC',#Innovative International Acquis
'INUV',#Inuvo Inc
'INTS',#Intensity Therapeutics Inc
'INTM',#Intermedia Cloud Communications
'INTG',#The InterGroup Corp
'INTEW',#Integral Acquisition Corp 1 Wt
'INTEU',#Integral Acquisition Corp 1 Uni
'INN_F',#Summit Hotel Properties Inc Ser
'INKAW',#KludeIn I Acquisition Corp Wt
'INKAU',#KludeIn I Acquisition Corp Unit
'INFR',#ClearBridge Sustainable Infrast
'INAQ_WS',#Insight Acquisition Corp Wt
'INAQ_U',#Insight Acquisition Corp Unit C
'INAQ',#Insight Acquisition Corp-A
'IMLP',#Ipath S&P MLP ETN
'IMCIW',#Infinite Group Inc Wt
'IMCI',#Infinite Group Inc
'IMAQU',#International Media Acquisition
'IMAQR',#International Media Acquisition
'IMACW',#IMAC Holdings Inc Wt
'ILSWB',#Insurance Income Strategies Ltd
'ILSWA',#Insurance Income Strategies Ltd
'ILSU',#Insurance Income Strategies Ltd
'ILS',#Insurance Income Strategies Ltd
'IIIIW',#INSU Acquisition Corp III Wt
'IIIIU',#INSU Acquisition Corp III Unit
'IIII',#INSU Acquisition Corp III-A
'IHYF',#Invesco High Yield Bond Factor
'IHY',#国际高收益债ETF-Market Vectors
'IHRT',#iHeartMedia Inc-A
'IGTAW',#Inception Growth Acquisition Lt
'IGTAU',#Inception Growth Acquisition Lt
'IGTAR',#Inception Growth Acquisition Lt
'IGTA',#Inception Growth Acquisition Lt
'IGICW',#International General Insurance
'IFIN_U',#InFinT Acquisition Corp Unit Co
'IFIN',#InFinT Acquisition Corp-A
'IDIV',#U.S. Equity Cumulative Dividend
'IDEX',#优点互动
'ICSH',#iShares Ultra Short-Term Bond E
'ICNC_WS',#Iconic Sports Acquisition Corp
'ICNC',#Iconic Sports Acquisition Corp-
'ICLO',#Invesco AAA CLO Floating Rate N
'ICG',#聪链
'IBTB',#iShares iBonds Dec 2022 Term Tr
'IBMQ',#iShares iBonds Dec 2028 Term Mu
'IBMM',#iShares iBonds Dec 2024 Term Mu
'IBMK',#iShares iBonds Dec 2022 Term Mu
'IBIO',#iBio Inc
'IBHE',#iShares iBonds 2025 Term High Y
'IBHB',#iShares iBonds 2022 Term High Y
'IBGW',#Innovation Beverage Group Ltd W
'IBG',#Innovation Beverage Group Ltd
'IBER_WS',#Ibere Pharmaceuticals Wt
'IBER_U',#Ibere Pharmaceuticals Unit Cons
'IBDO',#iShares iBonds Dec 2023 Term Co
'IBDN',#iShares iBonds Dec 2022 Term Co
'IBDD',#iShares iBonds Mar 2023 Term Co
'IBCE',#iShares iBonds Mar 2023 Term Co
'HZON_WS',#Horizon Acquisition Corp II Wt
'HZON_U',#Horizon Acquisition Corp II Uni
'HYRE',#HyreCar Inc
'HYLT',#HYLETE Inc-A
'HYLO',#iShares High Yield Low Beta ETF
'HYHI',#iShares High Yield High Beta ET
'HY',#海斯特-耶鲁物料搬运
'HWM_',#Howmet Aerospace Inc Pfd
'HWKZ_U',#Hawks Acquisition Corp Unit Con
'HWKZ',#Hawks Acquisition Corp-A
'HWELW',#Healthwell Acquisition Corp I W
'HWELU',#Healthwell Acquisition Corp I U
'HWEL',#Healthwell Acquisition Corp I-A
'HVT_A',#哈弗蒂家具-A
'HVBC',#HV Bancorp Inc
'HUSA',#休斯敦能源
'HUIZ',#慧择
'HUDA',#Hudson Acquisition I Corp
'HUAK',#奥凯发
'HT_C',#HT基金(优先股)
'HTPA_U',#Highland Transcend Partners I C
'HTPA',#Highland Transcend Partners I C
'HSUN',#Hartford Sustainable Income ETF
'HSPOW',#Horizon Space Acquisition I Cor
'HSPOR',#Horizon Space Acquisition I Cor
'HSPO',#Horizon Space Acquisition I Cor
'HSCS',#Heart Test Laboratories Inc
'HSAQ',#Health Sciences Acquisitions Co
'HROWM',#Harrow Health Inc Notes
'HRDG',#华瑞国际
'HPX_U',#HPX Corp Unit Cons of 1 CL A +
'HPS',#John Hancock Preferred Income F
'HPLTW',#Home Plate Acquisition Corp Wt
'HPLTU',#Home Plate Acquisition Corp Uni
'HPLT',#Home Plate Acquisition Corp-A
'HORIW',#Emerging Markets Horizon Corp W
'HORIU',#Emerging Markets Horizon Corp U
'HORI',#Emerging Markets Horizon Corp-A
'HOOK',#HOOKIPA Pharma Inc
'HOLOW',#MicroCloud Hologram Inc Wt
'HNVR',#Hanover Bancorp Inc
'HNST',#The Honest Co Inc
'HNRA_WS',#HNR Acquisition Corp Wt
'HNRA',#HNR Acquisition Corp
'HMU',#HomeUnion Holdings Inc
'HMLP_A',#Hoegh LNG Partners LP Series A
'HMIN',#如家
'HMCOW',#HumanCo Acquisition Corp Wt
'HMCOU',#HumanCo Acquisition Corp Unit C
'HMCO',#HumanCo Acquisition Corp-A
'HMA_WS',#Heartland Media Acquisition Cor
'HMA_U',#Heartland Media Acquisition Cor
'HMACW',#Hainan Manaslu Acquisition Corp
'HMACU',#Hainan Manaslu Acquisition Corp
'HMACR',#Hainan Manaslu Acquisition Corp
'HMA',#Heartland Media Acquisition Cor
'HL_B',#Hecla Mining Co Pfd-B
'HLP',#宏力型钢
'HLLY_WS',#Holley Inc Wt
'HLGE',#Hartford Longevity Economy ETF
'HLF',#康宝莱
'HLBZW',#Helbiz Inc Wt
'HLAHW',#Hamilton Lane Alliance Holdings
'HLAHU',#Hamilton Lane Alliance Holdings
'HLAH',#Hamilton Lane Alliance Holdings
'HKIT',#海天
'HIYS',#Invesco High Yield Select ETF
'HILS',#Hillstream BioPharma Inc
'HIIIW',#Hudson Executive Investment Cor
'HIIIU',#Hudson Executive Investment Cor
'HIII',#Hudson Executive Investment Cor
'HHR',#HeadHunter Group PLC ADR
'HHLA_WS',#HH&L Acquisition Co Wt
'HHGCW',#HHG Capital Corp Wt
'HHGCU',#HHG Capital Corp Unit Cons of 1
'HHGCR',#HHG Capital Corp Rt
'HHGC',#HHG Capital Corp
'HGTY_WS',#Hagerty Inc Wt
'HGIA',#恒光控股
'HFWA',#Heritage Financial Corp
'HFBL',#Home Federal Bancorp Inc of Lou
'HEZU',#iShares Currency Hedged MSCI Eu
'HERAW',#FTAC Hera Acquisition Corp Wt
'HERAU',#FTAC Hera Acquisition Corp Unit
'HEET',#Hartford Schroders ESG US Equit
'HEEM',#iShares Currency Hedged MSCI Em
'HDUS',#Hartford Disciplined US Equity
'HCXY',#Hercules Capital Inc Notes
'HCVIW',#Hennessy Capital Investment Cor
'HCVIU',#Hennessy Capital Investment Cor
'HCTI',#Healthcare Triangle Inc
'HCNEW',#Jaws Hurricane Acquisition Corp
'HCNEU',#Jaws Hurricane Acquisition Corp
'HCNE',#Jaws Hurricane Acquisition Corp
'HCMAW',#HCM Acquisition Corp Wt
'HCMAU',#HCM Acquisition Corp Unit Cons
'HCIIW',#Hudson Executive Investment Cor
'HCIIU',#Hudson Executive Investment Cor
'HCII',#Hudson Executive Investment Cor
'HCICW',#Hennessy Capital Investment Cor
'HCICU',#Hennessy Capital Investment Cor
'HCIC',#Hennessy Capital Investment Cor
'HCDIW',#Harbor Custom Development Inc W
'HCDI',#Harbor Custom Development Inc
'HCARW',#Healthcare Services Acquisition
'HCARU',#Healthcare Services Acquisition
'HCAR',#Healthcare Services Acquisition
'HBER',#胡贝儿
'HAIAW',#Healthcare AI Acquisition Corp
'HAIA',#Healthcare AI Acquisition Corp-
'GYRO',#旋翼物业
'GXIIW',#GX Acquisition Corp II Wt
'GXIIU',#GX Acquisition Corp II Unit Con
'GWII',#Good Works II Acquisition Corp
'GVCIW',#Green Visor Financial Technolog
'GVCI',#Green Visor Financial Technolog
'GTPBW',#Gores Technology Partners II In
'GTPBU',#Gores Technology Partners II In
'GTPB',#Gores Technology Partners II In
'GTPAW',#Gores Technology Partners Inc W
'GTPAU',#Gores Technology Partners Inc U
'GTPA',#Gores Technology Partners Inc-A
'GTH',#泛生子
'GTACW',#Global Technology Acquisition C
'GTACU',#Global Technology Acquisition C
'GS_J',#The Goldman Sachs Group Inc Ser
'GSRMR',#GSR II Meteora Acquisition Corp
'GSRM',#GSR II Meteora Acquisition Corp
'GSQD_U',#G Squared Ascend I Inc Unit Con
'GSQD',#G Squared Ascend I Inc-A
'GSQB_WS',#G Squared Ascend II Inc Wt
'GSQB',#G Squared Ascend II Inc-A
'GSMGW',#耀世星辉(权证)
'GSM',#Ferroglobe PLC
'GSEVW',#Gores Holdings VII Inc Wt
'GSEVU',#Gores Holdings VII Inc Unit Con
'GSEV',#Gores Holdings VII Inc-A
'GSDWW',#Global Systems Dynamics Inc Wt
'GSD',#Global Systems Dynamics Inc-A
'GRTS',#Gritstone bio Inc
'GRTRW',#Global Robotic Drone Acquisitio
'GRTRU',#Global Robotic Drone Acquisitio
'GRTR',#Global Robotic Drone Acquisitio
'GROY_WS',#Gold Royalty Corp Wt
'GROV_WS',#Grove Collaborative Holdings In
'GROMW',#Grom Social Enterprises Inc Wt
'GRNT_WS',#Granite Ridge Resources Inc Wt
'GRNR',#Global X Green Building ETF
'GRNAW',#GreenLight Biosciences Inc Wt
'GRCYW',#绿色城市收购(权证)
'GRCYU',#绿色城市收购(普通单位)
'GRCY',#绿色城市收购
'GPAL',#Goldman Sachs ActiveBeta Paris-
'GPACW',#Global Partner Acquisition Corp
'GPACU',#Global Partner Acquisition Corp
'GOXS',#Goxus Inc
'GOGN_WS',#GoGreen Investments Corp Wt
'GOGN_U',#GoGreen Investments Corp Unit C
'GOGN',#GoGreen Investments Corp-A
'GOEVW',#Canoo Inc Wt
'GNT_A',#GAMCO Natural Resources, Gold &
'GNLX',#Genelux Corp
'GNACW',#Group Nine Acquisition Corp Wt
'GNACU',#Group Nine Acquisition Corp Uni
'GNAC',#Group Nine Acquisition Corp-A
'GMTX',#Gemini Therapeutics Inc
'GMM',#环球墨非
'GMFIW',#Aetherium Acquisition Corp Wt
'GMFIU',#Aetherium Acquisition Corp Unit
'GMFI',#Aetherium Acquisition Corp-A
'GMBLZ',#Esports Entertainment Group Inc
'GMBLW',#Esports Entertainment Group Inc
'GMBL',#Esports Entertainment Group Inc
'GLXY',#Xtrackers Indxx Space & Explora
'GLU_B',#The Gabelli Global Utility & In
'GLTA_U',#Galata Acquisition Corp Unit Co
'GLTA',#Galata Acquisition Corp-A
'GLS_WS',#Gelesis Holdings Inc Wt
'GLSTW',#Global Star Acquisition Inc Wt
'GLSTR',#Global Star Acquisition Inc Rt
'GLS',#Gelesis Holdings Inc
'GLLIW',#Globalink Investment Inc Wt
'GLIG',#Goldman Sachs Access Investment
'GLIF',#AGFiQ Global Infrastructure ETF
'GLIBB',#GCI Liberty Inc-B
'GLHAW',#Glass Houses Acquisition Corp W
'GLHAU',#Glass Houses Acquisition Corp U
'GLHA',#Glass Houses Acquisition Corp-A
'GLE',#Global Engine Group Holding Ltd
'GLBL',#Cartesian Growth Corp-A
'GJT',#STRATS Trust for Allstate Corp
'GJS',#STRATS Trust for Goldman Sachs
'GJO',#STRATS Trust For Wal-Mart Store
'GIWWW',#GigInternational1 Inc Wt
'GIWWU',#GigInternational1 Inc Unit Cons
'GIPRW',#Generation Income Properties In
'GIIXW',#Gores Holdings VIII Inc Wt
'GIIXU',#Gores Holdings VIII Inc Unit Co
'GIIX',#Gores Holdings VIII Inc-A
'GIACW',#Gesher I Acquisition Corp Wt
'GIACU',#Gesher I Acquisition Corp Unit
'GHSI',#Guardion Health Sciences Inc
'GHIXU',#Gores Holdings IX Inc Unit Cons
'GHACW',#Gaming & Hospitality Acquisitio
'GHACU',#Gaming & Hospitality Acquisitio
'GHAC',#Gaming & Hospitality Acquisitio
'GGT_G',#The Gabelli Multimedia Trust In
'GGOV',#Goldman Sachs Access U.S. Treas
'GGN_B',#GAMCO Global Gold, Natural Reso
'GGMCW',#Glenfarne Merger Corp Wt
'GGMCU',#Glenfarne Merger Corp Unit Cons
'GGMC',#Glenfarne Merger Corp-A
'GGAA',#Genesis Growth Tech Acquisition
'GFX_WS',#Golden Falcon Acquisition Corp
'GFX_U',#Golden Falcon Acquisition Corp
'GFX',#Golden Falcon Acquisition Corp-
'GFOR_WS',#Graf Acquisition Corp IV Wt
'GFOR_U',#Graf Acquisition Corp IV Unit C
'GFLDW',#Gefen Landa Acquisition Corp Wt
'GFLDU',#Gefen Landa Acquisition Corp Un
'GFLD',#Gefen Landa Acquisition Corp-A
'GFGDR',#The Growth for Good Acquisition
'GFGD',#The Growth for Good Acquisition
'GFAIW',#卫安智能(权证)
'GENQW',#Growth Capital Acquisition Corp
'GENQU',#Growth Capital Acquisition Corp
'GENQ',#Growth Capital Acquisition Corp
'GELS',#Gelteq Ltd
'GEHCw',#GE HealthCare Technologies Inc
'GEEXW',#Games & Esports Experience Acqu
'GEEXU',#Games & Esports Experience Acqu
'GEEX',#Games & Esports Experience Acqu
'GECCO',#Great Elm Capital Corp Notes
'GECC',#Great Elm Capital Corp
'GDVD',#R3 Global Dividend Growth ETF
'GDSTW',#Goldenstone Acquisition Ltd Wt
'GDSTU',#Goldenstone Acquisition Ltd Uni
'GDSTR',#Goldenstone Acquisition Ltd Rt
'GDST',#Goldenstone Acquisition Ltd
'GDNRU',#Gardiner Healthcare Acquisition
'GDMA_',#Gadsden Dynamic Multi-Asset ETF
'GDL_C',#The GDL Fund Series C Pfd
'GDL',#The GDL Fund
'GDHG',#金生游乐
'GDEVW',#Nexters Inc Wt
'GDEV',#Nexters Inc
'GCV',#The Gabelli Convertible and Inc
'GCTK',#GlucoTrack Inc
'GCMGW',#GCM Grosvenor Inc Wt
'GBUG',#Pacer iPath Gold ETNs
'GBRGU',#Goldenbridge Acquisition Ltd Un
'GBRGR',#Goldenbridge Acquisition Ltd Rt
'GBRG',#Goldenbridge Acquisition Ltd
'GBNY',#Generations Bancorp NY Inc
'GBND',#BrandywineGLOBAL - Global Total
'GBIL',#Goldman Sachs Access Treasury 0
'GBBKW',#Global Blockchain Acquisition C
'GBBKR',#Global Blockchain Acquisition C
'GAU',#Galiano Gold Inc
'GATEW',#Marblegate Acquisition Corp Wt
'GATEU',#Marblegate Acquisition Corp Uni
'GATE',#Marblegate Acquisition Corp
'GAQ_WS',#Generation Asia I Acquisition L
'GAMCU',#Golden Arrow Merger Corp Unit C
'GAMC',#Golden Arrow Merger Corp-A
'GACQW',#Global Consumer Acquisition Cor
'GACQU',#Global Consumer Acquisition Cor
'FZT_U',#FAST Acquisition Corp II Unit C
'FXNC',#First National Corp
'FXCOW',#Financial Strategies Acquisitio
'FXCOR',#Financial Strategies Acquisitio
'FXCO',#Financial Strategies Acquisitio
'FWAC',#Fifth Wall Acquisition Corp III
'FULT',#富尔顿金融
'FUDA',#富达
'FTVIW',#FinTech Acquisition Corp VI Wt
'FTPAU',#FTAC Parnassus Acquisition Corp
'FTIIW',#FutureTech II Acquisition Corp
'FTHI',#First Trust BuyWrite Income ETF
'FTFT',#未来金融科技
'FTEV_WS',#FinTech Evolution Acquisition G
'FTEL',#Fitell Corp
'FTCVW',#FinTech Acquisition Corp V Wt
'FTCVU',#FinTech Acquisition Corp V Unit
'FTCV',#FinTech Acquisition Corp V-A
'FTAAW',#FTAC Athena Acquisition Corp Wt
'FTAAU',#FTAC Athena Acquisition Corp Un
'FTAA',#FTAC Athena Acquisition Corp-A
'FSSIW',#Fortistar Sustainable Solutions
'FSSIU',#Fortistar Sustainable Solutions
'FSSI',#Fortistar Sustainable Solutions
'FSRXW',#FinServ Acquisition Corp II Wt
'FSRXU',#FinServ Acquisition Corp II Uni
'FSRX',#FinServ Acquisition Corp II-A
'FSPR',#Four Springs Capital Trust
'FSNB_U',#Fusion Acquisition Corp II Unit
'FSMB',#First Trust Short Duration Mana
'FRXB',#Forest Road Acquisition Corp II
'FRWAW',#PWP Forward Acquisition Corp I
'FRWAU',#PWP Forward Acquisition Corp I
'FRW',#PWP Forward Acquisition Corp I-
'FRSX',#自动视角控股
'FRST',#Primis Financial Corp
'FRSGW',#First Reserve Sustainable Growt
'FRSGU',#First Reserve Sustainable Growt
'FRSG',#First Reserve Sustainable Growt
'FRONW',#Frontier Acquisition Corp Wt
'FRONU',#Frontier Acquisition Corp Unit
'FRON',#Frontier Acquisition Corp-A
'FRMEP',#First Merchants Corp Series A P
'FRLAW',#Fortune Rise Acquisition Corp W
'FRLAU',#Fortune Rise Acquisition Corp U
'FRLA',#Fortune Rise Acquisition Corp-A
'FRGT',#Freight Technologies Inc
'FRF',#The Fortegra Group Inc
'FPERW',#First Person Ltd Wt
'FPAC_WS',#Far Peak Acquisition Corp Wt
'FPAC',#Far Peak Acquisition Corp-A
'FP',#First Person Ltd
'FOXWW',#FoxWayne Enterprises Acquisitio
'FOXWU',#FoxWayne Enterprises Acquisitio
'FOXO_WS',#FOXO Technologies Inc Wt
'FORLW',#Four Leaf Acquisition Corp Wt
'FORLU',#Four Leaf Acquisition Corp Unit
'FORL',#Four Leaf Acquisition Corp-A
'FOA_WS',#Finance of America Companies In
'FNVTW',#Finnovate Acquisition Corp Wt
'FNVTU',#Finnovate Acquisition Corp Unit
'FNGS',#MicroSectors FANG+ ETNs
'FNGO',#MicroSectors FANG Index 2X Leve
'FNFw',#富达国民金融 WI
'FMIVW',#Forum Merger IV Corp Wt
'FMIVU',#Forum Merger IV Corp Unit Cons
'FLYA_WS',#SOAR Technology Acquisition Cor
'FLYA_U',#SOAR Technology Acquisition Cor
'FLYA',#SOAR Technology Acquisition Cor
'FLRZ',#F5 Finishes Inc
'FLRU',#Franklin FTSE Russia ETF
'FLRN',#SPDR Bloomberg Investment Grade
'FLMI',#Franklin Dynamic Municipal Bond
'FLME_U',#Flame Acquisition Corp Unit Con
'FLFVW',#Feutune Light Acquisition Corp
'FLFVR',#Feutune Light Acquisition Corp
'FLDZ',#RiverNorth Patriot ETF
'FLCTW',#Felicitex Therapeutics Inc Wt
'FLCT',#Felicitex Therapeutics Inc
'FLAG_U',#First Light Acquisition Group I
'FLAG',#First Light Acquisition Group I
'FISK',#Empire State Realty Op LP Serie
'FIP',#FTAI Infrastructure Inc
'FINMW',#Marlin Technology Corp Wt
'FINM',#Marlin Technology Corp-A
'FIHD',#UBS AG FI Enhanced Global High
'FIEE',#UBS AG FI Enhanced Europe 50 ET
'FICVW',#Frontier Investment Corp Wt
'FICVU',#Frontier Investment Corp Unit C
'FICV',#Frontier Investment Corp-A
'FIAX',#Nicholas Fixed Income Alternati
'FIACW',#Focus Impact Acquisition Corp W
'FHLTU',#Future Health ESG Corp Unit Con
'FGMCW',#FG Merger Corp Wt
'FGMC',#FG Merger Corp
'FGIWW',#FGI Industries Ltd Wt
'FGI',#FGI Industries Ltd
'FFWM',#First Foundation Inc
'FEXDW',#Fintech Ecosystem Development C
'FEXDU',#Fintech Ecosystem Development C
'FEXDR',#Fintech Ecosystem Development C
'FEO',#First Trust/abrdn Emerging Oppo
'FEMA',#Procure Disaster Recovery Strat
'FEDL',#ETRACS 2x Leveraged IFED Invest
'FEBZ',#TrueShares Structured Outcome (
'FDHA_WS',#First Digital Health Acquisitio
'FDHA_U',#First Digital Health Acquisitio
'FDHA',#First Digital Health Acquisitio
'FCRX',#First Eagle Alternative Capital
'FCNCP',#First Citizens BancShares Inc S
'FCAX_WS',#Fortress Capital Acquisition Co
'FCAL',#First Trust California Municipa
'FBRX',#Forte Biosciences Inc
'FBOX',#伟博控股
'FBINw',#Fortune Brands Home & Security
'FBC',#旗星银行
'FAZEW',#FaZe Holdings Inc Wt
'FATPU',#Fat Projects Acquisition Corp U
'FATH_WS',#Fathom Digital Manufacturing Co
'FATBW',#FAT Brands Inc Wt
'FAMI',#农米良品
'FAIL',#Cambria Global Tail Risk ETF
'FACT_WS',#Freedom Acquisition I Corp Wt
'FACA_WS',#Figure Acquisition Corp I Wt
'FACA',#Figure Acquisition Corp I-A
'EWX',#SPDR S&P Emerging Markets Small
'EWN',#荷兰ETF-iShares MSCI
'EVTS',#ev Transportation Services Inc
'EVSTC',#Eaton Vance Stock NextShares
'EVOJU',#Evo Acquisition Corp Unit Cons
'EVLMC',#Eaton Vance TABS 5-to-15 Year L
'EVGRW',#Evergreen Corp Wt
'EVGRU',#Evergreen Corp Unit Cons of 1 C
'EVGBC',#Eaton Vance Global Income Build
'EVE_WS',#EVe Mobility Acquisition Corp W
'EVEX_WS',#Eve Holding Inc Wt
'EUCRU',#Eucrates Biomedical Acquisition
'EUCR',#Eucrates Biomedical Acquisition
'ETWO_WS',#E2open Parent Holdings Inc Wt
'ETPA',#Ecofin Digital Payments Infrast
'ESUS',#ETRACS 2x Leveraged MSCI US ESG
'ESSF',#ETRE REIT LLC-A
'ESM_WS',#ESM Acquisition Corp Wt
'ESM_U',#ESM Acquisition Corp Unit Cons
'ESM',#ESM Acquisition Corp-A
'ESCA',#攀登者
'ESBA',#Empire State Realty Op LP Serie
'ESACW',#ESGEN Acquisition Corp Wt
'ERET',#iShares Environmentally Aware R
'ERESU',#East Resources Acquisition Co U
'EQOS',#EQONEX Ltd
'EQOP',#Natixis U.S. Equity Opportuniti
'EQHA_WS',#EQ Health Acquisition Corp Wt
'EQHA_U',#EQ Health Acquisition Corp Unit
'EQHA',#EQ Health Acquisition Corp-A
'EPWR_U',#Empowerment & Inclusion Capital
'EPWR',#Empowerment & Inclusion Capital
'EPHYW',#Epiphany Technology Acquisition
'EPHYU',#Epiphany Technology Acquisition
'EPHY',#Epiphany Technology Acquisition
'EOCW_WS',#Elliott Opportunity II Wt
'ENTXW',#Entera Bio Ltd Wt
'ENTFW',#Enterprise 4.0 Technology Acqui
'ENTFU',#Enterprise 4.0 Technology Acqui
'ENTF',#Enterprise 4.0 Technology Acqui
'ENJ',#Entergy New Orleans LLC Bonds
'ENERW',#Accretion Acquisition Corp Wt
'ENERU',#Accretion Acquisition Corp Unit
'ENERR',#Accretion Acquisition Corp Rt
'ENCPW',#Energem Corp Wt
'ENCPU',#Energem Corp Unit Cons of 1 CL
'ENCP',#Energem Corp-A
'ENACW',#Endeavor Acquisition Corp Wt
'ENACU',#Endeavor Acquisition Corp Unit
'ENAC',#Endeavor Acquisition Corp-A
'EMZA',#Emerge EMPWR Sustainable Global
'EMX',#EMX Royalty Corp
'EMTX',#EMulate Therapeutics Inc
'EMPW',#Emerge EMPWR Unified Sustainabl
'EMNT',#PIMCO Enhanced Short Maturity A
'EMLDU',#FTAC Emerald Acquisition Corp U
'EMLD',#FTAC Emerald Acquisition Cor-A
'EMCH',#Emerge EMPWR Sustainable Emergi
'EMCGW',#Embrace Change Acquisition Corp
'EMCGU',#Embrace Change Acquisition Corp
'EMCGR',#Embrace Change Acquisition Corp
'EMCA',#Emerge EMPWR Sustainable Divide
'EMBKW',#Embark Technology Inc Wt
'ELYSW',#Elys Game Technology Corp Wt
'ELYM',#Eliem Therapeutics Inc
'ELXR',#Xtrackers Indxx Advanced Life S
'ELLO',#Ellomay Capital Ltd
'ELGPW',#Elate Group Inc Wt
'ELGP',#Elate Group Inc-A
'EHR',#Energy Hunter Resources Inc
'EHIC',#一嗨租车
'EHI',#Western Asset Global High Incom
'EGLX',#Enthusiast Gaming Holdings Inc
'EGIO',#Edgio Inc
'EGGF_WS',#EG Acquisition Corp Wt
'EGGF_U',#EG Acquisition Corp Unit Cons o
'EGGF',#EG Acquisition Corp-A
'EFTRW',#eFFECTOR Therapeutics Inc Wt
'EFSH_WS',#1847 Holdings LLC Wt
'EFHTW',#EF Hutton Acquisition Corp I Wt
'EFHTU',#EF Hutton Acquisition Corp I Un
'EFHT',#EF Hutton Acquisition Corp I
'EDTXW',#EdtechX Holdings Acquisition Co
'EDTXU',#EdtechX Holdings Acquisition Co
'EDBLW',#Edible Garden AG Inc Wt
'EDBL',#Edible Garden AG Inc
'ECXWW',#亿咖通科技(权证)
'ECOR',#electroCore Inc
'ECCW',#Eagle Point Credit Co Inc Notes
'ECC',#Eagle Point Credit Co Inc
'EBACU',#European Biotech Acquisition Co
'EBAC',#European Biotech Acquisition Co
'EAST',#Eastside Distilling Inc
'EAR',#Eargo Inc
'EAPR',#Innovator Emerging Markets Powe
'EAOK',#iShares ESG Aware Conservative
'EACPW',#Edify Acquisition Corp Wt
'DWACU',#Digital World Acquisition Corp
'DWAC',#Digital World Acquisition Corp-
'DUNEU',#Dune Acquisition Corp Unit Cons
'DUETW',#DUET Acquisition Corp Wt
'DUETU',#DUET Acquisition Corp Unit Cons
'DUET',#DUET Acquisition Corp-A
'DTSTW',#Data Storage Corp Wt
'DTRTU',#DTRT Health Acquisition Corp Un
'DTRT',#DTRT Health Acquisition Corp-A
'DTOCU',#Digital Transformation Opportun
'DTEA',#DAVIDsTEA Inc
'DSX_B',#Diana Shipping Inc Pfd-B
'DSTX',#Distillate International Fundam
'DSJA',#Innovator Double Stacker ETF -
'DSEY',#Diversey Holdings Ltd
'DSCF',#Discipline Fund ETF
'DSAQ_WS',#Direct Selling Acquisition Corp
'DSAQ_U',#Direct Selling Acquisition Corp
'DRMA',#Dermata Therapeutics Inc
'DRIV',#Global X Autonomous & Electric
'DRAYU',#Macondray Capital Acquisition C
'DRAY',#Macondray Capital Acquisition C
'DPCSW',#DP Cap Acquisition Corp I Wt
'DPCSU',#DP Cap Acquisition Corp I Unit
'DPCS',#DP Cap Acquisition Corp I-A
'DOMA_WS',#Doma Holdings Inc Wt
'DNZ_U',#D and Z Media Acquisition Corp
'DNZ',#D and Z Media Acquisition Corp-
'DNK',#蛋壳公寓
'DNB',#邓白氏
'DNAB',#Social Capital Suvretta Holding
'DMYY_U',#dMY Squared Technology Group In
'DMYY',#dMY Squared Technology Group In
'DMYS',#dMY Technology Group Inc VI-A
'DMAQR',#Deep Medicine Acquisition Corp
'DMAQ',#Deep Medicine Acquisition Corp-
'DLNG_B',#Dynagas LNG Partners LP Series
'DLCAW',#Deep Lake Capital Acquisition C
'DLCAU',#Deep Lake Capital Acquisition C
'DLCA',#Deep Lake Capital Acquisition C
'DKDCW',#Data Knights Acquisition Corp W
'DKDCU',#Data Knights Acquisition Corp U
'DKDCA',#Data Knights Acquisition Corp-A
'DILAW',#DILA Capital Acquisition Corp W
'DILAU',#DILA Capital Acquisition Corp U
'DILA',#DILA Capital Acquisition Corp-A
'DHR_B',#Danaher Corp Series B Pfd
'DHHC',#DiamondHead Holdings Corp-A
'DHCAW',#DHC Acquisition Corp Wt
'DHCAU',#DHC Acquisition Corp Unit Cons
'DHCA',#DHC Acquisition Corp-A
'DHBCW',#DHB Capital Corp Wt
'DHBCU',#DHB Capital Corp Unit Cons of 1
'DHBC',#DHB Capital Corp-A
'DHACW',#Digital Health Acquisition Corp
'DHACU',#Digital Health Acquisition Corp
'DHAC',#Digital Health Acquisition Corp
'DGICB',#多尼戈尔股份-B
'DFH',#Dream Finders Homes Inc-A
'DFEM',#Dimensional Emerging Markets Co
'DESR',#DESRI Inc
'DESK',#Pacer Benchmark Office Real Est
'DEIF',#Sterling Capital Diverse Multi-
'DEI',#道格拉斯艾美特
'DEFI',#Hashdex Bitcoin Futures ETF
'DECZ',#TrueShares Structured Outcome (
'DECAW',#Denali Capital Acquisition Corp
'DDF',#Delaware Investments Dividend &
'DC_WS',#Dakota Gold Corp Wt
'DCRD',#Decarbonization Plus Acquisitio
'DCCA',#达艺
'DBRG',#DigitalBridge Group Inc-A
'DBEZ',#Xtrackers MSCI Eurozone Hedged
'DATSW',#DatChat Inc Wt-A
'DATE',#世纪佳缘
'DARE',#Dare Bioscience Inc
'DAOOW',#Crypto 1 Acquisition Corp Wt
'DAOOU',#Crypto 1 Acquisition Corp Unit
'DAOO',#Crypto 1 Acquisition Corp-A
'DANG',#当当网
'CZOO_WS',#Cazoo Group Ltd Wt
'CZFS',#Citizens Financial Services Inc
'CYTHW',#Cyclo Therapeutics Inc Wt
'CYD',#玉柴国际
'CYCCP',#Cyclacel Pharmaceuticals Inc Pf
'CXE',#MFS High Income Municipal Trust
'CXAC_U',#C5 Acquisition Corp Unit Cons o
'CWEN',#Clearway Energy Inc-C
'CWD',#CaliberCos Inc-A
'CVKD',#Cadrenal Therapeutics Inc
'CVII_U',#Churchill Capital Corp VII Unit
'CVAR',#Cultivar ETF
'CURIW',#CuriosityStream Inc Wt
'CULL',#Cullman Bancorp Inc
'CUENW',#Cuentas Inc Wt
'CUBT_WS',#Curative Biotechnology Inc Wt
'CUBT',#Curative Biotechnology Inc
'CTV_WS',#Innovid Corp Wt
'CTIB',#运鸿CTI
'CTGO',#Contango ORE Inc
'CTC',#21世纪不动产
'CTAQW',#Carney Technology Acquisition C
'CSTA_WS',#Constellation Acquisition Corp
'CSTA',#Constellation Acquisition Corp
'CSSEL',#心灵鸡汤娱乐 (权证)
'CSLMW',#Consilium Acquisition Corp I Lt
'CSLMU',#Consilium Acquisition Corp I Lt
'CSLMR',#Consilium Acquisition Corp I Lt
'CSLM',#Consilium Acquisition Corp I Lt
'CSCA',#基岩资本
'CRw',#Crane Co
'CRZNW',#Corazon Capital V838 Monoceros
'CRZNU',#Corazon Capital V838 Monoceros
'CRZN',#Corazon Capital V838 Monoceros
'CRVS',#Corvus Pharmaceuticals Inc
'CRU_U',#Crucible Acquisition Corp Unit
'CRU',#Crucible Acquisition Corp-A
'CRKN',#Crown Electrokinetics Corp
'CREXW',#Creative Realities Inc Wt
'CRECW',#Crescera Capital Acquisition Co
'CRECU',#Crescera Capital Acquisition Co
'CREC',#Crescera Capital Acquisition Co
'CRBP',#Corbus Pharmaceuticals Holdings
'CPUH_U',#Compute Health Acquisition Corp
'CPTK_U',#Crown PropTech Acquisitions Uni
'CPTK',#Crown PropTech Acquisitions-A
'CPII',#Ionic Inflation Protection ETF
'CPHI',#惠普森医药
'CPARW',#Catalyst Partners Acquisition C
'CPAR',#Catalyst Partners Acquisition C
'CPAQU',#Counter Press Acquisition Corp
'CPAQ',#Counter Press Acquisition Corp-
'CPAAW',#Conyers Park III Acquisition Co
'CPAAU',#Conyers Park III Acquisition Co
'COVAU',#COVA Acquisition Corp Unit Cons
'CORZW',#Core Scientific Inc Wt
'CORS_WS',#Corsair Partnering Corp Wt
'CORS_U',#Corsair Partnering Corp Unit Co
'COOLU',#Corner Growth Acquisition Corp
'COOL',#Corner Growth Acquisition Corp-
'CONXU',#CONX Corp Unit Cons of 1 CL A +
'COMSW',#COMSovereign Holding Corp Wt
'COMSP',#COMSovereign Holding Corp Serie
'COMS',#COMSovereign Holding Corp
'COLIW',#Colicity Inc Wt
'COLIU',#Colicity Inc Unit Cons of 1 CL
'COLI',#Colicity Inc-A
'CODI_B',#Compass Group Diversified Holdi
'CO',#国际脐带血库
'CNGLW',#Canna-Global Acquisition Corp W
'CNGLU',#Canna-Global Acquisition Corp U
'CNGL',#Canna-Global Acquisition Corp-A
'CNFRL',#Conifer Holdings Inc Notes
'CNFR',#康年控股
'CNET',#中网载线
'CND_WS',#Concord Acquisition Corp Wt
'CND_U',#Concord Acquisition Corp Unit C
'CNDB_U',#Concord Acquisition Corp III Un
'CNDB',#Concord Acquisition Corp III-A
'CNDA_U',#Concord Acquisition Corp II Uni
'CND',#Concord Acquisition Corp-A
'CNAQW',#Chardan NexTech Acquisition Cor
'CNAQU',#Chardan NexTech Acquisition Cor
'CNAQ',#Chardan NexTech Acquisition Cor
'CMU',#MFS High Yield Municipal Trust
'CMRE_D',#Costamare Inc Pfd-D
'CMDS',#达闼科技
'CMCTP',#Creative Media & Community Trus
'CMCAW',#Capitalworks Emerging Markets A
'CMCAU',#Capitalworks Emerging Markets A
'CMAXW',#CareMax Inc Wt
'CMAX',#CareMax Inc-A
'CLWT',#欧陆科仪
'CLVS',#Clovis Oncology Inc
'CLVRW',#Clever Leaves Holdings Inc Wt
'CLTL',#Invesco Treasury Collateral ETF
'CLST',#Catalyst Bancorp Inc
'CLRMW',#Clarim Acquisition Corp Wt
'CLRMU',#Clarim Acquisition Corp Unit Co
'CLRM',#Clarim Acquisition Corp-A
'CLRCW',#ClimateRock Wt
'CLRCU',#ClimateRock Unit Cons of 1 CL A
'CLRCR',#ClimateRock Rt
'CLRC',#ClimateRock-A
'CLOEU',#Clover Leaf Capital Corp Unit C
'CLOE',#Clover Leaf Capital Corp-A
'CLNNW',#Clene Inc Wt
'CLNN',#Clene Inc
'CLINW',#Clean Earth Acquisitions Corp W
'CLINU',#Clean Earth Acquisitions Corp U
'CLIN',#Clean Earth Acquisitions Corp-A
'CLIM_U',#Climate Real Impact Solutions I
'CLIM',#Climate Real Impact Solutions I
'CLDT_A',#Chatham Lodging信托(优先股)
'CLBR_U',#Colombier Acquisition Corp Unit
'CLAYW',#Chavant Capital Acquisition Cor
'CLAS_WS',#Class Acceleration Corp Wt
'CLAS_U',#Class Acceleration Corp Unit Co
'CLAA_WS',#Colonnade Acquisition Corp II W
'CLAA',#Colonnade Acquisition Corp II-A
'CJOY',#影高文化
'CITEU',#Cartica Acquisition Corp Unit C
'CIRC',#JPMorgan Sustainable Consumptio
'CIIGW',#CIIG Capital Partners II Inc Wt
'CIIGU',#CIIG Capital Partners II Inc Un
'CIH',#中指控股
'CIAN',#Cian PLC ADR
'CHY',#Calamos Convertible and High In
'CHSN',#乔治香颂
'CHKEZ',#Chesapeake Energy Corp Wt
'CHKEW',#Chesapeake Energy Corp Wt
'CHIU',#Global X MSCI China Utilities E
'CHIA',#Global X China Mid Cap ETF
'CHG_WS',#CorpHousing Group Inc Wt
'CHEAW',#Chenghe Acquisition Co Wt
'CHEAU',#Chenghe Acquisition Co Unit Con
'CHEA',#Chenghe Acquisition Co-A
'CHAA_U',#Catcha Investment Corp Unit Con
'CGMS',#Capital Group U.S. Multi-Sector
'CFRX',#ContraFect Corp
'CFIVW',#CF Acquisition Corp IV Wt
'CFFSU',#CF Acquisition Corp VII Unit Co
'CFFS',#CF Acquisition Corp VII-A
'CFFEU',#CF Acquisition Corp VIII Unit C
'CFFE',#CF Acquisition Corp VIII-A
'CEY',#VictoryShares Emerging Market H
'CENQW',#CENAQ Energy Corp Wt
'CEMI',#Chembio Diagnostics Inc
'CEADW',#CEA Industries Inc Wt
'CDTG',#城道通环保科技
'CDP',#CDP
'CDIOW',#Cardio Diagnostics Holdings Inc
'CDIO',#Cardio Diagnostics Holdings Inc
'CDAQW',#Compass Digital Acquisition Cor
'CCZ',#Comcast Corp Debentures
'CCV_U',#Churchill Capital Corp V Unit C
'CCV',#Churchill Capital Corp V-A
'CCTSW',#Cactus Acquisition Corp 1 Ltd W
'CCO',#Clear Channel Outdoor Holdings
'CCNEP',#CNB Financial Corp Series A Pfd
'CCD',#Calamos Dynamic Convertible and
'CCAIW',#Cascadia Acquisition Corp Wt
'CCAIU',#Cascadia Acquisition Corp Unit
'CCAI',#Cascadia Acquisition Corp-A
'CBRGW',#Chain Bridge I Wt
'CBRGU',#Chain Bridge I Unit Cons of 1 C
'CBRG',#Chain Bridge I-A
'CBFV',#CB金融服务
'CANBW',#Can B Corp Wt-X
'CANB',#Can B Corp
'CALQW',#Callodine Acquisition Corp Wt
'CALQU',#Callodine Acquisition Corp Unit
'CALQ',#Callodine Acquisition Corp-A
'CAE',#加拿大航空电子设备
'BZFDW',#BuzzFeed Inc Wt
'BYTSU',#BYTE Acquisition Corp Unit Cons
'BYTS',#BYTE Acquisition Corp-A
'BYN_WS',#Banyan Acquisition Corp Wt
'BYN_U',#Banyan Acquisition Corp Unit Co
'BYNOW',#byNordic Acquisition Corp Wt
'BYNOU',#byNordic Acquisition Corp Unit
'BWCAU',#Blue Whale Acquisition Corp I U
'BWAQW',#Blue World Acquisition Corp Wt
'BWACU',#Better World Acquisition Corp U
'BWAC',#Better World Acquisition Corp
'BTRY',#Clarios International Inc
'BTRS',#BTRS Holdings Inc-A
'BTMDW',#biote Corp Wt
'BTBDW',#BT Brands Inc Wt
'BSTZ',#BlackRock Science and Technolog
'BSMM',#Invesco BulletShares 2022 Munic
'BSKYW',#Big Sky Growth Partners Inc Wt
'BSKYU',#Big Sky Growth Partners Inc Uni
'BSKY',#Big Sky Growth Partners Inc-A
'BSJM',#Invesco BulletShares 2022 High
'BSGAU',#Blue Safari Group Acquisition C
'BSCM',#Invesco BulletShares 2022 Corpo
'BSBE',#Invesco BulletShares 2022 USD E
'BSAQ_U',#黑桃亚洲(普通单位)
'BSAQ',#黑桃亚洲-A
'BROGW',#Brooge Energy Ltd Wt
'BRMK_WS',#Broadmark Realty Capital Inc Wt
'BRLIW',#Brilliant Acquisition Corp Wt
'BRLIU',#Brilliant Acquisition Corp Unit
'BRLIR',#Brilliant Acquisition Corp Rt
'BRLI',#Brilliant Acquisition Corp
'BRKHU',#BurTech Acquisition Corp Unit C
'BRIVU',#B. Riley Principal 250 Merger C
'BRIV',#B. Riley Principal 250 Merger C
'BREZW',#Breeze Holdings Acquisition Cor
'BREZ',#Breeze Holdings Acquisition Cor
'BRD_WS',#Beard Energy Transition Acquisi
'BRD_U',#Beard Energy Transition Acquisi
'BRDS',#Bird Global Inc-A
'BRD',#Beard Energy Transition Acquisi
'BRACU',#Broad Capital Acquisition Corp
'BRACR',#Broad Capital Acquisition Corp
'BPTS',#Biophytis SA ADR
'BPAY',#BlackRock Future Financial and
'BPACW',#Bullpen Parlay Acquisition Co W
'BPACU',#Bullpen Parlay Acquisition Co U
'BPAC',#Bullpen Parlay Acquisition Co-A
'BOXX',#Alpha Architect 1-3 Month Box E
'BOXLW',#Boxlight Corp Wt
'BOXD',#Boxed Inc
'BOUW',#Boustead Wavefront Inc-A
'BOTZ',#Global X Robotics & Artificial
'BOCNW',#Blue Ocean Acquisition Corp Wt
'BOCNU',#Blue Ocean Acquisition Corp Uni
'BNw',#Brookfield Corp-A WI
'BNOX',#Bionomics Ltd ADR
'BNNRW',#Banner Acquisition Corp Wt
'BNNRU',#Banner Acquisition Corp Unit Co
'BNNR',#Banner Acquisition Corp-A
'BNIXR',#Bannix Acquisition Corp Rt
'BNGOW',#Bionano Genomics Inc Wt
'BMR',#Beamr Imaging Ltd
'BMAQW',#Blockchain Moon Acquisition Cor
'BMAQU',#Blockchain Moon Acquisition Cor
'BMAQR',#Blockchain Moon Acquisition Cor
'BMAC_WS',#Black Mountain Acquisition Corp
'BMAC',#Black Mountain Acquisition Corp
'BLUA_WS',#BlueRiver Acquisition Corp Wt
'BLUA',#BlueRiver Acquisition Corp-A
'BLU',#BELLUS Health Inc
'BLTSW',#Bright Lights Acquisition Corp
'BLTSU',#Bright Lights Acquisition Corp
'BLTS',#Bright Lights Acquisition Corp-
'BLNGU',#Belong Acquisition Corp Unit Co
'BLLD',#JPMorgan Sustainable Infrastruc
'BLFY',#Blue Foundry Bancorp
'BLEUW',#bleuacacia ltd Wt
'BLEUU',#bleuacacia ltd Unit Cons of 1 C
'BLEUR',#bleuacacia ltd Rt
'BLEU',#bleuacacia ltd-A
'BLBX',#Blackboxstocks Inc
'BLACW',#Bellevue Life Sciences Acquisit
'BLACU',#Bellevue Life Sciences Acquisit
'BLAC',#Bellevue Life Sciences Acquisit
'BKW',#汉堡王
'BKUS',#BNY Mellon Sustainable US Equit
'BKSW',#佰康生物
'BKIS',#BNY Mellon Sustainable Internat
'BKDT',#Brookdale Senior Living Inc Equ
'BITE_WS',#Bite Acquisition Corp Wt
'BITE_U',#Bite Acquisition Corp Unit Cons
'BIO_B',#Bio Rad实验室-B
'BIOT',#Biotech Acquisition Co-A
'BIOSW',#BioPlus Acquisition Corp Wt
'BIL',#美国1-3月国债ETF-SPDR
'BID',#苏富比
'BIAFW',#bioAffinity Technologies Inc Wt
'BH_A',#Biglari Holdings Inc-A
'BHR_D',#Braemar Hotels & Resorts Inc Se
'BHG',#Bright Health Group Inc
'BHACW',#Crixus BH3 Acquisition Co Wt
'BHACU',#Crixus BH3 Acquisition Co Unit
'BGXX',#Bright Green Corp
'BGSX_WS',#Build Acquisition Corp Wt
'BGSX_U',#Build Acquisition Corp Unit Con
'BFS_E',#Saul Centers Inc Series E Pfd
'BFRGW',#Bullfrog AI Holdings Inc Wt
'BFRG',#Bullfrog AI Holdings Inc
'BFL',#BankFlorida
'BFIX',#Build Bond Innovation ETF
'BFAC_U',#Battery Future Acquisition Corp
'BFAC',#Battery Future Acquisition Corp
'BEI',#Aberdeen Standard Bloomberg Ene
'BDS',#筑梦之星
'BCSAW',#Blockchain Coinvestors Acquisit
'BCSAU',#Blockchain Coinvestors Acquisit
'BCSA',#Blockchain Coinvestors Acquisit
'BCS30',#Barclays PLC Notes
'BCOV',#布莱克维
'BCGFW',#BCGF Acquisition Corp Wt
'BCGFU',#BCGF Acquisition Corp Unit Cons
'BCGF',#BCGF Acquisition Corp-A
'BBLG',#Bone Biologics Corp
'BBCP',#Concrete Pumping Holdings Inc
'BANL',#CBL International Ltd
'BACA_WS',#Berenson Acquisition Corp I Wt
'BACA_U',#Berenson Acquisition Corp I Uni
'AZTD',#Aztlan Global Stock Selection D
'AZCJ',#AllianzIM U.S. Large Cap Buffer
'AYTUP',#Aytu BioPharma Inc Series I Pfd
'AXTI',#AXT Inc
'AXDX',#Accelerate Diagnostics Inc
'AXACr',#AXIOS Sustainable Growth Acquis
'AXAC_WS',#AXIOS Sustainable Growth Acquis
'AXAC',#AXIOS Sustainable Growth Acquis
'AWX',#Avalon Holdings Corp-A
'AVHIW',#Achari Ventures Holdings Corp I
'AVHIU',#Achari Ventures Holdings Corp I
'AVHI',#Achari Ventures Holdings Corp I
'AVGR',#Avinger Inc
'AVEO',#AVEO制药
'AVACU',#Avalon Acquisition Inc Unit Con
'AUUDW',#Auddia Inc Series A Wt
'AURCW',#Aurora Acquisition Corp II Wt
'AURCU',#Aurora Acquisition Corp II Unit
'AUR',#Aurora Innovation Inc-A
'ATMVR',#AlphaVest Acquisition Corp Rt
'ATMV',#AlphaVest Acquisition Corp
'ATLX',#Atlas Lithium Corp
'ATIP_WS',#ATI Physical Therapy Inc Wt
'ATFV',#Alger 35 ETF
'ATFI',#Anfield Tactical Fixed Income E
'ATER',#Aterian Inc
'ATEK_WS',#Athena Technology Acquisition C
'ATEK_U',#Athena Technology Acquisition C
'ATEK',#Athena Technology Acquisition C
'ATA_WS',#Americas Technology Acquisition
'ATA_U',#Americas Technology Acquisition
'ATAQ_U',#Altimar Acquisition Corp III Un
'ATAQ',#Altimar Acquisition Corp III-A
'ATAKW',#Aurora Technology Acquisition C
'ATAKU',#Aurora Technology Acquisition C
'ATAKR',#Aurora Technology Acquisition C
'ATAK',#Aurora Technology Acquisition C
'ATA',#Americas Technology Acquisition
'ASXC',#Asensus Surgical Inc
'ASTIW',#Ascent Solar Technologies Inc W
'ASST',#Asset Entities Inc-B
'ASPU',#艾斯潘集团
'ASPPW',#Abri SPAC 2 Inc Wt
'ASPPU',#Abri SPAC 2 Inc Unit Cons of 1
'ASPPR',#Abri SPAC 2 Inc Rt
'ASPP',#Abri SPAC 2 Inc
'ASPAW',#Abri SPAC I Inc Wt
'ASPAU',#Abri SPAC I Inc Unit Cons of 1
'ASM',#Avino Silver & Gold Mines Ltd
'ASCBW',#A SPAC II Acquisition Corp Wt
'ASCBU',#A SPAC II Acquisition Corp Unit
'ASCAW',#A SPAC I Acquisition Corp Wt
'ASCAU',#A SPAC I Acquisition Corp Unit
'ASCAR',#A SPAC I Acquisition Corp Rt
'ASCA',#A SPAC I Acquisition Corp-A
'ASAXW',#Astrea Acquisition Corp Wt
'ASAXU',#Astrea Acquisition Corp Unit Co
'ASAP',#Waitr Holdings Inc
'ARYE',#ARYA Sciences Acquisition Corp
'ARYD',#ARYA Sciences Acquisition Corp
'ARVR',#First Trust Indxx Metaverse ETF
'ARTLW',#Artelo Biosciences Inc Wt
'ARTEW',#Artemis Strategic Investment Co
'ARTEU',#Artemis Strategic Investment Co
'ARRWU',#Arrowroot Acquisition Corp Unit
'ARRW',#Arrowroot Acquisition Corp-A
'ARMI',#Armor International Equity Inde
'ARKO',#ARKO Corp
'ARIZW',#Arisz Acquisition Corp Wt
'ARIZU',#Arisz Acquisition Corp Unit Con
'ARIZ',#Arisz Acquisition Corp
'ARGUW',#Argus Capital Corp Wt
'ARGUU',#Argus Capital Corp Unit Cons of
'ARGU',#Argus Capital Corp-A
'AREE',#Armor Emerging Markets Equity I
'ARCKW',#Arbor Rapha Capital Bioholdings
'ARBGW',#Aequi Acquisition Corp Wt
'ARBGU',#Aequi Acquisition Corp Unit Con
'ARAY',#精确射线
'ARAGW',#Arago Acquisition Corp Wt
'ARAGU',#Arago Acquisition Corp Unit Con
'ARAG',#Arago Acquisition Corp
'AQUNU',#Aquaron Acquisition Corp Unit C
'AQUNR',#Aquaron Acquisition Corp Rt
'AP_WS',#安博科-匹兹堡(权证)
'APXIW',#APx Acquisition Corp I Wt
'APXIU',#APx Acquisition Corp I Unit Con
'APXI',#APx Acquisition Corp I-A
'APTO',#Aptose Biosciences Inc
'APTMW',#Alpha Partners Technology Merge
'APTMU',#Alpha Partners Technology Merge
'APPHW',#AppHarvest Inc Wt
'APP',#Applovin Corp-A
'APN_WS',#Apeiron Capital Investment Corp
'APN_U',#Apeiron Capital Investment Corp
'APN',#Apeiron Capital Investment Corp
'APMIW',#AxonPrime Infrastructure Acquis
'APMIU',#AxonPrime Infrastructure Acquis
'APLD',#Applied Digital Corp
'APGB_U',#Apollo Strategic Growth Capital
'APDN',#Applied DNA Sciences Inc
'APCA_U',#AP收购(普通单位)
'APCA',#AP收购
'AOGOW',#Arogo Capital Acquisition Corp
'AOGOU',#Arogo Capital Acquisition Corp
'AOGO',#Arogo Capital Acquisition Corp-
'ANEW',#MSCI Transformational Changes E
'ANAC_WS',#Arctos NorthStar Acquisition Co
'AMPI_U',#Advanced Merger Partners Inc Un
'AMPI',#Advanced Merger Partners Inc-A
'AMPGW',#AmpliTech Group Inc Wt
'AMNA',#ETRACS Alerian Midstream Energy
'AMCIU',#AMCI Acquisition Corp II Unit C
'AMBO',#安博教育
'AMBC_WS',#Ambac Financial Group Inc Wt
'AMAOW',#American Acquisition Opportunit
'AMAOU',#American Acquisition Opportunit
'AMAO',#American Acquisition Opportunit
'ALTUU',#Altitude Acquisition Corp Unit
'ALTU',#Altitude Acquisition Corp
'ALTG_A',#Alta Equipment Group Series A P
'ALSAR',#Alpha Star Acquisition Corp Rt
'ALPX',#Alopexx Inc
'ALPAU',#Alpha Healthcare Acquisition Co
'ALPA',#Alpha Healthcare Acquisition Co
'ALORU',#ALSP Orchid Acquisition Corp I
'ALOR',#ALSP Orchid Acquisition Corp I-
'ALLG_WS',#Allego NV Wt
'ALEH',#奥利
'ALEF',#Aleph Group Inc-A
'ALBT',#Avalon GloboCare Corp
'AKUS',#Akouos Inc
'AKU',#Akumin Inc
'AKTX',#Akari Therapeutics PLC ADR
'AKICW',#Sports Ventures Acquisition Cor
'AKICU',#Sports Ventures Acquisition Cor
'AJX',#Great Ajax Corp
'AIV',#公寓投资管理
'AIRTP',#Air T Inc Pfd
'AIMD',#Ainos Inc
'AIMBU',#Aimfinity Investment Corp I Uni
'AIMA',#Aimfinity Investment Corp I-A
'AIBBU',#AIB Acquisition Corp Unit Cons
'AIBBR',#AIB Acquisition Corp Rt
'AHRNU',#Ahren Acquisition Corp Unit Con
'AHRN',#Ahren Acquisition Corp-A
'AHR',#American Healthcare REIT Inc
'AHOY',#Newday Ocean Health ETF
'AGTC',#Applied Genetic Technologies Co
'AGRIWI',#Aberdeen Standard Bloomberg Agr
'AGRH',#iShares Interest Rate Hedged U.
'AGM_A',#联邦农业抵押贷款-A
'AGLE',#Aeglea生物制药
'AGILW',#AgileThought Inc Wt
'AGII',#堂堂加
'AGIH',#iShares Inflation Hedged U.S. A
'AGGRW',#Agile Growth Corp Wt
'AGGRU',#Agile Growth Corp Unit Cons of
'AGGR',#Agile Growth Corp-A
'AGFY',#Agrify Corp
'AGFS',#AgroFresh Solutions Inc
'AGE',#AgeX Therapeutics Inc
'AGCB',#Altimeter Growth Corp 2-A
'AGAC_WS',#African Gold Acquisition Corp W
'AGAC_U',#African Gold Acquisition Corp U
'AGAC',#African Gold Acquisition Corp-A
'AFTR_U',#AfterNext HealthTech Acquisitio
'AFTR',#AfterNext HealthTech Acquisitio
'AFR',#Global X Emerging Africa ETF
'AFGL',#AFG Holdings Inc
'AFBI',#Affinity Bancshares Inc
'AFARW',#Aura FAT Projects Acquisition C
'AFARU',#Aura FAT Projects Acquisition C
'AFAR',#Aura FAT Projects Acquisition C
'AFAQW',#AF Acquisition Corp Wt
'AFAQU',#AF Acquisition Corp Unit Cons o
'AFAQ',#AF Acquisition Corp-A
'AFACW',#Arena Fortify Acquisition Corp
'AFACU',#Arena Fortify Acquisition Corp
'AFAC',#Arena Fortify Acquisition Corp-
'AEMD',#Aethlon Medical Inc
'AEI',#Alset Inc
'AEHAW',#Aesther Healthcare Acquisition
'AEHAU',#Aesther Healthcare Acquisition
'AEHA',#Aesther Healthcare Acquisition
'AEAEW',#AltEnergy Acquisition Corp Wt
'AEAEU',#AltEnergy Acquisition Corp Unit
'AEAE',#AltEnergy Acquisition Corp-A
'AEACW',#Authentic Equity Acquisition Co
'AEAC',#Authentic Equity Acquisition Co
'ADTHW',#AdTheorent Holding Co Inc Wt
'ADRT_U',#Ault Disruptive Technologies Co
'ADRA_WS',#Adara Acquisition Corp Wt
'ADRA_U',#Adara Acquisition Corp Unit Con
'ADRA',#Adara Acquisition Corp-A
'ADPV',#Adaptiv Select ETF
'ADOCW',#Edoc Acquisition Corp Wt
'ADOCR',#Edoc Acquisition Corp Rt
'ADMP',#Adamis Pharmaceuticals Corp
'ADILW',#Adial Pharmaceuticals Inc Wt
'ADEX_WS',#Adit EdTech Acquisition Corp Wt
'ADEX_U',#Adit EdTech Acquisition Corp Un
'ADEX',#Adit EdTech Acquisition Corp
'ADERU',#26 Capital Acquisition Corp Uni
'ADD',#Color Star Technology Co Ltd
'ADALW',#Anthemis Digital Acquisitions I
'ADALU',#Anthemis Digital Acquisitions I
'ADAL',#Anthemis Digital Acquisitions I
'ACRO_U',#Acropolis Infrastructure Acquis
'ACQRU',#Independence Holdings Corp Unit
'ACQR',#Independence Holdings Corp-A
'ACII_U',#Atlas Crest Investment Corp II
'ACII',#Atlas Crest Investment Corp II-
'ACDI_WS',#Ascendant Digital Acquisition C
'ACDI_U',#Ascendant Digital Acquisition C
'ACBAU',#Ace Global Business Acquisition
'ACBA',#Ace Global Business Acquisition
'ACAXW',#Alset Capital Acquisition Corp
'ACAXU',#Alset Capital Acquisition Corp
'ACAXR',#Alset Capital Acquisition Corp
'ACAX',#Alset Capital Acquisition Corp-
'ACAQ_WS',#Athena Consumer Acquisition Cor
'ACAQ_U',#Athena Consumer Acquisition Cor
'ACAHW',#Atlantic Coastal Acquisition Co
'ACAHU',#Atlantic Coastal Acquisition Co
'ACACW',#Acri Capital Acquisition Corp W
'ACACU',#Acri Capital Acquisition Corp U
'ACABW',#Atlantic Coastal Acquisition Co
'ACABU',#Atlantic Coastal Acquisition Co
'ABMD',#阿比奥梅德
'AAU',#Almaden Minerals Ltd
'AAQC_U',#Accelerate Acquisition Corp Uni
'AAQC',#Accelerate Acquisition Corp-A
'AAPL42',#Apple Inc Notes 2042
'AAPL29A',#Apple Inc Notes 2029
'AAPL29',#Apple Inc Notes 2029
'AAPL27',#Apple Inc Notes 2027
'AAPL26',#Apple Inc Notes 2026
'AAPL25',#Apple Inc Notes 2025
'AAPL24',#Apple Inc Notes 2024
'AAPL22',#Apple Inc Notes 2022
'AAMC',#Altisource Asset Management Cor
'AAIN',#Arlington Asset Investment Corp
'AACIW',#Armada Acquisition Corp I Wt
'AACIU',#Armada Acquisition Corp I Unit
'AACI',#Armada Acquisition Corp I
'SHV',#短期国债ETF-iShares
'SMH',#半导体ETF-VanEck Vectors
'VBK',#小型成长股指数ETF-Vanguard
'MINT',#PIMCO Enhanced Short Maturity A
'STIP',#0-5年抗通胀债ETF-iShares
'VCSH',#短期公司债指数ETF-Vanguard
'MMSI',#Merit Medical Systems Inc
'DFJ',#日本小型红利股ETF-WisdomTree
'HYHG',#ProShares High Yield Interest R
'SLMBP',#SLM Corp Series B Pfd
'ERIE',#伊瑞保险
'SCMB',#Schwab Municipal Bond ETF
'AVEM',#Avantis Emerging Markets Equity
'USFR',#WisdomTree Floating Rate Treasu
'IMSI',#Invesco Municipal Strategic Inc
'XONE',#BondBloxx Bloomberg One Year Ta
'GS',#高盛
'HOLD',#AdvisorShares North Square McKe
'FLTB',#Fidelity Limited Term Bond ETF
'GLU_A',#The Gabelli Global Utility & In
'DFSD',#Dimensional Short-Duration Fixe
'JPIB',#JPMorgan International Bond Opp
'STOT',#SPDR DoubleLine Short Duration
'ONEQ',#Fidelity Nasdaq Composite Index
'AVES',#Avantis Emerging Markets Value
'ARKQ',#ARK Autonomous Technology & Rob
'IGOV',#iShares International Treasury
'COUP',#Coupa Software Inc
'LH',#徕博科
'RYAAY',#瑞安航空(US ADR)
'HMOP',#Hartford Municipal Opportunitie
'RAVI',#FlexShares Ready Access Variabl
'PHYL',#PGIM Active High Yield Bond ETF
'DTEC',#ALPS Disruptive Technologies ET
'WUGI',#AXS Esoterica NextG Economy ETF
'TEAM',#Atlassian Corp-A
'MNA',#IQ Merger Arbitrage ETF
'GDMA',#Gadsden Dynamic Multi-Asset ETF
'BOX',#Box Inc-A
'PFF',#美国优先股ETF-iShares
'NVS',#诺华制药
'MAKX',#ProShares S&P Kensho Smart Fact
'DMAR',#FT Cboe Vest U.S. Equity Deep B
'ESGE',#iShares ESG MSCI EM ETF
'FTSM',#First Trust Enhanced Short Matu
'FCFS',#第一富金融服务
'MBNE',#SPDR Nuveen Municipal Bond ESG
'BAM',#布鲁克菲尔德资产管理
'UUP',#做多美元ETF-Powershares
'SAIC',#Science Applications Internatio
'EUDG',#WisdomTree Europe Quality Divid
'MTBCP',#CareCloud Inc Series A Pfd
'PFC',#第一金融
'WFC_L',#Wells Fargo & Co Series L Pfd
'OBND',#SPDR Loomis Sayles Opportunisti
'MS_P',#Morgan Stanley Series P Pfd
'MSFD',#Direxion Daily MSFT Bear 1X Sha
'LQDI',#iShares Inflation Hedged Corpor
'QMN',#IQ Hedge Market Neutral Tracker
'MS_F',#Morgan Stanley Series F Pfd
'IBML',#iShares iBonds Dec 2023 Term Mu
'CUBI_F',#Customers Bancorp Inc Series F
'IBMP',#iShares iBonds Dec 2027 Term Mu
'C_K',#Citigroup Inc Series K Pfd
'TANNL',#TravelCenters of America Inc No
'POWWP',#AMMO Inc Pfd
'UCBIO',#United Community Banks Inc Seri
'INTA',#Intapp Inc
'IBTD',#iShares iBonds Dec 2023 Term Tr
'ROMO',#Strategy Shares Newfound/ReSolv
'PBTP',#Invesco PureBeta 0-5 Yr US TIPS
'BFTR',#BlackRock Future Innovators ETF
'EAOM',#iShares ESG Aware Moderate Allo
'MMIT',#IQ MacKay Municipal Intermediat
'SCHO',#Schwab Short-Term U.S. Treasury
'SLQD',#iShares 0-5 Year Investment Gra
'MMIN',#IQ MacKay Municipal Insured ETF
'IBTE',#iShares iBonds Dec 2024 Term Tr
'ULTR',#IQ Ultra Short Duration ETF
'IYH',#iShares U.S. Healthcare ETF
'LDUR',#PIMCO Enhanced Low Duration Act
'WINC',#Western Asset Short Duration In
'INMU',#BlackRock Intermediate Muni Inc
'ATLO',#艾姆斯银行控股
'SEIX',#Virtus Seix Senior Loan ETF
'ISHG',#iShares 1-3 Year International
'COLL',#Collegium Pharmaceutical Inc
'AVMU',#Avantis Core Municipal Fixed In
'EJUL',#Innovator Emerging Markets Powe
'RIGS',#RiverFront Strategic Income Fun
'TTD',#The Trade Desk Inc-A
'IBDU',#iShares iBonds Dec 2029 Term Co
'DFNV',#Donoghue Forlines Risk Managed
'AMH_G',#American Homes 4 Rent Series G
'REW',#ProShares UltraShort Technology
'DFAE',#Dimensional Emerging Core Equit
'JCI',#江森自控
'GEN',#Gen Digital Inc
'HYMU',#BlackRock High Yield Muni Incom
'PICB',#Invesco International Corporate
'BSCN',#Invesco BulletShares 2023 Corpo
'BSMV',#Invesco BulletShares 2031 Munic
'BSCO',#Invesco BulletShares 2024 Corpo
'MBSD',#FlexShares Disciplined Duration
'SHY',#1-3年国债ETF-iShares
'CARY',#Angel Oak Income ETF
'BSCP',#Invesco BulletShares 2025 Corpo
'PCG_A',#Pacific Gas and Electric Co Pfd
'FPXE',#First Trust IPOX Europe Equity
'SPB',#Spectrum Brands Holdings Inc
'BCDF',#Horizon Kinetics Blockchain Dev
'DELL',#戴尔科技
'UFO',#Procure Space ETF
'INTL',#Main International ETF
'AU',#AngloGold Ashanti Ltd ADR
'ASAI',#Sendas Distribuidora SA ADR
'FPXI',#First Trust International Equit
'VGSH',#Vanguard Short-Term Treasury ET
'AFGE',#American Financial Group Inc No
'PGHY',#Invesco Global Short Term High
'BML_H',#Bank of America Corp Series 2 P
'HTAB',#Hartford Schroders Tax-Aware Bo
'DFP',#Flaherty & Crumrine Dynamic Pre
'GLDB',#Strategy Shares Gold-Hedged Bon
'DTB',#DTE Energy Co Series G Debentur
'QAT',#iShares MSCI Qatar ETF
'AGM_G',#Federal Agricultural Mortgage C
'PQDI',#Principal Spectrum Tax-Advantag
'IGV',#北美软件ETF-iShares
'WST',#西氏医药服务
'PFFA',#Virtus InfraCap U.S. Preferred
'BCBP',#BCB银行
'SOJE',#The Southern Co Series 2020C No
'INFY',#印孚瑟斯
'FTSD',#Franklin Short Duration U.S. Go
'PLOW',#Douglas Dynamics Inc
'SNCRL',#Synchronoss Technologies Note
'SPSK',#SP Funds Dow Jones Global Sukuk
'MUB',#美国市政债ETF-iShares
'VMW',#威睿
'EWV',#ProShares UltraShort MSCI Japan
'KMLM',#KFA Mount Lucas Index Strategy
'PSA_M',#Public Storage Series M Pfd
'IZRL',#ARK Israel Innovative Technolog
'BRLN',#BlackRock Floating Rate Loan ET
'USD',#ProShares Ultra Semiconductors
'FPE',#First Trust Preferred Securitie
'JMST',#JPMorgan Ultra-Short Municipal
'BNL',#Broadstone Net Lease Inc
'RAYC',#Rayliant Quantamental China Equ
'BIP_A',#布鲁克菲尔德公共建设(优先股)
'ARCM',#Arrow Reserve Capital Managemen
'SMMU',#Short Term Municipal Bond Activ
'PSA_N',#Public Storage Series N Pfd
'NTCT',#网侦系统
'REZI',#Resideo Technologies Inc
'TIME',#Clockwise Capital Innovation ET
'STOR',#STORE Capital Corp
'CNXN',#PC Connection Inc
'VBF',#Invesco Bond Fund
'SHM',#SPDR Nuveen Bloomberg Short Ter
'VITL',#Vital Farms Inc
'GSIG',#Goldman Sachs Access Investment
'EFIX',#First Trust TCW Emerging Market
'CFCV',#ClearBridge Focus Value ESG ETF
'FDN',#互联网指数ETF-First Trust
'JPIE',#JPMorgan Income ETF
'MMC',#威达信
'TTMI',#TTM科技
'SPSB',#SPDR Portfolio Short Term Corpo
'AGZD',#WisdomTree Interest Rate Hedged
'SPTS',#SPDR Portfolio Short Term Treas
'SOLR',#SmartETFs Sustainable Energy II
'SIFI',#Harbor Scientific Alpha Income
'MOH',#Molina Healthcare Inc
'TDS_V',#Telephone and Data Systems Inc
'MID',#American Century Mid Cap Growth
'HBB',#Hamilton Beach Brands Holding C
'EIC',#Eagle Point Income Co Inc
'XYL',#赛莱默
'CLFD',#克利尔菲尔德通讯
'ERO',#Ero Copper Corp
'TGIF',#SoFi Weekly Income ETF
'BIPC',#Brookfield Infrastructure Corp-
'FMNY',#First Trust New York Municipal
'ZM',#Zoom Video通讯
'UFEB',#Innovator U.S. Equity Ultra Buf
'QTEC',#First Trust NASDAQ-100- Technol
'DRSK',#Aptus Defined Risk ETF
'MGYR',#Magyar Bancorp Inc
'BYOB',#SoFi Be Your Own Boss ETF
'LITE',#Lumentum Holdings Inc
'CSR_C',#Centerspace Series C Pfd
'WSBCP',#WesBanco Inc Series A Pfd
'TRINL',#Trinity Capital Inc Note
'BSMN',#Invesco BulletShares 2023 Munic
'RYH',#Invesco S&P 500 Equal Weight He
'COWNL',#Cowen Inc Notes
'ARP',#PMV Adaptive Risk Parity ETF
'WFC_R',#Wells Fargo & Co Series R Pfd
'RCA',#Ready Capital Corp Notes
'IGSB',#iShares Short-Term Corporate Bo
'GSST',#Goldman Sachs Access Ultra Shor
'XTRE',#BondBloxx Bloomberg Three Year
'VTEB',#Vanguard Tax-Exempt Bond ETF
'MPV',#Barings Participation Investors
'BSMO',#Invesco BulletShares 2024 Munic
'UTWO',#US Treasury 2 Year Note ETF
'STAR_G',#iStar Inc Series G Pfd
'IBDP',#iShares iBonds Dec 2024 Term Co
'TNP_F',#Tsakos Energy Navigation Ltd Se
'AJXA',#Great Ajax Corp Notes
'ERSX',#ERShares Non-US Small Cap ETF
'BSDE',#Invesco BulletShares 2024 USD E
'RVNU',#Xtrackers Municipal Infrastruct
'CVLG',#契诺物流
'LMBS',#First Trust Low Duration Opport
'SNV_D',#Synovus Financial Corp Series D
'RADI',#Radius Global Infrastructure In
'SCHJ',#Schwab 1-5 Year Corporate Bond
'BKSB',#BNY Mellon Short Duration Corpo
'SFIG',#WisdomTree U.S. Short-Term Corp
'ISTB',#iShares Core 1-5 Year USD Bond
'BSMS',#Invesco BulletShares 2028 Munic
'JCPI',#JPMorgan Inflation Managed Bond
'EMSG',#Xtrackers MSCI Emerging Markets
'FMHI',#First Trust Municipal High Inco
'BSMT',#Invesco BulletShares 2029 Munic
'NUSA',#Nuveen Enhanced Yield 1-5 Year
'PJP',#Invesco Dynamic Pharmaceuticals
'BWX',#国际主权债ETF-SPDR
'FSLR',#第一太阳能
'HTRB',#Hartford Total Return Bond ETF
'NEA',#Nuveen AMT-Free Quality Municip
'EMF',#Templeton Emerging Markets Fund
'CAJ',#佳能
'MPA',#BlackRock MuniYield Pennsylvani
'COGT',#Cogent Biosciences Inc
'FEEM',#FlexShares ESG & Climate Emergi
'OVM',#Overlay Shares Municipal Bond E
'ASND',#Ascendis Pharma AS ADR
'OVT',#Overlay Shares Short Term Bond
'XMPT',#VanEck CEF Muni Income ETF
'BKEM',#BNY Mellon Emerging Markets Equ
'NMT',#Nuveen Massachusetts Quality Mu
'IBDV',#iShares iBonds Dec 2030 Term Co
'ESSA',#萨万通金控
'SPC',#CrossingBridge Pre-Merger SPAC
'LRGE',#ClearBridge Large Cap Growth ES
'DBMF',#iMGP DBi Managed Futures Strate
'PSCW',#Pacer Swan SOS Conservative (Ap
'RBCAA',#Republic Bancorp Inc-A
'VMCAU',#Valuence Merger Corp I Unit Con
'WIP',#国际抗通胀债ETF-SPDR
'ESAC',#ESGEN Acquisition Corp-A
'AXS_E',#AXIS Capital Holdings Ltd Serie
'TX',#特尔尼翁钢铁
'CION',#CION Investment Corp
'LATG',#LatAmGrowth SPAC-A
'HZNP',#Horizon Therapeutics plc
'RRAC',#Rigel Resource Acquisition Corp
'HAIAU',#Healthcare AI Acquisition Corp
'SCUA',#Sculptor Acquisition Corp I-A
'CCTS',#Cactus Acquisition Corp 1 Ltd-A
'SVNA',#7 Acquisition Corp-A
'CGEM',#Cullinan Oncology Inc
'INKA',#KludeIn I Acquisition Corp-A
'FOXF',#Fox Factory Holding Corp
'MTVC',#Motive Capital Corp II-A
'EVGR',#Evergreen Corp-A
'SKGRU',#SK Growth Opportunities Corp Un
'LGTO',#Legato Merger Corp II
'RAMMU',#Aries I Acquisition Corp Unit C
'AMWD',#美国伍德马克
'CXAC',#C5 Acquisition Corp-A
'FLFV',#Feutune Light Acquisition Corp-
'FIAC',#Focus Impact Acquisition Corp-A
'ARTE',#Artemis Strategic Investment Co
'IRM',#铁山
'GSQB_U',#G Squared Ascend II Inc Unit Co
'ADER',#26 Capital Acquisition Corp-A
'SLAMU',#Slam Corp Unit Cons of 1 CL A +
'BMAC_U',#Black Mountain Acquisition Corp
'NRACU',#Noble Rock Acquisition Corp Uni
'FACT',#Freedom Acquisition I Corp-A
'DWSH',#AdvisorShares Dorsey Wright Sho
'MSDAU',#MSD Acquisition Corp Unit Cons
'FTEV',#FinTech Evolution Acquisition G
'AAC',#Ares Acquisition Corp-A
'HSPOU',#Horizon Space Acquisition I Cor
'TIOA',#Tio Tech A-A
'PFDR',#Pathfinder Acquisition Corp-A
'MDH',#MDH Acquisition Corp-A
'HUGS',#USHG Acquisition Corp-A
'GFGF',#Guru Favorite Stocks ETF
'PSI',#Invesco Dynamic Semiconductors
'MITA',#Coliseum Acquisition Corp-A
'SKYA',#Skydeck Acquisition Corp-A
'FLME',#Flame Acquisition Corp-A
'CLAA_U',#Colonnade Acquisition Corp II U
'BHAC',#Crixus BH3 Acquisition Co-A
'SWSSU',#Springwater Special Situations
'IGIB',#iShares Intermediate-Term Corpo
'HUGS_U',#USHG Acquisition Corp Unit Cons
'TCOA',#Trajectory Alpha Acquisition Co
'FSNB',#Fusion Acquisition Corp II-A
'TWCBU',#Bilander Acquisition Corp Unit
'FTPA',#FTAC Parnassus Acquisition Corp
'TETC',#Tech and Energy Transition Corp
'BGSX',#Build Acquisition Corp-A
'ANZU',#Anzu Special Acquisition Corp I
'MET_F',#MetLife Inc Series F Pfd
'SCAQ',#Stratim Cloud Acquisition Corp-
'MIT',#Mason Industrial Technology Inc
'ANZUU',#Anzu Special Acquisition Corp I
'PSPC',#Post Holdings Partnering Corp-A
'CVII',#Churchill Capital Corp VII-A
'CCVI',#Churchill Capital Corp VI-A
'XTWO',#BondBloxx Bloomberg Two Year Ta
'FLDR',#Fidelity Low Duration Bond Fact
'CCVI_U',#Churchill Capital Corp VI Unit
'SOXS',#Direxion Daily Semiconductor Be
'CNDA',#Concord Acquisition Corp II-A
'HZON',#Horizon Acquisition Corp II-A
'CPAA',#Conyers Park III Acquisition Co
'BSCS',#Invesco BulletShares 2028 Corpo
'ALCC',#AltC Acquisition Corp-A
'ARBG',#Aequi Acquisition Corp-A
'YTPG',#TPG Pace Beneficial II Corp-A
'SOXL',#三倍做多半导体ETF-Direxion
'PSA_J',#Public Storage Series J Pfd
'LAUR',#Laureate Education Inc-A
'CACI',#CACI国际
'EEMS',#iShares MSCI Emerging Markets S
'ABBV',#艾伯维
'AOM',#iShares Core Moderate Allocatio
'NIWM',#NightShares 2000 ETF
'BSCR',#Invesco BulletShares 2027 Corpo
'BSCQ',#Invesco BulletShares 2026 Corpo
'BBSA',#JPMorgan BetaBuilders 1-5 Year
'BSV',#短期国债指数ETF-Vanguard
'KMPB',#Kemper Corp Debentures
'SHAG',#WisdomTree Yield Enhanced U.S.
'GVI',#iShares Intermediate Government
'DFSE',#Dimensional Emerging Markets Su
'SKOR',#FlexShares Credit-Scored US Cor
'BTA',#BlackRock Long-Term Municipal A
'TIPX',#SPDR Bloomberg 1-10 Year TIPS E
'FBRT_E',#Franklin BSP Realty Trust Inc S
'CLNR',#IQ Cleaner Transport ETF
'EPRF',#Innovator S&P Investment Grade
'AVSF',#Avantis Short-Term Fixed Income
'KORP',#American Century Diversified Co
'ESCR',#Xtrackers Bloomberg US Investme
'BHE',#Benchmark Electronics Inc
'ENX',#Eaton Vance New York Municipal
'MINC',#AdvisorShares Newfleet Multi-se
'ALEC',#Alector Inc
'CCCS',#CCC Intelligent Solutions Holdi
'CGMU',#Capital Group Municipal Income
'ONL',#Orion Office REIT Inc
'NYF',#iShares New York Muni Bond ETF
'TWIO',#Trajan Wealth Income Opportunit
'VCIT',#中期公司债指数ETF-Vanguard
'LDEM',#iShares ESG MSCI EM Leaders ETF
'FDS',#辉盛研究系统
'SJIV',#South Jersey Industries Inc Cor
'BNGE',#First Trust S-Network Streaming
'VHT',#医疗指数ETF-Vanguard
'CHSCL',#CHS Inc Class B Series 4 Pfd
'CLF',#克利夫兰克里夫
'SMB',#VanEck ETF Trust VanEck Short M
'RRBI',#Red River Bancshares Inc
'PSK',#SPDR Wells Fargo Preferred Stoc
'ONEM',#1Life Healthcare Inc
'AVGO',#博通
'PMT_C',#PennyMac Mortgage Investment Tr
'OAIA',#Teucrium AiLA Long-Short Agricu
'RILYL',#B. Riley Financial Inc Series B
'NREF',#NexPoint Real Estate Finance In
'JJU',#铝ETN-iPath
'EWQ',#法国ETF-iShares MSCI
'BLKC',#Invesco Alerian Galaxy Blockcha
'AGZ',#iShares Agency Bond ETF
'SQM',#智利矿业化工
'EOT',#Eaton Vance National Municipal
'STT_D',#State Street Corp Series D Pfd
'CLVT',#Clarivate Plc
'NNI',#Nelnet Inc-A
'IBDQ',#iShares iBonds Dec 2025 Term Co
'PHDG',#Invesco S&P 500 Downside Hedged
'XNTK',#SPDR NYSE Technology ETF
'QQQN',#VictoryShares Nasdaq Next 50 ET
'GBAB',#Guggenheim Taxable Municipal Ma
'SPIB',#SPDR Portfolio Intermediate Ter
'FHLC',#Fidelity MSCI Health Care Index
'CFG_D',#Citizens Financial Group Inc Se
'GLOP_C',#GasLog Partners LP Series C Pfd
'IIGD',#Invesco Investment Grade Defens
'NTSI',#WisdomTree International Effici
'SUSB',#iShares ESG 1-5 Year USD Corpor
'AIC',#Arlington Asset Investment Corp
'GF',#The New Germany Fund
'TDTF',#FlexShares iBoxx 5 Year Target
'TNP_D',#Tsakos Energy Navigation Ltd Se
'GUT_C',#The Gabelli Utility Trust Serie
'HNNAZ',#Hennessy Advisors Inc Notes
'SKYW',#西空航空
'IBTF',#iShares iBonds Dec 2025 Term Tr
'FLMB',#Franklin Municipal Green Bond E
'ALL_G',#The Allstate Corp Series G Pfd
'IEMG',#iShares Core MSCI Emerging Mark
'RISN',#Inspire Tactical Balanced ETF
'VNO_M',#Vornado Realty Trust Series M P
'JSCP',#JPMorgan Short Duration Core Pl
'VABS',#Virtus Newfleet ABS/MBS ETF
'EEM',#新兴市场ETF-iShares MSCI
'MCO',#穆迪
'SHAK',#Shake Shack Inc-A
'SNV_E',#Synovus Financial Corp Series E
'EIDO',#iShares MSCI Indonesia ETF
'DT',#Dynatrace Inc
'AIMC',#奥创控股
'OXLCN',#Oxford Lane Capital Corp Series
'BRKR',#布鲁克
'HISF',#First Trust High Income Strateg
'MUNI',#PIMCO Intermediate Municipal Bo
'PSQ',#做空纳斯达克100ETF-ProShares
'CBON',#人民币债券ETF-VanEckVectors华夏
'FCLD',#Fidelity Cloud Computing ETF
'KALL',#KraneShares MSCI All China Inde
'MTB',#美国制商银行
'GMAB',#Genmab A/S ADR
'IEX',#IDEX Corp
'MUSI',#American Century Multisector In
'EEMX',#SPDR MSCI Emerging Markets Fuel
'CXH',#MFS Investment Grade Municipal
'KARB',#Carbon Strategy ETF
'SRI',#石通瑞吉
'AIA',#iShares Asia 50 ETF
'CACG',#ClearBridge All Cap Growth ETF
'ULTA',#ULTA美妆
'ALLE',#安朗杰
'FIBR',#iShares Edge U.S. Fixed Income
'UEIC',#Universal Electronics Inc
'ICVT',#iShares Convertible Bond ETF
'MIDD',#The Middleby Corp
'QPFF',#American Century Quality Prefer
'SPAX',#Robinson Alternative Yield Pre-
'PROV',#Provident Financial Holdings In
'PNT',#POINT Biopharma Global Inc
'CCB',#Coastal Financial Corp
'AZN',#阿斯利康(US ADR)
'FT',#Franklin Universal Trust
'ITB',#美国家园建设ETF-iShares
'BIGZ',#BlackRock Innovation and Growth
'BAC_N',#Bank of America Corp Series LL
'LCFY',#Locafy Ltd
'PWOD',#Penns Woods Bancorp Inc
'DFEB',#FT Cboe Vest U.S. Equity Deep B
'GNL_B',#Global Net Lease Inc Series B P
'NKSH',#National Bankshares Inc
'INGN',#Inogen Inc
'PCRX',#Pacira BioSciences Inc
'THQ',#Tekla Healthcare Opportunities
'FLKR',#Franklin FTSE South Korea ETF
'PSCT',#小型信息科技股ETF
'GSEE',#Goldman Sachs MarketBeta Emergi
'USDU',#做多美元ETF-WisdomTree
'CCAP',#Crescent Capital BDC Inc
'CONN',#科恩
'BAC_S',#Bank of America Corp Series SS
'RULE',#Adaptive Core ETF
'FLIA',#Franklin International Aggregat
'LPRO',#Open Lending Corp-A
'FKU',#First Trust United Kingdom Alph
'COF_I',#Capital One Financial Corp Seri
'IART',#英特格拉生命科学
'SCHI',#Schwab 5-10 Year Corporate Bond
'PRLB',#Proto Labs Inc
'ALL_B',#The Allstate Corp Debentures
'MSTB',#LHA Market State Tactical Beta
'QGEN',#快而精医药
'HSTM',#健康流科技
'HT_D',#HT基金(优先股)
'UHS',#Universal Health Services Inc-B
'IBDT',#iShares iBonds Dec 2028 Term Co
'WDC',#西部数据
'FSEC',#Fidelity Investment Grade Secur
'QDEC',#FT Cboe Vest Nasdaq-100 Buffer
'PIFI',#ClearShares Piton Intermediate
'NICK',#Nicholas Financial Inc
'OPRA',#欧朋浏览器
'TBC',#AT&T Inc Notes
'ROBT',#First Trust Nasdaq Artificial I
'XT',#iShares Exponential Technologie
'NXDT',#NexPoint Diversified Real Estat
'EVA',#Enviva Inc
'FAAR',#First Trust Alternative Absolut
'PHAR',#Pharming Group NV ADR
'EBTC',#Enterprise Bancorp Inc
'TOST',#Toast Inc-A
'HCA',#HCA Healthcare Inc
'AAXJ',#亚洲除日本ETF-iShares MSCI
'DIAL',#Columbia Diversified Fixed Inco
'CCSO',#Carbon Collective Climate Solut
'CHIM',#中国原材料指数ETF-Global X
'HRZN',#Horizon Technology Finance Corp
'WFC_C',#Wells Fargo & Co Series CC Pfd
'GRNB',#VanEck Green Bond ETF
'BULD',#Pacer BlueStar Engineering the
'PFIG',#Invesco Fundamental Investment
'PBFS',#Pioneer Bancorp Inc
'SPBO',#SPDR Portfolio Corporate Bond E
'IIGV',#Invesco Investment Grade Value
'IESC',#IES Holdings Inc
'SONO',#搜诺思
'RNR',#RenaissanceRe Holdings Ltd
'SMI',#VanEck HIP Sustainable Muni ETF
'CGCP',#Capital Group Core Plus Income
'VERS',#ProShares Metaverse ETF
'TSLH',#Innovator Hedged TSLA Strategy
'RBC',#RBC轴承
'NBW',#Neuberger Berman California Mun
'MPAY',#Akros Monthly Payout ETF
'PUNK',#Subversive Metaverse ETF
'APD',#空气化工
'VIVO',#美鼎生物
'ACHC',#阿卡迪亚医疗保健
'JRVR',#James River Group Holdings Ltd
'HDAW',#Xtrackers MSCI All World ex US
'IEI',#3-7年ETF-iShares
'JHPI',#John Hancock Preferred Income E
'USB_Q',#US Bancorp Series L Pfd
'GHY',#PGIM Global High Yield Fund
'PSA_Q',#Public Storage Series Q Pfd
'BSCV',#Invesco BulletShares 2031 Corpo
'OVBC',#俄亥俄河谷银行
'CRWS',#Crown Crafts制衣
'FJP',#First Trust Japan AlphaDEX Fund
'FDIG',#Fidelity Crypto Industry and Di
'ARCKU',#Arbor Rapha Capital Bioholdings
'GLPG',#Galapagos NV ADR
'NCZ_A',#Virtus Convertible & Income Fun
'GCLN',#Goldman Sachs Bloomberg Clean E
'JIB',#Janus Henderson Sustainable & I
'EDAP',#EDAP TMS SA ADR
'AGNG',#Global X Aging Population ETF
'CMTG',#Claros Mortgage Trust Inc
'AFB',#AllianceBernstein National Muni
'ALC',#Alcon Inc
'CDNS',#铿腾电子
'GNE_A',#Genie Energy Ltd Pfd-A
'NXDT_A',#NexPoint Diversified Real Estat
'PONO',#Pono Capital Corp-A
'SKE',#Skeena Resources Ltd
'SEMI',#Columbia Seligman Semiconductor
'OMGA',#Omega Therapeutics Inc
'IVCB',#Investcorp Europe Acquisition C
'EPOL',#波兰ETF-iShares MSCI
'GRND',#Grindr Inc
'TXN',#德州仪器
'TETE',#Technology & Telecommunication
'BHFAM',#Brighthouse Financial Inc Serie
'PSTX',#Poseida Therapeutics Inc
'AEF',#abrdn Emerging Markets Equity I
'ASLE',#AerSale Corp
'BSX',#波士顿科学
'RONI',#Rice Acquisition Corp II-A
'SHAP',#Spree Acquisition Corp 1 Ltd-A
'LGVCU',#LAMF Global Ventures Corp I Uni
'FINV',#信也科技
'FEXD',#Fintech Ecosystem Development C
'PRBM',#Parabellum Acquisition Corp-A
'ROC',#ROC Energy Acquisition Corp
'IMAQ',#International Media Acquisition
'TFI',#SPDR Nuveen Bloomberg Municipal
'EML',#The Eastern Co
'AKYA',#Akoya Biosciences Inc
'BNJ',#Brookfield Finance Inc Notes
'TENK',#TenX Keane Acquisition
'OAEM',#OneAscent Emerging Markets ETF
'NAAC',#North Atlantic Acquisition Corp
'LHCG',#LHC Group Inc
'XM',#Qualtrics国际
'MCAF',#Mountain Crest Acquisition Corp
'JWSM',#Ares Acquisition Corp-A
'GFGDU',#The Growth for Good Acquisition
'AIMAU',#Aimfinity Investment Corp I Uni
'GPRO',#GoPro Inc-A
'DIN',#Dine Brands Global Inc
'MQT',#BlackRock MuniYield Quality Fun
'DMYS_U',#dMY Technology Group Inc VI Uni
'ACLS',#Axcelis Technologies Inc
'IGACU',#IG Acquisition Corp Unit Cons o
'SMIH',#Summit Healthcare Acquisition C
'DHHCU',#DiamondHead Holdings Corp Unit
'SCCE',#Sachem Capital Corp Notes
'NSPY',#NightShares 500 ETF
'GETY',#Getty Images Holdings Inc-A
'FPAC_U',#Far Peak Acquisition Corp Unit
'AGI',#Alamos Gold Inc-A
'GMRE_A',#Global Medical REIT Inc Series
'SLAC',#Social Leverage Acquisition Cor
'BNY',#BlackRock New York Municipal In
'WOR',#Worthington Industries Inc
'JPM_J',#JPMorgan Chase & Co Series GG P
'BTWN',#Bridgetown Holdings Ltd-A
'XDAT',#Franklin Exponential Data ETF
'BOAC_U',#Bluescape Opportunities Acquisi
'KOMP',#SPDR S&P Kensho New Economies C
'PMD',#Psychemedics Corp
'MUE',#BlackRock MuniHoldings Quality
'AMKR',#艾马克技术
'IBDX',#iShares iBonds Dec 2032 Term Co
'SCE_K',#SCE Trust V Preference Securiti
'IVES',#Wedbush ETFMG Global Cloud Tech
'ACV',#Virtus Diversified Income & Con
'WDFC',#WD-40 Co
'THW',#Tekla World Healthcare Fund
'MINO',#PIMCO Municipal Income Opportun
'TLS',#Telos Corp
'MTGP',#WisdomTree Mortgage Plus Bond F
'IBUY',#Amplify Online Retail ETF
'VWO',#新兴市场ETF-Vanguard FTSE
'SEIC',#SEI Investments Co
'BNDW',#Vanguard Total World Bond ETF
'CALX',#Calix Inc
'DCOMP',#Dime Community Bancshares Inc P
'INST',#Instructure Holdings Inc
'AOSL',#阿尔法和欧米伽半导体
'BNDX',#国际全债市指数ETF-Vanguard
'GJR',#STRATS Trust for Procter & Gamb
'DUNE',#Dune Acquisition Corp-A
'TSI',#TCW Strategic Income Fund
'SACH_A',#Sachem Capital Corp Pfd
'IHI',#iShares U.S. Medical Devices ET
'KMB',#金佰利
'IBDS',#iShares iBonds Dec 2027 Term Co
'IBDR',#iShares iBonds Dec 2026 Term Co
'QIPT',#Quipt Home Medical Corp
'MBB',#按揭抵押债ETF-iShares
'SUPN',#Supernus Pharmaceuticals Inc
'SPEM',#SPDR Index Shares Fund SPDR Por
'BNE',#Blue Horizon BNE ETF
'MDEV',#First Trust Indxx Medical Devic
'MCS',#马库斯
'SMBK',#SmartFinancial Inc
'EXTR',#极速网络
'ROBO',#全球机器人自动化ETF-ROBO
'DNL',#WisdomTree Global ex-US Quality
'TK',#Teekay Corp
'JMBS',#Janus Henderson Mortgage-Backed
'FNGD',#MicroSectors FANG Index -3X Inv
'TECB',#iShares U.S. Tech Breakthrough
'WBAT',#WisdomTree Battery Value Chain
'OXLCL',#Oxford Lane Capital Corp Notes
'NGL_B',#NGL Energy Partners LP Class B
'ALX',#亚历山大
'IVOL',#Quadratic Interest Rate Volatil
'GINN',#Goldman Sachs Innovate Equity E
'XPH',#SPDR S&P Pharmaceuticals ETF
'BAC_O',#Bank of America Corp Series NN
'CHIR',#Global X MSCI China Real Estate
'EVNT',#AltShares Event-Driven ETF
'BSCT',#Invesco BulletShares 2029 Corpo
'ROAD',#Construction Partners Inc-A
'CVLT',#康沃系统
'IBTH',#iShares iBonds Dec 2027 Term Tr
'PRM',#Perimeter Solutions SA
'TIP',#抗通胀债ETF-iShares
'DYLD',#LeaderShares Dynamic Yield ETF
'SUP',#Superior Industries Internation
'PTMN',#Portman Ridge Finance Corp
'AFIF',#Anfield Universal Fixed Income
'SPMB',#SPDR Portfolio Mortgage Backed
'MINN',#Mairs & Power Minnesota Municip
'SJR',#肖氏通信
'PBEE',#Invesco PureBeta FTSE Emerging
'MATW',#马修国际
'KKRS',#KKR & Co Inc Notes
'BSMU',#Invesco BulletShares 2030 Munic
'SCHP',#美国抗通胀债ETF-Schwab
'CHGG',#Chegg Inc
'OWNS',#Impact Shares Affordable Housin
'ATCO_H',#Atlas Corp Series H Pfd
'EVM',#Eaton Vance California Municipa
'CARS',#Cars.com
'HYD',#高收益市政债ETF-VanEck Vectors
'DAX',#Global X DAX Germany ETF
'BTT',#BlackRock Municipal 2030 Target
'MS_E',#Morgan Stanley Series E Pfd
'CGSD',#Capital Group Short Duration In
'INDT',#INDUS Realty Trust Inc
'HWBK',#Hawthorn Bancshares Inc
'TRTN_A',#Triton International Ltd Series
'VGIT',#Vanguard Intermediate-Term Trea
'JPM_C',#JPMorgan Chase & Co Series EE P
'DFCF',#Dimensional Core Fixed Income E
'CLBT',#Cellebrite DI Ltd
'IDAT',#iShares Future Cloud 5G and Tec
'ZNH',#南方航空
'SWAR',#Direxion Daily Software Bull 2X
'FBND',#Fidelity Total Bond ETF
'NNY',#Nuveen New York Municipal Value
'DFIP',#Dimensional Inflation-Protected
'AUBAP',#Atlantic Union Bankshares Corp
'HI',#希伦布兰德
'CNOBP',#ConnectOne Bancorp Inc Series A
'PSA_O',#Public Storage Series O Pfd
'MNRO',#Monro Inc
'HYMB',#SPDR Nuveen Bloomberg High Yiel
'BSY',#Bentley Systems Inc-B
'SCRD',#Janus Henderson Sustainable Cor
'TEL',#泰科电子
'GTIP',#Goldman Sachs Access Inflation
'MUST',#Columbia Multi-Sector Municipal
'BSCU',#Invesco BulletShares 2030 Corpo
'IBDW',#iShares iBonds Dec 2031 Term Co
'BSCW',#Invesco BulletShares 2032 Corpo
'OZKAP',#Bank OZK Inc Series A Pfd
'VALT',#ETFMG Sit Ultra Short ETF
'PSMC',#Invesco Conservative Multi-Asse
'ST',#Sensata科技控股
'DOOO',#BRP Inc
'NX',#Quanex Building Products Corp
'STLD',#Steel Dynamics Inc
'BUR',#伯福德资本
'GOLF',#高尔史密斯国际控股
'IBND',#国际公司债ETF-SPDR
'DUKB',#Duke Energy Corp Debentures
'ATKR',#Atkore Inc
'SLG_I',#SL Green Realty Corp Series I P
'KMDA',#Kamada Ltd
'GSK',#葛兰素史克(US)
'BF_B',#百富门-B
'GTO',#Invesco Total Return Bond ETF
'TIPZ',#PIMCO Broad U.S. TIPS Index ETF
'ISHP',#First Trust S-Network E-Commerc
'FCSH',#Federated Hermes Short Duration
'HIBS',#Direxion Daily S&P 500 High Bet
'EMCB',#新兴市场美元公司债-WisdomTree
'GRIN',#Grindrod Shipping Holdings Ltd
'SCHZ',#Schwab US Aggregate Bond ETF
'VMBS',#Vanguard Mortgage-Backed Securi
'BGCP',#BGC Partners Inc-A
'AXL',#美国车桥
'LQDW',#iShares Trust iShares Investmen
'BOND',#PIMCO Active Bond ETF
'SCHR',#Schwab Intermediate-Term U.S. T
'TREX',#Trex Co Inc
'IBTG',#iShares iBonds Dec 2026 Term Tr
'MNTX',#Manitex International Inc
'LSAK',#Lesaka Technologies Inc
'XFIV',#BondBloxx Bloomberg Five Year T
'PDI',#PIMCO Dynamic Income Fund
'EPR_E',#EPR Properties Series E Pfd
'FOR',#福里斯特
'ACEL',#Accel Entertainment Inc-A
'IFN',#The India Fund
'SJB',#做空高收益债ETF-ProShares
'AVIG',#Avantis Core Fixed Income ETF
'TECH',#Bio-Techne Corp
'GDV_K',#The Gabelli Dividend & Income T
'TWO_C',#Two Harbors Investment Corp Ser
'TUSK',#Mammoth Energy Services Inc
'BRW',#Saba Capital Income & Opportuni
'CWEN_A',#Clearway Energy Inc-A
'VRP',#Invesco Variable Rate Preferred
'DDD',#3D系统
'GBF',#iShares Government/Credit Bond
'NATH',#Nathan's Famous Inc
'CWCO',#Consolidated Water Co Ltd-A
'MIY',#BlackRock MuniYield Michigan Qu
'ETY',#Eaton Vance Tax-Managed Diversi
'BOSS',#Global X Funds Global X Founder
'QLVE',#FlexShares Emerging Markets Qua
'IGEB',#iShares Edge Investment Grade E
'JHS',#John Hancock Income Securities
'NOVT',#Novanta Inc
'TARS',#Tarsus Pharmaceuticals Inc
'CTO',#CTO Realty Growth Inc
'MYI',#BlackRock MuniYield Quality Fun
'BGB',#Blackstone/GSO Strategic Credit
'CNXC',#Concentrix Corp
'BFZ',#BlackRock California Municipal
'HIG_G',#The Hartford Financial Services
'JEWL',#Adamas One Corp
'THC',#泰尼特保健
'GSL_B',#Global Ship Lease Inc Series B
'JHMB',#John Hancock Mortgage-Backed Se
'CLAR',#Clarus Corp
'ITGR',#Integer Holdings Corp
'AAPL',#苹果
'ONLN',#ProShares Online Retail ETF
'INN_E',#Summit Hotel Properties Inc Ser
'PRA',#ProAssurance Corp
'MSVX',#LHA Market State Alpha Seeker E
'QQQA',#Nasdaq-100 Dorsey Wright Moment
'CAPR',#Capricor Therapeutics Inc
'EMHY',#iShares J.P. Morgan EM High Yie
'SPCX',#The SPAC and New Issue ETF
'BAC_L',#Bank of America Corp Series L P
'ETO',#Eaton Vance Tax-Advantaged Glob
'ESGB',#IQ MacKay ESG Core Plus Bond ET
'NMZ',#Nuveen Municipal High Income Op
'IUSB',#iShares Core Total USD Bond Mar
'IG',#Principal Investment Grade Corp
'PTRB',#PGIM Total Return Bond ETF
'MVT',#BlackRock MuniVest Fund II
'AVNW',#阿维亚网络
'HCRB',#Hartford Core Bond ETF
'NUAG',#Nuveen Enhanced Yield U.S. Aggr
'BLE',#BlackRock Municipal Income Trus
'EOLS',#Evolus Inc
'THAC',#Thrive Acquisition Corp-A
'SACH',#Sachem Capital Corp
'IVCA',#Investcorp India Acquisition Co
'PYN',#PIMCO New York Municipal Income
'LEGR',#First Trust Indxx Innovative Tr
'FXF',#瑞士法郎ETF-CurrencyShares
'JGGC',#Jaguar Global Growth Corp I-A
'EVE',#EVe Mobility Acquisition Corp-A
'NUW',#Nuveen AMT-Free Municipal Value
'PRLHU',#Pearl Holdings Acquisition Corp
'NTRSO',#Northern Trust Corp Series E Pf
'MCH',#Matthews China Active ETF
'CLVT_A',#Clarivate Plc Series A Pfd
'PCG_E',#Pacific Gas and Electric Co Ser
'FTIIU',#FutureTech II Acquisition Corp
'FLAX',#Franklin FTSE Asia ex Japan ETF
'EMGF',#iShares Edge MSCI Multifactor E
'GNMA',#iShares GNMA Bond ETF
'WWAC',#Worldwide Webb Acquisition Corp
'GLLIU',#Globalink Investment Inc Unit C
'CWS',#AdvisorShares Focused Equity ET
'BYN',#Banyan Acquisition Corp-A
'FCNCO',#First Citizens BancShares Inc S
'MYOV',#Myovant Sciences Ltd
'VRRM',#Verra Mobility Corp-A
'FINMU',#Marlin Technology Corp Unit Con
'RAYE',#Rayliant Quantamental Emerging
'CFIV',#CF Acquisition Corp IV-A
'SPKBU',#Silver Spike Acquisition Corp I
'MONCU',#Monument Circle Acquisition Cor
'EXK',#Endeavour Silver Corp
'IFV',#First Trust Dorsey Wright Inter
'FTEV_U',#FinTech Evolution Acquisition G
'SOJD',#The Southern Co Series 2020A No
'GAQ_U',#Generation Asia I Acquisition L
'FMB',#First Trust Managed Municipal E
'EAC',#Edify Acquisition Corp-A
'SLVR',#SILVERspac Inc-A
'VTN',#Invesco Trust for Investment Gr
'SNEX',#StoneX Group Inc
'CNRG',#SPDR S&P Kensho Clean Power ETF
'EFZ',#ProShares Short MSCI EAFE
'XEMD',#BondBloxx JP Morgan USD Emergin
'AQU',#Aquaron Acquisition Corp
'MDH_U',#MDH Acquisition Corp Unit Cons
'KINZ',#KINS Technology Group Inc-A
'IMTB',#iShares Core 5-10 Year USD Bond
'FRC_M',#First Republic Bank Series M Pf
'MS',#摩根士丹利
'JAGG',#JPMorgan U.S. Aggregate Bond ET
'CORS',#Corsair Partnering Corp-A
'PEPLU',#PepperLime Health Acquisition C
'AL_A',#Air Lease Corp Series A Pfd
'IBTK',#iShares iBonds Dec 2030 Term Tr
'ANIP',#ANI Pharmaceuticals Inc
'APMI',#AxonPrime Infrastructure Acquis
'IAC',#IAC Inc
'VPV',#Invesco Pennsylvania Value Muni
'GHIX',#Gores Holdings IX Inc-A
'LMAT',#勒梅特微管医疗
'BIV',#中期债券指数ETF-Vanguard
'OACP',#OneAscent Core Plus Bond ETF
'EXD',#Eaton Vance Tax-Managed Buy-Wri
'CORP',#PIMCO Investment Grade Corporat
'SSIC',#Silver Spike Investment Corp
'RVPH',#Reviva Pharmaceuticals Holdings
'ISRA',#VanEck Israel ETF
'LQD',#投资级公司债ETF-iShares
'SPXB',#ProShares S&P 500 Bond ETF
'MRND',#IQ U.S. Mid Cap R&D Leaders ETF
'HFRO_A',#Highland Income Fund Series A P
'VCEB',#Vanguard ESG U.S. Corporate Bon
'IAGG',#iShares International Aggregate
'C_N',#Citigroup Capital VIII Trust Pr
'WDI',#Western Asset Diversified Incom
'PFH',#Prudential Financial Inc Notes
'RFCI',#RiverFront Dynamic Core Income
'ASX',#日月光半导体
'PTF',#Invesco DWA Technology Momentum
'BRBR',#BellRing Brands Inc
'SPTI',#SPDR Portfolio Intermediate Ter
'IBTI',#iShares iBonds Dec 2028 Term Tr
'CIVB',#Civista Bancshares Inc
'BND',#全债市指数ETF-Vanguard
'IQI',#Invesco Quality Municipal Incom
'EKAR',#Capital Link Global Green Energ
'OLED',#Universal Display Corp
'PWP',#Perella Weinberg Partners-A
'NUBD',#Nuveen ESG U.S. Aggregate Bond
'CN',#Xtrackers MSCI All China Equity
'STEW',#SRH Total Return Fund, Inc.
'VTC',#Vanguard Total Corporate Bond E
'BNSO',#恒异电子
'WFIG',#WisdomTree U.S. Corporate Bond
'QLTA',#iShares Aaa A Rated Corporate B
'GMRE',#Global Medical REIT Inc
'SSFI',#Day Hagan/Ned Davis Research Sm
'OSEA',#Harbor International Compounder
'IBTJ',#iShares iBonds Dec 2029 Term Tr
'USIG',#iShares Broad USD Investment Gr
'TOTL',#SPDR DoubleLine Total Return Ta
'TCHI',#iShares MSCI China Multisector
'ETSY',#Etsy Inc
'RMPL_',#RiverNorth Capital and Income F
'WFC_A',#Wells Fargo & Co Series AA Pfd
'TACT',#TransAct Technologies Inc
'BGRN',#iShares USD Green Bond ETF
'LDSF',#First Trust Low Duration Strate
'MKTX',#MarketAxess Holdings Inc
'MTRX',#Matrix Service Co
'FXLV',#F45 Training Holdings Inc
'FCUV',#Focus Universal Inc
'BAC_M',#Bank of America Corp Series KK
'FSI',#Flexible Solutions Internationa
'DEED',#First Trust TCW Securitized Plu
'CMC',#美国工商五金
'FLCB',#Franklin U.S. Core Bond ETF
'T_C',#AT&T Inc Series C Pfd
'UBND',#VictoryShares ESG Core Plus Bon
'EUSB',#iShares ESG Advanced Total USD
'APH',#安费诺
'CHWY',#Chewy Inc-A
'FHN_F',#First Horizon Corp Series F Pfd
'DUK_A',#Duke Energy Corp Series A Pfd
'AVDX',#AvidXchange Holdings Inc
'BF_A',#百富门-A
'BKAG',#BNY Mellon Core Bond ETF
'MQ',#Marqeta Inc-A
'GURE',#海湾资源
'BL',#BlackLine Inc
'SPOT',#Spotify Technology SA
'TOL',#托尔兄弟
'RC',#Ready Capital Corp
'EUO',#二倍做空欧元ETF-ProShares
'CHAD',#做空沪深300ETF-Direxion
'XSOE',#WisdomTree Emerging Markets Ex-
'FAM',#First Trust/abrdn Global Opport
'PP',#The Meet Kevin Pricing Power ET
'EAGG',#iShares ESG U.S. Aggregate Bond
'TOTR',#T. Rowe Price Total Return ETF
'SR_A',#Spire Inc Series A Pfd
'XRX',#施乐
'QQQX',#Nuveen NASDAQ 100 Dynamic Overw
'CZNC',#市民北方
'BAC_Q',#Bank of America Corp Series QQ
'ICHR',#Ichor Holdings Ltd
'ALTO',#Alto Ingredients Inc
'FEIG',#FlexShares ESG & Climate Invest
'PSA_I',#Public Storage Series I PFd
'XSD',#SPDR S&P Semiconductor ETF
'RAMP',#LiveRamp Holdings Inc
'EMTL',#SPDR DoubleLine Emerging Market
'AGG',#美国全债市ETF-iShares
'MITT',#AG Mortgage Investment Trust In
'LQDB',#iShares BBB Rated Corporate Bon
'MEDI',#Harbor Health Care ETF
'AGGY',#WisdomTree Yield Enhanced U.S.
'GPMT',#格拉尼特角抵押信托
'SPIP',#SPDR Portfolio TIPS ETF
'LOAN',#曼哈顿大桥投资股份
'FPFD',#Fidelity Preferred Securities &
'EW',#爱德华兹生命科学
'SGFY',#Signify Health Inc-A
'USB_R',#US Bancorp Series M Pfd
'GRN',#iPath Series B Carbon ETN
'HLNE',#Hamilton Lane Inc-A
'NXN',#Nuveen New York Select Tax-Free
'BNDI',#NEOS Enhanced Income Aggregate
'EMCR',#Xtrackers Emerging Markets Carb
'MXL',#MaxLinear Inc
'KTRA',#Kintara Therapeutics Inc
'TBPH',#Theravance Biopharma Inc
'SDEF',#Sound Enhanced Fixed Income ETF
'SUSC',#iShares ESG USD Corporate Bond
'WFC_Y',#Wells Fargo & Co Series Y Pfd
'SPAB',#SPDR Portfolio Aggregate Bond E
'DSM',#BNY Mellon Strategic Municipal
'ILDR',#First Trust Innovation Leaders
'IQM',#Franklin Intelligent Machines E
'QTWO',#Q2 Holdings Inc
'DFFN',#Diffusion Pharmaceuticals Inc
'CHIC',#Global X MSCI China Communicati
'ARKF',#ARK Fintech Innovation ETF
'HRB',#H&R布洛克
'PAB',#PGIM ACTIVE AGGREGATE BOND ETF
'ADFI',#Anfield Dynamic Fixed Income ET
'ZIONO',#Zions Bancorp NA Series G Pfd
'TLRY',#Tilray Brands Inc Class-2
'LFMDP',#LifeMD Inc Series A Pfd
'EFT',#Eaton Vance Floating-Rate Incom
'PFUT',#Putnam Sustainable Future ETF
'IDT',#万威
'OYST',#Oyster Point Pharma Inc
'SAJ',#Saratoga Investment Corp Notes
'SANE',#Subversive Mental Health ETF
'SWAN',#Amplify BlackSwan Growth & Trea
'MNDY',#monday.com Ltd
'ISRG',#直觉外科
'MLAB',#Mesa Laboratories Inc
'FHN_B',#First Horizon Corp Series B Pfd
'EDRY',#EuroDry Ltd
'EBS',#Emergent BioSolutions Inc
'PBND',#Invesco PureBeta US Aggregate B
'WBS_F',#Webster Financial Corp Series F
'USB_S',#US Bancorp Series O Pfd
'SCHW_D',#The Charles Schwab Corp Series
'JCPB',#JPMorgan Core Plus Bond ETF
'IVR_B',#Invesco Mortgage Capital Inc Se
'CISO',#Cerberus Cyber Sentinel Corp
'BAC_B',#Bank of America Corp Series GG
'KESG',#KraneShares MSCI China ESG Lead
'GASS',#斯蒂加斯海运
'HBANM',#Huntington Bancshares Inc Serie
'INNO',#Harbor Disruptive Innovation ET
'DBND',#DoubleLine Opportunistic Bond E
'CRS',#卡朋特科技
'EMBD',#Global X Emerging Markets Bond
'EATV',#VegTech Plant-based Innovation
'NEWTZ',#Newtek Business Services Corp N
'MUC',#BlackRock MuniHoldings Californ
'PSA_G',#Public Storage Series G Pfd
'LEN_B',#莱纳建筑-B
'HURN',#休伦咨询
'LAND',#Gladstone Land Corp
'CSQ',#Calamos Strategic Total Return
'DFSB',#Dimensional Global Sustainabili
'ANAB',#AnaptysBio Inc
'GLOP_B',#GasLog Partners LP Series B Pfd
'CBL',#CBL & Associates Properties Inc
'PINK',#Simplify Health Care ETF
'FXH',#医疗ETF-First Trust AlphaDEX
'GROW',#美国全球投资者
'FLCO',#Franklin Investment Grade Corpo
'EXEL',#伊克力西斯
'FLCH',#Franklin FTSE China ETF
'ESTA',#Establishment Labs
'ENTA',#Enanta Pharmaceuticals Inc
'HYEM',#新兴市场高收益债ETF
'FMN',#Federated Premier Municipal Inc
'FSBD',#Fidelity Sustainable Core Plus
'FLGV',#Franklin U.S. Treasury Bond ETF
'BMEZ',#BlackRock Health Sciences Trust
'JHCB',#John Hancock Corporate Bond ETF
'X',#美国钢铁
'PXQ',#Invesco Dynamic Networking ETF
'OVB',#Overlay Shares Core Bond ETF
'FFTI',#FormulaFolios Tactical Income E
'EEA',#THE European Equity Fund
'AMAT',#应用材料
'KOSS',#高斯电子
'BOCN',#Blue Ocean Acquisition Corp-A
'TRMB',#天宝导航
'NRK',#Nuveen New York AMT-Free Qualit
'CODX',#科代诊断
'MFA_B',#MFA Financial Inc Series B Pfd
'USBF',#iShares USD Bond Factor ETF
'CCTSU',#Cactus Acquisition Corp 1 Ltd U
'UCRD',#VictoryShares ESG Corporate Bon
'GMS',#GMS Inc
'STAR',#iStar Inc
'UITB',#VictoryShares USAA Core Interme
'RMD',#瑞思迈
'RPAY',#Repay Holdings Corp-A
'OMER',#奥麦罗制药
'DSGX',#笛卡尔物流系统集团
'FORG',#ForgeRock Inc-A
'PKBO',#Peak Bio Inc
'MODN',#Model N Inc
'HA',#夏威夷控股
'ERES',#East Resources Acquisition Co-A
'NKE',#耐克
'EMGD',#Simplify Emerging Markets Equit
'RCII',#Rent-A-Center Inc
'MCAG',#Mountain Crest Acquisition Corp
'BMN',#BlackRock 2037 Municipal Target
'SSBK',#Southern States Bancshares Inc
'MARB',#First Trust Merger Arbitrage ET
'JIGB',#JPMorgan Corporate Bond Researc
'NEWP',#New Pacific Metals Corp
'IRVH',#Global X Interest Rate Volatili
'EIM',#Eaton Vance Municipal Bond Fund
'TAGG',#T. Rowe Price QM U.S. Bond ETF
'HOLO',#MicroCloud Hologram Inc
'BFK',#BlackRock Municipal Income Trus
'GIGB',#Goldman Sachs Access Investment
'SIMS',#SPDR S&P Kensho Intelligent Str
'ECC_D',#Eagle Point Credit Co Inc Serie
'BRBS',#Blue Ridge Bankshares Inc
'BXMT',#Blackstone Mortgage Trust Inc
'CLBR',#Colombier Acquisition Corp-A
'PFFD',#Global X U.S. Preferred ETF
'IDX',#印尼指数ETF-VanEck Vectors
'FFNW',#First Financial Northwest Inc
'DCP_B',#DCP Midstream LP Series B Pfd
'ETV',#Eaton Vance Tax-Managed Buy-Wri
'BNDC',#FlexShares Core Select Bond Fun
'RWM',#做空罗素2000ETF-ProShares
'LEXX',#Lexaria Bioscience Corp
'BHFAL',#Brighthouse Financial Inc Deben
'WEYS',#Weyco Group Inc
'TGI',#Triumph Group Inc
'LQIG',#SPDR MarketAxess Investment Gra
'GHM',#Graham Corp
'GAB_K',#The Gabelli Equity Trust Inc Se
'BAC_K',#Bank of America Corp Series HH
'NTSE',#WisdomTree Emerging Markets Eff
'TRFM',#AAM Transformers ETF
'URBN',#Urban Outfitters Inc
'ATLC',#Atlanticus Holdings Corp
'SPFF',#Global X SuperIncome Preferred
'PSA_P',#Public Storage Series P Pfd
'FSR',#Fisker Inc-A
'OGIG',#ALPS O'Shares Global Internet G
'MYNZ',#Mainz Biomed BV
'RITM_B',#Rithm Capital Corp Series B Pfd
'FIGB',#Fidelity Investment Grade Bond
'NBO',#Neuberger Berman New York Munic
'SEDG',#SolarEdge Technologies Inc
'EAT',#布林克国际
'MYFW',#First Western Financial Inc
'MOND',#Mondee Holdings Inc-A
'KVHI',#KVH通信
'MET_E',#MetLife Inc Series E Pfd
'VMO',#Invesco Municipal Opportunity T
'FXY',#日元ETF-CurrencyShares
'CYTO',#Altamira Therapeutics Ltd
'SKX',#斯凯奇
'SZK',#ProShares UltraShort Consumer G
'IMGN',#ImmunoGen Inc
'UPLD',#Upland Software Inc
'CUK',#嘉年华邮轮(US ADR)
'BMBL',#Bumble Inc-A
'BSX_A',#Boston Scientific Corp Series A
'BKN',#BlackRock Investment Quality Mu
'ALL_H',#The Allstate Corp Series H Pfd
'RWT',#Redwood Trust Inc
'EEMA',#iShares MSCI Emerging Markets A
'CMSC',#CMS Energy Corp Notes
'BCV_A',#Bancroft Fund Ltd Series A Pfd
'EBIZ',#Global X E-commerce ETF
'IBD',#Inspire Corporate Bond ETF
'UI',#优倍快
'PML',#PIMCO Municipal Income Fund II
'AVIR',#Atea Pharmaceuticals Inc
'SFST',#Southern First Bancshares Inc
'ELQD',#iShares ESG Advanced Investment
'IBTL',#iShares iBonds Dec 2031 Term Tr
'MQY',#BlackRock MuniYield Quality Fun
'GAINN',#Gladstone Investment Corp Notes
'TUA',#Simplify Short Term Treasury Fu
'GOVT',#美国债ETF-iShares
'ENO',#Entergy New Orleans LLC Bonds
'PGX',#优先股ETF-PowerShares
'CIA',#公民保险
'NMS',#Nuveen Minnesota Quality Munici
'RBND',#SPDR Bloomberg SASB Corporate B
'NXP',#Nuveen Select Tax-Free Income P
'ICLR',#ICON plc
'BKF',#金砖四国ETF-iShares MSCI
'SCE_J',#SCE Trust IV Pfd
'SWI',#SolarWinds Corp
'PL',#Planet Labs PBC-A
'ELSE',#伊莱克森
'BPRN',#普林斯顿银行
'MVF',#BlackRock MuniVest Fund
'NFJ',#Virtus Dividend, Interest & Pre
'VIPS',#唯品会
'PCB',#PCB Bancorp
'LULU',#lululemon athletica inc
'CHSCN',#CHS Inc Class B Series 2 Pfd
'RFMZ',#RiverNorth Flexible Municipal I
'IBIT',#Defiance Daily Short Digitizing
'BWB',#Bridgewater Bancshares Inc
'CNNE',#Cannae Holdings Inc
'MVBF',#MVB Financial Corp
'NGS',#Natural Gas Services Group Inc
'DOG',#做空道指ETF-ProShares
'ENTR',#ERShares Entrepreneur 30 ETF
'NI_B',#NiSource Inc Series B Pfd + Ser
'BITI',#ProShares Short Bitcoin Strateg
'IEF',#7-10年ETF-iShares
'CPZ',#Calamos Long/Short Equity & Dyn
'SPNT_B',#SiriusPoint Ltd Series B Pfd
'VWOB',#新兴市场美元政府债指数ETF
'USB_A',#US Bancorp Series A Pfd
'TINY',#ProShares Nanotechnology ETF
'LEE',#李氏企业
'ECON',#Columbia Emerging Markets Consu
'BHFAO',#Brighthouse Financial Inc Serie
'SCE_L',#Southern California Edison Co S
'HTBK',#Heritage Commerce Corp
'HACK',#网络安全ETF-PureFunds ISE
'FFIU',#UVA Unconstrained Medium-Term F
'GLV',#Clough Global Dividend and Inco
'AURA',#Aura Biosciences Inc
'ETG',#Eaton Vance Tax-Advantaged Glob
'RMT',#Royce Micro-Cap Trust
'PRIF_L',#Priority Income Fund Inc Series
'JPMB',#JPMorgan USD Emerging Markets S
'KPOP',#KPOP and Korean Entertainment E
'LEN',#莱纳建筑-A
'SAP',#思爱普
'VBND',#Vident Core U.S. Bond Strategy
'NL',#NL Industries Inc
'STT',#道富
'BROS',#Dutch Bros Inc-A
'PFFL',#ETRACS 2xMonthly Pay Leveraged
'CPRI',#Capri Holdings Ltd
'OND',#ProShares On-Demand ETF
'SQQQ',#三倍做空纳斯达克100ETF
'CSGP',#科斯塔
'MVPS',#Amplify Thematic All-Stars ETF
'ALKS',#阿尔凯默斯
'SMOG',#VanEck Low Carbon Energy ETF
'CIBR',#NASDAQ网络安全ETF-First Trust
'SNPS',#新思科技
'VHAQ',#Viveon Health Acquisition Corp
'WRB_F',#W. R. Berkley Corp Debentures
'BOSC',#BOS科技
'BMI',#Badger Meter Inc
'HOUS',#Anywhere Real Estate Inc
'GMF',#SPDR S&P Emerging Asia Pacific
'HOVNP',#Hovnanian Enterprises Inc Serie
'PGF',#金融优先股ETF-PowerShares
'ZGEN',#The Generation Z ETF
'AEMB',#American Century Emerging Marke
'PLTR',#Palantir Technologies Inc-A
'NKEL',#AXS 2X NKE Bull Daily ETF
'RPAR',#RPAR Risk Parity ETF
'FF',#FutureFuel Corp
'DMB',#BNY Mellon Municipal Bond Infra
'AMK',#AssetMark Financial Holdings In
'BKT',#BlackRock Income Trust
'GCOR',#Goldman Sachs Access U.S. Aggre
'FNWB',#First Northwest Bancorp
'ISWN',#Amplify BlackSwan ISWN ETF
'RILYG',#B. Riley Financial Inc Notes
'MACK',#Merrimack Pharmaceuticals Inc
'DUST',#二倍做空金矿指数ETF-Direxion
'SOGU',#AXS Short De-SPAC Daily ETF
'GACQ',#Global Consumer Acquisition Cor
'DRVN',#Driven Brands Holdings Inc
'POWI',#帕沃英蒂格盛
'NPO',#EnPro Industries Inc
'JAAA',#Janus Henderson AAA CLO ETF
'SSNC',#SS&C Technologies Holdings Inc
'EVE_U',#EVe Mobility Acquisition Corp U
'RITM_D',#Rithm Capital Corp Series D Pfd
'AIEQ',#AI Powered Equity ETF
'MBINP',#Merchants Bancorp Series A Pfd
'BATT',#Amplify Lithium & Battery Techn
'RF_E',#Regions Financial Corp Series E
'STXS',#趋实医疗设备
'JBL',#捷普
'UMH_D',#UMH Properties Inc Series D Pfd
'MCVT',#Mill City Ventures III Ltd
'WTAI',#WisdomTree Artificial Intellige
'NAACU',#North Atlantic Acquisition Corp
'EL',#雅诗兰黛
'FULTP',#Fulton Financial Corp Series A
'TASK',#TaskUs Inc-A
'MMU',#Western Asset Managed Municipal
'JPM_D',#JPMorgan Chase & Co Series DD P
'UTEN',#US Treasury 10 Year Note ETF
'ANET',#Arista Networks Inc
'BEEM',#Beam Global
'CHSCP',#CHS Inc Pfd
'CFIVU',#CF Acquisition Corp IV Unit Con
'NVMI',#Nova Ltd
'RSSS',#Research Solutions Inc
'GEG',#Great Elm Group Inc
'IDCC',#InterDigital Inc
'KEY_I',#KeyCorp Series E Pfd
'HOOD',#Robinhood Markets Inc-A
'MED',#快验保
'QID',#二倍做空纳斯达克100ETF
'ITEQ',#BlueStar Israel Technology ETF
'EVN',#Eaton Vance Municipal Income Tr
'MH_A',#Maiden Holdings Ltd Series A Pf
'AMGN',#安进
'KTN',#Structured Products Corp Credit
'HWCPZ',#Hancock Whitney Corp Notes
'EPR_G',#EPR Properties Series G Pfd
'CLOU',#Global X Cloud Computing ETF
'SUMO',#Sumo Logic Inc
'RIGZ',#Viridi Bitcoin Miners ETF
'KEJI',#Global X China Innovation ETF
'BOAC',#Bluescape Opportunities Acquisi
'CTDD',#Qwest Corp Notes
'EMHC',#SPDR Bloomberg Emerging Markets
'FLEX',#伟创力
'AEFC',#Aegon NV Capital Notes
'TWLO',#Twilio Inc-A
'TRIN',#Trinity Capital Inc
'IBTM',#iShares iBonds Dec 2032 Term Tr
'FRC_L',#First Republic Bank Series L Pf
'FGFPP',#FG Financial Group Inc Series A
'CYH',#Community Health Systems Inc
'ACES',#ALPS Clean Energy ETF
'XSW',#SPDR S&P Software & Services ET
'FRTY',#Alger Mid Cap 40 ETF
'VGM',#Invesco Trust for Investment Gr
'UNB',#联合银行
'FITBI',#Fifth Third Bancorp Series I Pf
'KCCA',#KraneShares California Carbon A
'GNL_A',#Global Net Lease Inc Series A P
'SCKT',#Socket Mobile Inc
'BST',#BlackRock Science and Technolog
'DGRE',#WisdomTree Emerging Markets Qua
'AMAL',#Amalgamated Financial Corp
'BIIB',#生化基因
'OSPN',#OneSpan Inc
'TSM',#台积电
'ZI',#ZoomInfo Technologies Inc
'FIXD',#First Trust TCW Opportunistic F
'INCR',#Intercure Ltd
'PHM',#普得集团(帕尔迪)
'BUG',#Global X Cybersecurity ETF
'DLR_J',#Digital Realty Trust Inc Series
'NXJ',#Nuveen New Jersey Quality Munic
'FRT_C',#Federal Realty Investment Trust
'ATRO',#Astronics Corp
'BDL',#Flanigan's Enterprises Inc
'TCBS',#Texas Community Bancshares Inc
'WFC_D',#Wells Fargo & Co Series DD Pfd
'QSWN',#Amplify BlackSwan Tech & Treasu
'SBNY',#Signature Bank
'SEER',#Seer Inc
'FRC_K',#First Republic Bank Series K Pf
'DWACW',#Digital World Acquisition Corp
'TBB',#AT&T Inc Notes
'ZS',#Zscaler Inc
'PKI',#珀金埃尔默
'PSO',#培生
'TYL',#泰勒科技
'GAMR',#视频游戏技术ETF-PureFunds
'SRT',#StarTek Inc
'LRNZ',#TrueShares Technology, AI & Dee
'ARR_C',#ARMOUR Residential REIT Inc Ser
'VFC',#威富
'IRL',#The New Ireland Fund
'OFLX',#欧美佳福莱克斯
'TPH',#Tri Pointe Homes Inc
'NCLH',#挪威邮轮
'PRAA',#PRA Group Inc
'NAIL',#Direxion Daily Homebuilders & S
'EMB',#新兴市场美元债ETF-iShares
'UPH',#UpHealth Inc
'VRDN',#Viridian Therapeutics Inc
'EDC',#三倍做多新兴市场ETF-Direxion
'BYM',#BlackRock Municipal Income Qual
'VECO',#维易科精密仪器
'TWO_B',#Two Harbors Investment Corp Ser
'SPDN',#Direxion Daily S&P 500 Bear 1X
'ROCK',#Gibraltar Industries Inc
'NAC',#Nuveen California Quality Munic
'ICLN',#iShares S&P Global Clean Energy
'EPV',#ProShares UltraShort FTSE Europ
'DHY',#Credit Suisse High Yield Bond F
'BCDA',#BioCardia Inc
'VR',#Global X Metaverse ETF
'GEGGL',#Great Elm Group Inc Notes
'WAVE',#Eco Wave Power Global AB (publ)
'SPLK',#Splunk Inc
'AUBN',#Auburn National Bancorporation
'MODG',#Topgolf Callaway Brands Corp
'STM',#意法半导体
'RELL',#理查森电子
'TATT',#TAT Technologies Ltd
'PPIH',#Perma-Pipe International Holdin
'JPM_M',#JPMorgan Chase & Co Series MM P
'DTC',#Solo Brands Inc-A
'CPAC',#Cementos Pacasmayo SAA ADR
'AHL_C',#Aspen Insurance Holdings Ltd Pf
'PNF',#PIMCO New York Municipal Income
'RVNC',#Revance Therapeutics Inc
'MS_O',#Morgan Stanley Series O Pfd
'MYE',#Myers Industries Inc
'SH',#做空标普500ETF-ProShares
'MTH',#Meritage Homes Corp
'HCP',#HashiCorp Inc-A
'SYF_A',#Synchrony Financial Series A Pf
'TIXT',#TELUS International (Cda) Inc
'VFL',#Delaware Investments National M
'KOD',#Kodiak Sciences Inc
'EIS',#以色列ETF-iShares MSCI
'BNH',#Brookfield Finance Inc Notes
'TGL',#Treasure Global Inc
'ELVT',#Elevate Credit Inc
'FCOR',#Fidelity Corporate Bond ETF
'RDVT',#Red Violet Inc
'FXI',#中国大型股ETF-iShares
'AG',#First Majestic Silver Corp
'MHO',#MI 家居
'PRS',#Prudential Financial Inc Notes
'RFM',#RiverNorth Flexible Municipal I
'MYD',#BlackRock MuniYield Fund
'ASB_E',#Associated Banc-Corp Series E P
'CIF',#MFS Intermediate High Income Fu
'AMCX',#AMC网络-A
'IDXX',#IDEXX实验室
'FISR',#SPDR SSGA Fixed Income Sector R
'SOHOO',#Sotherly Hotels Inc Series C Pf
'SHCA',#Spindletop Health Acquisition C
'NXGN',#NextGen Healthcare Inc
'GMED',#Globus Medical Inc-A
'NFTY',#First Trust India NIFTY 50 Equa
'ICUI',#ICU医疗
'GIW',#GigInternational1 Inc
'PGNY',#Progyny Inc
'BITQ',#Bitwise Crypto Industry Innovat
'AAPU',#Direxion Daily AAPL Bull 1.5X S
'ASPA',#Abri SPAC I Inc
'KTF',#DWS Municipal Income Trust
'PCTY',#Paylocity Holding Corp
'WDAY',#Workday Inc-A
'HALO',#奥洛兹美医疗
'IRBO',#iShares Robotics and Artificial
'VKI',#Invesco Advantage Municipal Inc
'CIL',#VictoryShares International Vol
'FUTU',#富途控股
'WTBA',#West Bancorporation Inc
'GLL',#二倍做空黄金ETF-ProShares
'MCHI',#中国ETF-iShares MSCI
'AVTX',#Avalo Therapeutics Inc
'FRNW',#Fidelity Clean Energy ETF
'EOS',#Eaton Vance Enhanced Equity Inc
'AIRS',#AirSculpt Technologies Inc
'BMED',#BlackRock Future Health ETF
'VCLT',#长期公司债指数ETF-Vanguard
'ESEB',#Xtrackers J.P. Morgan ESG Emerg
'MS_I',#Morgan Stanley Series I Pfd
'DKNG',#DraftKings Inc-A
'LPL',#LG Display Co Ltd ADR
'ATXS',#Astria Therapeutics Inc
'IVR',#景顺抵押资本
'IRTC',#iRhythm Technologies Inc
'NUE',#纽柯钢铁
'FMY',#First Trust Mortgage Income Fun
'CXSE',#中国民营企业ETF-WisdomTree
'IGIC',#International General Insurance
'AMTD',#尚乘国际
'FTDR',#Frontdoor Inc
'AIZN',#Assurant Inc Notes
'WBS_G',#Webster Financial Corp Series G
'SF_B',#Stifel Financial Corp Series B
'MFLX',#First Trust Flexible Municipal
'BPYPM',#Brookfield Property Partners LP
'ARI',#阿波罗房地产金融
'AIRG',#Airgain Inc
'XITK',#SPDR FactSet Innovative Technol
'RPD',#Rapid7 Inc
'FROG',#JFrog Ltd
'SE',#Sea Ltd ADR
'UPC',#大自然药业
'NPV',#Nuveen Virginia Quality Municip
'PFLD',#AAM Low Duration Preferred and
'RENW',#Harbor Energy Transition Strate
'QFIN',#360数科
'CCRN',#Cross Country Healthcare Inc
'SERA',#Sera Prognostics Inc-A
'LMND',#Lemonade Inc
'GILD',#吉利德科学
'CNM',#Core & Main Inc-A
'WFH',#Direxion Work From Home ETF
'CLPT',#ClearPoint Neuro Inc
'EDR',#Endeavor Group Holdings Inc-A
'NTWK',#纳索尔技术
'HGTY',#Hagerty Inc-A
'QRVO',#Qorvo Inc
'DOCU',#DocuSign Inc
'MS_L',#Morgan Stanley Series L Pfd
'JPM_K',#JPMorgan Chase & Co Series JJ P
'TDC',#天睿
'MUJ',#BlackRock MuniHoldings New Jers
'EVBG',#Everbridge Inc
'RNR_F',#RenaissanceRe Holdings Ltd Seri
'PCY',#新兴市场美元国债ETF-PowerShares
'BTEK',#BlackRock Future Tech ETF
'BXMX',#Nuveen S&P 500 Buy-Write Income
'LIT',#锂ETF-Global X
'CAH',#卡地纳健康
'NMCO',#Nuveen Municipal Credit Opportu
'GENY',#Principal Millennial Global Gro
'EDUC',#Educational Development Corp
'OPP_B',#RiverNorth/DoubleLine Strategic
'WFC_Z',#Wells Fargo & Co Series Z Pfd
'XHS',#SPDR S&P Health Care Services E
'REK',#ProShares Short Real Estate
'AZRE',#Azure Power Global Ltd
'BHB',#Bar Harbor Bankshares
'WYNN',#永利度假村
'GHLD',#Guild Holdings Co-A
'USB_H',#US Bancorp Series B Pfd
'GL_D',#Globe Life Inc Debentures
'NVR',#NVR Inc
'FSZ',#First Trust Switzerland AlphaDE
'EVER',#EverQuote Inc-A
'WIW',#Western Asset Inflation-Linked
'BWSN',#Babcock & Wilcox Enterprises In
'IBN',#印度工业信贷投资银行
'TMHC',#Taylor Morrison Home Corp
'YCL',#二倍做多日元ETF-ProShares
'WBD',#华纳兄弟探索
'VCAR',#Simplify Volt RoboCar Disruptio
'LPTV',#Loop Media Inc
'VC',#伟世通
'CIM',#奇美拉投资
'APTV_A',#Aptiv PLC Series A Pfd
'MNSB',#MainStreet Bancshares Inc
'TIPL',#Direxion Daily TIPS Bull 2X Sha
'AGM_D',#Federal Agricultural Mortgage C
'XTEN',#BondBloxx Bloomberg Ten Year Ta
'UCYB',#Ultra Nasdaq Cybersecurity
'SAMG',#Silvercrest Asset Management Gr
'BGFV',#Big 5体育用品
'TCBIO',#Texas Capital Bancshares Inc Se
'PSA_R',#Public Storage Series R Pfd
'LEO',#BNY Mellon Strategic Municipals
'DLO',#DLocal Ltd-A
'LAZY',#Lazydays Holdings Inc
'COHU',#科休半导体
'MGTX',#MeiraGTx Holdings plc
'RITM_A',#Rithm Capital Corp Series A Pfd
'CHN',#The China Fund
'ALNY',#Alnylam Pharmaceuticals Inc
'MSBIP',#Midland States Bancorp Inc Pfd
'RMMZ',#RiverNorth Managed Duration Mun
'ALYA',#Alithya Group inc-A
'MDRX',#麦赛斯医药
'AVID',#艾维科技
'SPFI',#South Plains Financial Inc
'POET',#POET Technologies Inc
'APXH',#APEX HealthCare ETF
'ENRG',#SoFi Smart Energy ETF
'ELC',#Entergy Louisiana Inc Bonds
'WGMI',#Valkyrie Bitcoin Miners ETF
'SAN',#桑坦德银行(US)
'USCTU',#TKB Critical Technologies 1 Uni
'HAE',#美国血液技术
'ZIM',#ZIM Integrated Shipping Service
'NVEC',#NVE Corp
'MHD',#BlackRock MuniHoldings Fund
'SHOC',#Strive U.S. Semiconductor ETF
'AEL_B',#American Equity Investment Life
'NFTZ',#Defiance Digital Revolution ETF
'HDGE',#Ranger Equity Bear Bear ETF
'ARKW',#ARK Next Generation Internet ET
'VABK',#Virginia National Bankshares Co
'CAMT',#康特科技
'MGRD',#Affiliated Managers Group Inc N
'SEF',#ProShares Short Financials
'AAPB',#GraniteShares 1.75x Long AAPL D
'LE',#Lands’ End Inc
'CINC',#CinCor Pharma Inc
'AACG',#ATA Creativity Global ADR
'PSA_F',#Public Storage Series F Pfd
'SNSE',#Sensei Biotherapeutics Inc
'RBCN',#卢比肯科技
'CRGE',#Charge Enterprises Inc
'CHII',#中国工业指数ETF-Global X
'AVPT',#AvePoint Inc-A
'MODV',#ModivCare Inc
'VTSI',#VirTra Inc
'VEGA',#AdvisorShares STAR Global Buy-W
'MORN',#晨星
'LIVN',#LivaNova PLC
'TBJL',#Innovator 20+ Year Treasury Bon
'AGGH',#Simplify Aggregate Bond PLUS Cr
'UBX',#Unity Biotechnology Inc
'BTTX',#Better Therapeutics Inc
'UNL',#United States 12 Month Natural
'SGRY',#Surgery Partners Inc
'NATI',#美国国家仪器
'SAVE',#Spirit Airlines Inc
'RAVE',#Rave Restaurant Group Inc
'QS',#QuantumScape Corp-A
'PCK',#PIMCO California Municipal Inco
'ARQQ',#Arqit Quantum Inc
'XPP',#二倍做多FTSE中国50ETF-ProShares
'KIM_M',#Kimco Realty Corp Class M Pfd
'CCRD',#CoreCard Corp
'KB',#韩国国民银行
'GPJA',#Georgia Power Co Notes
'PLW',#Invesco 1-30 Laddered Treasury
'LINC',#林肯教育服务
'TVE',#Tennessee Valley Authority Seri
'MDXG',#MiMedx Group Inc
'LNSR',#LENSAR Inc
'EVBN',#埃文斯万通金控
'RMBS',#Rambus Inc
'LTRX',#创力
'HYLD',#High Yield ETF
'MYY',#ProShares Short MidCap400
'FLWS',#1-800-FLOWERS.COM Inc-A
'SIEB',#Siebert Financial Corp
'VRNA',#维罗纳制药
'BAB',#Invesco Taxable Municipal Bond
'BML_G',#Bank of America Corp Series 1 P
'DDOG',#Datadog Inc-A
'LANC',#兰卡斯特食品
'PEGA',#Pegasystems Inc
'GDOC',#Goldman Sachs Future Health Car
'WCBR',#WisdomTree Cybersecurity Fund
'RACE',#法拉利
'ODC',#美国石油勘探
'IXHL',#Incannex Healthcare Ltd ADR
'ALRM',#Alarm.com Holdings Inc
'CAPL',#CrossAmerica Partners LP
'STK',#Columbia Seligman Premium Techn
'WBND',#Western Asset Total Return ETF
'BKD',#布鲁克代尔高级护理
'AIO',#Virtus Artificial Intelligence
'YCBD_A',#cbdMD Inc Series A Pfd
'ISUN',#iSun Inc
'MLN',#VanEck ETF Trust VanEck Long Mu
'PTC',#PTC Inc
'GEMD',#Goldman Sachs Access Emerging M
'OAK_B',#Oaktree Capital Group LLC Serie
'IGLB',#iShares Long-Term Corporate Bon
'RLJ_A',#RLJ Lodging Trust Series A Pfd
'CANG',#灿谷
'CMSD',#CMS Energy Corp Notes
'CNC',#康西哥
'IWFH',#iShares Virtual Work and Life M
'FORA',#Forian Inc
'ONBPP',#Old National Bancorp Series C P
'AMRK',#A-Mark Precious Metals Inc
'PSA_K',#Public Storage Series K Pfd
'BIPH',#Brookfield Infrastructure Corp
'VREX',#Varex Imaging Corp
'NEGG',#新蛋
'CSSEP',#Chicken Soup for the Soul Enter
'VVX',#V2X Inc
'PFES',#AXS 2X PFE Bear Daily ETF
'CARZ',#First Trust S-Network Future Ve
'PBD',#Invesco Global Clean Energy ETF
'ADUS',#爱德斯
'LFEQ',#VanEck Long/Flat Trend ETF
'HERO',#Global X Video Games & Esports
'NPCT',#Nuveen Core Plus Impact Fund
'ATEN',#A10 Networks Inc
'IHAK',#iShares Cybersecurity and Tech
'RLGT',#Radiant Logistics Inc
'INFN',#英飞朗
'OPRT',#Oportun Financial Corp
'ESMT',#EngageSmart Inc
'T_A',#AT&T Inc Series A Pfd
'PSA_L',#Public Storage Series L Pfd
'HUBS',#HubSpot Inc
'STAR_D',#iStar Inc Series D Pfd
'RF_C',#Regions Financial Corp Series C
'CFLT',#Confluent Inc-A
'PINS',#Pinterest Inc-A
'FOA',#Finance of America Companies In
'OFIX',#Orthofix Medical Inc
'UMMA',#Wahed Dow Jones Islamic World E
'REXR_B',#Rexford Industrial Realty Inc S
'TAIL',#Cambria Tail Risk ETF
'MTTR',#Matterport Inc-A
'SHO_H',#Sunstone Hotel Investors Inc Se
'SSSS',#SuRo Capital Corp
'CCLP',#CSI Compressco LP
'BHFAN',#Brighthouse Financial Inc Serie
'MRCY',#Mercury Systems Inc
'AFGC',#American Financial Group Inc No
'ATCX',#Atlas Technical Consultants Inc
'PCG_D',#Pacific Gas and Electric Co Pfd
'FDRV',#Fidelity Electric Vehicles and
'CIZ',#VictoryShares Developed Enhance
'BML_J',#Bank of America Corp Series 4 P
'SMAP',#SportsMap Tech Acquisition Corp
'ATLCL',#Atlanticus Holdings Corp Notes
'PLAB',#福尼克斯
'MHF',#Western Asset Municipal High In
'CRDF',#Cardiff Oncology Inc
'RXDX',#Prometheus Biosciences Inc
'ACMR',#ACM Research Inc-A
'AIQ',#Global X Future Analytics Tech
'AADI',#Aadi Bioscience Inc
'USPH',#美国理疗保健
'CLMB',#Climb Global Solutions Inc
'LGOV',#First Trust Long Duration Oppor
'GFS',#GLOBALFOUNDRIES Inc
'MLI',#木勒工业
'KLNE',#Direxion Daily Global Clean Ene
'INBKZ',#First Internet Bancorp Notes
'FDHT',#Fidelity Digital Health ETF
'NEOG',#纽勤
'BCOW',#1895 Bancorp of Wisconsin Inc
'SBB',#ProShares Short SmallCap600
'LKOR',#FlexShares Credit-Scored US Lon
'VRNS',#Varonis Systems Inc
'INSP',#Inspire Medical Systems Inc
'CODI_C',#Compass Group Diversified Holdi
'VLYPP',#Valley National Bancorp Series
'IMMR',#浸入科技
'ACNB',#ACNB Corp
'DM',#Desktop Metal Inc-A
'CIO',#City Office REIT Inc
'MSFU',#Direxion Daily MSFT Bull 1.5X S
'IDRV',#iShares Self-Driving EV and Tec
'DV',#DoubleVerify Holdings Inc
'RIV_A',#RiverNorth Opportunities Fund I
'SPLB',#SPDR Portfolio Long Term Corpor
'EET',#ProShares Ultra MSCI Emerging M
'JPM_L',#JPMorgan Chase & Co Series LL P
'ASML',#阿斯麦
'TSQ',#Townsquare Media Inc-A
'NNVC',#NanoViricides Inc
'SPRX',#Spear Alpha ETF
'ABUS',#Arbutus Biopharma Corp
'GLOG_A',#GasLog LP Series A Pfd
'EFU',#ProShares UltraShort MSCI EAFE
'GLBS',#Globus Maritime Ltd
'BML_L',#Bank of America Corp Series 5 P
'VKQ',#Invesco Municipal Trust
'SKYY',#云计算ETF-First Trust
'SPOK',#Spok Holdings Inc
'PETQ',#宠物IQ
'BERZ',#MicroSectors FANG & Innovation
'BBN',#BlackRock Taxable Municipal Bon
'UMPQ',#Umpqua控股
'BFS_D',#Saul Centers Inc Series D Pfd
'FRC_I',#First Republic Bank Series I Pf
'MUX',#McEwen Mining Inc
'FTNT',#防特网
'PED',#PEDEVCO Corp
'HDRO',#Defiance Next Gen H2 ETF
'DNN',#丹尼森矿业
'BEP',#Brookfield Renewable Partners L
'AFMD',#Affimed NV
'CRUS',#凌云半导体
'SAT',#Saratoga Investment Corp Notes
'UROY',#Uranium Royalty Corp
'RCON',#研控科技
'ARLO',#Arlo Technologies Inc
'MINV',#Matthews Asia Innovators Active
'MAV',#Pioneer Municipal High Income A
'CLDL',#Direxion Daily Cloud Computing
'PRE_J',#PartnerRe Ltd Series J Pfd
'ECF',#Ellsworth Growth and Income Fun
'SSYS',#Stratasys Ltd
'NVDA',#英伟达
'TTOO',#T2 Biosystems Inc
'QQQS',#Invesco NASDAQ Future Gen 200 E
'THNQ',#ROBO Global Artificial Intellig
'HLMN',#Hillman Solutions Corp
'AIG_A',#American International Group In
'NBXG',#Neuberger Berman Next Generatio
'BB',#黑莓
'WIT',#维布络
'ALRN',#艾勒朗制药
'FTII',#FutureTech II Acquisition Corp-
'STRS',#Stratus Properties Inc
'MBINO',#Merchants Bancorp Series B Pfd
'VNET',#世纪互联
'WRBY',#Warby Parker Inc-A
'DAT',#ProShares Big Data Refiners ETF
'GUG',#Guggenheim Active Allocation Fu
'TMAT',#Main Thematic Innovation ETF
'NBB',#Nuveen Taxable Municipal Income
'UMC',#联华电子
'TDF',#Templeton Dragon Fund
'RNG',#RingCentral Inc-A
'MMYT',#MakeMyTrip Ltd
'CTRM',#Castor Maritime Inc
'CLX',#高乐氏
'GBX',#格林布赖尔
'CCL',#嘉年华邮轮(US)
'MRBK',#Meridian Corp
'GXC',#中国ETF-SPDR S&P
'OPRX',#OptimizeRx Corp
'TWM',#二倍做空罗素2000ETF-ProShares
'WCLD',#WisdomTree Cloud Computing Fund
'PGTI',#PGT Innovations Inc
'HTFC',#Horizon Technology Finance Corp
'RILYT',#B. Riley Financial Inc Notes
'PCYO',#Pure Cycle Corp
'JAKK',#JAKKS Pacific Inc
'UPST',#Upstart Holdings Inc
'TALS',#Talaris Therapeutics Inc
'REAL',#The RealReal Inc
'VECT',#VectivBio Holding AG
'TSEM',#Tower半导体
'AFGD',#American Financial Group Inc De
'SITM',#SiTime Corp
'NMTR',#9 Meters Biopharma Inc
'ANNX',#Annexon, Inc.
'MX',#MagnaChip Semiconductor Corp
'IAS',#Integral Ad Science Holding Cor
'IDBA',#IDEX Biometrics ASA ADR
'ASTC',#Astrotech Corp
'PX',#P10 Inc-A
'TNP_E',#Tsakos Energy Navigation Ltd Se
'WDNA',#WisdomTree BioRevolution Fund
'RAIL',#FreightCar America Inc
'BZH',#贝哲房屋
'CBH',#Virtus Convertible & Income 202
'MHI',#Pioneer Municipal High Income T
'GBCI',#冰川万通金控
'INDF',#Nifty India Financials ETF
'LGHL',#狮子集团控股
'GLG',#铜道控股
'BILL',#Bill.com Holdings Inc
'PBW',#Invesco WilderHill Clean Energy
'FKWL',#Franklin Wireless Corp
'SKYT',#SkyWater Technology Inc
'RUN',#Sunrun Inc
'BVN',#布埃纳文图拉开采
'AHL_E',#Aspen Insurance Holdings Ltd Pf
'STT_G',#State Street Corp Series G Pfd
'NFLX',#奈飞
'BLV',#长期债券指数ETF-Vanguard
'REGN',#再生元制药
'AAIC_C',#Arlington Asset Investment Corp
'FRC_N',#First Republic Bank Series N Pf
'TRTN_C',#Triton International Ltd Series
'MRAM',#Everspin Technologies Inc
'FOSLL',#Fossil Group Inc Notes
'IAE',#Voya Asia Pacific High Dividend
'PRE',#Prenetics Global Ltd-A
'CEE',#The Central and Eastern Europe
'UST',#ProShares Ultra 7-10 Year Treas
'OXLCZ',#Oxford Lane Capital Corp Notes
'SWIM',#Latham Group Inc
'PFIE',#Profire Energy Inc
'JBI',#Janus International Group Inc
'SKYX',#SKYX Platforms Corp
'QSI',#Quantum-Si Inc-A
'OXLCO',#Oxford Lane Capital Corp Series
'SKYU',#Ultra Nasdaq Cloud Computing
'UPXI',#Upexi Inc
'KNSL',#Kinsale Capital Group Inc
'ESPO',#VanEck Video Gaming and eSports
'SRC_A',#Spirit Realty Capital Inc Serie
'NLY_G',#Annaly Capital Management Inc S
'VRA',#Vera Bradley Inc
'CQQQ',#中国科技指数ETF-Guggenheim
'HRMY',#Harmony Biosciences Holdings In
'HCAT',#Health Catalyst Inc
'ATHA',#Athira Pharma Inc
'CTEX',#ProShares S&P Kensho Cleantech
'EVGO',#EVgo Inc-A
'FLTN',#Rareview Inflation/Deflation ET
'OPEN',#Opendoor Technologies Inc
'ID',#PARTS iD Inc-A
'PDFS',#PDF Solutions Inc
'EBIX',#亚太交换中心
'COLB',#哥伦比亚银行系统
'ZTO',#中通快递
'IVR_C',#Invesco Mortgage Capital Inc Se
'ADRE',#ADR新兴市场50指数ETF-BLDRS
'BBGI',#比斯利广播
'QCLN',#First Trust NASDAQ Clean Edge G
'ELF',#elf Beauty Inc
'WVVI',#Willamette Valley Vineyards Inc
'CURV',#Torrid Holdings Inc
'HELX',#Franklin Genomic Advancements E
'KBH',#KB Home
'Z',#Zillow Group Inc-C
'ZG',#Zillow Group Inc-A
'GLDX',#USCF Gold Strategy Plus Income
'ERTH',#Invesco MSCI Sustainable Future
'ZGN',#Ermenegildo Zegna NV
'PLUR',#Pluri Inc
'OIA',#Invesco Municipal Income Opport
'LEV',#The Lion Electric Co
'GENE',#基因技术
'BIPI',#BIP Bermuda Holdings I Ltd Note
'CHIK',#Global X MSCI China Information
'AAON',#艾伦建材
'NKX',#Nuveen California AMT-Free Qual
'INDY',#iShares India 50 ETF
'ASAX',#Astrea Acquisition Corp
'APYX',#Apyx Medical Corp
'TLH',#10-20年国债ETF-iShares
'ELMD',#Electromed Inc
'PSCH',#Invesco S&P SmallCap Health Car
'BIDU',#百度
'MS_K',#Morgan Stanley Series K Pfd
'NEWR',#New Relic Inc
'TIGR',#老虎证券
'BYND',#Beyond Meat Inc
'PD',#PagerDuty Inc
'APEI',#美国公共教育
'CFSB',#CFSB Bancorp Inc
'BPMC',#Blueprint Medicines Corp
'XHE',#SPDR S&P Health Care Equipment
'BTMD',#biote Corp-A
'DXD',#二倍做空道指ETF-ProShares
'NXPL',#NextPlat Corp
'CADE_A',#Cadence Bank Series A Pfd
'CTG',#计算机作业集团
'BNKD',#MicroSectors U.S. Big Banks Ind
'RFI',#Cohen & Steers Total Return Rea
'FRC_H',#First Republic Bank Series H Pf
'FSEA',#First Seacoast Bancorp
'APGN',#Apexigen Inc
'KNSA',#Kiniksa Pharmaceuticals Ltd-A
'FTAIP',#FTAI Aviation Ltd Series A Pfd
'GP',#GreenPower Motor Co Inc
'DICE',#DICE Therapeutics Inc
'SVVC',#Firsthand Technology Value Fund
'MAYS',#梅斯物业
'HIMX',#奇景光电
'FIGS',#FIGZ Inc-A
'CPHC',#坎特伯雷帕克控股
'PHR',#Phreesia Inc
'THWWW',#Target Hospitality Corp Wt
'FORR',#佛罗斯特研究
'BTB',#Bit Brother Ltd-A
'DGZ',#做空黄金ETN-DB
'ETNB',#89bio Inc
'SABRP',#Sabre Corp Series A Pfd
'LICY',#Li-Cycle Holdings Corp
'ORRF',#Orrstown Financial Services Inc
'RETA',#Reata Pharmaceuticals Inc-A
'GKOS',#Glaukos Corp
'DZZ',#二倍做空黄金ETN-DB
'MYPS',#PlayStudios Inc-A
'FRC_J',#First Republic Bank Series J Pf
'CKPT',#标志点制药
'EICA',#Eagle Point Income Co Inc Serie
'GRPH',#Graphite Bio Inc
'LTPZ',#PIMCO 15 Year US TIPS Index ETF
'JILL',#J.Jill Inc
'AMS',#American Shared Hospital Servic
'SDS',#二倍做空标普500ETF-ProShares
'SNTG',#叁腾科技
'CCS',#Century Communities Inc
'LOCO',#El Pollo Loco Holdings Inc
'SDG',#iShares MSCI Global Sustainable
'GRBK',#Green Brick Partners Inc
'PRTG',#Portage Biotech Inc
'BFRI',#Biofrontera Inc
'INCO',#Columbia India Consumer ETF
'CFR_B',#Cullen/Frost Bankers Inc Series
'ILTB',#iShares Core 10+ Year USD Bond
'CUBA',#The Herzfeld Caribbean Basin Fu
'BIGC',#BigCommerce Holdings Inc-1
'CULP',#卡尔普纺织
'LEGN',#Legend Biotech Corp ADR
'SIJ',#ProShares UltraShort Industrial
'TFFP',#TFF Pharmaceuticals Inc
'MOTS',#Motus GI Holdings Inc
'CLOV',#Clover Health Investments Corp-
'TYA',#Simplify Intermediate Term Trea
'SID',#巴西国家钢铁
'CPSH',#CPS Technologies Corp
'WRB_E',#W. R. Berkley Corp Debentures
'ROCG',#Roth CH Acquisition IV Co
'VUZI',#Vuzix Corp
'BSAC',#桑坦德银行(智利)
'EPC',#Edgewell Personal Care Co
'REUN',#Reunion Neuroscience Inc
'DTG',#DTE Energy Co Series E Debentur
'NXTE',#AXS Green Alpha ETF
'CLIX',#ProShares Long Online/Short Sto
'CMRE_B',#Costamare Inc Pfd-B
'SOHU',#搜狐
'HYW',#海银控股
'KURA',#Kura Oncology Inc
'UPAR',#UPAR Ultra Risk Parity ETF
'ADN',#Advent Technologies Holdings In
'GAZ',#iPath Series B Bloomberg Natura
'DIOD',#Diodes Inc
'FFC',#Flaherty & Crumrine Preferred a
'IHIT',#Invesco High Income 2023 Target
'DAVA',#Endava plc ADR
'RVPHW',#Reviva Pharmaceuticals Holdings
'MPAC',#Model Performance Acquisition C
'EQ',#Equillium Inc
'AHT_G',#Ashford Hospitality Trust Inc S
'SOCL',#社交媒体指数ETF-Global X
'PMX',#PIMCO Municipal Income Fund III
'ESTC',#Elastic NV
'YELL',#Yellow Corp
'CXDO',#Crexendo Inc
'ANGH',#Anghami Inc
'KSTR',#KraneShares SSE STAR Market 50
'CYBR',#CyberArk Software Ltd
'ELA',#Envela Corp
'MASI',#麦斯莫医疗
'LQDA',#Liquidia Corp
'WYY',#WidePoint Corp
'PRDO',#Perdoceo Education Corp
'PMT',#PennyMac Mortgage Investment Tr
'AOUT',#American Outdoor Brands Inc
'SIMO',#慧荣科技
'HQH',#Tekla Healthcare Investors
'LOPE',#大峡谷教育
'AIRI',#Air Industries Group
'GET',#Getnet Adquirencia e Servicos p
'VIXM',#ProShares Trust VIX Mid-Term Fu
'ATRC',#AtriCure Inc
'GFI',#金田
'TLTW',#iShares Trust iShares 20+ Year
'WBX',#Wallbox NV-A
'EDN',#恩普雷萨电力
'COHR',#Coherent Corp
'OKTA',#Okta Inc-A
'WWR',#西水资源
'HPCO',#Hempacco Co Inc
'FTAI',#FTAI Aviation Ltd-A
'STG',#尚德机构
'YUMC',#百胜中国
'SEAL_B',#Seapeak LLC Series B Pfd
'SI',#Silvergate Capital Corp-A
'TTEC',#TTEC Holdings Inc
'KGRO',#KraneShares China Innovation ET
'EGHT',#8x8 Inc
'BTN',#Ballantyne Strong Inc
'PSTG',#Pure Storage Inc-A
'LJAQU',#LightJump Acquisition Corp Unit
'VIASP',#Via Renewables Inc Series A Pfd
'SRAD',#Sportradar Group AG-A
'SNAP',#Snap Inc-A
'AIP',#Arteris Inc
'UTZ',#Utz Brands Inc-A
'CDE',#科尔黛伦矿业
'ALTR',#Altair Engineering Inc-A
'AGOV',#ETC Gavekal Asia Pacific Govern
'MBINM',#Merchants Bancorp Series D Pfd
'BTBD',#BT Brands Inc
'ARKOW',#ARKO Corp Wt
'IHS',#IHS Holding Ltd
'CRVL',#CorVel Corp
'SDPI',#Superior Drilling Products Inc
'JAN',#JanOne Inc
'CEAD',#CEA Industries Inc
'KIM_L',#Kimco Realty Corp Class L Pfd
'RDY',#如瑞迪博士
'NRC',#National Research Corp
'F_B',#Ford Motor Co Notes
'HQL',#Tekla Life Sciences Investors
'UTAAU',#UTA Acquisition Corp I Unit Con
'AZPN',#艾斯本科技
'INDA',#印度ETF-iShares MSCI
'LAC',#Lithium Americas Corp
'SOBR',#SOBR Safe Inc
'DPRO',#Draganfly Inc
'GAQ',#Generation Asia I Acquisition L
'GDXD',#MicroSectors Gold Miners -3X In
'RLX',#雾芯科技
'MITK',#Mitek Systems Inc
'DNMR',#Danimer Scientific Inc-A
'CFB',#CrossFirst Bankshares Inc
'DC',#Dakota Gold Corp
'SSTI',#枪击探测
'DNA',#Ginkgo Bioworks Holdings Inc-A
'CGA',#中国绿色农业
'MMM',#3M公司
'AHL_D',#Aspen Insurance Holdings Ltd Pf
'FNKO',#Funko Inc-A
'TZA',#三倍做空小型股ETF-Direxion
'SOFO',#索尼克铸造科技
'INDIW',#indie Semiconductor Inc Wt
'CTHR',#诗思(香港)
'STBX',#Starbox Group Holdings Ltd
'LIAN',#联拓生物
'IPO',#Renaissance IPO ETF
'CVU',#CPI Aerostructures Inc
'SRNE',#Sorrento Therapeutics Inc
'AMAM',#Ambrx Biopharma Inc ADR
'AAIC_B',#Arlington Asset Investment Corp
'PATH',#UiPath Inc-A
'HTIBP',#Healthcare Trust Inc Series B P
'CTIC',#CTI BioPharma Corp
'GAB_G',#The Gabelli Equity Trust Inc Se
'HIMS',#Hims & Hers Health Inc-A
'PILL',#Direxion Daily Pharmaceutical &
'CERT',#Certara Inc
'APLT',#Applied Therapeutics Inc
'KEMQ',#KraneShares Emerging Markets Co
'ASRV',#AmeriServ Financial Inc
'EMQQ',#新兴市场互联网电商ETF
'MLPO',#CREDIT SUISSE S&P MLP INDEX ETN
'HIVE',#Hive Blockchain Technologies Lt
'VYGR',#Voyager Therapeutics Inc
'MIRM',#Mirum Pharmaceuticals Inc
'TAP_A',#摩森康胜-A
'BMRN',#拜玛林制药
'MOON',#Direxion Moonshot Innovators ET
'COMM',#CommScope Holding Co Inc
'JOJO',#ATAC Credit Rotation ETF
'PUBM',#PubMatic Inc-A
'HURC',#赫克
'DOUG',#Douglas Elliman Inc
'KFVG',#KraneShares CICC China 5G and T
'ECCC',#Eagle Point Credit Co Inc Serie
'S',#SentinelOne Inc-A
'FDNI',#First Trust Dow Jones Internati
'ATRI',#Atrion Corp
'KREF_A',#KKR Real Estate Finance Trust I
'AI',#C3.ai Inc-A
'EWTX',#Edgewise Therapeutics Inc
'HTEC',#ROBO Global Healthcare Technolo
'IBEX',#IBEX Ltd
'BMY',#百时美施贵宝
'GORO',#黄金资源
'ADTH',#AdTheorent Holding Co Inc
'BNDD',#Quadratic Deflation ETF
'BHFAP',#Brighthouse Financial Inc Serie
'KODK',#柯达
'ALLG',#Allego NV
'BBH',#VanEck Biotech ETF
'SQZ',#SQZ Biotechnologies Co
'HUGE',#FSD Pharma Inc-B
'GBBK',#Global Blockchain Acquisition C
'SCHQ',#Schwab Long-Term U.S. Treasury
'IBLC',#iShares Blockchain and Tech ETF
'FNGG',#Direxion Daily Select Large Cap
'TYD',#Direxion Daily 7-10 Year Treasu
'NYMTZ',#New York Mortgage Trust Inc Ser
'IIPR_A',#Innovative Industrial Propertie
'BHIL',#Benson Hill Inc
'LIVE',#Live Ventures Inc
'FGB',#First Trust Specialty Finance a
'TGH_A',#Textainer Group Holdings Ltd Se
'GLBE',#Global-E Online Ltd
'DHI',#霍顿房屋
'SQFTP',#Presidio Property Trust Inc Ser
'VGLT',#Vanguard Long-Term Treasury ETF
'CNTB',#康乃德生物
'CGEN',#Compugen医疗
'ALKT',#Alkami Technology Inc
'DASH',#DoorDash Inc-A
'NHIC',#NewHold Investment Corp II-A
'ANIK',#阿尼卡医疗
'AC',#Associated Capital Group Inc-A
'PANW',#派拓网络
'TWEB',#SoFi Web 3 ETF
'IIIN',#Insteel Industries Inc
'GROY',#Gold Royalty Corp
'VTYX',#Ventyx Biosciences Inc
'AZTA',#Azenta Inc
'RAYS',#Global X Solar ETF
'TAN',#太阳能ETF-Guggenheim
'CTEC',#Global X CleanTech ETF
'F_C',#Ford Motor Co Notes
'FBT',#First Trust Amex Biotech Index
'MDXH',#MDxHealth SA ADR
'GXTG',#Global X Thematic Growth ETF
'TH',#Target Hospitality Corp
'SNOW',#Snowflake Inc-A
'PARAP',#Paramount Global Series A Pfd
'TMDX',#TransMedics Group Inc
'SRTY',#三倍做空罗素2000ETF-ProShares
'IBB',#NASDAQ生物技术ETF-iShares
'EVLV',#Evolv Technologies Holdings Inc
'FIVN',#Five9 Inc
'SCCD',#Sachem Capital Corp Notes
'FMQQ',#FMQQ The Next Frontier Internet
'PRVA',#Privia Health Group Inc
'KARS',#KraneShares Electric Vehicles a
'SPCE',#维珍银河
'BBAI',#BigBear.ai Holdings Inc
'F_D',#Ford Motor Co Notes
'XMTR',#Xometry Inc-A
'MTSI',#MACOM Technology Solutions Hold
'SKF',#二倍做空金融ETF-ProShares
'PRST',#Presto Automation Inc
'SPTL',#SPDR Portfolio Long Term Treasu
'MARA',#Marathon Digital Holdings Inc
'PSB_Y',#PS Business Parks Inc Series Y
'KE',#Kimball Electronics Inc
'VERU',#Veru Inc
'MTLS',#Materialise NV ADR
'ENSC',#Ensysce Biosciences Inc
'DCT',#Duck Creek Technologies Inc
'CDRE',#Cadre Holdings Inc
'ACRS',#Aclaris Therapeutics Inc
'EFC_B',#Ellington Financial Inc Series
'FITBO',#Fifth Third Bancorp Series K Pf
'ATH_B',#Athene Holding Ltd Series B Pfd
'MXCT',#MaxCyte Inc
'IIF',#Morgan Stanley India Investment
'RPID',#Rapid Micro Biosystems Inc-A
'KEY_J',#KeyCorp Series F Pfd
'GRWG',#GrowGeneration Corp
'GTEC',#格陵兰科技
'ETWO',#E2open Parent Holdings Inc-A
'AVXL',#Anavex Life Sciences Corp
'EBMT',#Eagle Bancorp Montana Inc
'VXZ',#恐慌指数期货中期合约ETN-iPath
'NQP',#Nuveen Pennsylvania Quality Mun
'PIN',#印度ETF-PowerShares
'EVG',#Eaton Vance Short Duration Dive
'TPHS',#Trinity Place Holdings Inc
'PGEN',#Precigen Inc
'BGNE',#百济神州
'JFWD',#Jacob Forward ETF
'ARVN',#Arvinas Holding Co LLC
'LEJU',#乐居
'BNR',#燃石医学
'CNO_A',#CNO Financial Group Inc Debentu
'EGRX',#Eagle制药
'USCB',#USCB Financial Holdings Inc-A
'APPN',#Appian Corp-A
'PXLW',#美国像素
'EVGOW',#EVgo Inc Wt
'APVO',#Aptevo Therapeutics Inc
'SFB',#Stifel Financial Corp Notes
'FLGT',#Fulgent Genetics Inc
'EMBC',#Embecta Corp
'FREY',#FREYR Battery
'CGNT',#Cognyte Software Ltd
'BIMI',#必迈医药
'VRTX',#福泰制药
'LANDO',#Gladstone Land Corp Series B Pf
'SCU',#Sculptor Capital Management Gro
'TPIC',#TPI Composites Inc
'GFOF',#Grayscale Future of Finance ETF
'RCM',#R1 RCM Inc
'VTVT',#vTv Therapeutics Inc-A
'ENOB',#Enochian Biosciences Inc
'LGF_A',#狮门娱乐-A
'LANDM',#Gladstone Land Corp Series D Pf
'TVC',#Tennessee Valley Authority Seri
'OSUR',#奥瑞许科技
'OSW',#OneSpaWorld Holdings Ltd
'DHCNI',#Diversified Healthcare Trust No
'RSKD',#Riskified Ltd-A
'SPXS',#Direxion Daily S&P 500 Bear 3X
'PROC',#Procaps Group SA
'TLT',#20年+国债ETF-iShares
'KEY_K',#KeyCorp Series G Pfd
'IONS',#Ionis Pharmaceuticals Inc
'COUR',#Coursera Inc
'CABO',#Cable One Inc
'QNST',#QuinStreet Inc
'SPWR',#太阳电力
'LNTH',#Lantheus Holdings Inc
'APPF',#AppFolio Inc-A
'SWTX',#SpringWorks Therapeutics Inc
'PRTH',#Priority Technology Holdings In
'TWST',#Twist Bioscience Corp
'ALLO',#Allogene Therapeutics Inc
'ACET',#Adicet Bio Inc
'IBBQ',#Invesco Nasdaq Biotechnology ET
'SEM',#Select Medical Holdings Corp
'JANX',#Janux Therapeutics Inc
'LBRDP',#Liberty Broadband Corp Series A
'SMN',#二倍做空基础材料ETF-ProShares
'PSB_X',#PS Business Parks Inc Series X
'HCWB',#HCW Biologics Inc
'FAZ',#三倍做空金融ETF-Direxion
'MZZ',#ProShares UltraShort MidCap400
'CREG',#Smart Powerr Corp
'SDOW',#三倍做空道指ETF-ProShares
'TFJL',#Innovator 20+ Year Treasury Bon
'AGM_C',#Federal Agricultural Mortgage C
'NTES',#网易
'HOTH',#Hoth Therapeutics Inc
'FENC',#Fennec Pharmaceuticals Inc
'ACVA',#ACV Auctions Inc-A
'XNET',#迅雷
'SNGX',#Soligenix Inc
'BGRY',#Berkshire Grey Inc-A
'AUDC',#奥科
'IXSE',#WisdomTree India Ex-State-Owned
'NVDL',#GraniteShares 1.5x Long NVDA Da
'TMBR',#Timber Pharmaceuticals Inc
'PTH',#Invesco DWA Healthcare Momentum
'PACWP',#PacWest Bancorp Series A Pfd
'ADSE',#Ads-Tec Energy PLC
'ATCO_D',#Atlas Corp Series D Pfd
'OCFCP',#OceanFirst Financial Corp Serie
'PYCR',#Paycor HCM Inc
'ARGX',#argenx SE ADR
'IRMD',#iRadimed Corp
'PTSI',#P.A.M. Transportation Services
'CTAQ',#Carney Technology Acquisition C
'CRNT',#Ceragon网络
'EKG',#First Trust Nasdaq Lux Digital
'EXPI',#eXp World Holdings Inc
'CYAD',#Celyad Oncology SA ADR
'FRSH',#Freshworks Inc-A
'VIR',#Vir Biotechnology Inc
'PBE',#Invesco Dynamic Biotechnology &
'STGW',#Stagwell Inc-A
'SMAR',#Smartsheet Inc-A
'RXRX',#Recursion Pharmaceuticals Inc-A
'GGLS',#Direxion Daily GOOGL Bear 1X Sh
'KULR',#KULR Technology Group Inc
'FGEN',#FibroGen Inc
'ADV',#Advantage Solutions Inc-A
'AB',#联博控股
'PGRU',#PropertyGuru Group Ltd
'APLS',#Apellis Pharmaceuticals Inc
'TIVC',#Tivic Health Systems Inc
'EMTY',#ProShares Decline of the Retail
'FTAIN',#FTAI Aviation Ltd Series C Pfd
'AMZD',#Direxion Daily AMZN Bear 1X Sha
'XBIT',#XBiotech Inc
'PRTA',#Prothena Corp plc
'UTI',#环球技术学院
'NSSC',#纳普科安全技术
'SILK',#Silk Road Medical Inc
'TMCI',#Treace Medical Concepts Inc
'IOT',#Samsara Inc-A
'FAT',#FAT Brands Inc-A
'GENC',#范科工业
'TSLY',#YieldMax TSLA Option Income Str
'CEA',#东方航空
'MC',#Moelis & Co-A
'NYMTN',#New York Mortgage Trust Inc Ser
'DRRX',#DURECT Corp
'BAND',#Bandwidth Inc-A
'IDNA',#iShares Genomics Immunology and
'RSI',#Rush Street Interactive Inc-A
'THRN',#Thorne HealthTech Inc
'SREA',#Sempra Energy Notes
'JDST',#二倍做空小金矿指数ETF-Direxion
'RCG',#RENN Fund
'ACHR',#Archer Aviation Inc-A
'CHIQ',#中国消费者指数ETF-Global X
'INMD',#InMode Ltd
'PCOR',#Procore Technologies Inc
'FRPT',#Freshpet Inc
'IBRN',#iShares Neuroscience and Health
'STAF',#Staffing 360 Solutions Inc
'ENPH',#Enphase Energy Inc
'STIM',#Neuronetics Inc
'TRTN_E',#Triton International Ltd Series
'SRPT',#Sarepta Therapeutics Inc
'CTKB',#Cytek Biosciences Inc
'ZVIA',#Zevia PBC-A
'PARA',#派拉蒙全球-B
'MPLN',#MultiPlan Corp-A
'TENB',#Tenable Holdings Inc
'ACLX',#Arcellx Inc
'STOK',#Stoke Therapeutics Inc
'AMLX',#Amylyx Pharmaceuticals Inc
'CVGW',#卡拉沃养殖
'WOLF',#Wolfspeed Inc
'SIBN',#SI-BONE Inc
'JAZZ',#爵士制药
'MIO',#Pioneer Municipal High Income O
'KSPN',#Kaspien Holdings Inc
'BEST',#百世集团
'AVPTW',#AvePoint Inc Wt
'CEVA',#CEVA Inc
'SG',#Sweetgreen Inc-A
'PLUG',#普拉格能源
'VCXB',#10X Capital Venture Acquisition
'ACU',#Acme United Corp
'SRS',#二倍做空房地产ETF-ProShares
'SCOR',#康姆斯克
'CURI',#CuriosityStream Inc-A
'HQI',#HireQuest Inc
'SDD',#ProShares UltraShort SmallCap60
'AMBA',#安霸
'EDOC',#Global X Telemedicine & Digital
'FLIN',#Franklin FTSE India ETF
'WHG',#Westwood Holdings Group Inc
'VCLO',#Simplify Volt Cloud and Cyberse
'TOPS',#TOP Ships Inc
'CPTN',#Cepton Inc
'INVA',#Innoviva Inc
'NBIX',#神经分泌生物科学
'PDD',#拼多多
'TTCF',#Tattooed Chef Inc
'CELU',#Celularity Inc-A
'GDRX',#GoodRx Holdings Inc-A
'TBCP',#Thunder Bridge Capital Partners
'VRAX',#Virax Biolabs Group Ltd
'DLHC',#DLH Holdings Corp
'VERX',#Vertex Inc-A
'FSLY',#Fastly Inc-A
'HMY',#哈莫尼黄金
'EVTL',#Vertical Aerospace Ltd
'SHC',#Sotera Health Co
'BBP',#Virtus LifeSci Biotech Products
'XTWY',#BondBloxx Bloomberg Twenty Year
'SF_D',#Stifel Financial Corp Series D
'SCHN',#史尼泽钢铁
'PEN',#Penumbra Inc
'QTRX',#Quanterix Corp
'BSQR',#BSQUARE科技
'TSLA',#特斯拉
'SPXU',#三倍做空标普500ETF-ProShares
'RPTX',#Repare Therapeutics Inc
'CPRX',#Catalyst Pharmaceuticals Inc
'RORO',#ATAC US Rotation ETF
'QRHC',#Quest Resource Holding Corp
'SUNL',#Sunlight Financial Holdings Inc
'KOPN',#高平电子
'QURE',#uniQure NV
'NTIC',#Northern Technologies Internati
'MAXN',#Maxeon Solar Technologies Ltd
'EWEB',#Global X Emerging Markets Inter
'LZ',#LegalZoom.com Inc
'NVEI',#Nuvei Corp
'AXSM',#Axsome Therapeutics Inc
'RGF',#The Real Good Food Co Inc-A
'NTIP',#Network-1 Technologies Inc
'ENTX',#Entera Bio Ltd
'CRSR',#Corsair Gaming Inc
'YINN',#三倍做多FTSE中国ETF-Direxion
'DAM',#VanEck Digital Assets Mining ET
'HDB',#HDFC银行
'CSH',#Morgan Creek-Exos Active SPAC A
'AHCO',#AdaptHealth Corp
'DAPP',#VanEck Digital Transformation E
'ZSL',#二倍做空白银ETF-ProShares
'GENI',#Genius Sports Ltd
'CIXX',#CI Financial Corp
'SJ',#思享无限
'MRUS',#Merus NV
'PDSB',#PDS Biotechnology Corp
'TWOU',#2U Inc
'MBC',#MasterBrand Inc
'CNCE',#Concert Pharmaceuticals Inc
'FRBNU',#Forbion European Acquisition Co
'CSTL',#Castle Biosciences Inc
'LEDS',#旭明光电
'CIFR',#Cipher Mining Inc
'BILI',#哔哩哔哩
'ITCI',#Intra-Cellular Therapies Inc
'JMIA',#Jumia Technologies AG ADR
'CANO',#Cano Health Inc-A
'AKO_A',#Embotelladora Andina SA ADR-A
'FHN_E',#First Horizon Corp Series E Pfd
'ATTO',#Atento SA
'KTEC',#KraneShares Hang Seng TECH Inde
'VMEO',#Vimeo Inc
'PCTI',#PCTEL Inc
'GNUS',#Genius Brands International Inc
'BHR_B',#Braemar Hotels & Resorts Inc Se
'HKD',#尚乘数科
'HEXO',#HEXO Corp
'NYMTM',#New York Mortgage Trust Inc Ser
'PARAA',#派拉蒙全球-A
'RF_B',#Regions Financial Corp Series B
'VOYA_B',#Voya Financial Inc Series B Pfd
'CMTL',#康姆泰克通讯
'INBK',#First Internet Bancorp
'DCFC',#Tritium DCFC Ltd
'FORM',#FormFactor Inc
'DENN',#Denny’s Corp
'GGR',#Gogoro Inc
'GERN',#杰龙
'LUNA',#Luna Innovations Inc
'MYSZ',#My Size Inc
'SMDD',#UltraPro Short MidCap400
'HLVX',#HilleVax Inc
'RKT',#Rocket Companies Inc-A
'VEEV',#Veeva Systems Inc-A
'SYPR',#Sypris Solutions Inc
'NUTX',#Nutex Health Inc
'MVST',#Microvast Holdings Inc
'FEDU',#四季教育
'VVI',#Viad Corp
'UTMD',#犹他医疗产品
'ROIVW',#Roivant Sciences Ltd Wt
'LASR',#恩耐激光
'ADC_A',#Agree Realty Corp Series A Pfd
'NLY_I',#Annaly Capital Management Inc S
'CRWD',#CrowdStrike Holdings Inc-A
'HRTX',#Heron Therapeutics Inc
'PTRA',#Proterra Inc-A
'TSL',#GraniteShares 1.25x Long TSLA D
'SLDB',#Solid Biosciences Inc
'QUOT',#Quotient Technology Inc
'DX_C',#Dynex Capital Inc Series C Pfd
'AHT_D',#Ashford Hospitality Trust Inc S
'TYNE',#Direxion Nanotechnology ETF
'TIPT',#Tiptree Inc
'HAPP',#幸福来
'PODD',#银休特
'QQD',#Simplify Growth Equity Plus Dow
'XIN',#鑫苑置业
'SOHOB',#Sotherly Hotels Inc Series B Pf
'DFIN',#Donnelley Financial Solutions I
'BLTE',#Belite Bio Inc ADR
'SATO',#Invesco Alerian Galaxy Crypto E
'CVNA',#Carvana Co-A
'SPRY',#ARS Pharmaceuticals Inc
'SPIR',#Spire Global Inc-A
'NYMTL',#New York Mortgage Trust Inc Ser
'AUPH',#Aurinia Pharmaceuticals Inc
'MGR',#Affiliated Managers Group Inc N
'MRTX',#Mirati Therapeutics Inc
'W',#Wayfair Inc-A
'OPTT',#Ocean Power Technologies Inc
'LIXT',#Lixte Biotechnology Holdings In
'KGRN',#KraneShares MSCI China Clean Te
'JOBY_WS',#Joby Aviation Inc Wt
'BLDE',#Blade Air Mobility Inc-A
'SPT',#Sprout Social Inc-A
'TNDM',#Tandem Diabetes Care Inc
'FARO',#法如科技
'LVWR',#LiveWire Group Inc
'ABCM',#Abcam plc ADR
'PRIF_F',#Priority Income Fund Inc Series
'DXCM',#德康医疗
'SBIO',#ALPS Medical Breakthroughs ETF
'CFBK',#CF Bankshares Inc
'TUP',#特百惠
'FNI',#First Trust Chindia ETF
'EPI',#印度收入指数ETF-WisdomTree
'SSNT',#SilverSun Technologies Inc
'KORE',#KORE Group Holdings Inc
'ABCL',#AbCellera Biologics Inc
'ARKK',#ARK Innovation ETF
'PSYK',#PSYK ETF
'JCTCF',#朱伊特卡梅伦贸易
'YSG',#逸仙电商
'RVYL',#Ryvyl Inc
'CLPR',#Clipper Realty Inc
'OMQS',#Omniq Corp
'BLNKW',#Blink Charging Co Wt
'GWRE',#Guidewire Software Inc
'VSEC',#VSE Corp
'VCIF',#Vertical Capital Income Fund
'MOVE',#Movano Inc
'ATY',#AcuityAds Holdings Inc
'FOLD',#爱美医疗
'DGIN',#VanEck Digital India ETF
'RMTI',#Rockwell Medical Inc
'RMNI',#Rimini Street Inc
'NEOVW',#NeoVolta Inc Wt
'PLTK',#Playtika Holding Corp
'PAYS',#Paysign Inc
'DZSI',#DZS Inc
'SINT',#Sintx Technologies Inc
'BRZE',#Braze Inc-A
'FONR',#福纳
'SPNT',#SiriusPoint Ltd
'RDW',#Redwire Corp
'ONON',#On Holding AG-A
'JOBY',#Joby Aviation Inc
'ATH_A',#Athene Holding Ltd Series A Pfd
'BTAI',#BioXcel Therapeutics Inc
'HITI',#High Tide Inc
'AXNX',#Axonics Inc
'PCVX',#Vaxcyte Inc
'PI',#英频杰
'SGML',#Sigma Lithium Corp
'IONQ',#IonQ Inc
'SCC',#ProShares UltraShort Consumer S
'GOVZ',#iShares 25+ Year Treasury STRIP
'QDEL',#QuidelOrtho Corp
'PHAT',#Phathom Pharmaceuticals Inc
'SLDPW',#Solid Power Inc Wt
'ML',#MoneyLion Inc-A
'AVCT',#American Virtual Cloud Technolo
'ABIO',#方舟生物医药
'RDCM',#Radcom Ltd
'RBT',#Rubicon Technologies Inc-A
'WWE',#世界摔角娱乐
'PTLO',#Portillo’s Inc-A
'ALT',#Altimmune Inc
'BRP',#BRP Group Inc-A
'LFCR',#Lifecore Biomedical Inc
'LEU',#Centrus Energy Corp-A
'SRDX',#Surmodics Inc
'ARKR',#Ark Restaurants Corp
'SEAL_A',#Seapeak LLC Series A Pfd
'SDIG',#Stronghold Digital Mining Inc-A
'LITB',#兰亭集势
'CYAN',#赛安诺科技
'MHH',#Mastech Digital Inc
'JD',#京东
'EDV',#美国超长期国债ETF-Vanguard
'GLIN',#VanEck India Growth Leaders ETF
'MSTR',#MicroStrategy Inc-A
'MDGS',#Medigus Ltd ADR
'ERAS',#Erasca Inc
'ISEE',#IVERIC bio Inc
'ARCT',#Arcturus Therapeutics Holdings
'MEGL',#智富
'MAX',#MediaAlpha Inc-A
'SKIN',#The Beauty Health Co-A
'DSWL',#德斯维尔工业
'NC',#NACCO Industries Inc-A
'PTCT',#PTC Therapeutics Inc
'BNTX',#BioNTech SE ADR
'SGMA',#喜玛庆国际
'FHN_C',#First Horizon Corp Series C Pfd
'DOCS',#Doximity Inc-A
'GOCO',#GoHealth Inc-A
'FGBIP',#First Guaranty Bancshares Serie
'TUYA',#涂鸦智能
'GAINZ',#Gladstone Investment Corp Notes
'SDP',#ProShares UltraShort Utilities
'OABI',#OmniAb Inc
'LGF_B',#狮门娱乐-B
'CNCR',#Loncar Cancer Immunotherapy ETF
'SNCY',#Sun Country Airlines Holdings I
'AKA',#a.k.a. Brands Holding Corp
'FVRR',#Fiverr International Ltd
'ACAD',#阿卡迪亚
'FIACU',#Focus Impact Acquisition Corp U
'MSGR',#Direxion mRNA ETF
'ZENV',#Zenvia Inc-A
'ENVB',#Enveric Biosciences Inc
'BHAT',#蓝帽子
'BFI',#BurgerFi International Inc
'BTEC',#Principal Healthcare Innovators
'TTM',#塔塔汽车
'OARK',#YieldMax Innovation Option Inco
'FAZE',#FaZe Holdings Inc
'FENG',#凤凰新媒体
'MPX',#海洋产品
'ATGE',#Adtalem Global Education Inc
'ULCC',#Frontier Group Holdings Inc
'KRYS',#Krystal Biotech Inc
'NVTS',#Navitas Semiconductor Corp
'ABSI',#Absci Corp
'NRSN',#NeuroSense Therapeutics Ltd
'CERE',#Cerevel Therapeutics Holdings I
'AE',#亚当斯资源与能源
'BOIL',#二倍做多天然气ETF-ProShares
'TREE',#LendingTree Inc
'RDFN',#红鳍公司
'HUT',#Hut 8 Mining Corp
'BDTX',#Black Diamond Therapeutics Inc
'MLCO',#新濠博亚娱乐
'STRO',#Sutro Biopharma Inc
'INVE',#单片机微系统
'CYA',#Simplify Tail Risk Strategy ETF
'KMPH',#KemPharm Inc
'THCX',#The Cannabis ETF
'EAF',#GrafTech International Ltd
'TVTX',#Travere Therapeutics Inc
'TRMR',#Tremor International Ltd ADR
'VORB',#Virgin Orbit Holdings Inc
'PRSO',#Peraso Inc
'GENI_WS',#Genius Sports Ltd Wt
'TPST',#Tempest Therapeutics Inc
'NVRO',#Nevro Corp
'EHAB',#Enhabit Inc
'ECBK',#ECB Bancorp Inc
'INPX',#Inpixon
'ILMN',#Illumina Inc
'MDNA',#Medicenna Therapeutics Corp
'FREY_WS',#FREYR Battery Wt
'PRTS',#CarParts.com Inc
'PRO',#PROS Holdings Inc
'IPWR',#Ideal Power Inc
'XBI',#生物技术ETF-SPDR S&P
'DIBS',#1stdibs.com Inc
'SWAV',#ShockWave Medical Inc
'INSG',#Inseego Corp
'FFHL',#富维薄膜
'SQSP',#Squarespace Inc-A
'AXGN',#AxoGen Inc
'KMPR',#Kemper Corp
'INDI',#indie Semiconductor Inc-A
'SUZ',#Suzano SA ADR
'VOR',#Vor Biopharma Inc
'HUYA',#虎牙
'QRTEP',#Qurate Retail Inc Series A Pfd
'MRVI',#Maravai LifeSciences Holdings I
'BLFS',#BioLife Solutions Inc
'SVRE',#SaverOne 2014 Ltd ADR
'SSKN',#STRATA Skin Sciences Inc
'SPI',#绿能宝
'SNCE',#Science 37 Holdings Inc
'OST',#奥斯汀科技
'LSF',#Laird Superfood Inc
'BITF',#Bitfarms Ltd
'ARRY',#Array Technologies Inc
'MORF',#Morphic Holding Inc
'TCOM',#携程
'ROKU',#Roku Inc-A
'ALHC',#Alignment Healthcare Inc
'XDNA',#Kelly CRISPR & Gene Editing Tec
'KWE',#KWESST Micro Systems Inc
'INDL',#Direxion Daily MSCI India Bull
'HLIT',#谐波
'TMDI',#Titan Medical Inc
'CRDO',#Credo Technology Group Holding
'VCEL',#Vericel Corp
'MBRX',#Moleculin Biotech Inc
'PRPL',#Purple Innovation Inc-A
'WKSP',#Worksport Ltd
'NYXH',#Nyxoah SA
'NVFY',#诺华家具
'MNOV',#美第奇新星生物技术
'EXN',#Excellon Resources Inc
'ATHX',#Athersys Inc
'DOCN',#DigitalOcean Holdings Inc
'NTRB',#Nutriband Inc
'MOMO',#挚文集团
'VRAY',#ViewRay Inc
'BOTJ',#詹姆斯金融银行
'HHS',#哈特-汉克斯
'LWLG',#Lightwave Logic Inc
'FBIOP',#Fortress Biotech Inc Series A P
'RNA',#Avidity Biosciences Inc
'MEME',#Roundhill MEME ETF
'KWEB',#中概互联网ETF-KraneShares
'WEAV',#Weave Communications Inc
'KIDS',#OrthoPediatrics Corp
'KNDI',#康迪车业
'PAYO',#Payoneer Global Inc
'XELAP',#Exela Technologies Inc Series B
'VLTA',#Volta Inc-A
'SCYX',#SCYNEXIS Inc
'PZG',#Paramount Gold Nevada Corp
'OGI',#Organigram Holdings Inc
'OESX',#Orion Energy Systems Inc
'NCNA',#NuCana plc ADR
'KAVL',#Kaival Brands Innovations Group
'AAOI',#应用光电
'NUVL',#Nuvalent Inc-A
'STEM',#Stem Inc-A
'TDCX',#TDCX Inc ADR
'IMVT',#Immunovant Inc
'HTHT',#华住
'AVAH',#Aveanna Healthcare Holdings Inc
'TRDA',#Entrada Therapeutics Inc
'MTEX',#寰泰生技
'GNOM',#Global X Genomics & Biotechnolo
'ZROZ',#美国25年+零息票国债ETF-PIMCO
'RAIN',#Rain Therapeutics Inc
'HCC',#勇士煤业
'SATL',#Satellogic Inc-A
'UNMA',#Unum Group Notes
'DRV',#三倍做空房地产ETF-Direxion
'SGEN',#Seagen Inc
'INDP',#Indaptus Therapeutics Inc
'AVRO',#AVROBIO Inc
'ASLN',#亚狮康药业
'CDMO',#Avid Bioservices Inc
'XPER',#Xperi Inc
'BTCR',#Volt Crypto Industry Revolution
'MVIS',#维视图像
'MIST',#Milestone Pharmaceuticals Inc
'EMAN',#eMagin Corp
'DNUT',#Krispy Kreme Inc
'PSIL',#AdvisorShares Psychedelics ETF
'XENE',#Xenon制药
'VINE',#Fresh Vine Wine Inc
'JCE',#Nuveen Core Equity Alpha Fund
'ORGS',#Orgenesis Inc
'OMIC',#Singular Genomics Systems Inc
'INMB',#INmune Bio Inc
'HFRO',#Highland Income Fund
'GRFX',#烯石电车新材料
'BZFD',#BuzzFeed Inc-A
'BABA',#阿里巴巴
'ROIV',#Roivant Sciences Ltd
'ANGO',#血管造影动力
'BLDP',#巴拉德动力系统
'RIOT',#Riot Blockchain Inc
'LGIH',#LGI Homes Inc
'OLIT',#OmniLit Acquisition Corp-A
'NARI',#Inari Medical Inc
'GAME',#Engine Gaming and Media Inc
'HIPO',#Hippo Holdings Inc
'TFSA',#Terra Income Fund 6 Inc Notes
'VERY',#Vericity Inc
'CYCC',#Cyclacel Pharmaceuticals Inc
'BWMX',#Betterware de México SAPI de C
'LCTX',#Lineage Cell Therapeutics Inc
'GTBP',#GT Biopharma Inc
'FLYD',#MicroSectors Travel -3X Inverse
'BPOPM',#Popular Inc Trust Preferred Sec
'ABST',#Absolute Software Corp
'LLAP',#Terran Orbital Corp
'PLPC',#Preformed Line Products Co
'FUSN',#Fusion Pharmaceuticals Inc
'NABL',#N-able Inc
'CPNG',#Coupang Inc-A
'VXX',#恐慌指数期货短期合约ETN-iPath
'BWAY',#Brainsway Ltd ADR
'LUNG',#Pulmonx Corp
'BICK',#First Trust BICK Index Fund
'VRPX',#Virpax Pharmaceuticals Inc
'BARK',#Bark Inc
'RGEN',#Repligen Corp
'LPSN',#LivePerson Inc
'IMTX',#Immatics NV
'SUNW',#Sunworks Inc
'ULBI',#Ultralife Corp
'MITQ',#Moving iMage Technologies Inc
'LCID',#Lucid Group Inc-A
'KINS',#金石保险
'VIXY',#恐慌指数期货短期合约ETF
'TSLL',#Direxion Daily TSLA Bull 1.5X S
'CTAQU',#Carney Technology Acquisition C
'ZH',#知乎
'WRN',#西方铜金
'SYBX',#合成生物
'MCG',#Membership Collective Group Inc
'KRKR',#36氪
'HPX_WS',#HPX Corp Wt
'FFIE',#法拉第未来
'FATBP',#FAT Brands Inc Series B Pfd
'AEY',#ADDvantage Technologies Group I
'BEAT',#HeartBeam Inc
'SHOP',#Shopify Inc-A
'SY',#新氧
'BLNK',#Blink Charging Co
'CLDX',#塞德斯医疗
'KRTX',#Karuna Therapeutics Inc
'POCI',#Precision Optics Corp Inc
'VBFC',#农村金融信托银行
'CAN',#嘉楠科技
'DH',#Definitive Healthcare Corp-A
'NTRA',#Natera Inc
'TDOC',#Teladoc Health Inc
'DBGI',#Digital Brands Group Inc
'UBT',#二倍做多20年+国债ETF-ProShares
'KD',#Kyndryl Holdings Inc
'CUTR',#古特拉
'BBC',#Virtus LifeSci Biotech Clinical
'VACC',#Vaccitech plc ADR
'NIO',#蔚来
'IDN',#Intellicheck Inc
'OM',#Outset Medical Inc
'EDUT',#Global X Education ETF
'PAY',#Paymentus Holdings Inc-A
'OLO',#Olo Inc-A
'RARE',#Ultragenyx Pharmaceutical Inc
'PHUNW',#Phunware Inc Wt
'IGC',#India Globalization Capital Inc
'HLLY',#Holley Inc
'FSTX',#F-star Therapeutics Inc
'INVZ',#Innoviz Technologies Ltd
'BDRY',#Breakwave Dry Bulk Shipping ETF
'IDR',#Idaho Strategic Resources Inc
'AUUD',#Auddia Inc
'SST',#System1 Inc-A
'TME',#腾讯音乐
'SGHT',#Sight Sciences Inc
'RRGB',#红罗宾汉堡连琐店
'FHTX',#Foghorn Therapeutics Inc
'TALK',#Talkspace Inc-A
'LU',#陆金所控股
'ESOA',#Energy Services of America Corp
'SFE',#安科投资
'NSTG',#NanoString Technologies Inc
'FTHM',#Fathom Holdings Inc
'ATHM',#汽车之家
'HASI',#Hannon Armstrong Sustainable In
'AMEH',#Apollo Medical Holdings Inc
'SRRK',#Scholar Rock Holding Corp
'AEL_A',#American Equity Investment Life
'INKT',#MiNK Therapeutics Inc
'MD',#Pediatrix Medical Group Inc
'XTNT',#Xtant Medical Holdings Inc
'SPPI',#Spectrum Pharmaceuticals Inc
'SBFM',#Sunshine Biopharma Inc
'ONTX',#Onconova Therapeutics Inc
'NYMX',#Nymox Pharmaceutical Corp
'CYN',#Cyngn Inc
'CSIQ',#阿特斯太阳能
'RNXT',#RenovoRx Inc
'PCG_B',#Pacific Gas and Electric Co Pfd
'EDIT',#Editas Medicine Inc
'VIOT',#云米
'TANH',#碳博士控股
'CBAT',#中比能源
'DCBO',#Docebo Inc
'SCPH',#scPharmaceuticals Inc
'LCI',#Lannett Co Inc
'ALZN',#Alzamend Neuro Inc
'RIVN',#Rivian Automotive Inc-A
'CLEU',#华夏博雅
'ALBO',#Albireo Pharma Inc
'REPL',#Replimune Group Inc
'UXIN',#优信
'ARMP',#Armata Pharmaceuticals Inc
'WIX',#Wix.com Ltd
'MNSO',#名创优品
'GWH',#ESS Tech Inc
'NTLA',#Intellia Therapeutics Inc
'SOLO',#Electrameccanica Vehicles Corp
'HMPT',#Home Point Capital Inc
'HARP',#Harpoon Therapeutics Inc
'GRF',#Eagle Capital Growth Fund
'CLVR',#Clever Leaves Holdings Inc
'CANF',#Can-Fite BioPharma Ltd ADR
'EFSCP',#Enterprise Financial Services C
'HCM',#和黄医药(US ADR)
'AHT_H',#Ashford Hospitality Trust Inc S
'ONVO',#Organovo Holdings Inc
'BNED',#Barnes & Noble Education Inc
'DHCNL',#Diversified Healthcare Trust No
'ARAV',#Aravive Inc
'AEVA',#Aeva Technologies Inc
'OLK',#Olink Holding AB (publ) ADR
'BHC',#Bausch Health Companies Inc
'LYT',#Lytus Technologies Holdings PTV
'ASMB',#Assembly Biosciences Inc
'RDNT',#RadNet Inc
'LL',#LL Flooring Holdings Inc
'LSTA',#Lisata Therapeutics Inc
'AMRN',#阿玛琳
'DSKE',#Daseke Inc
'LTBR',#Lightbridge Corp
'PGJ',#中概股ETF-PowerShares
'WSO_B',#华斯科-B
'PETZ',#天地荟
'NERV',#Minerva Neurosciences Inc
'DATS',#DatChat Inc
'CYBN',#Cybin Inc
'BKSY',#BlackSky Technology Inc-A
'AMPX_WS',#Amprius Technologies Inc Wt
'BIB',#二倍做多NASDAQ生物技术ProShares
'ZNTL',#Zentalis Pharmaceuticals Inc
'PRPH',#ProPhase Labs Inc
'FTAIO',#FTAI Aviation Ltd Series B Pfd
'KDNY',#Chinook Therapeutics Inc
'ASTI',#Ascent Solar Technologies Inc
'INQQ',#India Internet & Ecommerce ETF
'INSM',#Insmed Inc
'LBPH',#Longboard Pharmaceuticals Inc
'BCTX',#BriaCell Therapeutics Corp
'KPRX',#Kiora Pharmaceuticals Inc
'BTBT',#比特数字
'BLND',#Blend Labs Inc-A
'MRSN',#梅莎娜制药
'AVDL',#Avadel Pharmaceuticals plc ADR
'THTX',#Theratechnologies Inc
'WILC',#G. Willi-Food International Ltd
'AAME',#美国大西洋
'ARKG',#ARK Genomic Revolution ETF
'EWCZ',#European Wax Center Inc-A
'NUZE',#NuZee Inc
'HEPA',#Hepion Pharmaceuticals Inc
'GNLN',#Greenlane Holdings Inc-A
'ATHE',#Alterity Therapeutics Ltd ADR
'SGH',#SMART Global Holdings Inc
'CELC',#Celcuity LLC
'ENLV',#Enlivex Therapeutics Ltd
'GLSTU',#Global Star Acquisition Inc Uni
'DIT',#AMCON Distributing Co
'PEAR',#Pear Holdings Corp-A
'IVA',#Inventiva SA ADR
'PALT',#Paltalk Inc
'GGB',#盖尔道钢铁
'STSS',#Sharps Technology Inc
'PROCW',#Procaps Group SA Wt
'APPS',#Digital Turbine Inc
'PMO',#Putnam Municipal Opportunities
'SURGW',#SurgePays Inc Wt
'PRVB',#Provention Bio Inc
'SGBX',#SG建筑
'LIND',#Lindblad Expeditions Holdings I
'KTTA',#Pasithea Therapeutics Corp
'IVDA',#Iveda Solutions Inc
'ISR',#IsoRay Inc
'IMAB',#天境生物
'DMTK',#DermTech Inc
'ARTL',#Artelo Biosciences Inc
'RYTM',#Rhythm Pharmaceuticals Inc
'STAA',#STAAR Surgical Co
'SNOA',#Sonoma Pharmaceuticals Inc
'HUMA',#Humacyte Inc
'BEATW',#HeartBeam Inc Wt
'QLI',#祁连国际
'SPKX',#ConvexityShares 1x SPIKES Futur
'UK',#优客工场
'SDGR',#Schrodinger Inc
'PKOH',#Park-Ohio Holdings Corp
'OPK',#OPKO健康
'CREX',#Creative Realities Inc
'IMAX',#IMAX Corp
'QVCC',#QVC Inc Notes
'NET',#Cloudflare Inc-A
'BCYC',#Bicycle Therapeutics Ltd ADR
'CRON',#Cronos Group Inc
'PRCT',#PROCEPT BioRobotics Corp
'ONDS',#Ondas Holdings Inc
'ELBM',#Electra Battery Materials Corp
'SMIN',#iShares MSCI India Small-Cap ET
'CLSK',#CleanSpark Inc
'MNMD',#Mind Medicine (MindMed) Inc
'GDS',#万国数据
'NHWK',#NightHawk Biosciences Inc
'LX',#乐信
'KPLT',#Katapult Holdings Inc
'ANGN',#Angion Biomedica Corp
'MAIA',#MAIA Biotechnology Inc
'OCUP',#Ocuphire Pharma Inc
'ABEO',#Abeona Therapeutics Inc
'PTON',#Peloton Interactive Inc-A
'RVLP',#RVL Pharmaceuticals plc
'TARA',#Protara Therapeutics Inc
'CPOP',#普普文化
'ME',#23andMe Holding Co-A
'CD',#秦淮数据
'TMC',#TMC the metal company Inc
'SONN',#Sonnet BioTherapuetics Holdings
'RANI',#Rani Therapeutics Holdings Inc-
'BODY',#The Beachbody Co Inc-A
'CDNA',#CareDx Inc
'PCTTU',#PureCycle Technologies Inc Unit
'KZR',#Kezar Life Sciences Inc
'MAPS',#WM Technology Inc-A
'EMBK',#Embark Technology Inc-A
'ADAP',#Adaptimmune Therapeutics plc AD
'KITT',#Nauticus Robotics Inc
'MESO',#Mesoblast Ltd ADR
'NCMI',#National CineMedia Inc
'MICT',#MICT Inc
'LODE',#Comstock Inc
'IMPP',#Imperial Petroleum Inc
'CSSE',#心灵鸡汤娱乐
'MNK',#Mallinckrodt plc
'PRIF_I',#Priority Income Fund Inc Series
'SNTI',#Senti Biosciences Inc-A
'MNKD',#曼恩凯德生物医疗
'SMRT',#SmartRent Inc-A
'EMXF',#iShares ESG Advanced MSCI EM ET
'FUBO',#fuboTV Inc
'OCUL',#Ocular Therapeutix Inc
'NGL_C',#NGL Energy Partners LP Class C
'BZ',#BOSS直聘
'IMNN',#Imunon Inc
'SHLS',#Shoals Technologies Group Inc-A
'TSVT',#2seventy bio Inc
'MXC',#Mexco Energy Corp
'TOMZ',#TOMI Environmental Solutions In
'SKLZ',#Skillz Inc-A
'OABIW',#OmniAb Inc Wt
'CRDL',#Cardiol Therapeutics Inc
'NOAH',#诺亚财富
'SNDX',#Syndax Pharmaceuticals Inc
'RXT',#Rackspace Technology Inc
'NBN',#东北银行
'CSBR',#Champions Oncology Inc
'MNTS',#Momentus Inc-A
'JNCE',#Jounce Therapeutics Inc
'NAII',#Natural Alternatives Internatio
'AORT',#Artivion Inc
'BFLY',#Butterfly Network Inc-A
'CVAC',#CureVac NV
'MCRB',#Seres Therapeutics Inc
'CXM',#Sprinklr Inc-A
'CTA_B',#E. I. du Pont de Nemours and Co
'RLAY',#Relay Therapeutics Inc
'SQL',#SeqLL Inc
'SFR',#Appreciate Holdings Inc-A
'MDVL',#MedAvail Holdings Inc
'IPAXW',#Inflection Point Acquisition Co
'GLT',#Glatfelter Corp
'JSM',#Navient Corp Notes
'MTBC',#CareCloud Inc
'VFF',#Village Farms国际
'SALM',#Salem Media Group Inc-A
'GSUN',#金太阳教育
'BWV',#Blue Water Vaccines Inc
'AEYE',#AudioEye Inc
'ZETA',#Zeta Global Holdings Corp-A
'YMAB',#Y-mAbs Therapeutics Inc
'SENS',#Senseonics Holdings Inc
'NEO',#NeoGenomics Inc
'ITRI',#埃创
'BNGO',#Bionano Genomics Inc
'INAB',#IN8bio Inc
'NSYS',#Nortech Systems Inc
'WB',#微博
'BEAM',#Beam Therapeutics Inc
'SECO',#寺库
'VERI',#Veritone Inc
'GOOS',#加拿大鹅
'CYTK',#Cytokinetics Inc
'UP',#Wheels Up Experience Inc-A
'PEGY',#Pineapple Energy Inc
'GWH_WS',#ESS Tech Inc Wt
'GREE',#Greenidge Generation Holdings I
'CNXA',#Connexa Sports Technologies Inc
'AWRE',#艾卫
'ATIP',#ATI Physical Therapy Inc-A
'BELFA',#Bel Fuse Inc-A
'SAGE',#Sage Therapeutics Inc
'BABX',#GraniteShares 1.75x Long BABA D
'BLUE',#蓝鸟生物
'DCPH',#Deciphera Pharmaceuticals Inc
'EVAX',#Evaxion Biotech A/S ADR
'CALT',#Calliditas Therapeutics AB ADR
'ATOM',#Atomera Inc
'TRUP',#Trupanion Inc
'CLGN',#CollPlant Biotechnologies Ltd
'SELB',#Selecta Biosciences Inc
'CRIS',#居里
'HIHO',#骇维金属加工
'CHPT',#ChargePoint Holdings Inc
'SPLP',#Steel Partners Holdings LP
'LAW',#CS Disco Inc
'SPKY',#ConvexityShares Daily 1.5x SPIK
'UVXY',#1.5倍做多恐慌指数短期期货ETF
'ADMA',#ADMA Biologics Inc
'NNOX',#Nano-X Imaging Ltd
'PRCH',#Porch Group Inc
'DQ',#大全新能源
'FANH',#泛华控股集团
'PCSA',#Processa Pharmaceuticals Inc
'AMPL',#Amplitude Inc-A
'GDYN',#Grid Dynamics Holdings Inc
'VVOS',#Vivos Therapeutics Inc
'FLGC',#Flora Growth Corp
'RMI',#RiverNorth Opportunistic Munici
'RMBL',#RumbleOn Inc-B
'SHCR',#Sharecare Inc
'BZUN',#宝尊电商
'UDMY',#Udemy Inc
'MICS',#The Singing Machine Co Inc
'IBRX',#ImmunityBio Inc
'KROS',#Keros Therapeutics Inc
'FTCI',#FTC Solar Inc
'MYGN',#万基遗传
'NBY',#NovaBay Pharmaceuticals Inc
'TXMD',#TherapeuticsMD Inc
'PXMD',#PaxMedica Inc
'BZQ',#二倍做空MSCI巴西ETF-ProShares
'AGL',#agilon health inc
'DNLI',#Denali Therapeutics Inc
'RILY',#B. Riley Financial Inc
'WLDS',#Wearable Devices Ltd
'INVZW',#Innoviz Technologies Ltd Wt
'FWBI',#First Wave BioPharma Inc
'STRT',#STRATTEC SECURITY CORP
'VNDA',#Vanda Pharmaceuticals Inc
'YQ',#一起教育科技
'OLITU',#OmniLit Acquisition Corp Unit C
'GLDG',#GoldMining Inc
'WLDN',#Willdan Group Inc
'CIX',#CompX国际
'ALGS',#Aligos Therapeutics Inc
'NXGL',#NexGel Inc
'MBOT',#Microbot Medical Inc
'ELOX',#Eloxx Pharmaceuticals Inc
'BLCM',#Bellicum制药
'NVTA',#Invitae Corp
'PNTG',#The Pennant Group Inc
'ISPO',#Inspirato Inc-A
'MOGO',#Mogo Inc
'LMDX',#LumiraDx Ltd
'BSFC',#Blue Star Foods Corp
'ELTK',#Eltek Ltd
'TMF',#三倍做多20年+国债ETF-Direxion
'TDUP',#ThredUp Inc-A
'AGEN',#艾吉纳斯
'OUST',#Ouster Inc
'EDU',#新东方
'CRSP',#CRISPR Therapeutics AG
'RBOT',#Vicarious Surgical Inc-A
'ALLK',#Allakos Inc
'NRIX',#Nurix Therapeutics Inc
'RERE',#万物新生
'BRID',#Bridgford Foods Corp
'SONM',#Sonim Technologies Inc
'SASI',#Sigma Additive Solutions Inc
'MCLD',#mCloud Technologies Corp
'IRNT',#IronNet Inc
'HSTO',#Histogen Inc
'GRNA',#GreenLight Biosciences Inc
'AMWL',#American Well Corp-A
'AMST',#Amesite Inc
'UG',#United-Guardian Inc
'AMPS',#Altus Power Inc-A
'NRDS',#NerdWallet Inc-A
'SOPH',#Sophia Genetics SA
'GTHX',#G1 Therapeutics Inc
'YY',#欢聚
'INO',#Inovio制药
'HYZN',#Hyzon Motors Inc-A
'MMAT',#Meta Materials Inc
'PETV',#PetVivo Holdings Inc
'OCFT',#金融壹账通
'BOLT',#Bolt Biotherapeutics Inc
'OPT',#Opthea Ltd ADR
'SMMT',#Summit Therapeutics Inc
'KPTI',#Karyopharm Therapeutics Inc
'TCRX',#TScan Therapeutics Inc
'RLMD',#Relmada Therapeutics Inc
'KXIN',#开心汽车
'MRNA',#Moderna Inc
'ITOS',#iTeos Therapeutics Inc
'KRUS',#Kura Sushi USA Inc-A
'MFH',#Mercurity Fintech Holding Inc A
'IMPL',#Impel Pharmaceuticals Inc
'DAO',#网易有道
'RXST',#RxSight Inc
'FGF',#FG Financial Group Inc
'ONCY',#Oncolytics Biotech Inc
'RCUS',#Arcus Biosciences Inc
'ASUR',#Asure Software Inc
'DYNT',#Dynatronics Corp
'BRQS',#播思科技
'BCDAW',#BioCardia Inc Wt
'ESPR',#Esperion Therapeutics Inc
'CMS_B',#CMS Energy Corp Pfd
'FEAM',#5E Advanced Materials Inc
'GAN',#GAN Ltd
'FLNC',#Fluence Energy Inc-A
'PSHG',#Performance Shipping Inc
'OTMO',#Otonomo Technologies Ltd
'AYLA',#Ayala Pharmaceuticals Inc
'VZIO',#Vizio Holding Corp-A
'VERV',#Verve Therapeutics Inc
'PMVP',#PMV Pharmaceuticals Inc
'TWKS',#Thoughtworks Holding Inc
'MDGL',#Madrigal Pharmaceuticals Inc
'SAVA',#疼痛治疗
'SILO',#Silo Pharma Inc
'SIF',#SIFCO Industries Inc
'SCLXW',#Scilex Holding Co Wt
'RAAS',#容联云通讯
'MMMB',#MamaMancini's Holdings Inc
'JWEL',#聚好商城
'GNPX',#Genprex Inc
'DS',#Drive Shack Inc
'DOYU',#斗鱼
'CYRX',#Cryoport Inc
'BACK',#IMAC Holdings Inc
'ADNWW',#Advent Technologies Holdings In
'TRT',#Trio-Tech International
'MPW',#Medical Properties Trust Inc
'PWFL',#PowerFleet Inc
'FIXX',#Homology Medicines Inc
'DDI',#DoubleDown Interactive Co Ltd A
'PRTK',#Paratek Pharmaceuticals Inc
'CWBR',#CohBar Inc
'AHI',#Advanced Health Intelligence Lt
'VINP',#Vinci Partners Investments Ltd-
'EMKR',#埃姆科
'ONCS',#OncoSec Medical Inc
'VYNT',#Vyant Bio Inc
'DRCT',#Direct Digital Holdings Inc-A
'CWEB',#Direxion Daily CSI China Intern
'MOR',#MorphoSys AG ADR
'AKTS',#Akoustis Technologies Inc
'MSGM',#Motorsport Games Inc-A
'MVSTW',#Microvast Holdings Inc Wt
'MTMT',#Mega Matrix Corp
'LEXXW',#Lexaria Bioscience Corp Wt
'DRIO',#DarioHealth Corp
'AGRX',#Agile Therapeutics Inc
'ACONW',#Aclarion Inc Wt
'PCG_C',#Pacific Gas and Electric Co Pfd
'XAIR',#Beyond Air Inc
'IPSC',#Century Therapeutics Inc
'AMSC',#美国超导
'QNRX',#Quoin Pharmaceuticals Ltd ADR
'SANA',#Sana Biotechnology Inc
'VLDR',#Velodyne Lidar
'JXJT',#金铉集团
'JT',#简普科技
'BE',#Bloom Energy Corp-A
'EXAS',#精密科学
'SCO',#二倍做空原油ETF-ProShares
'LUXH',#LuxUrban Hotels Inc
'AGIO',#Agios Pharmaceuticals Inc
'ATNM',#Actinium Pharmaceuticals Inc
'YMM',#满帮
'IPW',#iPower Inc
'AFRI',#Forafric Global PLC
'CDXS',#Codexis Inc
'DHX',#戴斯控股
'XOS',#Xos Inc
'RGNX',#REGENXBIO Inc
'ARHS',#Arhaus Inc-A
'ACNT',#Ascent Industries Co
'GLUE',#Monte Rosa Therapeutics Inc
'SQNS',#Sequans Communications SA ADR
'BARK_WS',#Bark Inc Wt
'ALPAW',#Alpha Healthcare Acquisition Co
'AEVA_WS',#Aeva Technologies Inc Wt
'RLYB',#Rallybio Corp
'BBIO',#BridgeBio Pharma Inc
'SRAX',#SRAX Inc-A
'NIU',#小牛电动
'UWMC',#UWM Holdings Corp-A
'TGTX',#TG Therapeutics Inc
'BEKE',#贝壳
'CMPS',#COMPASS Pathways plc ADR
'TARK',#AXS 2X Innovation ETF
'SEEL',#Seelos Therapeutics Inc
'NEPH',#Nephros Inc
'SGMO',#Sangamo Therapeutics Inc
'UVIX',#VS Trust 2x Long VIX Futures ET
'PTPI',#Petros Pharmaceuticals Inc
'MATH',#龙运国际
'KUKE',#库客音乐
'ACST',#Acasti Pharma Inc-A
'RCKT',#Rocket Pharmaceuticals Inc
'RSVR',#Reservoir Media Inc
'UNCY',#Unicycive Therapeutics Inc
'QVCD',#QVC Inc Notes
'AGRI',#AgriFORCE Growing Systems Ltd
'DVAX',#德纳维制药
'POAI',#Predictive Oncology Inc
'PAVM',#PAVmed Inc
'OWLT',#Owlet Inc
'KLR',#Kaleyra Inc
'JFU',#玖富
'BNTC',#Benitec Biopharma Inc
'AUTL',#Autolus Therapeutics plc ADR
'DRTS',#Alpha Tau Medical Ltd
'FATE',#Fate Therapeutics Inc
'CDRO',#Codere Online Luxembourg SA
'YOU',#Clear Secure Inc-A
'CCNC',#码链新大陆
'EVAV',#Direxion Daily Electric and Aut
'OSH',#Oak Street Health Inc
'RUM',#Rumble Inc-A
'GCBC',#格林县万通金控
'MOBQ',#Mobiquity Technologies Inc
'AUVI',#Applied UV Inc
'SLQT',#SelectQuote Inc
'CYRN',#Cyren Ltd
'CPIX',#坎伯兰药业
'CHEK',#Check-Cap Ltd
'DAWN',#Day One Biopharmaceuticals Hold
'KIRK',#Kirkland's Inc
'CRBU',#Caribou Biosciences Inc
'CUE',#Cue Biopharma Inc
'FATBB',#FAT Brands Inc-B
'ADTX',#Aditxt Inc
'GROM',#Grom Social Enterprises Inc
'NUVB',#Nuvation Bio Inc-A
'ERESW',#East Resources Acquisition Co W
'CENN',#Centro Electric Group Ltd
'BTOG',#Bit Origin Ltd
'NVAX',#诺瓦瓦克斯医药
'VIEW',#View Inc-A
'PL_WS',#Planet Labs PBC Wt
'NLS',#鹦鹉螺体育
'GRND_WS',#Grindr Inc Wt
'CTOS_WS',#Custom Truck One Source Inc Wt
'QLGN',#Qualigen Therapeutics Inc
'LUCD',#Lucid Diagnostics Inc
'SYM',#Symbotic Inc-A
'NUWE',#Nuwellis Inc
'VLCN',#Volcon Inc
'RAYA',#雷亚电子
'QSIAW',#Quantum-Si Inc Wt
'CYXT',#Cyxtera Technologies Inc-A
'PACB',#Pacific Biosciences of Californ
'NDRA',#恩德拉生命科学
'MTEK',#Maris-Tech Ltd
'DOMO',#Domo Inc-B
'DUG',#二倍做空油气ETF-ProShares
'PT',#品钛
'CMRX',#Chimerix Inc
'ERY',#二倍做空能源ETF-Direxion
'LTRPB',#Liberty TripAdvisor Holdings In
'SOS',#艾斯欧艾斯
'KNTE',#Kinnate Biopharma Inc
'CASI',#CASI制药
'COCP',#Cocrystal Pharma Inc
'TXG',#10x Genomics Inc-A
'OCGN',#Ocugen Inc
'LRMR',#Larimar Therapeutics Inc
'KALV',#KalVista Pharmaceuticals Inc
'OGEN',#Oragenics Inc
'NSPR',#InspireMD Inc
'IVDAW',#Iveda Solutions Inc Wt
'IMH',#Impac Mortgage Holdings Inc
'HLBZ',#Helbiz Inc-A
'EVTL_WS',#Vertical Aerospace Ltd Wt
'EFOI',#Energy Focus Inc
'CZOO',#Cazoo Group Ltd-A
'BOXL',#宝视来
'DDL',#叮咚买菜
'ABOS',#Acumen Pharmaceuticals Inc
'LMB',#Limbach Holdings Inc
'BFAM',#Bright Horizons Family Solution
'VIVK',#Vivakor Inc
'PLRX',#Pliant Therapeutics Inc
'QH',#趣活
'TSRI',#TSR软件
'NGM',#NGM Biopharmaceuticals Inc
'ASPS',#Altisource Portfolio Solutions
'ZCMD',#众巢医学
'CNF',#泛华金融
'LUMO',#Lumos Pharma Inc
'NKTR',#内克塔治疗
'GAIA',#Gaia Inc-A
'ADVM',#Adverum Biotechnologies Inc
'TEDU',#达内教育
'OTLY',#Oatly Group AB ADR
'GOTU',#高途
'EXAI',#Exscientia plc ADR
'SUNL_WS',#Sunlight Financial Holdings Inc
'SNMP',#Evolve Transition Infrastructur
'SMIHW',#Summit Healthcare Acquisition C
'LFST',#LifeStance Health Group Inc
'IRRX_WS',#Integrated Rail and Resources A
'GFAI',#卫安智能
'EZGO',#易电行
'CPUH_WS',#Compute Health Acquisition Corp
'JKS',#晶科能源
'TWND',#Tailwind Acquisition Corp-A
'IONQ_WS',#IonQ Inc Wt
'GGE',#汉广厦房地产
'MIRO',#Miromatrix Medical Inc
'RGLS',#Regulus Therapeutics Inc
'INBX',#Inhibrx Inc
'ATRA',#Atara Biotherapeutics Inc
'ATXI',#大道制药
'PIII',#P3 Health Partners Inc-A
'IMTXW',#Immatics NV Wt
'ADPT',#Adaptive Biotechnologies Corp
'MASS',#908 Devices Inc
'DBGIW',#Digital Brands Group Inc Wt
'ICU',#SeaStar Medical Holding Corp
'BBIG',#Vinco Ventures Inc
'HRTG',#Heritage Insurance Holdings Inc
'CARA',#Cara Therapeutics Inc
'LABU',#三倍做多生物技术ETF-Direxion
'WIMI',#微美全息
'WE',#WeWork Inc-A
'TIRX',#天睿祥
'XPEV',#小鹏汽车
'UGRO',#urban-gro Inc
'VCYT',#Veracyte Inc
'TRKA',#Troika Media Group Inc
'FOXO',#FOXO Technologies Inc-A
'DGLY',#Digital Ally Inc
'BFLY_WS',#Butterfly Network Inc Wt
'MRNS',#Marinus Pharmaceuticals Inc
'BMEA',#Biomea Fusion Inc
'TERN',#Terns Pharmaceuticals Inc
'GLTO',#Galecto Inc
'BLIN',#Bridgeline Digital Inc
'CYTH',#Cyclo Therapeutics Inc
'GBIO',#Generation Bio Co
'CASA',#Casa Systems Inc
'VRCA',#Verrica制药
'ALVR',#AlloVir Inc
'FWP',#Forward Pharma AS ADR
'SATX',#SatixFy Communications Ltd
'DRIP',#二倍做空每日标普油气出口与生产
'VYNE',#VYNE Therapeutics Inc
'SMFR',#Sema4 Holdings Corp
'OBLG',#Oblong Inc
'NEXI',#NexImmune Inc
'GRRRW',#大猩猩科技(权证)
'BTTR',#Better Choice Co Inc
'GH',#Guardant Health Inc
'DYN',#Dyne Therapeutics Inc
'VXRT',#Vaxart Inc
'CNK',#喜满客影城
'PTN',#Palatin Technologies Inc
'RAPT',#RAPT Therapeutics Inc
'OLB',#The OLB Group Inc
'LOV',#Spark Networks SE ADR
'VRAR',#The Glimpse Group Inc
'LFLY',#Leafly Holdings Inc
'LOCL',#Local Bounti Corp
'SLN',#Silence Therapeutics plc ADR
'NTNX',#路坦力
'MDIA',#MediaCo Holding Inc-A
'NAAS',#能链智电
'AMRS',#阿米瑞斯
'RVMD',#Revolution Medicines Inc
'EHTH',#易康
'VSTM',#Verastem Inc
'LI',#理想汽车
'CCCC',#C4 Therapeutics Inc
'TRVI',#Trevi Therapeutics Inc
'REBN',#Reborn Coffee Inc
'PW_A',#Power REIT Series A Pfd
'ZEV',#Lightning eMotors Inc
'VBLT',#Vascular Biogenics Ltd
'LTCH',#Latch Inc
'HSDT',#Helius Medical Technologies Inc
'APCX',#AppTech Payments Corp
'ALLR',#Allarity Therapeutics Inc
'CTV',#Innovid Corp
'FLUX',#Flux Power Holdings Inc
'LMNR',#Limoneira Co
'GLMD',#Galmed Pharmaceuticals Ltd
'NVCR',#NovoCure Ltd
'ZYME',#Zymeworks Inc
'ECX',#亿咖通科技
'EH',#亿航智能
'LVWR_WS',#LiveWire Group Inc Wt
'SMWB',#Similarweb Ltd
'FUV',#Arcimoto Inc
'KC',#金山云
'EM',#怪兽充电
'POLA',#Polar Power Inc
'IH',#洪恩
'CABA',#Cabaletta Bio Inc
'FEMY',#Femasys Inc
'AXLA',#Axcella Health Inc
'MTP',#Midatech Pharma PLC ADR
'BJDX',#Bluejay Diagnostics Inc
'IONR',#ioneer Ltd ADS
'BIVI',#BioVie Inc-A
'SAI',#SAI TECH Global Corp-A
'OPFI_WS',#OppFi Inc Wt
'CUEN',#Cuentas Inc
'REAX',#The Real Brokerage Inc
'NVNO',#enVVeno Medical Corp
'ACRX',#AcelRx Pharmaceuticals Inc
'BSGM',#BioSig Technologies Inc
'NPCE',#NeuroPace Inc
'IONM',#Assure Holdings Corp
'RUMBW',#Rumble Inc Wt
'MYMD',#MyMD Pharmaceuticals Inc
'CERS',#Cerus Corp
'QTNT',#Quotient Ltd
'DNA_WS',#Ginkgo Bioworks Holdings Inc Wt
'AYTU',#Aytu BioPharma Inc
'OILD',#MicroSectors Oil & Gas Exp. & P
'HLTH',#Cue Health Inc
'MODD',#Modular Medical Inc
'QBTS',#D-Wave Quantum Inc
'DBD',#迪堡金融设备
'ANTE',#悦航阳光
'SNAL',#Snail Inc-A
'BTCS',#BTCS Inc
'LVTX',#LAVA Therapeutics NV
'ALPN',#Alpine Immune Sciences Inc
'COSM',#Cosmos Health Inc
'KYMR',#Kymera Therapeutics Inc
'WISA',#WiSA Technologies Inc
'STAB',#Statera BioPharma Inc
'SLAMW',#Slam Corp Wt
'REVB',#Revelation Biosciences Inc
'MSSAR',#Metal Sky Star Acquisition Corp
'JAGX',#Jaguar Health Inc
'IFIN_WS',#InFinT Acquisition Corp Wt
'DFLIW',#Dragonfly Energy Holdings Corp
'BFRIW',#Biofrontera Inc Wt
'PEV',#Phoenix Motor Inc
'SLGG',#Super League Gaming Inc
'SDC',#SmileDirectClub Inc-A
'YRD',#宜人金科
'NAVB',#Navidea Biopharmaceuticals Inc
'MRKR',#Marker Therapeutics Inc
'ACER',#Acer Therapeutics Inc
'AMC',#AMC院线
'BKYI',#生物钥匙国际
'THCH',#TH International Ltd-A
'IFBD',#讯鸟软件
'NRGD',#MicroSectors U.S. Big Oil Index
'IMMX',#Immix Biopharma Inc
'VEDU',#Visionary Education Technology
'SCRMW',#Screaming Eagle Acquisition Cor
'MREO',#Mereo BioPharma Group plc ADR
'LIPO',#Lipella Pharmaceuticals Inc
'SIDU',#Sidus Space Inc-A
'UTRS',#Minerva Surgical Inc
'SHCRW',#Sharecare Inc Wt
'PLXP',#PLx Pharma Inc
'PGYWW',#Pagaya Technologies Ltd Wt
'IDAI',#T Stamp Inc-A
'ICUCW',#SeaStar Medical Holding Corp Wt
'CLBR_WS',#Colombier Acquisition Corp Wt
'BWAQR',#Blue World Acquisition Corp Rt
'BKSY_WS',#BlackSky Technology Inc Wt
'ARVL',#Arrival Group
'STRC',#Sarcos Technology and Robotics
'AGBA',#AGBA Group Holding Ltd
'ZVSA',#ZyVersa Therapeutics Inc
'SKYH_WS',#Sky Harbour Group Corp Wt
'IRS_WS',#IRSA Inversiones y Representaci
'TCDA',#Tricida Inc
'CNDA_WS',#Concord Acquisition Corp II Wt
'ATNX',#Athenex Inc
'VIRX',#Viracta Therapeutics Inc
'AYRO',#AYRO Inc
'PROK',#ProKidney Corp-A
'JCICW',#Jack Creek Investment Corp Wt
'ADIL',#Adial Pharmaceuticals Inc
'TAL',#好未来
'CADL',#Candel Therapeutics Inc
'ATAI',#ATAI Life Sciences NV
'ICPT',#Intercept Pharmaceuticals Inc
'BBLN',#Babylon Holdings Ltd-A
'PRFX',#PainReform Ltd
'FNCH',#Finch Therapeutics Group Inc
'NOTE_WS',#FiscalNote Holdings Inc Wt
'XCUR',#Exicure Inc
'VCXB_WS',#10X Capital Venture Acquisition
'TUEM',#Tuesday Morning Corp
'PNTM_WS',#Pontem Corp Wt
'MBTCR',#Nocturne Acquisition Corp Rt
'LILMW',#Lilium NV Wt
'IRAAW',#Iris Acquisition Corp Wt
'CLOER',#Clover Leaf Capital Corp Rt
'AKAN',#Akanda Corp
'MLGO',#MicroAlgo Inc
'GETR',#Getaround Inc
'PAYOW',#Payoneer Global Inc Wt
'CHRS',#Coherus BioSciences Inc
'RCMT',#RCM Technologies Inc
'BKKT',#Bakkt Holdings Inc-A
'MF',#每日优鲜
'PTIX',#Protagenic Therapeutics Inc
'DMYS_WS',#dMY Technology Group Inc VI Wt
'CLXT',#Calyxt Inc
'RCRT',#Recruiter.com Group Inc
'AQB',#AquaBounty Technologies Inc
'POL',#Polished.com Inc
'UIHC',#United Insurance Holdings Corp
'GMVD',#G Medical Innovations Holdings
'WBX_WS',#Wallbox NV Wt
'MRDB',#MariaDB plc
'WEJO',#Wejo Group Ltd
'UP_WS',#Wheels Up Experience Inc Wt
'TMPOW',#Tempo Automation Holdings Inc W
'TENX',#Tenax Therapeutics Inc
'TALKW',#Talkspace Inc Wt
'POL_WS',#Polished.com Inc Wt
'NBSTW',#Newbury Street Acquisition Corp
'IDRA',#井寺制药
'GBRGW',#Goldenbridge Acquisition Ltd Wt
'FFIEW',#法拉第未来(权证)
'CRESW',#Cresud Wt
'ASCBR',#A SPAC II Acquisition Corp Rt
'LIZI',#荔枝
'BLPH',#Bellerophon Therapeutics Inc
'LANV',#复朗集团
'VINO',#Gaucho Group Holdings Inc
'EZFL',#EzFill Holdings Inc
'CANO_WS',#Cano Health Inc Wt
'VLON',#Vallon Pharmaceuticals Inc
'AVO',#Mission Produce Inc
'JUPW',#Jupiter Wellness Inc
'NOVVR',#Nova Vision Acquisition Corp Rt
'INM',#InMed Pharmaceuticals Inc
'CDROW',#Codere Online Luxembourg SA Wt
'DMYY_WS',#dMY Squared Technology Group In
'SMIT',#Schmitt Industries Inc
'MARK',#Remark Holdings Inc
'ZIVOW',#Zivo Bioscience Inc Wt
'ACHR_WS',#Archer Aviation Inc Wt
'AIMDW',#Ainos Inc Wt
'KAL',#Kalera plc
'BXRX',#Baudax Bio Inc
'SONDW',#Sonder Holdings Inc Wt
'PEARW',#Pear Holdings Corp Wt
'LGL_WS',#The LGL Group Inc Wt
'HOFVW',#Hall of Fame Resort & Entertain
'GSRMW',#GSR II Meteora Acquisition Corp
'GOVXW',#GeoVax Labs Inc Wt
'GETR_WS',#Getaround Inc Wt
'DTOCW',#Digital Transformation Opportun
'CMRAW',#Comera Life Sciences Holdings I
'BFIIW',#BurgerFi International Inc Wt
'ATNFW',#180 Life Sciences Corp Wt
'ANGHW',#Anghami Inc Wt
'ALTUW',#Altitude Acquisition Corp Wt
'CEI',#Camber Energy Inc
'DADA',#达达
'BTCM',#比特矿业
'PBYI',#Puma Biotechnology Inc
'CTXR',#Citius Pharmaceuticals Inc
'ACRO_WS',#Acropolis Infrastructure Acquis
'AUID',#authID Inc
'XOSWW',#Xos Inc Wt
'WNNR_WS',#Andretti Acquisition Corp Wt
'WLDSW',#Wearable Devices Ltd Wt
'TRCA_WS',#Twin Ridge Capital Acquisition
'SNRHW',#Senior Connect Acquisition Corp
'KORE_WS',#KORE Group Holdings Inc Wt
'EMLDW',#FTAC Emerald Acquisition Corp W
'CFFSW',#CF Acquisition Corp VII Wt
'BOXD_WS',#Boxed Inc Wt
'APGNW',#Apexigen Inc Wt
'APCXW',#AppTech Payments Corp Wt
'HOFV',#Hall of Fame Resort & Entertain
'EFHTR',#EF Hutton Acquisition Corp I Rt
'ATNF',#180 Life Sciences Corp
'THMO',#ThermoGenesis Holdings Inc
'CINGW',#Cingulate Inc Wt
'DRTSW',#Alpha Tau Medical Ltd Wt
'RENN',#人人网
'WNW',#知食谷
'YOTAW',#Yotta Acquisition Corp Wt
'WAVC_WS',#Waverley Capital Acquisition Co
'VLATW',#Valor Latitude Acquisition Corp
'SVFAW',#SVF Investment Corp Wt
'SPTKW',#SportsTek Acquisition Corp Wt
'SOLOW',#Electrameccanica Vehicles Corp
'MAPSW',#WM Technology Inc Wt
'LEGAW',#Lead Edge Growth Opportunities
'KINZW',#KINS Technology Group Inc Wt
'GIA_WS',#GigCapital5 Inc Wt
'GFGDW',#The Growth for Good Acquisition
'FLAG_WS',#First Light Acquisition Group I
'EUCRW',#Eucrates Biomedical Acquisition
'CPAQW',#Counter Press Acquisition Corp
'COOLW',#Corner Growth Acquisition Corp
'AIMAW',#Aimfinity Investment Corp I Wt-
'ADSEW',#Ads-Tec Energy PLC Wt
'ACDCW',#ProFrac Holding Corp Wt
'DFLI',#Dragonfly Energy Holdings Corp
'HTGM',#HTG Molecular Diagnostics Inc
'ML_WS',#MoneyLion Inc Wt
'MIMO_WS',#Airspan Networks Holdings Inc W
'GDNRW',#Gardiner Healthcare Acquisition
'BGRYW',#Berkshire Grey Inc Wt
'SSU',#SIGNA Sports United NV
'SATX_WS_A',#SatixFy Communications Ltd Wt
'MIMO_WS_A',#Airspan Networks Holdings Inc W
'HCDIZ',#Harbor Custom Development Inc W
'WTMAR',#Welsbach Technology Metals Acqu
'LMDXW',#LumiraDx Ltd Wt
'DHHCW',#DiamondHead Holdings Corp Wt
'GHIXW',#Gores Holdings IX Inc Wt
'NLSPW',#NLS Pharmaceutics Ltd Wt
'SBIGW',#SpringBig Holdings Inc Wt
'PPYAW',#Papaya Growth Opportunity Corp
'OSAAW',#ProSomnus Inc Wt
'NXGLW',#NexGel Inc Wt
'IMAQW',#International Media Acquisition
'IGACW',#IG Acquisition Corp Wt
'GGAAW',#Genesis Growth Tech Acquisition
'FATPW',#Fat Projects Acquisition Corp W
'DMS_WS',#Digital Media Solutions Inc Wt
'BODY_WS',#The Beachbody Co Inc Wt
'ANZUW',#Anzu Special Acquisition Corp I
'EVK',#华瑞服装
'LCFYW',#Locafy Ltd Wt
'BRSHW',#Bruush Oral Care Inc Wt
'NRBO',#NeuroBo Pharmaceuticals Inc
'SSU_WS',#SIGNA Sports United NV Wt
'QTEKW',#QualTek Services Inc Wt
'TRKAW',#Troika Media Group Inc Wt
'SQLLW',#SeqLL Inc Wt
'PWUPW',#PowerUp Acquisition Corp Wt
'OXUSW',#Oxus Acquisition Corp Wt
'GLTA_WS',#Galata Acquisition Corp Wt
'CVII_WS',#Churchill Capital Corp VII Wt
'BRIVW',#B. Riley Principal 250 Merger C
'BIOTW',#Biotech Acquisition Co Wt
'IPVF_WS',#InterPrivate III Financial Part
'KBNTW',#Kubient Inc Wt
'EVOJW',#Evo Acquisition Corp Wt
'LJAQW',#LightJump Acquisition Corp Wt
'JGGCR',#Jaguar Global Growth Corp I Rt
'AGRIW',#AgriFORCE Growing Systems Ltd W
'RVSNW',#Rail Vision Ltd Wt
'XBIOW',#Xenetic Biosciences Inc Wt
'VRMEW',#VerifyMe Inc Wt
'UPTDW',#TradeUP Acquisition Corp Wt
'SNAXW',#Stryve Foods Inc Wt
'SMFRW',#Sema4 Holdings Corp Wt
'SHPW_WS',#Shapeways Holdings Inc Wt
'OWLT_WS',#Owlet Inc Wt
'NSTB_WS',#Northern Star Investment Corp I
'KNSW_WS',#KnightSwan Acquisition Corp Wt
'HIPO_WS',#Hippo Holdings Inc Wt
'GLLIR',#Globalink Investment Inc Rt
'DRMAW',#Dermata Therapeutics Inc Wt
'CHEKZ',#Check-Cap Ltd Wt-C
'AREBW',#American Rebel Holdings Inc Wt
'ALSAW',#Alpha Star Acquisition Corp Wt
'YGMZ',#明珠货运
'EJH',#e家快服
'TCBPW',#TC BioPharm (Holdings) plc Wt
'OXBRW',#Oxbridge Re Holdings Ltd Wt
'MACAW',#Moringa Acquisition Corp Wt
'MTEKW',#Maris-Tech Ltd Wt
'AMTI',#Applied Molecular Transport Inc
'TLGYW',#TLGY Acquisition Corp Wt
'DUNEW',#Dune Acquisition Corp Wt
'DISAW',#Disruptive Acquisition Corp I W
'ACQRW',#Independence Holdings Corp Wt
'IQMDW',#Intelligent Medicine Acquisitio

]

zhonggaigu = [
    'WB',  # 微博
    'BABA',  # 阿里巴巴
    'NTES',  # 网易
    'SOHU',  # 搜狐
    'BIDU',  # 百度
    'TCOM',  # 携程
    # 'JOBS',  # 前程无忧
    'TAL',  # 好未来
    'EDU',  # 新东方
    'SFUN',  # 房天下
    'VNET',  # 世纪互联
    'RENN',  # 人人公司
    'FENG',  # 凤凰新媒体
    'VIPS',  # 唯品会
    'YY',  # 欢聚集团
    'LITB',  # 兰亭集势
    'BTCM',  # 比特矿业
    'ATHM',  # 汽车之家
    'LEJU',  # 乐居
    'CMCM',  # 猎豹移动
    'TOUR',  # 途牛
    'JD',  # 京东
    'XNET',  # 迅雷
    'MOMO',  # 挚文集团
    'BZUN',  # 宝尊电商
    'YRD',  # 宜人金科
    'COE',  # 51Talk
    'ZTO',  # 中通
    'BEST',  # 百世集团
    'SECO',  # 寺库
    'QD',  # 趣店
    'FINV',  # 信也科技
    'LX',  # 乐信
    'JT',  # 简普科技
    'BILI',  # 哔哩哔哩
    'IQ',  # 爱奇艺
    'HUYA',  # 虎牙
    'UXIN',  # 优信
    'PDD',  # 拼多多
    'NIO',  # 蔚来
    'YI',  # 1药网
    'QTT',  # 趣头条
    'VIOT',  # 云米科技
    'XYF',  # 小赢科技
    # 'LAIX',  # 流利说
    'CTK',  # 触宝
    'NIU',  # 小牛电动
    'PT',  # 品钛
    'MOGU',  # 蘑菇街
    'TME',  # 腾讯音乐
    'WEI',  # 微贷网
    'TC',  # 团车
    'QFIN',  # 360数科
    'TIGR',  # 老虎证券
    'DOYU',  # 斗鱼
    'YJ',  # 云集
    'CAN',  # 嘉楠科技
    'LIZI',  # 荔枝
    'COE',  # 51Talk
    'SY',  # 新氧
    'EH',  # 亿航
    'GOTU',  # 高途
    'DAO',  # 网易有道
    'KC',  # 金山云
    'BEKE',  # 贝壳
    'LI',  # 理想汽车
    'YSG',  # 逸仙电商
    'KRKR',  # 36氪
    'XPEV',  # 小鹏汽车
    'GDS',  # 万国数据
    'DADA',  # 达达集团
    'MOMO',  # 挚文集团
    # 'QK',  #
    'MF',  # 每日优鲜
    'DDL',  # 叮咚买菜
    'ZH',  # 知乎
    'DIDI',  # 滴滴(已退市)
    'YMM',  # 满帮
    'MF',  # 每日优鲜
    'ZME',  # 掌门教育
    'EM',  # 怪兽充电

]

zhonggaigu_nyse = [

]
us_select: list = [
    'KO', 'DE', 'PG', 'PCAR', 'MRK', 'CB', 'JNJ', 'PEP'
]
if __name__ == '__main__':
    pass
    slist = [

    ]

    result_list = []

    slist += zhonggaigu

    for i in slist:
        result_element = []
        try:
            df = ef.stock.get_quote_history(i, '20221207', '20221207', klt=101)
        except:
            pass
        if len(df) == 0:
            continue

        result_element.append(df['股票代码'].iloc[0])
        result_element.append(df['股票名称'].iloc[0])
        print('i:{},result_element[0]:{},result_element[1]:{}'.format(i, result_element[0], result_element[1]))
    #     result_list.append(result_element)
    #
    # for i in result_list:
    #     print("'{}', #{}".format(i[0], i[1]))

# 中字头股票：


bak = [
    # 沪深三百 周线K值低于30 成交额大于5亿元。
    '000301',
    '002050',
    '002241',
    '002371',
    '002459',
    '002466',
    '002714',
    '002812',
    '002920',
    '300014',
    '300450',
    '300498',
    '300751',
    '300750',
    '300763',
    '300957',
    '600009',
    '600188',
    '600438',
    '601225',
    '603185',
    '688363',
    # 沪深三百 换手率高 上升通道
    '601658',
    '002064',
    '601919',
    '600426',
    '600050',
    '000425',
    '600176',
    '002142',
    '601668',
    '601800',
    # 沪深三百 11月日均成交额大于15亿
    '600519',
    '002603',
    '300750',
    '300059',
    '601012',
    '002317',
    '000858',
    '002466',
    '002594',
    '002241',
    '600536',
    '601899',
    '300274',
    '002460',
    '002432',
    '600036',
    '601318',
    '601888',
    '600056',
    '603259',
    '600438',
    '000002',
    '000568',
    '002475',
    '000032',
    '600522',
    '002371',
    '000625',
    '600196',
    '002077',
    '002129',
    '000948',
    '688185',
    '600048',
    '000831',
    '000001',
    '600111',
    '300014',
    '600276',
    '600745',
    '002271',
    '300760',
    '000792',
    '600050',
    '600418',
    '000333',
    '603986',
    '002223',
    '600809',
    '601788',
    '601668',
    # 沪深三百 日线kdj金叉
    '600196',
    '603806',
    '603882',
    '605499',
    '000938',
    '300003',
    '300496',
    '300628',
    '300751',
    '300866',
    # kdj买入信号，按换手率，成交额排序
    '002335',
    '600478',
    '603858',
    '600062',
    '300925',
    '688223',
    '600196',
    '000681',
    '000721',
    # 平仓品种，尝试做T
    '600026',
    '600613',
    # 中字头 日线kdj值比较低
]

ganggutong = [

    '00001',  # 长和　　　　　　
    '00002',  # 中电控股　　　　
    '00003',  # 香港中华煤气　　
    '00004',  # 九龙仓集团　　　
    '00005',  # 汇丰控股　　　　
    '00006',  # 电能实业　　　　
    '00008',  # 电讯盈科　　　　
    '00011',  # 恒生银行　　　　
    '00012',  # 恒基地产　　　　
    '00013',  # 和黄医药　　　　
    '00014',  # 希慎兴业　　　　
    '00016',  # 新鸿基地产　　　
    '00017',  # 新世界发展　　　
    '00019',  # 太古股份公司Ａ　
    '00020',  # 商汤－Ｗ　　　　
    '00023',  # 东亚银行　　　　
    '00027',  # 银河娱乐　　　　
    '00038',  # 第一拖拉机股份　
    '00066',  # 港铁公司　　　　
    '00083',  # 信和置业　　　　
    '00101',  # 恒隆地产　　　　
    '00107',  # 四川成渝高速公路
    '00123',  # 越秀地产　　　　
    '00135',  # 昆仑能源　　　　
    '00136',  # 中国儒意　　　　
    '00144',  # 招商局港口　　　
    '00148',  # 建滔集团　　　　
    '00151',  # 中国旺旺　　　　
    '00152',  # 深圳国际　　　　
    '00165',  # 中国光大控股　　
    '00168',  # 青岛啤酒股份　　
    '00175',  # 吉利汽车　　　　
    '00177',  # 江苏宁沪高速公路
    '00179',  # 德昌电机控股　　
    '00187',  # 京城机电股份　　
    '00189',  # 东岳集团　　　　
    '00200',  # 新濠国际发展　　
    '00220',  # 统一企业中国　　
    '00241',  # 阿里健康　　　　
    '00257',  # 光大环境　　　　
    '00267',  # 中信股份　　　　
    '00268',  # 金蝶国际　　　　
    '00270',  # 粤海投资　　　　
    '00285',  # 比亚迪电子　　　
    '00288',  # 万洲国际　　　　
    '00291',  # 华润啤酒　　　　
    '00293',  # 国泰航空　　　　
    '00303',  #
    '00316',  # 东方海外国际　　
    '00317',  # 中船防务　　　　
    '00322',  # 康师傅控股　　　
    '00323',  # 马鞍山钢铁股份　
    '00336',  # 华宝国际　　　　
    '00338',  # 上海石油化工股份
    '00345',  #
    '00347',  # 鞍钢股份　　　　
    '00354',  # 中国软件国际　　
    '00358',  # 江西铜业股份　　
    '00371',  # 北控水务集团　　
    '00384',  # 中国燃气　　　　
    '00386',  # 中国石油化工股份
    '00388',  # 香港交易所　　　
    '00390',  # 中国中铁　　　　
    '00392',  # 北京控股　　　　
    '00425',  # 敏实集团　　　　
    '00460',  # 四环医药　　　　
    '00467',  # 联合能源集团　　
    '00489',  # 东风集团股份　　
    '00493',  # 国美零售　　　　
    '00512',  # 远大医药　　　　
    '00522',  #
    '00525',  # 广深铁路股份　　
    '00535',  # 金地商置　　　　
    '00548',  # 深圳高速公路股份
    '00551',  # 裕元集团　　　　
    '00553',  # 南京熊猫电子股份
    '00558',  # 力劲科技　　　　
    '00564',  # 郑煤机　　　　　
    '00568',  # 山东墨龙　　　　
    '00570',  # 中国中药　　　　
    '00586',  # 海螺创业　　　　
    '00588',  # 北京北辰实业股份
    '00598',  # 中国外运　　　　
    '00604',  # 深圳控股　　　　
    '00631',  # 三一国际　　　　
    '00636',  # 嘉里物流　　　　
    '00656',  # 复星国际　　　　
    '00659',  # 新创建集团　　　
    '00667',  # 中国东方教育　　
    '00669',  # 创科实业　　　　
    '00670',  # 中国东方航空股份
    '00683',  # 嘉里建设　　　　
    '00688',  # 中国海外发展　　
    '00696',  # 中国民航信息网络
    '00700',  # 腾讯控股　　　　
    '00719',  # 山东新华制药股份
    '00728',  # 中国电信　　　　
    '00753',  # 中国国航　　　　
    '00754',  # 合生创展集团　　
    '00762',  # 中国联通　　　　
    '00763',  # 中兴通讯　　　　
    '00772',  # 阅文集团　　　　
    '00780',  # 同程旅行　　　　
    '00788',  # 中国铁塔　　　　
    '00811',  # 新华文轩　　　　
    '00817',  # 中国金茂　　　　
    '00836',  # 华润电力　　　　
    '00839',  # 中教控股　　　　
    '00853',  # 微创医疗　　　　
    '00857',  # 中国石油股份　　
    '00867',  # 康哲药业　　　　
    '00868',  # 信义玻璃　　　　
    '00873',  # 世茂服务　　　　
    '00874',  # 白云山　　　　　
    '00880',  # 澳博控股　　　　
    '00881',  # 中升控股　　　　
    '00883',  # 中国海洋石油　　
    '00884',  # 旭辉控股集团　　
    '00895',  # 东江环保　　　　
    '00902',  # 华能国际电力股份
    '00909',  # 明源云　　　　　
    '00914',  # 海螺水泥　　　　
    '00916',  # 龙源电力　　　　
    '00921',  # 海信家电　　　　
    '00939',  # 建设银行　　　　
    '00941',  # 中国移动　　　　
    '00956',  # 新天绿色能源　　
    '00960',  # 龙湖集团　　　　
    '00966',  # 中国太平　　　　
    '00968',  # 信义光能　　　　
    '00981',  # 中芯国际　　　　
    '00991',  # 大唐发电　　　　
    '00992',  # 联想集团　　　　
    '00995',  # 安徽皖通高速公路
    '00998',  # 中信银行　　　　
    '01024',  # 快手－Ｗ　　　　
    '01030',  # 新城发展　　　　
    '01033',  # 中石化油服　　　
    '01038',  # 长江基建集团　　
    '01044',  # 恒安国际　　　　
    '01053',  # 重庆钢铁股份　　
    '01055',  # 中国南方航空股份
    '01057',  # 浙江世宝　　　　
    '01060',  # 阿里影业　　　　
    '01065',  # 天津创业环保股份
    '01066',  # 威高股份　　　　
    '01071',  # 华电国际电力股份
    '01072',  # 东方电气　　　　
    '01088',  # 中国神华　　　　
    '01093',  # 石药集团　　　　
    '01099',  # 国药控股　　　　
    '01108',  # 洛阳玻璃股份　　
    '01109',  # 华润置地　　　　
    '01113',  # 长实集团　　　　
    '01128',  # 永利澳门　　　　
    '01138',  # 中远海能　　　　
    '01157',  # 中联重科　　　　
    '01171',  # 兖矿能源　　　　
    '01177',  # 中国生物制药　　
    '01186',  # 中国铁建　　　　
    '01193',  # 华润燃气　　　　
    '01199',  # 中远海运港口　　
    '01208',  # 五矿资源　　　　
    '01209',  # 华润万象生活　　
    '01211',  # 比亚迪股份　　　
    '01238',  # 宝龙地产　　　　
    '01268',  # 美东汽车　　　　
    '01288',  # 农业银行　　　　
    '01299',  # 友邦保险　　　　
    '01308',  # 海丰国际　　　　
    '01310',  # 香港宽频　　　　
    '01313',  # 华润水泥控股　　
    '01316',  # 耐世特　　　　　
    '01330',  # 绿色动力环保　　
    '01336',  # 新华保险　　　　
    '01339',  # 中国人民保险集团
    '01347',  # 华虹半导体　　　
    '01349',  # 复旦张江　　　　
    '01359',  # 中国信达　　　　
    '01368',  # 特步国际　　　　
    '01375',  # 中州证券　　　　
    '01378',  # 中国宏桥　　　　
    '01385',  # 上海复旦　　　　
    '01398',  # 工商银行　　　　
    '01456',  # 国联证券　　　　
    '01458',  # 周黑鸭　　　　　
    '01513',  # 丽珠医药　　　　
    '01516',  # 融创服务　　　　
    '01528',  # 红星美凯龙　　　
    '01530',  # 三生制药　　　　
    '01548',  # 金斯瑞生物科技　
    '01579',  # 颐海国际　　　　
    '01585',  # 雅迪控股　　　　
    '01618',  # 中国中冶　　　　
    '01635',  # 大众公用　　　　
    '01658',  # 邮储银行　　　　
    '01691',  # ＪＳ环球生活　　
    '01717',  # 澳优　　　　　　
    '01766',  # 中国中车　　　　
    '01772',  # 赣锋锂业　　　　
    '01776',  # 广发证券　　　　
    '01787',  # 山东黄金　　　　
    '01800',  # 中国交通建设　　
    '01801',  # 信达生物　　　　
    '01810',  # 小米集团－Ｗ　　
    '01811',  # 中广核新能源　　
    '01812',  # 晨鸣纸业　　　　
    '01813',  # 合景泰富集团　　
    '01816',  # 中广核电力　　　
    '01821',  #
    '01833',  # 平安好医生　　　
    '01839',  # 中集车辆　　　　
    '01858',  # 春立医疗　　　　
    '01876',  # 百威亚太　　　　
    '01877',  # 君实生物　　　　
    '01880',  # 中国中免　　　　
    '01882',  # 海天国际　　　　
    '01888',  # 建滔积层板　　　
    '01898',  # 中煤能源　　　　
    '01907',  # 中国旭阳集团　　
    '01908',  # 建发国际集团　　
    '01919',  # 中远海控　　　　
    '01928',  # 金沙中国有限公司
    '01929',  # 周大福　　　　　
    '01951',  # 锦欣生殖　　　　
    '01963',  # 重庆银行　　　　
    '01972',  # 太古地产　　　　
    '01988',  # 民生银行　　　　
    '01995',  # 旭辉永升服务　　
    '01997',  # 九龙仓置业　　　
    '01999',  # 敏华控股　　　　
    '02005',  # 石四药集团　　　
    '02007',  # 碧桂园　　　　　
    '02009',  # 金隅集团　　　　
    '02013',  # 微盟集团　　　　
    '02015',  # 理想汽车－Ｗ　　
    '02016',  # 浙商银行　　　　
    '02018',  # 瑞声科技　　　　
    '02020',  # 安踏体育　　　　
    '02039',  # 中集集团　　　　
    '02068',  # 中铝国际　　　　
    '02096',  # 先声药业　　　　
    '02128',  # 中国联塑　　　　
    '02137',  # 腾盛博药－Ｂ　　
    '02150',  # 奈雪的茶　　　　
    '02158',  # 医渡科技　　　　
    '02160',  # 心通医疗－Ｂ　　
    '02171',  # 科济药业－Ｂ　　
    '02186',  # 绿叶制药　　　　
    '02192',  # 医脉通　　　　　
    '02196',  # 复星医药　　　　
    '02202',  # 万科企业　　　　
    '02208',  # 金风科技　　　　
    '02218',  # 安德利果汁　　　
    '02238',  # 广汽集团　　　　
    '02252',  # 微创机器人－Ｂ　
    '02269',  # 药明生物　　　　
    '02282',  # 美高梅中国　　　
    '02285',  # 泉峰控股　　　　
    '02313',  # 申洲国际　　　　
    '02314',  # 理文造纸　　　　
    '02318',  # 中国平安　　　　
    '02319',  # 蒙牛乳业　　　　
    '02328',  # 中国财险　　　　
    '02331',  # 李宁　　　　　　
    '02333',  # 长城汽车　　　　
    '02338',  # 潍柴动力　　　　
    '02357',  # 中航科工　　　　
    '02359',  # 药明康德　　　　
    '02380',  # 中国电力　　　　
    '02382',  # 舜宇光学科技　　
    '02388',  # 中银香港　　　　
    '02400',  # 心动公司　　　　
    '02500',  # 启明医疗－Ｂ　　
    '02588',  # 中银航空租赁　　
    '02600',  # 中国铝业　　　　
    '02601',  # 中国太保　　　　
    '02607',  # 上海医药　　　　
    '02611',  # 国泰君安　　　　
    '02618',  # 京东物流　　　　
    '02628',  # 中国人寿　　　　
    '02669',  # 中海物业　　　　
    '02688',  # 新奥能源　　　　
    '02689',  # 玖龙纸业　　　　
    '02727',  # 上海电气　　　　
    '02772',  # 中梁控股　　　　
    '02777',  # 富力地产　　　　
    '02800',  # 盈富基金　　　　
    '02828',  # 恒生中国企业　　
    '02866',  # 中远海发　　　　
    '02869',  # 绿城服务　　　　
    '02880',  # 辽港股份　　　　
    '02883',  # 中海油田服务　　
    '02899',  # 紫金矿业　　　　
    '03033',  # 南方恒生科技　　
    '03037',  # 南方恒指ＥＴＦ　
    '03067',  # 安硕恒生科技　　
    '03311',  # 中国建筑国际　　
    '03319',  # 雅生活服务　　　
    '03320',  # 华润医药　　　　
    '03323',  # 中国建材　　　　
    '03328',  # 交通银行　　　　
    '03331',  # 维达国际　　　　
    '03347',  # 泰格医药　　　　
    '03360',  # 远东宏信　　　　
    '03369',  # 秦港股份　　　　
    '03383',  # 雅居乐集团　　　
    '03396',  # 联想控股　　　　
    '03606',  # 福耀玻璃　　　　
    '03618',  # 重庆农村商业银行
    '03633',  # 中裕能源　　　　
    '03669',  # 永达汽车　　　　
    '03678',  # 弘业期货　　　　
    '03690',  # 美团－Ｗ　　　　
    '03692',  # 翰森制药　　　　
    '03759',  # 康龙化成　　　　
    '03799',  # 达利食品　　　　
    '03800',  # 协鑫科技　　　　
    '03808',  # 中国重汽　　　　
    '03866',  # 青岛银行　　　　
    '03868',  # 信义能源　　　　
    '03888',  # 金山软件　　　　
    '03898',  # 时代电气　　　　
    '03899',  # 中集安瑞科　　　
    '03900',  # 绿城中国　　　　
    '03908',  # 中金公司　　　　
    '03958',  # 东方证券　　　　
    '03968',  # 招商银行　　　　
    '03969',  # 中国通号　　　　
    '03988',  # 中国银行　　　　
    '03990',  # 美的置业　　　　
    '03993',  # 洛阳钼业　　　　
    '03996',  # 中国能源建设　　
    '03998',  # 波司登　　　　　
    '06030',  # 中信证券　　　　
    '06060',  # 众安在线　　　　
    '06066',  # 中信建投证券　　
    '06078',  # 海吉亚医疗　　　
    '06098',  # 碧桂园服务　　　
    '06099',  # 招商证券　　　　
    '06110',  # 滔搏　　　　　　
    '06127',  # 昭衍新药　　　　
    '06158',  # 正荣地产　　　　
    '06160',  # 百济神州　　　　
    '06178',  # 光大证券　　　　
    '06185',  # 康希诺生物　　　
    '06186',  # 中国飞鹤　　　　
    '06196',  # 郑州银行　　　　
    '06198',  # 青岛港　　　　　
    '06606',  # 诺辉健康－Ｂ　　
    '06618',  # 京东健康　　　　
    '06655',  # 华新水泥　　　　
    '06680',  # 金力永磁　　　　
    '06690',  # 海尔智家　　　　
    '06699',  # 时代天使　　　　
    '06806',  # 申万宏源　　　　
    '06808',  # 高鑫零售　　　　
    '06818',  # 中国光大银行　　
    '06821',  # 凯莱英　　　　　
    '06826',  # 昊海生物科技　　
    '06837',  # 海通证券　　　　
    '06862',  # 海底捞　　　　　
    '06865',  # 福莱特玻璃　　　
    '06869',  # 长飞光纤光缆　　
    '06881',  # 中国银河　　　　
    '06886',  # HTSC
    '06969',  # 思摩尔国际　　　
    '06993',  # 蓝月亮集团　　　
    '09633',  # 农夫山泉　　　　
    '09666',  # 金科服务　　　　
    '09688',  # 再鼎医药　　　　
    '09696',  # 天齐锂业　　　　
    '09858',  # 优然牧业　　　　
    '09863',  # 零跑汽车　　　　
    '09868',  # 小鹏汽车－Ｗ　　
    '09869',  # 海伦司　　　　　
    '09899',  # 云音乐　　　　　
    '09922',  # 九毛九　　　　　
    '09923',  # 移卡　　　　　　
    '09926',  # 康方生物－Ｂ　　
    '09959',  # 联易融科技－Ｗ　
    '09969',  # 诺诚健华－Ｂ　　
    '09987',  # 百胜中国　　　　
    '09989',  # 海普瑞　　　　　
    '09992',  # 泡泡玛特　　　　
    '09995',  # 荣昌生物－Ｂ　　
    '09997',  # 康基医疗　　　　

]

us_stock_202212 = [
    'ABCB',
    'ACA',
    'ADUS',
    'AGGP',
    'ALB',
    'ALG',
    'ALK',
    'AMAL',
    'AMN',
    'AMR',
    'APA',
    'ARES',
    'ARLP',
    'ATGE',
    'ATW',
    'AXN',
    'AXNX',
    'AYI',
    'AZPN',
    'BANF',
    'BANR',
    'BAP',
    'BERK',
    'BHF',
    'BIF',
    'BKOR',
    'BMS',
    'CAR',
    'CATC',
    'CBP',
    'CBT',
    'CCBG',
    'CCFI',
    'CCRN',
    'CF',
    'CFD',
    'CFR',
    'CHCO',
    'CHK',
    'CIVI',
    'CLMT',
    'CLW',
    'CNQ',
    'CNXN',
    'COGT',
    'COP',
    'CR',
    'CRED',
    'CRK',
    'CSWI',
    'CTS',
    'CTVA',
    'CVI',
    'CWCO',
    'DDR',
    'DDS',
    'DEJ',
    'DGAS',
    'DIT',
    'DK',
    'DMLP',
    'DRV',
    'DVN',
    'DWRE',
    'DXD',
    'DYB',
    'EDZ',
    'EEV',
    'EFSC',
    'EMAG',
    'EOG',
    'EQBK',
    'EQT',
    'ERF',
    'ERX',
    'ERY',
    'EUO',
    'EXM',
    'FANG',
    'FBNC',
    'FC',
    'FCB',
    'FCBC',
    'FCNCA',
    'FENY',
    'FIBK',
    'FNGD',
    'FSS',
    'FTXN',
    'FXP',
    'GBCI',
    'GJM',
    'GLD',
    'GLL',
    'GLNG',
    'GRIN',
    'GTLS',
    'GUSH',
    'HAE',
    'HCC',
    'HEUS',
    'HFWA',
    'HLIT',
    'HQY',
    'HTCH',
    'HTHT',
    'HUM',
    'HWC',
    'IBA',
    'IBKR',
    'IBOC',
    'ICFI',
    'IEO',
    'IEP',
    'IMO',
    'INDB',
    'INDU',
    'INSW',
    'IONS',
    'IXC',
    'IYE',
    'JCO',
    'JHS',
    'KEX',
    'KFN',
    'KNSL',
    'KRTX',
    'KRU',
    'KRUS',
    'LEU',
    'LHCG',
    'LKFN',
    'LNG',
    'LNTH',
    'LPLA',
    'LTHM',
    'MBG',
    'MIC',
    'MICR',
    'MLI',
    'MLPQ',
    'MLPS',
    'MPB',
    'MPC',
    'MPO',
    'MRO',
    'MTB',
    'MTDR',
    'MUR',
    'MUSA',
    'MWG',
    'NBHC',
    'NBR',
    'NBTB',
    'NC',
    'NDP',
    'NE',
    'NFE',
    'NOG',
    'NOV',
    'NRGU',
    'NSM',
    'OASI',
    'OILU',
    'ORA',
    'OXY',
    'PARR',
    'PBF',
    'PCC',
    'PCTY',
    'PDCE',
    'PGC',
    'PLMR',
    'PNK',
    'PVD',
    'PXD',
    'PXE',
    'PXI',
    'PXP',
    'REW',
    'ROL',
    'RRM',
    'RSTI',
    'RVNC',
    'RXDX',
    'RYE',
    'SCC',
    'SDS',
    'SENEA',
    'SIGI',
    'SM',
    'SNDX',
    'SOXS',
    'SPEX',
    'SPFI',
    'SQM',
    'SQQQ',
    'SRS',
    'SSB',
    'STZ',
    'SWAV',
    'SWIN',
    'SWIR',
    'SYBT',
    'TBF',
    'TCAP',
    'TCBK',
    'TECS',
    'TGD',
    'TLR',
    'TMP',
    'TMV',
    'TNP',
    'TPGI',
    'TRMK',
    'TRNS',
    'TRT',
    'TTT',
    'TWNK',
    'UAN',
    'UBSI',
    'UCBI',
    'UI',
    'UNM',
    'USOI',
    'VAL',
    'VDE',
    'VHS',
    'VIST',
    'VIVO',
    'VLO',
    'VNOM',
    'WCG',
    'WEXP',
    'WFM',
    'WSBC',
    'WTM',
    'WWE',
    'XLE',
    'XOP',
    'XPEL',
    'YANG',
]

kechuangban = [
'688141',#N杰华特
'688051',#佳华科技
'688147',#N微导
'688428',#诺诚健华-U
'688158',#优刻得-W
'688670',#金迪克
'688351',#微电生理-U
'688561',#奇安信-U
'688235',#百济神州-U
'688331',#荣昌生物
'688575',#亚辉龙
'688426',#康为世纪
'688500',#慧辰股份
'688246',#嘉和美康
'688588',#凌志软件
'688212',#澳华内镜
'688513',#苑东生物
'688293',#奥浦迈
'688276',#百克生物
'688793',#倍轻松
'688617',#惠泰医疗
'688555',#*ST泽达
'688489',#三未信安
'688278',#特宝生物
'688258',#卓易信息
'688060',#云涌科技
'688579',#山大地纬
'688161',#威高骨科
'689009',#九号公司-WD
'688222',#成都先导
'688382',#益方生物-U
'688292',#浩瀚深度
'688016',#心脉医疗
'688114',#华大智造
'688039',#当虹科技
'688111',#金山办公
'688211',#中科微至
'688098',#申联生物
'688606',#奥泰生物
'688265',#南模生物
'688169',#石头科技
'688369',#致远互联
'688321',#微芯生物
'688677',#海泰新光
'688787',#海天瑞声
'688607',#康众医疗
'688767',#博拓生物
'688131',#皓元医药
'688089',#嘉必优
'688192',#迪哲医药-U
'688311',#盟升电子
'688031',#星环科技-U
'688139',#海尔生物
'688004',#博汇科技
'688029',#南微医学
'688639',#华恒生物
'688026',#洁特生物
'688298',#东方生物
'688189',#南新制药
'688058',#宝兰德
'688203',#海正生材
'688301',#奕瑞科技
'688590',#新致软件
'688085',#三友医疗
'688687',#凯因科技
'688280',#精进电动-UW
'688075',#安旭生物
'688300',#联瑞新材
'688375',#国博电子
'688009',#中国通号
'688205',#德科立
'688102',#斯瑞新材
'688271',#联影医疗
'688137',#近岸蛋白
'688253',#英诺特
'688277',#天智航-U
'688244',#永信至诚
'688656',#浩欧博
'688105',#诺唯赞
'688038',#中科通达
'688517',#金冠电气
'688680',#海优新材
'688273',#麦澜德
'688365',#光云科技
'688073',#毕得医药
'688013',#天臣医疗
'688319',#欧林生物
'688050',#爱博医疗
'688023',#安恒信息
'688626',#翔宇医疗
'688119',#中钢洛耐
'688285',#高铁电气
'688289',#圣湘生物
'688318',#财富趋势
'688046',#药康生物
'688317',#之江生物
'688312',#燕麦科技
'688737',#中自科技
'688373',#盟科药业-U
'688113',#联测科技
'688096',#京源环保
'688616',#西力科技
'688468',#科美诊断
'688358',#祥生医疗
'688503',#聚和材料
'688236',#春立医疗
'688238',#和元生物
'688509',#正元地信
'688310',#迈得医疗
'688129',#东来技术
'688488',#艾迪药业
'688196',#卓越新能
'688613',#奥精医疗
'688295',#中复神鹰
'688288',#鸿泉物联
'688088',#虹软科技
'688323',#瑞华泰
'688181',#八亿时空
'688166',#博瑞医药
'688290',#景业智能
'688163',#赛伦生物
'688336',#三生国健
'688100',#威胜信息
'688030',#山石网科
'688133',#泰坦科技
'688578',#艾力斯-U
'688297',#中无人机
'688041',#海光信息
'688217',#睿昂基因
'688609',#九联科技
'688150',#莱特光电
'688055',#龙腾光电
'688260',#昀冢科技
'688101',#三达膜
'688520',#神州细胞-U
'688257',#新锐股份
'688022',#瀚川智能
'688728',#格科微
'688621',#阳光诺和
'688092',#爱科科技
'688021',#奥福环保
'688219',#会通股份
'688505',#复旦张江
'688228',#开普云
'688255',#凯尔达
'688399',#硕世生物
'688201',#信安世纪
'688132',#邦彦技术
'688197',#首药控股-U
'688466',#金科环境
'688586',#江航装备
'688367',#工大高科
'688108',#赛诺医疗
'688095',#福昕软件
'688393',#安必平
'688225',#亚信安全
'688356',#键凯科技
'688229',#博睿数据
'688117',#圣诺生物
'688733',#壹石通
'688272',#富吉瑞
'688076',#诺泰生物
'688510',#航亚科技
'688165',#埃夫特-U
'688127',#蓝特光学
'688538',#和辉光电-U
'688067',#爱威科技
'688057',#金达莱
'688252',#天德钰
'688418',#震有科技
'688068',#热景生物
'688330',#宏力达
'688303',#大全能源
'688389',#普门科技
'688777',#中控技术
'688171',#纬德信息
'688191',#智洋创新
'688398',#赛特新材
'688232',#新点软件
'688065',#凯赛生物
'688618',#三旺通信
'688287',#观典防务
'688182',#灿勤科技
'688660',#电气风电
'688159',#有方科技
'688090',#瑞松科技
'688360',#德马科技
'688315',#诺禾致源
'688220',#翱捷科技-U
'688619',#罗普特
'688448',#磁谷科技
'688681',#科汇股份
'688190',#云路股份
'688327',#云从科技-UW
'688799',#华纳药厂
'688357',#建龙微纳
'688151',#华强科技
'688011',#新光光电
'688778',#厦钨新能
'688296',#和达科技
'688316',#青云科技-U
'688231',#隆达股份
'688115',#思林杰
'688565',#力源科技
'688525',#佰维存储
'688506',#百利天恒
'688496',#清越科技
'688475',#萤石网络
'688456',#有研粉材
'688410',#山外山
'688395',#正弦电气
'688176',#亚虹医药-U
'688086',#*ST紫晶
'688193',#仁度生物
'688981',#中芯国际
'688511',#天微电子
'688281',#华秦科技
'688679',#通源环境
'688109',#品茗科技
'688215',#瑞晟智能
'688501',#青达环保
'688028',#沃尔德
'688177',#百奥泰
'688788',#科思科技
'688199',#久日新材
'688387',#信科移动-U
'688230',#芯导科技
'688379',#华光新材
'688350',#富淼科技
'688420',#美腾科技
'688291',#金橙子
'688233',#神工股份
'688062',#迈威生物-U
'688077',#大地熊
'688157',#松井股份
'688665',#四方光电
'688168',#安博通
'688183',#生益电子
'688568',#中科星图
'688739',#成大生物
'688600',#皖仪科技
'688175',#高凌信息
'688152',#麒麟信安
'688550',#瑞联新材
'688722',#同益中
'688425',#铁建重工
'688819',#天能股份
'688416',#恒烁股份
'688097',#博众精工
'688718',#唯赛勃
'688526',#科前生物
'688313',#仕佳光子
'688682',#霍莱沃
'688226',#威腾电气
'688499',#利元亨
'688185',#康希诺
'688529',#豪森股份
'688363',#华熙生物
'688366',#昊海生科
'688566',#吉贝尔
'688370',#丛麟科技
'688266',#泽璟制药-U
'688655',#迅捷兴
'688455',#科捷智能
'688207',#格灵深瞳-U
'688678',#福立旺
'688005',#容百科技
'688349',#三一重能
'688059',#华锐精密
'688459',#哈铁科技
'688012',#中微公司
'688079',#美迪凯
'688701',#卓锦股份
'688359',#三孚新科
'688091',#上海谊众-U
'688567',#孚能科技
'688081',#兴图新科
'688084',#晶品特装
'688309',#*ST恒誉
'688049',#炬芯科技
'688685',#迈信林
'688329',#艾隆科技
'688186',#广大特材
'688010',#福光股份
'688383',#新益昌
'688001',#华兴源创
'688069',#德林海
'688080',#映翰通
'688571',#杭华股份
'688120',#华海清科
'688401',#路维光电
'688015',#交控科技
'688126',#沪硅产业-U
'688580',#伟思医疗
'688223',#晶科能源
'688314',#康拓医疗
'688002',#睿创微纳
'688328',#深科达
'688707',#振华新材
'688162',#巨一科技
'688768',#容知日新
'688083',#中望软件
'688608',#恒玄科技
'688698',#伟创电气
'688308',#欧科亿
'688155',#先惠技术
'688061',#灿瑞科技
'688338',#赛科希德
'688251',#井松智能
'688020',#方邦股份
'688380',#中微半导
'688557',#兰剑智能
'688008',#澜起科技
'688160',#步科股份
'688143',#长盈通
'688256',#寒武纪-U
'688779',#长远锂科
'688661',#和林微纳
'688585',#上纬新材
'688130',#晶华微
'688611',#杭州柯林
'688569',#铁科轨道
'688248',#南网科技
'688066',#航天宏图
'688439',#振华风光
'688007',#光峰科技
'688179',#阿拉丁
'688595',#芯海科技
'688388',#嘉元科技
'688333',#铂力特
'688669',#聚石化学
'688103',#国力股份
'688282',#理工导航
'688558',#国盛智科
'688553',#汇宇制药-W
'688018',#乐鑫科技
'688209',#英集芯
'688198',#佰仁医疗
'688221',#前沿生物-U
'688178',#万德斯
'688625',#呈和科技
'688306',#均普智能
'688070',#纵横股份
'688118',#普元信息
'688597',#煜邦电力
'688299',#长阳科技
'688093',#世华科技
'688362',#甬矽电子
'688320',#禾川科技
'688376',#美埃科技
'688371',#菲沃泰
'688658',#悦康药业
'688087',#英科再生
'688786',#悦安新材
'688559',#海目星
'688078',#龙软科技
'688213',#思特威-W
'688206',#概伦电子
'688337',#普源精电-U
'688208',#道通科技
'688378',#奥来德
'688184',#帕瓦股份
'688696',#极米科技
'688325',#赛微微电
'688173',#希荻微
'688027',#国盾量子
'688596',#正帆科技
'688700',#东威科技
'688368',#晶丰明源
'688326',#经纬恒润-W
'688200',#华峰测控
'688112',#鼎阳科技
'688003',#天准科技
'688789',#宏华数科
'688697',#纽威数控
'688138',#清溢光电
'688659',#元琛科技
'688516',#奥特维
'688210',#统联精密
'688577',#浙海德曼
'688218',#江苏北人
'688396',#华润微
'688247',#宣泰医药
'688480',#赛恩斯
'688006',#杭可科技
'688332',#中科蓝讯
'688636',#智明达
'688268',#华特气体
'688270',#臻镭科技
'688180',#君实生物-U
'688528',#秦川物联
'688676',#金盘科技
'688391',#钜泉科技
'688148',#芳源股份
'688601',#力芯微
'688630',#芯碁微装
'688195',#腾景科技
'688107',#安路科技-U
'688036',#传音控股
'688776',#国光电气
'688110',#东芯股份
'688035',#德邦科技
'688381',#帝奥微
'688122',#西部超导
'688053',#思科瑞
'688259',#创耀科技
'688662',#富信科技
'688071',#华依科技
'688699',#明微电子
'688599',#天合光能
'688386',#泛亚微透
'688227',#品高股份
'688686',#奥普特
'688518',#联赢激光
'688711',#宏微科技
'688106',#金宏气体
'688400',#凌云光
'688622',#禾信仪器
'688234',#天岳先进
'688116',#天奈科技
'688125',#安达智能
'688128',#中国电研
'688239',#航宇科技
'688305',#科德数控
'688033',#天宜上佳
'688690',#纳微科技
'688121',#卓然股份
'688261',#东微半导
'688589',#力合微
'688202',#美迪西
'688082',#盛美上海
'688279',#峰岹科技
'688188',#柏楚电子
'688392',#骄成超声
'688668',#鼎通科技
'688598',#金博股份
'688156',#路德环境
'688237',#超卓航科
'688283',#坤恒顺维
'688267',#中触媒
'688275',#万润新能
'688170',#德龙激光
'688432',#有研硅
'688667',#菱电电控
'688408',#中信博
'688419',#耐科装备
'688322',#奥比中光-UW
'688335',#复洁环保
'688135',#利扬芯片
'688123',#聚辰股份
'688056',#莱伯泰科
'688345',#博力威
'688772',#珠海冠宇
'688385',#复旦微电
'688683',#莱尔科技
'688536',#思瑞浦
'688663',#新风光
'688019',#安集科技
'688353',#华盛锂电
'688025',#杰普特
'688689',#银河微电
'688269',#凯立新材
'688348',#昱能科技
'688047',#龙芯中科
'688800',#瑞可达
'688521',#芯原股份-U
'688628',#优利德
'688372',#伟测科技
'688508',#芯朋微
'688032',#禾迈股份
'688099',#晶晨股份
'688533',#上声电子
'688560',#明冠新材
'688409',#富创精密
'688045',#必易微
'688498',#C源杰
'688339',#亿华通-U
'688262',#国芯科技
'688551',#科威尔
'688519',#南亚新材
'688187',#时代电气
'688048',#长光华芯
'688153',#唯捷创芯-U
'688377',#迪威尔
'688286',#敏芯股份
'688172',#燕东微
'688633',#星球石墨
'688136',#科兴制药
'688017',#绿的谐波
'688063',#派能科技
'688556',#高测股份
'688302',#海创药业-U
'688355',#明志科技
'688072',#拓荆科技-U
'688798',#艾为电子
'688766',#普冉股份
'688390',#固德威
'688403',#汇成股份
'688052',#纳芯微
'688167',#炬光科技
'688216',#气派科技
'688037',#芯源微
]

chuangyeban = [
'300359',#全通教育
'301313',#凡拓数创
'300050',#世纪鼎利
'300659',#中孚信息
'300869',#康泰医学
'300562',#乐心医疗
'301230',#泓博医药
'300605',#恒锋信息
'300356',#*ST光一
'301129',#瑞纳智能
'300148',#天舟文化
'300212',#易华录
'300246',#宝莱特
'300832',#新产业
'300730',#科创信息
'300364',#中文在线
'300206',#理邦仪器
'301248',#杰创智能
'300396',#迪瑞医疗
'300463',#迈克生物
'300253',#卫宁健康
'300633',#开立医疗
'300165',#天瑞仪器
'300578',#会畅通讯
'300773',#拉卡拉
'300559',#佳发教育
'300467',#迅游科技
'300440',#运达科技
'300434',#金石亚药
'301091',#深城交
'300242',#佳云科技
'301363',#美好医疗
'300192',#科德教育
'300063',#天龙集团
'300536',#农尚环境
'300002',#神州泰岳
'300010',#豆神教育
'300235',#方直科技
'300595',#欧普康视
'300632',#光莆股份
'300573',#兴齐眼药
'300071',#福石控股
'300688',#创业黑马
'301079',#邵阳液压
'300608',#思特奇
'300451',#创业慧康
'300845',#捷安高科
'301087',#可孚医疗
'300300',#海峡创新
'300895',#铜牛信息
'300280',#紫天科技
'300911',#亿田智能
'300074',#华平股份
'300248',#新开普
'300550',#和仁科技
'300766',#每日互动
'300781',#因赛集团
'300702',#天宇股份
'301367',#怡和嘉业
'300952',#恒辉安防
'301256',#华融化学
'301097',#天益医疗
'300089',#*ST文化
'300529',#健帆生物
'301316',#慧博云通
'300788',#中信出版
'300426',#唐德影视
'300291',#百纳千成
'300553',#集智股份
'300188',#美亚柏科
'300076',#GQY视讯
'300738',#奥飞数据
'300133',#华策影视
'300310',#宜通世纪
'300949',#奥雅股份
'300027',#华谊兄弟
'300997',#欢乐家
'300454',#深信服
'300081',#恒信东方
'301185',#鸥玛软件
'301025',#读客文化
'300158',#振东制药
'300009',#安科生物
'301030',#仕净科技
'300921',#南凌科技
'300584',#海辰药业
'300774',#倍杰特
'300332',#天壕环境
'300846',#首都在线
'300295',#三六五网
'300987',#川网传媒
'300860',#锋尚文化
'300329',#海伦钢琴
'300556',#丝路视觉
'301299',#卓创资讯
'300380',#安硕信息
'301218',#华是科技
'300805',#电声股份
'300439',#美康生物
'300399',#天利科技
'300249',#依米康
'300482',#万孚生物
'300973',#立高食品
'301231',#荣信文化
'300649',#杭州园林
'300513',#恒实科技
'300756',#金马游乐
'300353',#东土科技
'300996',#普联软件
'300412',#迦南科技
'300612',#宣亚国际
'300745',#欣锐科技
'300150',#世纪瑞尔
'300239',#东宝生物
'300785',#值得买
'300354',#东华测试
'300417',#南华仪器
'300211',#亿通科技
'300287',#飞利信
'300347',#泰格医药
'300250',#初灵信息
'300683',#海特生物
'300830',#金现代
'300079',#数码视讯
'300654',#世纪天鸿
'300634',#彩讯股份
'300025',#华星创业
'300030',#阳普医疗
'300979',#华利集团
'301117',#佳缘科技
'300047',#天源迪科
'300393',#中来股份
'301331',#恩威医药
'300078',#思创医惠
'301169',#零点有数
'300760',#迈瑞医疗
'300294',#博雅生物
'300318',#博晖创新
'300144',#宋城演艺
'300029',#ST天龙
'300052',#中青宝
'300201',#*ST海伦
'300271',#华宇软件
'300925',#法本信息
'300677',#英科医疗
'300229',#拓尔思
'300791',#仙乐健康
'300459',#汤姆猫
'300111',#向日葵
'301290',#东星医疗
'300171',#东富龙
'301026',#浩通科技
'301171',#易点天下
'301178',#天亿马
'300264',#佳创视讯
'300311',#任子行
'300369',#绿盟科技
'300377',#赢时胜
'300624',#万兴科技
'300945',#曼卡龙
'300175',#朗源股份
'300143',#盈康生命
'301060',#兰卫医学
'300020',#银江技术
'301361',#众智科技
'300292',#吴通控股
'301075',#多瑞医药
'300065',#海兰信
'301085',#亚康股份
'300366',#创意信息
'300238',#冠昊生物
'300494',#盛天网络
'301052',#果麦文化
'300678',#中科信息
'301159',#三维天地
'300663',#科蓝软件
'300468',#四方精创
'300561',#汇金科技
'300336',#*ST新文
'300588',#熙菱信息
'300039',#上海凯宝
'300015',#爱尔眼科
'300058',#蓝色光标
'300231',#银信科技
'301326',#捷邦科技
'300885',#海昌新材
'300273',#*ST和佳
'300392',#*ST腾信
'300299',#富春股份
'300113',#顺网科技
'300648',#星云股份
'300044',#赛为智能
'300085',#银之杰
'300942',#易瑞生物
'300142',#沃森生物
'300448',#浩云科技
'300333',#兆日科技
'300159',#ST新研
'300368',#汇金股份
'301152',#天力锂能
'301162',#国能日新
'300413',#芒果超媒
'300209',#有棵树
'300753',#爱朋医疗
'300449',#汉邦高科
'300061',#旗天科技
'300213',#佳讯飞鸿
'300103',#达刚控股
'300344',#立方数科
'300674',#宇信科技
'300169',#天晟新材
'300815',#玉禾田
'300298',#三诺生物
'300166',#东方国信
'301062',#上海艾录
'300036',#超图软件
'301130',#西点药业
'300167',#迪威迅
'300479',#神思电子
'300282',#ST三盛
'300315',#掌趣科技
'300555',#路通视信
'300314',#戴维医疗
'300289',#利德曼
'301207',#华兰疫苗
'300966',#共同药业
'300768',#迪普科技
'300837',#浙矿股份
'300168',#万达信息
'300262',#巴安水务
'300106',#西部牧业
'301011',#华立科技
'301080',#百普赛斯
'300961',#深水海纳
'300352',#北信源
'300383',#光环新网
'301083',#百胜智能
'300096',#易联众
'300981',#中红医疗
'300146',#汤臣倍健
'300321',#同大股份
'300003',#乐普医疗
'300032',#金龙机电
'300326',#凯利泰
'300603',#立昂技术
'300043',#星辉娱乐
'300385',#雪浪环境
'300182',#捷成股份
'300419',#浩丰科技
'300601',#康泰生物
'300528',#幸福蓝海
'300653',#正海生物
'300031',#宝通科技
'300523',#辰安科技
'300245',#天玑科技
'300302',#同有科技
'301380',#挖金客
'300374',#中铁装配
'300743',#天地数码
'300244',#迪安诊断
'300288',#朗玛信息
'300542',#新晨科技
'300386',#飞天诚信
'300379',#东方通
'300540',#蜀道装备
'301257',#普蕊斯
'300391',#康跃科技
'300546',#雄帝科技
'301116',#益客食品
'300692',#中环环保
'300732',#设研院
'300427',#红相股份
'301239',#普瑞眼科
'300937',#药易购
'300947',#德必集团
'300400',#劲拓股份
'301339',#通行宝
'300406',#九强生物
'300190',#维尔利
'300390',#天华超净
'300866',#安克创新
'300226',#上海钢联
'300770',#新媒股份
'300838',#浙江力诺
'300358',#楚天科技
'300799',#左江科技
'300790',#宇瞳光学
'301041',#金百泽
'300378',#鼎捷软件
'300290',#荣科科技
'300636',#同和药业
'301234',#五洲医疗
'300485',#赛升药业
'301113',#雅艺科技
'300645',#正元智慧
'300442',#润泽科技
'300322',#硕贝德
'300615',#欣天科技
'300162',#雷曼光电
'300324',#旋极信息
'300338',#ST开元
'301188',#力诺特玻
'300541',#先进数通
'300571',#平治信息
'300642',#透景生命
'300277',#海联讯
'301037',#保立佳
'301139',#元道通信
'301186',#超达装备
'301033',#迈普医学
'300130',#新国都
'300884',#狄耐克
'300107',#建新股份
'300355',#蒙草生态
'300263',#隆华科技
'300193',#佳士科技
'301101',#明月镜片
'300269',#联建光电
'300098',#高新兴
'300664',#鹏鹞环保
'300959',#线上线下
'300220',#金运激光
'300306',#远方信息
'300977',#深圳瑞捷
'300695',#兆丰股份
'300414',#中光防雷
'300097',#智云股份
'300894',#火星人
'300803',#指南针
'300215',#电科院
'300560',#中富通
'300017',#网宿科技
'300152',#新动力
'300685',#艾德生物
'301333',#诺思格
'300871',#回盛生物
'300172',#中电环保
'300237',#美晨生态
'301208',#中亦科技
'300453',#三鑫医疗
'300255',#常山药业
'300579',#数字认证
'300365',#恒华科技
'301182',#凯旺科技
'300922',#天秦装备
'300662',#科锐国际
'300110',#华仁药业
'300170',#汉得信息
'300056',#中创环保
'300465',#高伟达
'300149',#睿智医药
'300995',#奇德新材
'301258',#富士莱
'300131',#英唐智控
'301338',#凯格精机
'301396',#宏景科技
'300810',#中科海讯
'300464',#星徽股份
'300535',#达威股份
'300334',#津膜科技
'300864',#南大环境
'300948',#冠中生态
'300247',#融捷健康
'301330',#熵基科技
'300676',#华大基因
'300234',#开尔新材
'301220',#亚香股份
'300789',#唐源电气
'300134',#大富科技
'301236',#软通动力
'300180',#华峰超纤
'300872',#天阳科技
'300194',#福安药业
'300006',#莱美药业
'301166',#优宁维
'300657',#弘信电子
'300199',#翰宇药业
'301270',#汉仪股份
'300198',#纳川股份
'300563',#神宇股份
'300691',#联合光电
'300473',#德尔股份
'300759',#康龙化成
'301049',#超越科技
'300430',#诚益通
'300487',#蓝晓科技
'300958',#建工修复
'300184',#力源信息
'300609',#汇纳科技
'300187',#永清环保
'300483',#首华燃气
'300012',#华测检测
'300530',#达志科技
'300984',#金沃股份
'301168',#通灵股份
'300155',#安居宝
'301043',#绿岛风
'300915',#海融科技
'300070',#碧水源
'300616',#尚品宅配
'300094',#国联水产
'300521',#爱司凯
'300519',#新光药业
'300572',#安车检测
'300590',#移为通信
'300276',#三丰智能
'300348',#长亮科技
'300251',#光线传媒
'301318',#维海德
'300147',#香雪制药
'301016',#雷尔伟
'300618',#寒锐钴业
'300868',#杰美特
'300469',#信息发展
'300575',#中旗股份
'300512',#中亚股份
'301176',#逸豪新材
'300117',#嘉寓股份
'301228',#实朴检测
'300004',#南风股份
'300531',#优博讯
'300330',#*ST计通
'300195',#长荣股份
'300879',#大叶股份
'300476',#胜宏科技
'301082',#久盛电气
'300597',#吉大通信
'301328',#维峰电子
'300755',#华致酒行
'300640',#德艺文创
'300867',#圣元环保
'300826',#测绘股份
'300933',#中辰股份
'300508',#维宏股份
'301161',#唯万密封
'300833',#浩洋股份
'300492',#华图山鼎
'300626',#华瑞股份
'301098',#金埔园林
'301227',#森鹰窗业
'300055',#万邦达
'300102',#乾照光电
'301175',#中科环保
'301286',#侨源股份
'300767',#震安科技
'300549',#优德精密
'300543',#朗科智能
'300462',#华铭智能
'300950',#德固特
'301221',#光庭信息
'300935',#盈建科
'300986',#志特新材
'301235',#华康医疗
'300275',#梅安森
'300931',#通用电梯
'301010',#晶雪节能
'300887',#谱尼测试
'300533',#冰川网络
'300083',#创世纪
'300021',#大禹节水
'300317',#珈伟新能
'300985',#致远新能
'300059',#东方财富
'300478',#杭州高新
'300183',#东软载波
'301336',#趣睡科技
'300455',#康拓红外
'300857',#协创数据
'300370',#*ST安控
'300122',#智飞生物
'301090',#华润材料
'300279',#和晶科技
'300598',#诚迈科技
'300405',#科隆股份
'300558',#贝达药业
'300339',#润和软件
'300771',#智莱科技
'300520',#科大国创
'301191',#菲菱科思
'300342',#天银机电
'300557',#理工光科
'300141',#和顺电气
'300270',#中威电子
'301123',#奕东电子
'300137',#先河环保
'300486',#东杰智能
'301063',#海锅股份
'300126',#锐奇股份
'300606',#金太阳
'300040',#九洲集团
'300293',#蓝英装备
'301065',#本立科技
'300746',#汉嘉设计
'300210',#森远股份
'300112',#万讯自控
'300587',#天铁股份
'300067',#安诺其
'300497',#富祥药业
'300177',#中海达
'301379',#天山电子
'300862',#蓝盾光电
'300504',#天邑股份
'300682',#朗新科技
'300181',#佐力药业
'300957',#贝泰妮
'300016',#北陆药业
'300908',#仲景食品
'301180',#万祥科技
'300741',#华宝股份
'300091',#金通灵
'300675',#建科院
'300580',#贝斯特
'301277',#新天地
'300072',#海新能科
'300303',#聚飞光电
'301138',#华研精机
'301013',#利和兴
'300305',#裕兴股份
'300092',#科新机电
'300778',#新城市
'300762',#上海瀚讯
'300491',#通合科技
'301024',#霍普股份
'300668',#杰恩设计
'300853',#申昊科技
'300698',#万马科技
'300865',#大宏立
'300811',#铂科新材
'300844',#山水比德
'301219',#腾远钴业
'301190',#善水科技
'300502',#新易盛
'300946',#恒而达
'301223',#中荣股份
'300684',#中石科技
'300547',#川环科技
'300641',#正丹股份
'300484',#蓝海华腾
'300656',#民德电子
'300011',#鼎汉技术
'300711',#广哈通信
'301070',#开勒股份
'300870',#欧陆通
'300018',#中元股份
'300120',#经纬辉开
'300943',#春晖智控
'300388',#节能国祯
'300515',#三德科技
'300852',#四会富仕
'301136',#招标股份
'300411',#金盾股份
'300635',#中达安
'300889',#爱克股份
'300387',#富邦股份
'300527',#中船应急
'300461',#田中精机
'300570',#太辰光
'300086',#康芝药业
'300357',#我武生物
'300207',#欣旺达
'301283',#聚胶股份
'300384',#三联虹普
'300599',#雄塑科技
'300265',#通光线缆
'300621',#维业股份
'300992',#泰福泵业
'301106',#骏成科技
'300891',#惠云钛业
'300899',#上海凯鑫
'300875',#捷强装备
'301111',#粤万年青
'300849',#锦盛新材
'300394',#天孚通信
'301110',#青木股份
'300717',#华信新材
'300880',#迦南智能
'300501',#海顺新材
'300001',#特锐德
'300905',#宝丽迪
'301288',#清研环境
'301196',#唯科科技
'300525',#博思软件
'301259',#艾布鲁
'301312',#智立方
'300093',#金刚光伏
'300660',#江苏雷利
'300813',#泰林生物
'300709',#精研科技
'301179',#泽宇智能
'301086',#鸿富瀚
'301301',#川宁生物
'301297',#富乐德
'301289',#国缆检测
'301280',#珠城科技
'301255',#通力科技
'301216',#万凯新材
'301127',#天源环保
'301105',#鸿铭股份
'301103',#何氏眼科
'300932',#三友联众
'300907',#康平科技
'300886',#华业香料
'300807',#天迈科技
'300690',#双一科技
'300665',#飞鹿股份
'300651',#金陵体育
'300600',#国瑞科技
'300589',#江龙船艇
'300503',#昊志机电
'300489',#光智科技
'300431',#暴风退
'300420',#五洋停车
'300372',#欣泰退
'300367',#网力退
'300362',#天翔退
'300341',#麦克奥迪
'300325',#德威退
'300312',#邦讯退
'300307',#慈星股份
'300297',#*ST蓝盾
'300283',#温州宏丰
'300281',#金明精机
'300272',#开能健康
'300267',#尔康制药
'300227',#光韵达
'300216',#千山退
'300202',#聚龙退
'300197',#节能铁汉
'300186',#大华农
'300178',#腾邦退
'300176',#派生科技
'300164',#通源石油
'300163',#先锋新材
'300157',#恒泰艾普
'300156',#神雾退
'300153',#科泰电源
'300145',#中金环境
'300135',#宝利国际
'300119',#瑞普生物
'300116',#保力新
'300104',#乐视退
'300090',#盛运退
'300075',#数字政通
'300064',#金刚退
'300048',#合康新能
'300038',#数知退
'300028',#金亚退
'300026',#红日药业
'300023',#宝德退
'300470',#中密控股
'300712',#永福股份
'301093',#华兰股份
'300471',#厚普股份
'300042',#朗科科技
'300800',#力合科技
'300371',#汇中股份
'301197',#工大科雅
'300650',#太龙股份
'300708',#聚灿光电
'300024',#机器人
'301201',#诚达药业
'301181',#标榜股份
'300639',#凯普生物
'301115',#建科股份
'301278',#快可电子
'300710',#万隆光电
'300968',#格林精密
'301073',#君亭酒店
'301167',#建研设计
'300257',#开山股份
'300576',#容大感光
'300500',#启迪设计
'300511',#雪榕生物
'301366',#一博科技
'300222',#科大智能
'301217',#铜冠铜箔
'300610',#晨化股份
'300328',#宜安科技
'300088',#长信科技
'300798',#锦鸡股份
'300099',#精准信息
'300123',#亚光科技
'300564',#筑博设计
'301050',#雷电微力
'300929',#华骐环保
'300062',#中能电气
'300296',#利亚德
'300567',#精测电子
'300232',#洲明科技
'300873',#海晨股份
'300896',#爱美客
'300878',#维康药业
'300225',#金力泰
'300054',#鼎龙股份
'300906',#日月明
'300881',#盛德鑫泰
'300481',#濮阳惠成
'301125',#腾亚精工
'301135',#瑞德智能
'300644',#南京聚隆
'300080',#易成新能
'301359',#东南电子
'300335',#迪森股份
'301200',#大族数控
'301137',#哈焊华通
'300084',#海默科技
'300824',#北鼎股份
'300444',#双杰电气
'300425',#中建环能
'300696',#爱乐达
'300007',#汉威科技
'301148',#嘉戎技术
'301068',#大地海洋
'300611',#美力科技
'300452',#山河药辅
'300854',#中兰环保
'301233',#盛帮股份
'300139',#晓程科技
'300230',#永利股份
'300909',#汇创达
'300705',#九典制药
'300053',#欧比特
'301047',#义翘神州
'300200',#高盟新材
'300077',#国民技术
'301199',#迈赫股份
'300793',#佳禾智能
'300539',#横河精密
'300727',#润禾材料
'301213',#观想科技
'300045',#华力创通
'300593',#新雷能
'300697',#电工合金
'300259',#新天科技
'300823',#建科机械
'301158',#德石股份
'300033',#同花顺
'300349',#金卡智能
'301267',#华厦眼科
'300962',#中金辐照
'300723',#一品红
'301008',#宏昌科技
'300191',#潜能恒信
'301088',#戎美股份
'300422',#博世科
'300284',#苏交科
'300625',#三雄极光
'300516',#久之洋
'301282',#金禄电子
'300228',#富瑞特装
'300350',#华鹏飞
'300963',#中洲特材
'300069',#金利华电
'300834',#星辉环材
'300749',#顶固集创
'300447',#全信股份
'300409',#道氏技术
'300066',#三川智慧
'300343',#联创股份
'301187',#欧圣电气
'300221',#银禧科技
'301045',#天禄科技
'300445',#康斯特
'300687',#赛意信息
'300397',#天和防务
'301092',#争光股份
'301028',#东亚机械
'300219',#鸿利智汇
'301107',#瑜欣电子
'300109',#新开源
'300851',#交大思诺
'300304',#云意电气
'300331',#苏大维格
'301226',#祥明智能
'300713',#英可瑞
'301279',#金道科技
'300196',#长海股份
'300514',#友讯达
'300795',#米奥会展
'301156',#美农生物
'300622',#博士眼镜
'300218',#安利股份
'301006',#迈拓股份
'300818',#耐普矿机
'300953',#震裕科技
'300037',#新宙邦
'300842',#帝科股份
'300423',#昇辉科技
'301122',#采纳股份
'301053',#远信工业
'300014',#亿纬锂能
'300725',#药石科技
'300913',#兆龙互连
'300630',#普利制药
'300967',#晓鸣股份
'300375',#鹏翎股份
'300941',#创识科技
'301238',#瑞泰新材
'300897',#山科智能
'300812',#易天股份
'300551',#古鳌科技
'300821',#东岳硅材
'300956',#英力股份
'301048',#金鹰重工
'300477',#合纵科技
'301165',#锐捷网络
'300836',#佰奥智能
'301189',#奥尼电子
'301263',#泰恩康
'300669',#沪宁股份
'300323',#华灿光电
'300637',#扬帆新材
'300703',#创源股份
'301206',#三元生物
'300965',#恒宇信通
'300604',#长川科技
'300569',#天能重工
'301285',#鸿日达
'300882',#万胜智能
'300057',#万顺新材
'301198',#喜悦智行
'301020',#密封科技
'300989',#蕾奥规划
'301036',#双乐股份
'300780',#德恩精工
'300983',#尤安设计
'301061',#匠心家居
'301038',#深水规院
'300125',#聆达股份
'300161',#华中数控
'300316',#晶盛机电
'300340',#科恒股份
'301183',#东田微
'300731',#科创新源
'300792',#壹网壹创
'300923',#研奥股份
'300538',#同益股份
'300008',#天海防务
'300735',#光弘科技
'301056',#森赫股份
'300236',#上海新阳
'300095',#华伍股份
'300214',#日科化学
'300114',#中航电测
'300912',#凯龙高科
'301128',#强瑞技术
'300975',#商络电子
'300105',#龙源技术
'300403',#汉宇集团
'300930',#屹通新材
'301153',#中科江南
'300041',#回天新材
'300243',#瑞丰高材
'300829',#金丹科技
'301002',#崧盛股份
'300843',#胜蓝股份
'300927',#江天化学
'300801',#泰和科技
'301222',#浙江恒威
'300750',#宁德时代
'300381',#溢多利
'301109',#军信股份
'300876',#蒙泰高新
'301027',#华蓝集团
'300707',#威唐工业
'300509',#新美星
'300892',#品渥食品
'300722',#新余国科
'301003',#江苏博云
'301150',#中一科技
'301300',#远翔新材
'300136',#信维通信
'300647',#超频三
'300308',#中际旭创
'300424',#航新科技
'300999',#金龙鱼
'301215',#中汽股份
'300971',#博亚精工
'301205',#联特科技
'300118',#东方日升
'301015',#百洋医药
'301066',#万事利
'301298',#东利机械
'300602',#飞荣达
'300631',#久吾高科
'300346',#南大光电
'300510',#金冠股份
'300883',#龙利得
'301039',#中集车辆
'300278',#华昌达
'300241',#瑞丰光电
'300652',#雷迪克
'301046',#能辉科技
'300389',#艾比森
'300841',#康华生物
'301042',#安联锐视
'300446',#乐凯新材
'300087',#荃银高科
'300552',#万集科技
'300395',#菲利华
'300655',#晶瑞电材
'301081',#严牌股份
'301017',#漱玉平民
'300507',#苏奥传感
'300715',#凯伦股份
'301192',#泰祥股份
'300154',#瑞凌股份
'300976',#达瑞电子
'300466',#赛摩智能
'300667',#必创科技
'300816',#艾可蓝
'301132',#满坤科技
'300160',#秀强股份
'300901',#中胤时尚
'300627',#华测导航
'300582',#英飞特
'300817',#双飞股份
'300786',#国林科技
'300998',#宁波方正
'300493',#润欣科技
'300410',#正业科技
'300787',#海能实业
'300982',#苏文电能
'300401',#花园生物
'301195',#北路智控
'300748',#金力永磁
'300720',#海川智能
'300319',#麦捷科技
'300739',#明阳电路
'300475',#香农芯创
'300716',#国立科技
'300960',#通业科技
'300972',#万辰生物
'301120',#新特电气
'300628',#亿联网络
'300534',#陇神戎发
'300129',#泰胜风能
'301276',#嘉曼服饰
'300496',#中科创达
'300699',#光威复材
'300474',#景嘉微
'300747',#锐科激光
'300951',#博硕科技
'301059',#金三江
'301019',#宁波色母
'300407',#凯发电气
'301119',#正强股份
'301069',#凯盛新材
'300701',#森霸传感
'301237',#和顺科技
'300205',#天喻信息
'301072',#中捷精工
'301388',#欣灵电气
'301007',#德迈仕
'301055',#张小泉
'301211',#亨迪药业
'300680',#隆盛科技
'300939',#秋田微
'301327',#华宝新能
'300802',#矩子科技
'300522',#世名科技
'300402',#宝色股份
'301021',#英诺激光
'301057',#汇隆新材
'300700',#岱勒新材
'301369',#联动科技
'300775',#三角防务
'300285',#国瓷材料
'300772',#运达股份
'300435',#中泰股份
'300429',#强力新材
'300179',#四方达
'300797',#钢研纳克
'300545',#联得装备
'300499',#高澜股份
'300877',#金春股份
'300256',#ST星星
'300694',#蠡湖股份
'300128',#锦富技术
'300806',#斯迪克
'300623',#捷捷微电
'301212',#联盛化学
'300840',#酷特智能
'300046',#台基股份
'300591',#万里马
'301121',#紫建电子
'301133',#金钟股份
'300568',#星源材质
'300765',#新诺威
'300376',#易事特
'300360',#炬华科技
'301012',#扬电科技
'300005',#探路者
'300100',#双林股份
'300488',#恒锋工具
'300666',#江丰电子
'300847',#中船汉光
'300919',#中伟股份
'301309',#万得凯
'301023',#江南奕帆
'300679',#电连技术
'300689',#澄天伟业
'300554',#三超新材
'300719',#安达维尔
'301040',#中环海陆
'301319',#唯特偶
'300433',#蓝思科技
'300428',#立中集团
'300820',#英杰电气
'300737',#科顺股份
'300763',#锦浪科技
'301004',#嘉益股份
'300266',#兴源环境
'300936',#中英科技
'300592',#华凯易佰
'300441',#鲍斯股份
'300917',#特发服务
'300082',#奥克股份
'300581',#晨曦航空
'300938',#信测标准
'300726',#宏达电子
'300457',#赢合科技
'300855',#图南股份
'300019',#硅宝科技
'300822',#贝仕达克
'300185',#通裕重工
'301149',#隆华新材
'300980',#祥源新材
'300920',#润阳科技
'300613',#富瀚微
'300124',#汇川技术
'300706',#阿石创
'301151',#冠龙节能
'300638',#广和通
'300742',#越博动力
'300132',#青松股份
'300208',#青岛中程
'300049',#福瑞股份
'300928',#华安鑫创
'300421',#力星股份
'301377',#鼎泰高科
'300978',#东箭科技
'300761',#立华股份
'300752',#隆利科技
'300751',#迈为股份
'300777',#中简科技
'301022',#海泰科
'301076',#新瀚新材
'300548',#博创科技
'300596',#利安隆
'301306',#西测测试
'301193',#家联科技
'300629',#新劲刚
'300736',#百邦科技
'300351',#永贵电器
'301356',#天振股份
'301389',#隆扬电子
'300926',#博俊科技
'300839',#博汇股份
'300776',#帝尔激光
'300670',#大烨智能
'300363',#博腾股份
'301391',#卡莱特
'300408',#三环集团
'300320',#海达股份
'300916',#朗特智能
'300856',#科思股份
'300127',#银河磁体
'300532',#今天国际
'300607',#拓斯达
'300831',#派瑞股份
'300898',#熊猫乳品
'300151',#昌红科技
'300740',#水羊股份
'300189',#神农科技
'300432',#富临精工
'300337',#银邦股份
'300620',#光库科技
'301126',#达嘉维康
'300850',#新强联
'300115',#长盈精密
'300173',#福能东方
'301209',#联合化学
'300224',#正海磁材
'300673',#佩蒂股份
'300970',#华绿生物
'300313',#ST天山
'300258',#精锻科技
'300583',#赛托生物
'300450',#先导智能
'300121',#阳谷华泰
'300217',#东方电热
'300617',#安靠智电
'300619',#金银河
'300681',#英搏尔
'300900',#广联航空
'301368',#丰立智能
'300233',#金城医药
'301321',#翰博高新
'301051',#信濠光电
'300964',#本川智能
'300203',#聚光科技
'300729',#乐歌股份
'301269',#华大九天
'301266',#宇邦新材
'301112',#信邦智能
'301398',#星源卓镁
'300035',#中科电气
'301018',#申菱环境
'300565',#科信技术
'300890',#翔丰华
'300825',#阿尔特
'301335',#天元宠物
'300994',#久祺股份
'300661',#圣邦股份
'300819',#聚杰微纤
'301029',#怡合达
'301067',#显盈科技
'300758',#七彩化学
'300828',#锐新科技
'301296',#新巨丰
'300223',#北京君正
'301005',#超捷股份
'300861',#美畅股份
'300418',#昆仑万维
'300537',#广信材料
'301095',#广立微
'301001',#凯淳股份
'301102',#兆讯传媒
'301349',#信德新材
'301273',#瑞晨环保
'300108',#*ST吉药
'300991',#创益通
'300301',#*ST长方
'300498',#温氏股份
'301078',#孩子王
'300286',#安科瑞
'301229',#纽泰格
'300658',#延江股份
'301365',#矩阵股份
'300460',#惠伦晶体
'300438',#鹏辉能源
'300138',#晨光生物
'301177',#迪阿股份
'300594',#朗进科技
'301155',#海力风电
'300863',#卡倍亿
'300693',#盛弘股份
'300274',#阳光电源
'300902',#国安达
'300910',#瑞丰新材
'300443',#金雷股份
'301096',#百诚医药
'300345',#华民股份
'300835',#龙磁科技
'300721',#怡达股份
'300614',#百川畅银
'300518',#盛讯达
'301302',#华如科技
'300796',#贝斯美
'300733',#西菱动力
'300990',#同飞股份
'300517',#海波重科
'300888',#稳健医疗
'300769',#德方纳米
'300940',#南极光
'300686',#智动力
'301009',#可靠股份
'300814',#中富电路
'300415',#伊之密
'301089',#拓新药业
'300903',#科翔股份
'300783',#三只松鼠
'301031',#中熔电气
'300848',#美瑞新材
'301099',#雅创电子
'301035',#润丰股份
'300140',#中环装备
'300240',#飞力达
'300672',#国科微
'300808',#久量股份
'301077',#星华新材
'300373',#扬杰科技
'300480',#光力科技
'300022',#吉峰科技
'301071',#力量钻石
'300073',#当升科技
'300252',#金信诺
'300724',#捷佳伟创
'300101',#振芯科技
'300495',#*ST美尚
'300893',#松原股份
'300034',#钢研高纳
'300416',#苏试试验
'301265',#华新环保
'300404',#博济医药
'301163',#宏德股份
'301000',#肇民科技
'300472',#新元科技
'300382',#斯莱克
'300643',#万通智控
'300327',#中颖电子
'300757',#罗博特科
'300585',#奥联电子
'300858',#科拓生物
'300566',#激智科技
'300969',#恒帅股份
'301032',#新柴股份
'300577',#开润股份
'300779',#惠城环保
'300068',#南都电源
'300261',#雅本化学
'300013',#新宁物流
'301268',#铭利达
'301108',#洁雅股份
'300398',#飞凯材料
'300988',#津荣天宇
'301311',#昆船智能
'300051',#三五互联
'300782',#卓胜微
'300174',#元力股份
'301160',#翔楼新材
'300671',#富满微
'300458',#全志科技
'300827',#上能电气
'300506',#名家汇
'300505',#川金诺
'300437',#清水源
'300993',#玉马遮阳
'300254',#仟源医药
'300260',#新莱应材
'300526',#*ST中潜
'301118',#恒光股份
'300268',#佳沃食品
'300859',#西域旅游
'300490',#华自科技
'300809',#华辰装备
'301100',#风光股份
'300456',#赛微电子
'301058',#中粮科工
'300586',#美联新材
'300436',#广生堂
'300955',#嘉亨家化
'301131',#聚赛龙
'300309',#*ST吉艾
'300718',#长盛轴承
'300204',#舒泰神
'300918',#南山智尚
'301308',#江波龙
]
bankuai = [
'BK1118',#数据确权
'BK1022',#职业教育
'BK0972',#快手概念
'BK1055',#虚拟数字人
'BK0912',#远程办公
'BK0839',#知识产权
'BK1110',#Web3.0
'BK0662',#在线教育
'BK0997',#NFT概念
'BK1054',#DRG/DIP
'BK0841',#体外诊断
'BK1117',#抗原检测
'BK0886',#智慧政务
'BK1008',#国资云概念
'BK0982',#电子车牌
'BK1061',#数字经济
'BK1084',#数字哨兵
'BK1075',#电子身份证
'BK0885',#VPN
'BK1111',#AIGC概念
'BK1047',#数据安全
'BK1062',#新冠检测
'BK0904',#广电
'BK1050',#昨日涨停_含一字
'BK0903',#云游戏
'BK1104',#信创
'BK0655',#网络安全
'BK0942',#商汤概念
'BK1064',#东数西算
'BK0923',#字节概念
'BK0642',#手游概念
'BK0579',#云计算
'BK0959',#数字阅读
'BK1085',#痘病毒防治
'BK0897',#IPv6
'BK0509',#网络游戏
'BK1009',#元宇宙概念
'BK0696',#国产软件
'BK0837',#互联医疗
'BK0706',#人脑工程
'BK0634',#大数据
'BK0853',#电子竞技
'BK0830',#区块链
'BK0815',#昨日涨停
'BK0922',#数据中心
'BK0847',#影视概念
'BK0806',#精准医疗
'BK0883',#数字货币
'BK0995',#华为昇腾
'BK0937',#蚂蚁概念
'BK1121',#第四代半导体
'BK0861',#数字孪生
'BK0953',#鸿蒙概念
'BK0919',#RCS概念
'BK0692',#在线旅游
'BK0693',#基因测序
'BK0880',#UWB概念
'BK0956',#eSIM
'BK0628',#智慧城市
'BK0668',#医疗器械概念
'BK0973',#注射器概念
'BK1013',#华为欧拉
'BK1063',#重组蛋白
'BK0860',#边缘计算
'BK1025',#预制菜概念
'BK1071',#跨境支付
'BK0801',#增强现实
'BK1069',#智慧灯杆
'BK0698',#免疫治疗
'BK0986',#CAR-T细胞疗法
'BK0800',#人工智能
'BK0845',#百度概念
'BK0896',#白酒
'BK0983',#核污染防治
'BK0954',#盲盒经济
'BK0671',#彩票概念
'BK0653',#养老概念
'BK0970',#生物识别
'BK0979',#低碳冶金
'BK1081',#核酸采样亭
'BK0870',#单抗概念
'BK1056',#幽门螺杆菌概念
'BK0831',#万达概念
'BK0849',#京东金融
'BK0689',#阿里概念
'BK0899',#CRO
'BK0667',#国家安防
'BK0822',#租售同权
'BK0722',#虚拟现实
'BK0677',#粤港自贸
'BK1078',#肝炎概念
'BK0548',#生物疫苗
'BK0866',#人造肉
'BK0719',#健康中国
'BK1067',#杭州亚运会
'BK1080',#新型城镇化
'BK0914',#医废处理
'BK0859',#超清视频
'BK0803',#股权转让
'BK0711',#券商概念
'BK0675',#病毒防治
'BK0928',#抖音小店
'BK1087',#超超临界发电
'BK0944',#肝素概念
'BK0940',#网红直播
'BK0637',#互联金融
'BK0554',#物联网
'BK1074',#托育服务
'BK0967',#水产养殖
'BK1106',#创新药
'BK0556',#移动支付
'BK1103',#熔盐储能
'BK1083',#千金藤素
'BK0684',#京津冀
'BK0614',#食品安全
'BK0832',#工业互联
'BK0811',#超级品牌
'BK0906',#流感
'BK0872',#青蒿素
'BK0835',#独角兽
'BK0854',#华为概念
'BK0998',#机器视觉
'BK0813',#雄安新区
'BK0506',#创投
'BK0604',#参股保险
'BK0939',#辅助生殖
'BK0635',#中超概念
'BK0878',#分拆预期
'BK0721',#PPP模式
'BK0615',#中药概念
'BK0868',#GDR
'BK0708',#体育产业
'BK0622',#地热能
'BK1070',#土壤修复
'BK0875',#ETC
'BK0957',#拼多多概念
'BK1057',#电子纸概念
'BK0920',#车联网
'BK1105',#世界杯
'BK0964',#6G概念
'BK1107',#科创板做市商
'BK1053',#低价股
'BK0742',#创业板综
'BK1088',#F5G概念
'BK0941',#疫苗冷链
'BK0966',#碳交易
'BK0610',#央视50_
'BK0524',#参股期货
'BK0948',#MicroLED
'BK0656',#智能电视
'BK0892',#乳业
'BK0514',#参股券商
'BK1098',#生物质能发电
'BK0717',#北京冬奥
'BK0581',#智能电网
'BK0600',#参股新三板
'BK0950',#草甘膦
'BK0566',#滨海新区
'BK0713',#2025规划
'BK1058',#地下管网
'BK1120',#熊去氧胆酸
'BK0943',#汽车拆解
'BK0945',#装配建筑
'BK0710',#量子通信
'BK1112',#破净股
'BK0992',#REITs概念
'BK1024',#绿色电力
'BK0592',#铁路基建
'BK0999',#茅指数
'BK0851',#纾困概念
'BK0549',#深圳特区
'BK0519',#稀缺资源
'BK0929',#地塞米松
'BK0672',#沪企改革
'BK0867',#富时罗素
'BK0980',#债转股
'BK0534',#成渝特区
'BK0499',#AH股
'BK0978',#光伏建筑一体化
'BK0683',#国企改革
'BK0718',#证金持股
'BK0701',#中证500
'BK0597',#水利建设
'BK0611',#上证50_
'BK0505',#中字头
'BK0862',#超级真菌
'BK0690',#氟化工
'BK0632',#土地流转
'BK1007',#植物照明
'BK0918',#特高压
'BK0804',#深股通
'BK1003',#抽水蓄能
'BK0699',#全息技术
'BK0623',#海洋经济
'BK0714',#5G概念
'BK1114',#人造太阳
'BK0568',#深成500
'BK0570',#预亏预减
'BK0879',#标准普尔
'BK0500',#HS300_
'BK0852',#冷链物流
'BK1068',#净水概念
'BK1049',#EDR概念
'BK0664',#婴童概念
'BK0567',#股权激励
'BK0612',#上证180_
'BK0743',#深证100R
'BK0498',#AB股
'BK1026',#调味品概念
'BK0638',#创业成份
'BK0724',#海绵城市
'BK0528',#转债标的
'BK1076',#建筑节能
'BK0596',#融资融券
'BK1012',#PVDF概念
'BK1000',#宁组合
'BK0490',#军工
'BK0494',#节能环保
'BK0511',#ST股
'BK0805',#钛白粉
'BK0676',#独家药品
'BK0855',#纳米银
'BK0962',#RCEP概念
'BK0895',#维生素
'BK1095',#钒电池
'BK0808',#军民融合
'BK0552',#机构重仓
'BK0577',#核能核电
'BK0925',#北交所概念
'BK0843',#天然气
'BK0987',#盐湖提锂
'BK0994',#空间站概念
'BK0619',#3D打印
'BK0525',#参股银行
'BK0709',#赛马概念
'BK0873',#垃圾分类
'BK0704',#无人机
'BK0971',#注册制次新股
'BK0889',#医疗美容
'BK1051',#昨日连板_含一字
'BK0947',#屏下摄像
'BK0697',#IPO受益
'BK0629',#北斗导航
'BK0641',#智能穿戴
'BK0594',#长江三角
'BK0665',#电商概念
'BK1090',#机器人概念
'BK0810',#工业4.0
'BK1065',#气溶胶检测
'BK0974',#化妆品概念
'BK0821',#MSCI中国
'BK0640',#智能机器
'BK0493',#新能源
'BK0707',#沪股通
'BK0902',#MiniLED
'BK0894',#阿兹海默
'BK0911',#口罩
'BK0695',#小金属概念
'BK0838',#东北振兴
'BK0921',#天基互联
'BK0882',#猪肉概念
'BK0850',#进口博览
'BK0993',#宠物经济
'BK0601',#海工装备
'BK1006',#碳基材料
'BK0712',#一带一路
'BK0985',#换电概念
'BK0938',#代糖概念
'BK0856',#工业大麻
'BK0680',#智能家居
'BK0700',#充电桩
'BK0965',#社区团购
'BK0501',#次新股
'BK0705',#上证380
'BK1060',#新冠药物
'BK0571',#预盈预增
'BK0535',#QFII重仓
'BK0703',#超级电容
'BK0561',#基本金属
'BK1004',#工业母机
'BK0901',#3D摄像头
'BK0926',#湖北自贸
'BK0823',#养老金
'BK0492',#煤化工
'BK0932',#尾气治理
'BK0595',#风能
'BK0834',#乡村振兴
'BK0833',#小米概念
'BK0523',#新材料
'BK1005',#专精特新
'BK0666',#苹果概念
'BK0536',#基金重仓
'BK0669',#生态农业
'BK0887',#鸡肉概念
'BK1052',#动力电池回收
'BK1096',#光伏高速公路
'BK0643',#上海自贸
'BK0814',#大飞机
'BK0606',#油气设服
'BK0520',#社保重仓
'BK0625',#通用航空
'BK0981',#工业气体
'BK1102',#空气能热泵
'BK0963',#航天概念
'BK0864',#氢能源
'BK0617',#石墨烯
'BK0715',#航母概念
'BK0578',#稀土永磁
'BK0877',#PCB
'BK0563',#油价相关
'BK0915',#WiFi
'BK0958',#虚拟电厂
'BK0955',#C2M概念
'BK0547',#黄金概念
'BK0913',#消毒剂
'BK0818',#可燃冰
'BK0603',#页岩气
'BK0723',#高送转
'BK0893',#无线耳机
'BK0905',#传感器
'BK0881',#3D玻璃
'BK0960',#无线充电
'BK0682',#燃料电池
'BK0580',#LED
'BK0820',#壳资源
'BK1014',#发电机概念
'BK0840',#OLED
'BK1001',#内贸流通
'BK1108',#科创板做市股
'BK0812',#贬值受益
'BK1023',#培育钻石
'BK0976',#被动元件
'BK0685',#举牌
'BK0588',#太阳能
'BK0909',#降解塑料
'BK0961',#有机硅
'BK0975',#磁悬浮概念
'BK1073',#啤酒概念
'BK0927',#免税概念
'BK0574',#锂电池
'BK0802',#无人驾驶
'BK0865',#电子烟
'BK0807',#共享经济
'BK1089',#汽车热管理
'BK0996',#毛发医疗
'BK0842',#富士康
'BK1079',#户外露营
'BK0991',#工程机械概念
'BK0644',#特斯拉
'BK1115',#跨境电商
'BK0891',#国产芯片
'BK0900',#新能源车
'BK0934',#蝗虫防治
'BK0989',#储能
'BK0512',#化工原料
'BK1059',#百元股
'BK1113',#复合集流体
'BK0817',#昨日触板
'BK1010',#磷化工
'BK0633',#送转预期
'BK0946',#EDA概念
'BK0890',#MLCC
'BK0949',#氦气概念
'BK0888',#农业种植
'BK0825',#新零售
'BK0990',#快递概念
'BK1119',#PLC概念
'BK1011',#环氧丙烷
'BK0907',#转基因
'BK0898',#胎压监测
'BK0884',#光刻胶
'BK1072',#中俄贸易概念
'BK1099',#轮毂电机
'BK0916',#氮化镓
'BK0951',#刀片电池
'BK1082',#噪声防治
'BK0968',#固态电池
'BK0674',#蓝宝石
'BK0936',#长寿药
'BK1094',#钙钛矿电池
'BK0984',#华为汽车
'BK0933',#退税商店
'BK1048',#IGBT概念
'BK1002',#激光雷达
'BK0952',#第三代半导体
'BK0924',#地摊经济
'BK0679',#超导概念
'BK0977',#碳化硅
'BK1092',#麒麟电池
'BK0917',#半导体概念
'BK0988',#钠离子电池
'BK1097',#TOPCon电池
'BK1109',#供销社概念
'BK0908',#HIT电池
'BK0636',#B股
'BK1086',#粮食概念
'BK1100',#减速器
'BK0816',#昨日连板
'BK0935',#中芯概念
'BK0969',#汽车芯片
'BK1077',#统一大市场
'BK1066',#民爆概念
'BK1093',#汽车一体化压铸
'BK1116',#抗菌面料
'BK1101',#Chiplet概念
]

hangye = [
'BK0740',#教育
'BK0486',#文化传媒
'BK1041',#医疗器械
'BK0736',#通信服务
'BK0737',#软件开发
'BK0447',#互联网服务
'BK1046',#游戏
'BK1044',#生物制品
'BK0735',#计算机设备
'BK0727',#医疗服务
'BK1043',#专业服务
'BK0473',#证券
'BK0733',#包装材料
'BK0726',#工程咨询服务
'BK0485',#旅游酒店
'BK0438',#食品饮料
'BK0465',#化学制药
'BK1042',#医药商业
'BK1015',#能源金属
'BK1028',#燃气
'BK0477',#酿酒行业
'BK0428',#电力行业
'BK1040',#中药
'BK0451',#房地产开发
'BK0474',#保险
'BK0440',#家用轻工
'BK0425',#工程建设
'BK1045',#房地产服务
'BK0725',#装修装饰
'BK0448',#通信设备
'BK0458',#仪器仪表
'BK0420',#航空机场
'BK0730',#农药兽药
'BK0427',#公用事业
'BK0478',#有色金属
'BK0437',#煤炭行业
'BK0456',#家电行业
'BK0734',#珠宝首饰
'BK0728',#环保行业
'BK1038',#光学光电子
'BK1027',#小金属
'BK1017',#采掘行业
'BK0729',#船舶制造
'BK0457',#电网设备
'BK0475',#银行
'BK0479',#钢铁行业
'BK1030',#电机
'BK1037',#消费电子
'BK0424',#水泥建材
'BK0480',#航天航空
'BK0738',#多元金融
'BK0546',#玻璃玻纤
'BK0454',#塑料制品
'BK0433',#农牧饲渔
'BK1016',#汽车服务
'BK1018',#橡胶制品
'BK0545',#通用设备
'BK0731',#化肥行业
'BK0450',#航运港口
'BK0476',#装修建材
'BK0910',#专用设备
'BK0471',#化纤行业
'BK1020',#非金属材料
'BK1034',#电源设备
'BK0421',#铁路公路
'BK0429',#交运设备
'BK0470',#造纸印刷
'BK0739',#工程机械
'BK0539',#综合行业
'BK0459',#电子元件
'BK1019',#化学原料
'BK0484',#贸易行业
'BK1032',#风电设备
'BK0538',#化学制品
'BK0422',#物流行业
'BK0481',#汽车零部件
'BK1039',#电子化学品
'BK1033',#电池
'BK0732',#贵金属
'BK0464',#石油行业
'BK1031',#光伏设备
'BK1035',#美容护理
'BK0482',#商业百货
'BK0436',#纺织服装
'BK1029',#汽车整车
'BK1036',#半导体
]