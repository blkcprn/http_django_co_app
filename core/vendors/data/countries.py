from collections import namedtuple
from django.utils.translation import gettext_lazy as _


Country = namedtuple("Country", ["name", "iso"])


"""
Afghanistan	af	AFG	Kabul
Albania	al	ALB	Tirana
Algeria	dz	DZA	Algiers
American Samoa	as	ASM	Pago Pago
Andorra	ad	AND	Andorra
Angola	ao	AGO	Luanda
Anguilla	ai	AIA	The Valley
Antarctica	aq	ATA	None
Antigua and Barbuda	ag	ATG	St. Johns
Argentina	ar	ARG	Buenos Aires
Armenia	am	ARM	Yerevan
Aruba	aw	ABW	Oranjestad
Australia	au	AUS	Canberra
Austria	at	AUT	Vienna
Azerbaijan	az	AZE	Baku
Bahamas	bs	BHS	Nassau
Bahrain	bh	BHR	Al-Manamah
Bangladesh	bd	BGD	Dhaka
Barbados	bb	BRB	Bridgetown
Belarus	by	BLR	Minsk
Belgium	be	BEL	Brussels
Belize	bz	BLZ	Belmopan
Benin	bj	BEN	Porto-Novo
Bermuda	bm	BMU	Hamilton
Bhutan	bt	BTN	Thimphu
Bolivia	bo	BOL	La Paz
Bonaire, Sint Eustatius and Saba	bq	BES	Kralendijk
Bosnia-Herzegovina	ba	BIH	Sarajevo
Botswana	bw	BWA	Gaborone
Bouvet Island	bv	BVT	None
Brazil	br	BRA	Brasilia
British Indian Ocean Territory	io	IOT	None
Brunei Darussalam	bn	BRN	Bandar Seri Begawan
Bulgaria	bg	BGR	Sofia
Burkina Faso	bf	BFA	Ouagadougou
Burundi	bi	BDI	Bujumbura
Cabo Verde	cv	CPV	Praia
Cambodia	kh	KHM	Phnom Penh
Cameroon	cm	CMR	Yaounde
Canada	ca	CAN	Ottawa
Cayman Islands	ky	CYM	Georgetown
Central African Republic	cf	CAF	Bangui
Chad	td	TCD	N'Djamena
Chile	cl	CHL	Santiago
China	cn	CHN	Beijing
Christmas Island	cx	CXR	The Settlement
Cocos (Keeling) Islands	cc	CCK	West Island
Colombia	co	COL	Bogota
Comoros	km	COM	Moroni
Congo	cg	COG	Brazzaville
Congo, Dem. Republic	cd	COD	Kinshasa
Cook Islands	ck	COK	Avarua
Costa Rica	cr	CRI	San Jose
Croatia	hr	HRV	Zagreb
Cuba	cu	CUB	Havana
Curaçao	cw	CUW	Willemstad
Cyprus	cy	CYP	Nicosia
Czechia	cz	CZE	Prague
Côte d'Ivoire	ci	CIV	Abidjan
Denmark	dk	DNK	Copenhagen
Djibouti	dj	DJI	Djibouti
Dominica	dm	DMA	Roseau
Dominican Rep.	do	DOM	Santo Domingo
Ecuador	ec	ECU	Quito
Egypt	eg	EGY	Cairo
El Salvador	sv	SLV	San Salvador
Equatorial Guinea	gq	GNQ	Malabo
Eritrea	er	ERI	Asmara
Estonia	ee	EST	Tallinn
Eswatini	sz	SWZ	Mbabane
Ethiopia	et	ETH	Addis Ababa
European Union	eu	INT	Brussels
Falkland Islands (Malvinas)	fk	FLK	Stanley
Faroe Islands	fo	FRO	Torshavn
Fiji	fj	FJI	Suva
Finland	fi	FIN	Helsinki
France	fr	FRA	Paris
French Guiana	gf	GUF	Cayenne
French Polynesia	pf	PYF	Papeete
French Southern Territories	tf	ATF	None
Gabon	ga	GAB	Libreville
Gambia	gm	GMB	Banjul
Georgia	ge	GEO	Tbilisi
Germany	de	DEU	Berlin
Ghana	gh	GHA	Accra
Gibraltar	gi	GIB	Gibraltar
Great Britain	gb	GBR	London
Greece	gr	GRC	Athens
Greenland	gl	GRL	Godthab
Grenada	gd	GRD	St. George's
Guadeloupe	gp	GLP	Basse-Terre
Guam	gu	GUM	Agana
Guatemala	gt	GTM	Guatemala City
Guernsey	gg	GGY	St. Peter Port
Guinea	gn	GIN	Conakry
Guinea-Bissau	gw	GNB	Bissau
Guyana	gy	GUY	Georgetown
Haiti	ht	HTI	Port-au-Prince
Heard Island and
McDonald Islands	hm	HMD	None
Holy See	va	VAT	Vatican City
Honduras	hn	HND	Tegucigalpa
Hong Kong	hk	HKG	Victoria
Hungary	hu	HUN	Budapest
Iceland	is	ISL	Reykjavik
India	in	IND	New Delhi
Indonesia	id	IDN	Jakarta
Iran	ir	IRN	Tehran
Iraq	iq	IRQ	Baghdad
Ireland	ie	IRL	Dublin
Isle of Man	im	IMN	Douglas
Israel	il	ISR	Jerusalem
Italy	it	ITA	Rome
Jamaica	jm	JAM	Kingston
Japan	jp	JPN	Tokyo
Jersey	je	JEY	Saint Helier
Jordan	jo	JOR	Amman
Kazakhstan	kz	KAZ	Astana
Kenya	ke	KEN	Nairobi
Kiribati	ki	KIR	Tarawa
Korea, N.	kp	PRK	Pyongyang
Korea, S.	kr	KOR	Seoul
Kosovo	xk	XKX	Priština
Kuwait	kw	KWT	Kuwait City
Kyrgyzstan	kg	KGZ	Bishkek
Lao	la	LAO	Vientiane
Latvia	lv	LVA	Riga
Lebanon	lb	LBN	Beirut
Lesotho	ls	LSO	Maseru
Liberia	lr	LBR	Monrovia
Libya	ly	LBY	Tripoli
Liechtenstein	li	LIE	Vaduz
Lithuania	lt	LTU	Vilnius
Luxembourg	lu	LUX	Luxembourg
Macao	mo	MAC	Macau
Madagascar	mg	MDG	Antananarivo
Malawi	mw	MWI	Lilongwe
Malaysia	my	MYS	Kuala Lumpur
Maldives	mv	MDV	Male
Mali	ml	MLI	Bamako
Malta	mt	MLT	Valletta
Marshall Islands	mh	MHL	Majuro
Martinique	mq	MTQ	Fort-de-France
Mauritania	mr	MRT	Nouakchott
Mauritius	mu	MUS	Port Louis
Mayotte	yt	MYT	Dzaoudzi
Mexico	mx	MEX	Mexico City
Micronesia	fm	FSM	Palikir
Moldova	md	MDA	Kishinev
Monaco	mc	MCO	Monaco
Mongolia	mn	MNG	Ulan Bator
Montenegro	me	MNE	Podgorica
Montserrat	ms	MSR	Plymouth
Morocco	ma	MAR	Rabat
Mozambique	mz	MOZ	Maputo
Myanmar	mm	MMR	Naypyidaw
Namibia	na	NAM	Windhoek
Nauru	nr	NRU	Yaren
Nepal	np	NPL	Kathmandu
Netherlands	nl	NLD	Amsterdam
New Caledonia	nc	NCL	Noumea
New Zealand	nz	NZL	Wellington
Nicaragua	ni	NIC	Managua
Niger	ne	NER	Niamey
Nigeria	ng	NGA	Lagos
Niue	nu	NIU	Alofi
Norfolk Island	nf	NFK	Kingston
North Macedonia	mk	MKD	Skopje
Northern Mariana Islands	mp	MNP	Saipan
Norway	no	NOR	Oslo
Oman	om	OMN	Muscat
Pakistan	pk	PAK	Islamabad
Palau	pw	PLW	Koror
Panama	pa	PAN	Panama City
Papua New Guinea	pg	PNG	Port Moresby
Paraguay	py	PRY	Asuncion
Peru	pe	PER	Lima
Philippines	ph	PHL	Manila
Pitcairn Island	pn	PCN	Adamstown
Poland	pl	POL	Warsaw
Portugal	pt	PRT	Lisbon
Puerto Rico	pr	PRI	San Juan
Qatar	qa	QAT	Doha
Reunion	re	REU	Saint-Denis
Romania	ro	ROU	Bucharest
Russia	ru	RUS	Moscow
Rwanda	rw	RWA	Kigali
Saint Barthélemy	bl	BLM	Gustavia
Saint Helena	sh	SHN	Jamestown
Saint Kitts & Nevis	kn	KNA	Basseterre
Saint Lucia	lc	LCA	Castries
Saint Martin (French part)	mf	MAF	Marigot
Saint Pierre and Miquelon	pm	SPM	St. Pierre
Saint Vincent & Grenadines	vc	VCT	Kingstown
Samoa	ws	WSM	Apia
San Marino	sm	SMR	San Marino
Sao Tome and Principe	st	STP	Sao Tome
Saudi Arabia	sa	SAU	Riyadh
Senegal	sn	SEN	Dakar
Serbia	rs	SRB	Belgrade
Seychelles	sc	SYC	Victoria
Sierra Leone	sl	SLE	Freetown
Singapore	sg	SGP	Singapore
Sint Maarten (Dutch part)	sx	SXM	Philipsburg
Slovakia	sk	SVK	Bratislava
Slovenia	si	SVN	Ljubljana
Solomon Islands	sb	SLB	Honiara
Somalia	so	SOM	Mogadishu
South Africa	za	ZAF	Pretoria
South Georgia &
South Sandwich Islands	gs	SGS	None
South Sudan	ss	SSD	Ramciel
Spain	es	ESP	Madrid
Sri Lanka	lk	LKA	Colombo
Sudan	sd	SDN	Khartoum
Suriname	sr	SUR	Paramaribo
Svalbard and Jan Mayen Islands	sj	SJM	Longyearbyen
Sweden	se	SWE	Stockholm
Switzerland	ch	CHE	Bern
Syria	sy	SYR	Damascus
Taiwan	tw	TWN	Taipei
Tajikistan	tj	TJK	Dushanbe
Tanzania	tz	TZA	Dodoma
Thailand	th	THA	Bangkok
Timor-Leste	tl	TLS	Dili
Togo	tg	TGO	Lome
Tokelau	tk	TKL	None
Tonga	to	TON	Nuku'alofa
Trinidad and Tobago	tt	TTO	Port of Spain
Tunisia	tn	TUN	Tunis
Turkey	tr	TUR	Ankara
Turkmenistan	tm	TKM	Ashgabat
Turks and Caicos Islands	tc	TCA	Grand Turk
Tuvalu	tv	TUV	Funafuti
US Minor Outlying Islands	um	UMI	None
USA	us	USA	Washington
Uganda	ug	UGA	Kampala
Ukraine	ua	UKR	Kiev
United Arab Emirates	ae	ARE	Abu Dhabi
Uruguay	uy	URY	Montevideo
Uzbekistan	uz	UZB	Tashkent
Vanuatu	vu	VUT	Port Vila
Venezuela	ve	VEN	Caracas
Vietnam	vn	VNM	Hanoi
Virgin Islands (British)	vg	VGB	Road Town
Virgin Islands (US)	vi	VIR	Charlotte Amalie
Wallis and Futuna Islands	wf	WLF	Mata-Utu
Western Sahara	eh	ESH	El Aaiun
Yemen	ye	YEM	San'a
Zambia	zm	ZMB	Lusaka
Zimbabwe	zw	ZWE	Harare
"""