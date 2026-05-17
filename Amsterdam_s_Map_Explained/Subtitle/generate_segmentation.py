#!/usr/bin/env python3
"""
Generate segmentation alignment markers for bilingual subtitle alignment.
Handles: normal splits, [copy] cases, single sub-clause lines.
"""

import re

# Parse input files
def parse_file(filepath):
    result = {}
    with open(filepath, 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            m = re.match(r'^\[(\d+)\]\s+(.*)', line)
            if m:
                result[int(m.group(1))] = m.group(2)
    return result

en_texts = parse_file("/Users/gtt/Documents/YTV_C/Amsterdam_s_Map_Explained/Subtitle/4.en.formatted.indexed.md")
zh_texts = parse_file("/Users/gtt/Documents/YTV_C/Amsterdam_s_Map_Explained/Subtitle/5.en.formatted.indexed.zh.md")

# For each index, define splits.
# format: {idx: {'en': [(end, begin), ...], 'zh': [(end, begin_or_COPY), ...]}}
# .en and .zh must have same length (k-1 where k = number of sub-clauses)
# For [copy] entries in zh, use "COPY" as the second element
# For empty list, there is 1 sub-clause total.

S = {}

# [0] Roughly a quarter of the surface area of Amsterdam is covered in water.
# ZH: 阿姆斯特丹大约四分之一的地表面积都被水覆盖。
S[0] = {'en': [], 'zh': []}

# [1] 165 canals run over 100 km throughout the city | and more than 1200 bridges make it walkable or bikable.
S[1] = {'en': [('city', 'and')], 'zh': [('里，', '1200')]}

# [2] Most of it was built in the span of a single century | and its growth can be simplified into a couple specific stages.
S[2] = {'en': [('century', 'and')], 'zh': [('的，', '其')]}

# [3] >> Amsterdam is much more of a planned city | and there's a lot of constraints.
S[3] = {'en': [('city', 'and')], 'zh': [('市，', '而且')]}

# [4] The way people deal with these constraints are very interesting, | I think.
S[4] = {'en': [('interesting,', 'I')], 'zh': [('得', '人们')]}

# [5] And when you start to understand the motivations for each section, | you can read the map like a book.
S[5] = {'en': [('section,', 'you')], 'zh': [('时，', '你')]}

# [6] We made it to Amsterdam | and it is so beautiful.
S[6] = {'en': [('Amsterdam', 'and')], 'zh': [('了，', '这里')]}

# [7] I am so excited to make this video | because this is one I've been looking forward to for a long time.
S[7] = {'en': [('video', 'because')], 'zh': [('频，', '因为')]}

# [8] Honestly, at this point, I don't really know much about the city yet, | but I've gotten in contact with a couple people who know a lot.
S[8] = {'en': [('yet,', 'but')], 'zh': [('解，', '但')]}

# [9] My name is Yap Aford Abrahamsa | and I uh I'm an architectural historian | and I work for the cultural heritage agency of the Netherlands | and as an endowed professor of architectural history at the VU University uh in Amsterdam.
S[9] = {
    'en': [('Abrahamsa', 'and'), ('historian', 'and'), ('Netherlands', 'and')],
    'zh': [('萨，', '嗯'), ('家，', '在'), ('作，', '同时')]
}

# [10] >> My name is Yohim.
S[10] = {'en': [], 'zh': []}

# [11] I was born and raised in Amsterdam | and I run the YouTube channel the present past.
S[11] = {'en': [('Amsterdam', 'and')], 'zh': [('大，', '我')]}

# [12] >> My name is Alar Deil.
S[12] = {'en': [], 'zh': []}

# [13] I'm a historian | and I've worked for a long time as a curator at the Amsterdam Museum.
S[13] = {'en': [('historian', 'and')], 'zh': [('家，', '长期')]}

# [14] If you follow the Amstl River to the sea, | just as you get to the canal belt, | you will see an unnaturally straight stretch of river.
S[14] = {
    'en': [('sea,', 'just'), ('belt,', 'you')],
    'zh': [('走，', '就'), ('方，', '你')]
}

# [15] This is the first man-made canal in the city, | and it's the reason Amsterdam exists here.
S[15] = {'en': [('city,', 'and')], 'zh': [('道，', '也')]}

# [16] Dug in the 12th or 13th century, | this canal was the solution to a problem that farmers in the region had been dealing with.
S[16] = {'en': [('century,', 'this')], 'zh': [('纪，', '是')]}

# [17] The landscape they farmed was a low-lying, flat, marshy area | made up of pete.
S[17] = {'en': [('area', 'made')], 'zh': [('带，', '由')]}

# [18] So Pete is basically dead leaves that have stacked on top of each other, | have been pressed together over the millennia | to make a ground that is um organic and quite soft.
S[18] = {
    'en': [('other,', 'have'), ('millennia', 'to')],
    'zh': [('叠，', '经过'), ('起', '形成')]
}

# [19] To make the land suitable for farming, | the water needed to be drained.
S[19] = {'en': [('farming,', 'the')], 'zh': [('耕，', '需')]}

# [20] There are still places not far from the city | where you can visualize what this would have been like.
S[20] = {'en': [('city', 'where')], 'zh': [('方，', '仍然')]}

# [21] But there was a problem.
S[21] = {'en': [], 'zh': []}

# [22] The land wasn't draining as fast as they needed it to.
S[22] = {'en': [], 'zh': []}

# [23] It was too far upstream from its outlet.
S[23] = {'en': [], 'zh': []}

# [24] But if they could connect it to a closer outlet, | then it could drain much faster.
S[24] = {'en': [('outlet,', 'then')], 'zh': [('口，', '排水')]}

# [25] So that's exactly what they did.
S[25] = {'en': [], 'zh': []}

# [26] Building this canal turned two rivers into one, | the Amstl.
S[26] = {'en': [('one,', 'the')], 'zh': [('一，', '形成')]}

# [27] And it solved their problem of drainage, | but it also created a new problem.
S[27] = {'en': [('drainage,', 'but')], 'zh': [('题，', '但')]}

# [28] Now, when there was a storm surge, | salty water could be pushed up river and threaten the crops.
S[28] = {'en': [('surge,', 'salty')], 'zh': [('时，', '咸')]}

# [29] And this leads us to modern-day Dam Square.
S[29] = {'en': [], 'zh': []}

# [30] Okay, | this place is called Dam Square | and it's called Dam Square | because this used to be the dam in the river Amstel | that gave Amsterdam its name | and it closed off the mouth of the river Amsel.
S[30] = {
    'en': [('Okay,', 'this'), ('Square', 'and'), ('Square', 'because'), ('Amstel', 'that'), ('name', 'and')],
    'zh': [('的，', '这个'), ('场，', '之所以'), ('场，', '是'), ('坝，', '阿姆斯特丹'), ('名，', '这座')]
}

# [31] But as you look around here now, | you don't see any dam and you don't see any any river.
S[31] = {'en': [('now,', 'you')], 'zh': [('在，', '看')]}

# [32] The canals have been filled in and lots of new buildings have been created | and instead of boats, | you see the trams and the cars and the bikes going over this place right now.
S[32] = {
    'en': [('created', 'and'), ('boats,', 'you')],
    'zh': [('筑，', '船只'), ('了，', '取而代')]
}

# [33] As unassuming as it may seem now, | this dam was the foundation of the city.
S[33] = {'en': [('now,', 'this')], 'zh': [('起，', '这座')]}

# [34] It could be opened to let the fresh water out | and closed to prevent the salt water from coming in.
S[34] = {'en': [('out', 'and')], 'zh': [('出', '关闭')]}

# [35] >> The pet soil uh is subsiding | while the sea uh is still there.
S[35] = {'en': [('subsiding', 'while')], 'zh': [('沉，', '而')]}

# [36] So you have to build um uh dams and dikes to contain the sea.
S[36] = {'en': [], 'zh': []}

# [37] >> But the creation of the dam had a bigger impact.
S[37] = {'en': [], 'zh': []}

# [38] Without it, | the Amstel would have remained a minor river in a swampy delta.
S[38] = {'en': [('it,', 'the')], 'zh': [('它，', '阿姆斯特尔河')]}

# [39] But with the canal and the dam, | this was now a hub for trade.
S[39] = {'en': [('dam,', 'this')], 'zh': [('坝，', '这里')]}

# [40] >> The river Amsel was inland connection | where you could get to Rotterdam and Dor.
S[40] = {'en': [('connection', 'where')], 'zh': [('道，', '你')]}

# [41] So you didn't have to sail the North Sea | which was a very dangerous place.
S[41] = {'en': [('Sea', 'which')], 'zh': [('域', '那是')]}

# [42] So this was the crossing of a river and an important road.
S[42] = {'en': [], 'zh': []}

# [43] So this is the place | where a lot of where the harbor of Amsterdam um was created.
S[43] = {'en': [('place', 'where')], 'zh': [('方', '阿姆斯特丹')]}

# [44] >> Literally the beginning of the city goes back to controlling the water.
S[44] = {'en': [], 'zh': []}

# [45] When looking at the first section of the city, | it becomes clear that the dam is at its center.
S[45] = {'en': [('city,', 'it')], 'zh': [('展，', '很')]}

# [46] From there, | buildings were built on both sides of the river | and the city turned into an H shape.
S[46] = {
    'en': [('there,', 'buildings'), ('river', 'and')],
    'zh': [('里，', '建筑'), ('岸，', '城市')]
}

# [47] By the way, | this map is oriented with north on the bottom and south on the top.
S[47] = {'en': [('way,', 'this')], 'zh': [('句，', '这张')]}

# [48] >> This year, | we're celebrating the 750th birthday of Amsterdam.
S[48] = {'en': [('year,', "we're")], 'zh': [('年，', '我们')]}

# [49] It's not actually the birthday because people were living here, | but they were mentioned in in 1275 in a document | that granted the people living in Amsterdama.
S[49] = {
    'en': [('here,', 'but'), ('document', 'that')],
    'zh': [('住，', '但'), ('及，', '这份')]
}

# [50] So the people living in where the dam and the Amsterl was constructed, | they were granted privileges to trade their goods in the in the bigger area.
S[50] = {'en': [('constructed,', 'they')], 'zh': [('处，', '人们')]}

# [51] The effect was that it accelerated growth, | that it attracted other people who came to the city.
S[51] = {'en': [('growth,', 'that')], 'zh': [('展，', '吸引')]}

# [52] So gradually, you know, | the city started to expand, | which meant that every time they had to deal with this marshy lands and and build dikes to to stop the water.
S[52] = {
    'en': [('know,', 'the'), ('expand,', 'which')],
    'zh': [('地，', '城市'), ('张，', '这')]
}

# [53] As the city grew, | they built two additional drainage canals on either side of the Amstl.
S[53] = {'en': [('grew,', 'they')], 'zh': [('展，', '他们')]}

# [54] And building on this swampy soft soil was not easy.
S[54] = {'en': [], 'zh': []}

# [55] Because many of the structures of the medieval city were made of wood | and because there's been centuries of redevelopment since then | very few original buildings from this period exist | but this is one of them.
S[55] = {
    'en': [('wood', 'and'), ('then', 'very'), ('exist', 'but')],
    'zh': [('的，', '而且'), ('建，', '所以'), ('少，', '但')]
}

# [56] This is the outer the old church | and well as the name would have it.
S[56] = {'en': [('church', 'and')], 'zh': [('堂，', '正如')]}

# [57] It's the old church.
S[57] = {'en': [], 'zh': []}

# [58] Uh it's actually the oldest building we have left in Amsterdam | and it rests on top of more than 2,000 wooden piles.
S[58] = {'en': [('Amsterdam', 'and')], 'zh': [('筑，', '坐')]}

# [59] These are massive tree trunks planted beneath the buildings | to keep them from sinking into the soil.
S[59] = {'en': [('buildings', 'to')], 'zh': [('面，', '用来')]}

# [60] And this was common across the entire city.
S[60] = {'en': [], 'zh': []}

# [61] >> The poles we we we ram into the ground either 12, 20, or 50 m | because that is the three layers where you actually have a sandy soil.
S[61] = {'en': [('m', 'because')], 'zh': [('米，', '因为')]}

# [62] >> It's proven to be probably the best solution, | but it's definitely not perfect.
S[62] = {'en': [('solution,', 'but')], 'zh': [('案，', '但')]}

# [63] Uh the buildings are actually in place, | but the rest of Amsterdam is same.
S[63] = {'en': [('place,', 'but')], 'zh': [('了，', '但')]}

# [64] So the the streets have to be redone every few years | and they have to be heightened up every time.
S[64] = {'en': [('years', 'and')], 'zh': [('次，', '每次')]}

# [65] >> In addition to the drainage canals, | they would also build raised dikes to prevent certain areas from flooding | and a lot of these doubled as roads | and their names make it quite clear what they were.
S[65] = {
    'en': [('canals,', 'they'), ('flooding', 'and'), ('roads', 'and')],
    'zh': [('河，', '他们'), ('没，', '其中'), ('路，', '它们')]
}

# [66] >> We're now walking on uh zyke, | which literally translates to sea dyke.
S[66] = {'en': [('zyke,', 'which')], 'zh': [('上，', '字面')]}

# [67] So this is literally where the old dyke of the city used to be.
S[67] = {'en': [], 'zh': []}

# [68] And if you look at the map, | you can see this this curve around it.
S[68] = {'en': [('map,', 'you')], 'zh': [('图，', '可以')]}

# [69] If you're just tracing the outline of the coast | where you're going to put your dyke, | it's never going to be super straight.
S[69] = {
    'en': [('coast', 'where'), ('dyke,', "it's")],
    'zh': [('线', '来'), ('向，', '它')]
}

# [70] So you can really see the height difference.
S[70] = {'en': [], 'zh': []}

# [71] If you look over there and you see the people drinking a beer, | they're literally on a different level.
S[71] = {'en': [('beer,', "they're")], 'zh': [('酒，', '他们')]}

# [72] So if you are on a patch of elevation like we're here now on the Z D, | it means it is it is man-made.
S[72] = {'en': [('D,', 'it')], 'zh': [('上', '那就')]}

# [73] It's not a it's an unnatural occurrence.
S[73] = {'en': [], 'zh': []}

# [74] >> The boundary of the medieval city is marked by these two canals | which also served as its moat.
S[74] = {'en': [('canals', 'which')], 'zh': [('志，', '它们')]}

# [75] >> It's Amsel with dam square and two canals on either side | and then a new city wall was built around it with a new canal | and that's basically the medieval structure of the city.
S[75] = {
    'en': [('side', 'and'), ('canal', 'and')],
    'zh': [('河，', '然后'), ('河，', '这')]
}

# [76] When you look at the medieval city versus the rest of the canal belt, | there's a distinct visual difference between the irregular windy roads of the center of the city versus the more planned areas beyond it.
S[76] = {'en': [('belt,', "there's")], 'zh': [('来，', '市中心')]}

# [77] So when you're walking around the city, | there's a clear distinction between each of these expansions.
S[77] = {'en': [('city,', "there's")], 'zh': [('时，', '每一次')]}

# [78] And you can see it where we're standing really clearly | because this water, this canal is now just part of the canal system, | but it used to be the moat.
S[78] = {
    'en': [('clearly', 'because'), ('system,', 'but')],
    'zh': [('楚，', '因为'), ('分，', '但')]
}

# [79] And the city gate is back there that we were looking at.
S[79] = {'en': [], 'zh': []}

# [80] But this side you can see just a solid wall of all the buildings.
S[80] = {'en': [], 'zh': []}

# [81] And on this side you can see the roads cutting in to each of these blocks.
S[81] = {'en': [], 'zh': []}

# [82] There are two other structures from this era that I want to point out.
S[82] = {'en': [], 'zh': []}

# [83] Over there is the edge of the medieval city | and you can see one part of the medieval city wall that's still standing.
S[83] = {'en': [('city', 'and')], 'zh': [('界，', '你')]}

# [84] It's called the store.
S[84] = {'en': [], 'zh': []}

# [85] This is often referred to as the weeping tower | because it was from this spot that sailors would leave their families for months or years on long voyages.
S[85] = {'en': [('tower', 'because')], 'zh': [('塔', '因为')]}

# [86] If you follow just a short way down the path of the old city wall, | you'll come to another surviving building, the old city gate.
S[86] = {'en': [('wall,', "you'll")], 'zh': [('径，', '就会')]}

# [87] So, if you look over there, | you can see where it says restaurant cafe.
S[87] = {'en': [('there,', 'you')], 'zh': [('儿，', '可以')]}

# [88] Um, that is actually where the old gate to the city used to be.
S[88] = {'en': [('Um,', 'that')], 'zh': [('嗯，', '那')]}

# [89] It's like a tree has rings to indicate its age. | And a city also has rings.
S[89] = {'en': [('age.', 'And')], 'zh': [('样，', '城市')]}

# [90] And a city also has rings.
S[90] = {'en': [], 'zh': []}

# [91] And we're standing right here on one of these rings | showing the medieval part of the city | and outside there the more modern part of the city.
S[91] = {
    'en': [('rings', 'showing'), ('city', 'and')],
    'zh': [('上，', '展示'), ('分，', '而')]
}

# [92] The world changes fast | and you want to be ready for when it does.
S[92] = {'en': [('fast', 'and')], 'zh': [('快，', '你')]}

# [93] And that's what can make debt so scary.
S[93] = {'en': [], 'zh': []}

# [94] But it's as scary as it is common.
S[94] = {'en': [], 'zh': []}

# [95] So that's why when PDS debt reached out to sponsor today's video | and I saw that they have an A+ with the Better Business Bureau | as well as over a thousand positive reviews on Google, | that made me feel confident | that this is a service that could really help you if you're dealing with debt.
S[95] = {
    'en': [('video', 'and'), ('Bureau', 'as'), ('Google,', 'that'), ('confident', 'that')],
    'zh': [('时，', '我'), ('级，', '在'), ('价，', '这'), ('心，', '如果')]
}

# [96] They've helped hundreds of thousands of people break free from credit cards and loans and highinterest traps.
S[96] = {'en': [], 'zh': []}

# [97] PDS Debt crafts a personalized plan designed just for your unique financial situation.
S[97] = {'en': [], 'zh': []}

# [98] Their job is to help you save more, | pay off your debt faster, | and keep more money in your pocket where it belongs, | and there's no minimum credit score requirement.
S[98] = {
    'en': [('more,', 'pay'), ('faster,', 'and'), ('belongs,', 'and')],
    'zh': [('钱，', '更快'), ('务，', '把'), ('里，', '而且')]
}

# [99] If I were dealing with debt, | this would be a service I would absolutely be looking into.
S[99] = {'en': [('debt,', 'this')], 'zh': [('题，', '我')]}

# [100] So, you're just 30 seconds away from beginning your journey to being debtfree.
S[100] = {'en': [('So,', "you're")], 'zh': [('以，', '你')]}

# [101] Get your free assessment | and find the best option for you at pdsdebt.com/danielststeiner.
S[101] = {'en': [('assessment', 'and')], 'zh': [('估，', '在')]}

# [102] That's pdsdebt.com/danielsteiner.
S[102] = {'en': [], 'zh': []}

# [103] pds.com/danielststeiner.
S[103] = {'en': [], 'zh': []}

# [104] Back to the video about Amsterdam's map.
S[104] = {'en': [], 'zh': []}

# [105] It's kind of hard to overstate the impact | that the Reformation had on Europe.
S[105] = {'en': [('impact', 'that')], 'zh': [('响', '怎么')]}

# [106] Not just directly, | but also the chain of events that it caused.
S[106] = {'en': [('directly,', 'but')], 'zh': [('响，', '还有')]}

# [107] The Reformation sparked wars across Europe.
S[107] = {'en': [], 'zh': []}

# [108] Backed by the Pope, | kings and emperors sent out armies to crush cities that opposed Catholic rule.
S[108] = {'en': [('Pope,', 'kings')], 'zh': [('下，', '国王')]}

# [109] At first, Amsterdam stayed loyal to Catholic Spain, | but by 1578, it officially became Protestant.
S[109] = {'en': [('Spain,', 'but')], 'zh': [('班牙，', '但')]}

# [110] >> It was called the Alterasi.
S[110] = {'en': [], 'zh': []}

# [111] So, we're welcoming sort of Protestant refugees also from all over Europe.
S[111] = {'en': [('So,', "we're")], 'zh': [('以，', '我们')]}

# [112] >> And this happened just before the fall of Antworp, | the moment when the Spanish captured the largest and wealthiest city in the low countries.
S[112] = {'en': [('Antworp,', 'the')], 'zh': [('前，', '当时')]}

# [113] And fell into the into Spanish hands | and almost half of the population left the city | and Amsterdam took over as the main trade hub in the Netherlands and even in in the northwest Europe.
S[113] = {
    'en': [('hands', 'and'), ('city', 'and')],
    'zh': [('中，', '近一半'), ('市，', '阿姆斯特丹')]
}

# [114] So at that time Amsterdam started to grow really really really fast | and new harbor areas were created | and they really had to be designed to accommodate this large influx of people.
S[114] = {
    'en': [('fast', 'and'), ('created', 'and')],
    'zh': [('长，', '新的'), ('来，', '而且')]
}

# [115] A new city wall was built further out | and the original one was torn down.
S[115] = {'en': [('out', 'and')], 'zh': [('来，', '原来')]}

# [116] This actually created an open space around that original city gate that we were looking at, | which would now be used as a way station in the center of a city market, | which is still referenced in the name of the area.
S[116] = {
    'en': [('at,', 'which'), ('market,', 'which')],
    'zh': [('地，', '现在'), ('站，', '这一点')]
}

# [117] On the east side of the city, a canal was added, | and on the west side, a much more robust harbor.
S[117] = {'en': [('added,', 'and')], 'zh': [('道；', '在')]}

# [118] This harbor area is the perfect visual example on a map | of what was about to happen to Amsterdam.
S[118] = {'en': [('map', 'of')], 'zh': [('子', '展示')]}

# [119] The Dutch were going to take the naval strength they had | and turn it into a global power.
S[119] = {'en': [('had', 'and')], 'zh': [('力', '转变')]}

# [120] If you look at the map, | you can see that Amsterdam is sort of between the eastern part of Europe, Finland to to Denmark to Poland | and the southern parts, Spain.
S[120] = {
    'en': [('map,', 'you'), ('Poland', 'and')],
    'zh': [('图，', '可以'), ('波兰', '和')]
}

# [121] So Amsterdam is perfectly positioned in the middle.
S[121] = {'en': [], 'zh': []}

# [122] And there's a second nice position.
S[122] = {'en': [], 'zh': []}

# [123] You can see actually that Amsterdam is at the end of a huge European delta of rivers.
S[123] = {'en': [], 'zh': []}

# [124] crisscrossing all the way through the continent. | By capitalizing on this position, | Amsterdam ushered in the Dutch golden age.
S[124] = {
    'en': [('continent.', 'By'), ('position,', 'Amsterdam')],
    'zh': [('陆。', '凭借'),('势，', '阿姆斯特丹')]
}

# [125] Amsterdam became the financial capital of the world.
S[125] = {'en': [], 'zh': []}

# [126] And it was under these circumstances | that the modern stock exchange was born.
S[126] = {'en': [('circumstances', 'that')], 'zh': [('下，', '现代')]}

# [127] It was during this era | that the canal belt we know was created.
S[127] = {'en': [('era', 'that')], 'zh': [('代，', '我们')]}

# [128] The Dutch East India Company and later the Dutch West India Company were established | and began extracting resources from all over the world.
S[128] = {'en': [('established', 'and')], 'zh': [('立，', '开始')]}

# [129] The Dutch Golden Age was more than just money.
S[129] = {'en': [], 'zh': []}

# [130] It was an era of scientific advancement, | an outpouring of art from people like Rembrandt and Vermeier, | and closely related, mapping.
S[130] = {
    'en': [('advancement,', 'an'), ('Vermeier,', 'and')],
    'zh': [('代，', '是'), ('代，', '与之')]
}

# [131] The Dutch got really good at mapping.
S[131] = {'en': [], 'zh': []}

# [132] The largest and most expensive book published in the 17th century was a 600page atlas published by Yan Blau.
S[132] = {'en': [], 'zh': []}

# [133] It displayed the precision and quality of mapmaking at the height of the Dutch Golden Age.
S[133] = {'en': [], 'zh': []}

# [134] As Amsterdam grew in global prominence, | so did its risk of outside threat.
S[134] = {'en': [('prominence,', 'so')], 'zh': [('升，', '其')]}

# [135] Surrounded by Spain, England, and France, | it became clear that fortifications and canals would need to be built to protect the city.
S[135] = {'en': [('France,', 'it')], 'zh': [('围，', '显然')]}

# [136] >> The city was expanding | and was doing well.
S[136] = {'en': [('expanding', 'and')], 'zh': [('张，', '发展')]}

# [137] So also a lot of people from from Germany, for instance, from Scandinavia came here to work | to build these canals uh | to work on the ships that were sailing to uh Asia.
S[137] = {
    'en': [('work', 'to'), ('uh', 'to')],
    'zh': [('作，', '修建'), ('河，', '在')]
}

# [138] So the city grew very very fast in the 17th century.
S[138] = {'en': [], 'zh': []}

# [139] >> The solution was drawn up under the city surveyor and the city engineer.
S[139] = {'en': [], 'zh': []}

# [140] The plan would double the size of Amsterdam.
S[140] = {'en': [], 'zh': []}

# [141] Streets and canals followed a carefully designed grid and arc pattern | adapted to the swampy terrain.
S[141] = {'en': [('pattern', 'adapted')], 'zh': [('式，', '适应')]}

# [142] But there was a risk.
S[142] = {'en': [], 'zh': []}

# [143] Would the city continue to grow in population at the same rate?
S[143] = {'en': [], 'zh': []}

# [144] What if they built all this | and no one came?
S[144] = {'en': [('this', 'and')], 'zh': [('切', '但')]}

# [145] So the solution was to do it in two parts.
S[145] = {'en': [], 'zh': []}

# [146] >> It's almost like a windscreen wiper.
S[146] = {'en': [], 'zh': []}

# [147] You see the city expanding like a like a windscreen | and at one point it's it stops.
S[147] = {'en': [('windscreen', 'and')], 'zh': [('器', '到')]}

# [148] >> And within this plan there are two distinct sections.
S[148] = {'en': [], 'zh': []}

# [149] The first is a series of canals.
S[149] = {'en': [], 'zh': []}

# [150] These were positioned at different distances from each other | to create one row for the wealthiest canal houses with the largest garden areas | and another for the slightly less wealthy.
S[150] = {
    'en': [('other', 'to'), ('areas', 'and')],
    'zh': [('同，', '为'), ('积，', '为稍逊')]
}

# [151] These were very much intended to be separated from the rest of the expansion, | the Jordan.
S[151] = {'en': [('expansion,', 'the')], 'zh': [('分——', '约旦')]}

# [152] This area was for the lower class | to keep their smelly, noisy work.
S[152] = {'en': [('class', 'to')], 'zh': [('备，', '让')]}

# [153] But by the time they started building this, | they had a problem.
S[153] = {'en': [('this,', 'they')], 'zh': [('时，', '遇到')]}

# [154] There had been so many immigrants moving to the city | that many of them had just started building on random plots outside the city wall.
S[154] = {'en': [('city', 'that')], 'zh': [('了，', '许多')]}

# [155] This turned into like like a giant puzzle of people | they had to move around.
S[155] = {'en': [('people', 'they')], 'zh': [('图，', '必须')]}

# [156] So what they did was they created the canals next to the existing city.
S[156] = {'en': [], 'zh': []}

# [157] And many of the people who are already living there, | they moved out into the agricultural land that was also urbanized.
S[157] = {'en': [('there,', 'they')], 'zh': [('人', '被')]}

# [158] It was like a a phob informally urbanized area | and they had to move out from the canal to make room for the canals.
S[158] = {'en': [('area', 'and')], 'zh': [('域，', '他们')]}

# [159] They moved them out into the Yordan area. | Uh and then the structure of this Yordan area couldn't be changed anymore | because part of the building was already there. | So it was already urbanized
S[159] = {
    'en': [('area.', 'Uh'), ('anymore', 'because'), ('there.', 'So')],
    'zh': [('区。', '而后来'), ('变，', '因为'), ('了。', '所以')]
}

# [160] before it really became part of the city. | And that is why you see these different structures on the map.
# ZH: 这就是为什么你在地图上看到这些不同的结构。
# ZH is a single sentence covering both EN sub-clauses -> [copy] for ZH[160.2]
S[160] = {
    'en': [('city.', 'And')],
    'zh': [('构。', 'COPY')]  # Second sub-clause is [copy]
}

# [161] >> You can see that the angle and width of the roads in the Jordan area perfectly match the farming pattern. | This is a direct result of how fast the city was growing.
S[161] = {
    'en': [('pattern.', 'This')],
    'zh': [('合。', '这是')]
}

# [162] >> So this was really an outskirt of Amsterdam. | There were no burrow fairs. | You couldn't go through and nobody needed to go through because it was like the edge of the city.
S[162] = {
    'en': [('Amsterdam.', 'There'), ('fairs.', 'You')],
    'zh': [('区。', '那里'), ('集。', '你')]
}

# [163] No industries were allowed in the canal zone | because this was the residential zone and zoning was very strict.
S[163] = {'en': [('zone', 'because')], 'zh': [('业', '因为')]}

# [164] So all the industries were pushed out into uh the Yordan area | which at the same time was uh lying lower.
S[164] = {'en': [('area', 'which')], 'zh': [('区，', '而')]}

# [165] So also the canals were uh less deep and like the the profile the the water didn't flow through it at all. | So the water was still | so there was a very big environmental problem that was created by this fragmentation of the plan.
S[165] = {
    'en': [('all.', 'So'), ('still', 'so')],
    'zh': [('通。', '水是'), ('的，', '所以')]
}

# [166] >> The city must have stunk. | Everywhere I've read about this, it's mentioned how bad the city smelled.
S[166] = {
    'en': [('stunk.', 'Everywhere')],
    'zh': [('天。', '我读过的')]
}

# [167] It was used as an open sewer all the way to 1930. | So, I don't think there was anywhere in the city that wasn't smelly.
S[167] = {
    'en': [('1930.', 'So,')],
    'zh': [('年。', '所以')]
}

# [168] But because Jordan was made up of a bunch of wooden structures that were really densely packed together, | many of the fires that did happen in the city happened in this area.
S[168] = {'en': [('together,', 'many')], 'zh': [('起，', '城市')]}

# [169] And on its other side was the new bastioned wall and moat, | the path of which is still visible in a modern map.
S[169] = {'en': [('moat,', 'the')], 'zh': [('河，', '其')]}

# [170] By the time they built this, | it was already fully populated.
S[170] = {'en': [('this,', 'it')], 'zh': [('时，', '这里')]}

# [171] Population growth had slowed slightly, | but it was still growing, | and the Dutch were still expanding their colonies.
S[171] = {
    'en': [('slightly,', 'but'), ('growing,', 'and')],
    'zh': [('缓，', '但'), ('长，', '荷兰人')]
}

# [172] So, they decided to continue on with their plan, | completing the full star-shaped bastion ring around the city. | But just 10 years after it was finished being constructed
S[172] = {
    'en': [('plan,', 'completing'), ('city.', 'But')],
    'zh': [('划，', '完成'), ('环。', '但')]
}

# [173] came what would be known as the year of disaster. | A moment of attack from England and France that marked the end of the golden age. | The population stopped growing and urban development froze.
S[173] = {
    'en': [('disaster.', 'A'), ('age.', 'The')],
    'zh': [('年。', '来自'), ('结。', '人口')]
}

# [174] >> The upside of economic downturn was that there was a lot of greenery in inside Amsterdam.
S[174] = {'en': [], 'zh': []}

# [175] The burglar masters of Amsterdam, the Amsterdam government, | they chose to make the best of it.
S[175] = {'en': [('government,', 'they')], 'zh': [('府，', '他们')]}

# [176] And as they couldn't sell these as building plots, | they uh chose to rent them as um garden plots. | The area was called the Plantagia, | which we translate as plantation, | a big green area inside the city. | The only remnant of this plantation area, this Plantagia, is the zoo called artistis, | but the rest was parcel out and sold.
S[176] = {
    'en': [('plots,', 'they'), ('plots.', 'The'), ('Plantagia,', 'which'), ('plantation,', 'a'), ('city.', 'The'), ('artistis,', 'but')],
    'zh': [('售，', '他们'), ('租。', '这个'), ('Plantagia，', '我们'), ('园，', '城内'), ('地。', '这片'), ('物园，', '其余')]
}

# [177] Amsterdam's modern development has jumped the canal belt. | But it was the golden age that forged the iconic foundation of the city.
S[177] = {
    'en': [('belt.', 'But')],
    'zh': [('带。', '但')]
}

# [178] In the 19th century, after 200 years of stagnation, | everything started again
S[178] = {'en': [('stagnation,', 'everything')], 'zh': [('后，', '一切')]}

# [179] with the creation of the North Sea Canal, | which gave Amsterdam a new link to the North Sea and a new connection to the world for bigger ships.
S[179] = {
    'en': [('Canal,', 'which')],
    'zh': [('建，', '为')]
}

# [180] So that gave a big impulse to the harbor.
S[180] = {'en': [], 'zh': []}

# [181] And at the same time the central station was created | and they built central station on an artificial island in front of the harbor.
S[181] = {'en': [('created', 'and')], 'zh': [('来，', '他们')]}

# [182] >> The construction of this central station really cut off the city from that harbor.
S[182] = {'en': [], 'zh': []}

# [183] >> There were huge discussions concerning about the location of this station. | So actually the Dutch government not the Amsterdam government took the decision to create central station over there.
S[183] = {
    'en': [('station.', 'So')],
    'zh': [('议。', '实际上')]
}

# [184] >> There have been many efforts over the years | to make the city center more accessible.
S[184] = {'en': [('years', 'to')], 'zh': [('力，', '为了')]}

# [185] They created a breakthrough street strat city hall street | which connects the now palace on dam square which used to be city hall | to the new areas that were being developed beyond the city walls in the 19th century.
S[185] = {
    'en': [('street', 'which'), ('hall', 'to')],
    'zh': [('street，', '将'), ('厅）', '与')]
}

# [186] So this street is from the from the 1880s. | This is like a quite a nice ensemble of 19th century building by the Fronent architectural firm | which was one of the best I think in Amsterdam's 19th century >> architecture scene.
S[186] = {
    'en': [('1880s.', 'This'), ('firm', 'which')],
    'zh': [('的。', '这是一组'), ('计，', '我认为')]
}

# [187] Yeah. >> But despite all of the changes and proposals, | Amsterdam has still managed to keep its charm.
S[187] = {'en': [('proposals,', 'Amsterdam')], 'zh': [('议，', '阿姆斯特丹')]}

# [188] >> If you're on the canals, | you never have a line of sight that goes on for too long.
S[188] = {'en': [('canals,', 'you')], 'zh': [('上，', '你的')]}

# [189] And that makes it feel cozy. | Because if you compare that to a place like Paris | where they completely redesigned the city in the 19th century | and it's very clear that it's not tailored to to a person but it has a different idea. | But Amsterdam is still very very human.
S[189] = {
    'en': [('cozy.', 'Because'), ('Paris', 'where'), ('century', 'and'), ('idea.', 'But')],
    'zh': [('馨。', '因为'), ('比，', '巴黎'), ('计过，', '明显'), ('念。', '但')]
}

# [190] I have to say after making all of the videos that I have made about New York and about New Amsterdam | and now being here and thinking about that, | it's making me wonder what New York could have been like if the English hadn't taken over.
S[190] = {
    'en': [('Amsterdam', 'and'), ('that,', "it's")],
    'zh': [('后，', '现在'), ('些，', '让')]
}

# [191] could have been a very different city. | Might have felt like this.
S[191] = {
    'en': [('city.', 'Might')],
    'zh': [('市。', '也许')]
}

# [192] >> For me, it's always a feeling of, you know, actually walking through history. | The further you move away from the center, from the origins of the city, | you move through history and you get more and more to contemporary city.
S[192] = {
    'en': [('history.', 'The'), ('city,', 'you')],
    'zh': [('觉。', '你从'), ('走，', '就越')]
}

# [193] >> And if you can't go walk physically through it, | maybe now you can read it on its map.
S[193] = {'en': [('it,', 'maybe')], 'zh': [('过，', '也许')]}

# [194] Huge thanks to Yap, Yakam, and Anmarie for helping me with this video. | I've put links in the description to all of their work, | so you can go check that out.
S[194] = {
    'en': [('video.', "I've"), ('work,', 'so')],
    'zh': [('频。', '我在'), ('接，', '你们')]
}

# [195] And to the rest of you, | thank you for watching.
S[195] = {'en': [('you,', 'thank')], 'zh': [('位，', '感谢')]}

# [196] If you liked this, | please hit the like button. | Please subscribe to the channel if you haven't. | We just hit 300,000, so that's really exciting. | Share with your friends and family.
S[196] = {
    'en': [('this,', 'please'), ('button.', 'Please'), ("haven't.", 'We'), ('exciting.', 'Share')],
    'zh': [('频，', '请'), ('赞。', '如果'), ('道。', '我们'), ('动。', '分享')]
}

# [197] And if you want to support me on my Patreon, | that's also linked below. | But either way, I'll see you guys in another video very soon.
S[197] = {
    'en': [('Patreon,', "that's"), ('below.', 'But')],
    'zh': [('我，', '链接'), ('下。', '但')]
}

# [198] Peace.
S[198] = {'en': [], 'zh': []}


def get_last_word(text):
    """Get the last word of the text, preserving punctuation."""
    words = text.split()
    return words[-1] if words else ""

def get_last_chinese_chars(text, n=2):
    """Get the last 1-2 Chinese characters (汉字) from the text."""
    # Scan from end to find Chinese characters
    chinese_chars = []
    for ch in reversed(text):
        if '一' <= ch <= '鿿' or '　' <= ch <= '〿' or ch in '，。、；：？！""''（）【】《》—…·':
            chinese_chars.append(ch)
            if len(chinese_chars) == n:
                break
    if chinese_chars:
        return ''.join(reversed(chinese_chars))
    # Fallback: last char
    return text[-1] if text else ""


def generate_output():
    lines = []
    for idx in range(199):
        en_text = en_texts.get(idx, "")
        zh_text = zh_texts.get(idx, "")
        if not en_text and not zh_text:
            continue

        sp_en = S[idx]['en']
        sp_zh = S[idx]['zh']
        k = len(sp_en) + 1  # number of sub-clauses

        # Validate lengths
        if len(sp_en) != len(sp_zh):
            print(f"WARNING: Index {idx}: {len(sp_en)} EN splits but {len(sp_zh)} ZH splits")
            continue

        # Generate EN lines
        for m in range(k):
            sub_idx = m + 1
            if m < k - 1:
                last_word, first_word = sp_en[m]
                lines.append(f"[{idx}.{sub_idx}:en] {last_word}[segment]{first_word}")
            else:
                last_word = get_last_word(en_text)
                lines.append(f"[{idx}.{sub_idx}:en] {last_word}[segment]")

        # Generate ZH lines
        zh_copy_pending = False
        for m in range(k):
            sub_idx = m + 1
            if zh_copy_pending:
                lines.append(f"[{idx}.{sub_idx}:zh] [copy]")
                zh_copy_pending = False
                continue
            if m < k - 1:
                last_chars = sp_zh[m][0]
                if len(sp_zh[m]) >= 2 and sp_zh[m][1] == 'COPY':
                    # Current sub-clause ends normally, NEXT sub-clause is [copy]
                    lines.append(f"[{idx}.{sub_idx}:zh] {last_chars}[segment]")
                    zh_copy_pending = True
                else:
                    first_chars = sp_zh[m][1]
                    lines.append(f"[{idx}.{sub_idx}:zh] {last_chars}[segment]{first_chars}")
            else:
                last_chars = get_last_chinese_chars(zh_text)
                lines.append(f"[{idx}.{sub_idx}:zh] {last_chars}[segment]")

    return lines


output_lines = generate_output()

# Write output
output_path = "/Users/gtt/Documents/YTV_C/Amsterdam_s_Map_Explained/Subtitle/step6_chunks/chunk-01-segmented.md"
with open(output_path, 'w') as f:
    for line in output_lines:
        f.write(line + '\n')

print(f"Generated {len(output_lines)} lines total")

# Print first 20 and last 20 lines for verification
print("\n=== FIRST 20 LINES ===")
for l in output_lines[:20]:
    print(l)

print("\n=== LAST 20 LINES ===")
for l in output_lines[-20:]:
    print(l)

# Count indices
indices = set()
for l in output_lines:
    m = re.match(r'\[(\d+)', l)
    if m:
        indices.add(int(m.group(1)))
print(f"\nLines cover indices: {sorted(indices)}")
print(f"Count: {len(indices)}")
