from ttapi import Bot
import re
import threading
import random

AUTH   = 'NsmyqibhgBhWfNImLgzjaMAV'
USERID = '50f34338aaa5cd0c2e7d1d1e'
#ROOMID = '4e1f8b6614169c5fba0005a0' 
#ROOMID = '4f1e02590c4cc807574030f1' #treehouise
ROOMID = '5105bbc1aaa5cd73a44088ac' #Electronic Indie Mix

#QT's having too much fun!
# LOL go away. LOL


autobopStat = True

bot = Bot(AUTH, USERID, ROOMID)

loly = '4fdbf002eb35c13d060003fc'
jr = '4fb79594aaa5cd2ea4000083'
jr_msg = 'ew, its jordan'
blue = '4e0fb8894fe7d074cd08c1b7'
me = '4e373deaa3f75118b10a9139'

greet = ['You are such a rockstar', 'ILYSM', 'Been waiting FOREVER for you', 'Long time no see']

butts = ['I like big BUTTS and I cannot lie!',
	'Guess who got a big \'ole butt?',
	'I got a butt!',
	'But what?', 'That\'s not much of a trunk to work with!?',
	'Butts are for sitting',
	'Stop starring at my arse already!',
	'No you can\'t touch my butt',
 	'I like my butt where it is thanks',
	'No buts about it', 'Those tight jeans make your butt disappear', 
	'I can fit my butt into your shirt',
	'My butt got scratches on it!!',
	'Who\'s spreading rumors about my butt??',
	'Butts up for grabs!', 'Exit only dude',
	'You can squeeze my butt anytime',
	'BUTTS WANTED. APPLY WITHIN.',
	'Gimmme your butt', 'Your butt is saagggggging', 
	'Anyone with tats on their butts?',
	'I am very familiar with butts',
	'I prefer the Rugby-butt over the Football-butt.',
	'Leb can squeeze a nickle between his butt-cheeks',
	'You prefer bigger or smaller butts?',
	'Did your butt shrink lately?',
	'brb. gotta go poop',
	'pop a little sugar on ma booty!',
	'I want in on the birthday spankings!',
	'Shake it',
	'Shake it like you got some',
	'Butt-off',
	'Grow up already.',
	'smack that boo-tay!'
	]

trivia = [ 'No trivia yet.'
 	]

randoms = ['Loly is my favorite brown bear', 'We\'re all a part of the hobo :eggplant: cult', 'I wanna be a bear to join the hobos',
	'When will you admit you love me?', 'If I won a zillion dollars I\'d def give you a million', 'It\'s currently half-past a freckle',
	'Douse me with your admiration!', 'I just wanna be luved', 'I can wink with both my eyes at the same time', 
	'Someone fetch the hose and cool that bear off!', 'My heart is reserved for Tom-o', 'GIMME MY TWO DOLLA\'S!'
	]

jokes = [ 'Do not argue with an idiot. He will drag you down to his level and beat you with experience.',
	'I want to die peacefully in my sleep, like my grandfather.. Not screaming and yelling like the passengers in his car.',
	'I asked God for a bike, but I know God doesn\'t work that way. So I stole a bike and asked for forgiveness.',
	'Sex is not the answer. Sex is the question. \'Yes\' is the answer.',
	'Going to church doesn\'t make you a Christian any more than standing in a garage makes you a car.',
	'We live in a society where pizza gets to your house before the police.',
	'Women might be able to fake orgasms. But men can fake a whole relationship.',
	'The last thing I want to do is hurt you. But it\'s still on the list.',
	'Light travels faster than sound. This is why some people appear bright until you hear them speak.',
	'If I agreed with you we\'d both be wrong.',
	'Men have two emotions: Hungry and Horny. If you see him without an erection, make him a sandwich.',
	'We never really grow up, we only learn how to act in public.',
	'War does not determine who is right - only who is left.',
	'Knowledge is knowing a tomato is a fruit; Wisdom is not putting it in a fruit salad.',
	'Children: You spend the first 2 years of their life teaching them to walk and talk. Then you spend the next 16 years telling them to sit down and shut-up.',
	'Politicians and diapers have one thing in common. They should both be changed regularly, and for the same reason.',
	'My mother never saw the irony in calling me a son-of-a-bitch.',
	'Having sex is like playing bridge. If you don\'t have a good partner, you\'d better have a good hand.',
	'The early bird might get the worm, but the second mouse gets the cheese.',
	'Evening news is where they begin with \'Good evening\', and then proceed to tell you why it isn\'t.',
	'Fighting for peace is like fucking for virginity.',
	'If sex is a pain in the ass, then you\'re doing it wrong...',
	'To steal ideas from one person is plagiarism. To steal from many is research.',
	'If God is watching us, the least we can do is be entertaining.',
	'If 4 out of 5 people SUFFER from diarrhea... does that mean that one enjoys it?',
	'If you think nobody cares if you\'re alive, try missing a couple of payments.',
	'Better to remain silent and be thought a fool, than to speak and remove all doubt.',
	'How is it one careless match can start a forest fire, but it takes a whole box to start a campfire?',
	'A bus station is where a bus stops. A train station is where a train stops. On my desk, I have a work station..',
	'Some people are like Slinkies ... not really good for anything, but you can\'t help smiling when you see one tumble down the stairs.',
	'Did you know that dolphins are so smart that within a few weeks of captivity, they can train people to stand on the very edge of the pool and throw them fish?',
	'A bank is a place that will lend you money, if you can prove that you don\'t need it.',
	'I thought I wanted a career, turns out I just wanted paychecks.',
	'Never, under any circumstances, take a sleeping pill and a laxative on the same night.',
	'Whenever I fill out an application, in the part that says \'If an emergency, notify:\' I put "DOCTOR". What\'s my mother going to do?',
	'I didn\'t fight my way to the top of the food chain to be a vegetarian',
	'A computer once beat me at chess, but it was no match for me at kick boxing.',
	'I didn\'t say it was your fault, I said I was blaming you.',
	'I saw a woman wearing a sweat shirt with \'Guess\' on it...so I said \'Implants?\'',
	'Why does someone believe you when you say there are four billion stars, but check when you say the paint is wet?',
	'The sole purpose of a child\'s middle name, is so he can tell when he\'s really in trouble.',
	'God must love stupid people. He made SO many.',
	'Women will never be equal to men until they can walk down the street with a bald head and a beer gut, and still think they are sexy.',
	'Good girls are bad girls that never get caught.',
	'Behind every successful man is his woman. Behind the fall of a successful man is usually another woman.',
	'Some people say \'If you can\'t beat them, join them\'. I say \'If you can\'t beat them, beat them\', because they will be expecting you to join them, so you will have the element of surprise.',
	'Why do Americans choose from just two people to run for president and 50 for Miss America?',
	'Crowded elevators smell different to midgets.',
	'You do not need a parachute to skydive. You only need a parachute to skydive twice.',
	'The voices in my head may not be real, but they have some good ideas!',
	'A clear conscience is usually the sign of a bad memory.',
	'The main reason Santa is so jolly is because he knows where all the bad girls live.',
	'Laugh at your problems, everybody else does.',
	'Never get into fights with ugly people, they have nothing to lose.',
	'It\'s not the fall that kills you; it\'s the sudden stop at the end.',
	'Artificial intelligence is no match for natural stupidity.',
	'Always borrow money from a pessimist. He won\'t expect it back.',
	'He who smiles in a crisis has found someone to blame.',
	'A diplomat is someone who can tell you to go to hell in such a way that you will look forward to the trip.',
	'We have enough gun control. What we need is idiot control.',
	'Hospitality: making your guests feel like they\'re at home, even if you wish they were.',
	'My opinions may have changed, but not the fact that I am right.',
	'Money can\'t buy happiness, but it sure makes misery easier to live with.',
	'When in doubt, mumble.',
	'I discovered I scream the same way whether I\'m about to be devoured by a great white shark or if a piece of seaweed touches my foot.',
	'I intend to live forever. So far, so good.',
	'Women may not hit harder, but they hit lower.',
	'A little boy asked his father, \'Daddy, how much does it cost to get married?\' Father replied, \'I don\'t know son, I\'m still paying.\'',
	'Worrying works! 90% of the things I worry about never happen.',
	'Just remember...if the world didn\'t suck, we\'d all fall off.',
	'My psychiatrist told me I was crazy and I said I want a second opinion. He said okay, you\'re ugly too.',
	'Some cause happiness wherever they go. Others whenever they go.',
	'Jesus loves you, but everyone else thinks you\'re an asshole.',
	'I don\'t trust anything that bleeds for five days and doesn\'t die.',
	'I like work. It fascinates me. I sit and look at it for hours.',
	'I should\'ve known it wasn\'t going to work out between my ex-wife and me. After all, I\'m a Libra and she\'s a bitch.',
	'I always take life with a grain of salt, ...plus a slice of lemon, ...and a shot of tequila.',
	'Never hit a man with glasses. Hit him with a baseball bat.',
	'There\'s a fine line between cuddling and holding someone down so they can\'t get away.',
	'I used to be indecisive. Now I\'m not sure.',
	'You\'re never too old to learn something stupid.',
	'When tempted to fight fire with fire, remember that the Fire Department usually uses water.',
	'You are such a good friend that if we were on a sinking ship together and there was only one life jacket... I\'d miss you heaps and think of you often.',
	'I got in a fight one time with a really big guy, and he said, "I\'m going to mop the floor with your face.\' I said, "You\'ll be sorry." He said, "Oh, yeah? Why?" I said, "Well, you won\'t be able to get into the corners very well."',
	'Knowledge is power, and power corrupts. So study hard and be evil.',
	'Does this rag smell like chloroform to you?',
	'With sufficient thrust, pigs fly just fine.',
	'To be sure of hitting the target, shoot first and call whatever you hit the target.',
	'A bargain is something you don\'t need at a price you can\'t resist.',
	'Some people hear voices.. Some see invisible people.. Others have no imagination whatsoever.',
	'A TV can insult your intelligence, but nothing rubs it in like a computer.',
	'If winning isn\'t everything why do they keep score?',
	'Virginity is like a soapbubble, one prick and it is gone.',
	'If at first you don\'t succeed, skydiving is not for you!',
	'A bus is a vehicle that runs twice as fast when you are after it as when you are in it.',
	'Hallmark Card: "I\'m so miserable without you, it\'s almost like you\'re still here."',
	'Whoever coined the phrase "Quiet as a mouse" has never stepped on one.',
	'If you are supposed to learn from your mistakes, why do some people have more than one child.',
	'Nostalgia isn\'t what it used to be.',
	'The shinbone is a device for finding furniture in a dark room.'
	]

cats = ['What does a cat drive? A Catillac!', 
	'If a cats head can fit through something, so can the rest of its body', 
	'Ancient Egyptian family members shaved their eyebrows in mourning when the family cat died.', 
	'A cat has two vocal chords, and can make over 100 sounds.', 
	'Why do people love cats? Because they are purrrrr-fect!', 
	'Cat urine glows under a blacklight.', 
	'If a cats head can fit through something, so can the rest of its body', 
	'Cats dislike citrus scent.' ,
	'A cat has a total of 24 whiskers, 4 rows of whiskers on each side. The upper two rows can move independently of the bottom two rows.', 
	'Cats have 30 teeth (12 incisors, 10 premolars, 4 canines, and 4 molars), while dogs have 42. Kittens have baby teeth, which are replaced by permanent teeth around the age of 7 months.',
	'A cat\'s jaw has only up and down motion; it does not have any lateral, side to side motion, like dogs and humans.',
	'A cat\'s tongue has tiny barbs on it.', 
	'Cats lap liquid from the underside of their tongue, not from the top.',
	'Cats purr at the same frequency as an idling diesel engine, about 26 cycles per second.', 
	'Domestic cats purr both when inhaling and when exhaling.',
	'The cat\'s front paw has 5 toes, but the back paws have 4. Some cats are born with as many as 7 front toes and extra back toes (polydactl).',
	'Cats walk on their toes.',
	'A domestic cat can sprint at about 31 miles per hour.',
	'A kitten will typically weigh about 3 ounces at birth.  The typical male housecat will weigh between  7 and 9 pounds, slightly less for female housecats.',
	'Cats take between 20-40 breaths per minute.',
	'A cat\'s field of vision is about 200 degrees.',
	'Unlike humans, cats do not need to blink their eyes on a regular basis to keep their eyes lubricated.',
	'Blue-eyed, pure white cats are frequently deaf.',
	'It may take as long as 2 weeks for a kitten to be able to hear well.  Their eyes usually open between 7 and 10 days, but sometimes it happens in as little as 2 days.',
	'Cats can judge within 3 inches the precise location of a sound being made 1 yard away.',
	'Cats can be right-pawed or left-pawed.',
	'A cat cannot see directly under its nose.',
	'Almost 10% of a cat\'s bones are in its tail, and the tail is used to maintain balance.',
	'Cats have 30 vertebrae (humans have 33 vertebrae during early development; 26 after the sacral and coccygeal regions fuse)',
	'The cat\'s clavicle, or collarbone, does not connect with other bones but is buried in the muscles of the shoulder region. This lack of a functioning collarbone allows them to fit through any opening the size of their head.',
	'The cat has 500 skeletal muscles (humans have 650).',
	'Cats have 32 muscles that control the outer ear (compared to human\'s 6 muscles each). A cat can rotate its ears independently 180 degrees, and can turn in the direction of sound 10 times faster than those of the best watchdog.',
	'Cats\' hearing is much more sensitive than humans and dogs.',
	'Cats\' hearing stops at 65 khz (kilohertz); humans\' hearing stops at 20 khz.',
	'A cat sees about 6 times better than a human at night, and needs 1/6 the amount of of light that a human does - it has a layer of extra reflecting cells which absorb light.',
	'Every year, nearly four million cats are eaten in Asia.',
	'On average, cats spend 2/3 of every day sleeping. That means a nine-year-old cat has been awake for only three years of its life.',
	'Unlike dogs, cats do not have a sweet tooth. Scientists believe this is due to a mutation in a key taste receptor.',
	'When a cat chases its prey, it keeps its head level. Dogs and humans bob their heads up and down.',
	'The technical term for a cat\'s hairball is a "bezoar."',
	'A group of cats is called a "clowder."',
	'Female cats tend to be right pawed, while male cats are more often left pawed. Interestingly, while 90% of humans are right handed, the remaining 10% of lefties also tend to be male.',
	'A cat cannot climb head first down a tree because its claws are curved the wrong way  A cat can\'t climb head first down a tree because every claw on a cat\'s paw points the same way. To get down from a tree, a cat must back down.',
	'Cats make about 100 different sounds. Dogs make only about 10.',
	'A cat\'s brain is biologically more similar to a human brain than it is to a dog\'s. Both humans and cats have identical regions in their brains that are responsible for emotions.',
	'There are more than 500 million domestic cats in the world, with approximately 40 recognized breeds.',
	'Approximately 24 cat skins can make a coat.',
	'While it is commonly thought that the ancient Egyptians were the first to domesticate cats, the oldest known pet cat was recently found in a 9,500-year-old grave on the Mediterranean island of Cyprus. This grave predates early Egyptian art depicting cats by 4,000 years or more.',
	'During the time of the Spanish Inquisition, Pope Innocent VIII condemned cats as evil and thousands of cats were burned. Unfortunately, the widespread killing of cats led to an explosion of the rat population, which exacerbated the effects of the Black Death.',
	'During the Middle Ages, cats were associated with withcraft, and on St. John\'s Day, people all over Europe would stuff them into sacks and toss the cats into bonfires. On holy days, people celebrated by tossing cats from church towers.',
	'Cats are the most popular pet in North American  Cats are North America\'s most popular pets: there are 73 million cats compared to 63 million dogs. Over 30% of households in North America own a cat.',
	'The first cat in space was a French cat named Felicette (a.k.a. "Astrocat") In 1963, France blasted the cat into outer space. Electrodes implanted n her brains sent neurological signals back to Earth. She survived the trip.',
	'The group of words associated with cat (catt, cath, chat, katze) stem from the Latin catus, meaning domestic cat, as opposed to feles, or wild cat.',
	'Approximately 40,000 people are bitten by cats in the U.S. annually.',
	'According to Hebrew legend, Noah prayed to God for help protecting all the food he stored on the ark from being eaten by rats. In reply, God made the lion sneeze, and out popped a cat.',
	'A cat\'s hearing is better than a dog\'s. And a cat can hear high-frequency sounds up to two octaves higher than a human.',
	'A cat can travel at a top speed of approximately 31 mph (49 km) over a short distance.',
	'A cat can jump up to five times its own height in a single bound.',
	'Some cats have survived falls of over 65 feet (20 meters), due largely to their "righting reflex." The eyes and balance organs in the inner ear tell it where it is in space so the cat can land on its feet. Even cats without a tail have this ability.',
	'A cat rubs against people to mark them as their territory  A cat rubs against people not only to be affectionate but also to mark out its territory with scent glands around its face. The tail area and paws also carry the cat\'s scent.',
	'Researchers are unsure exactly how a cat purrs. Most veterinarians believe that a cat purrs by vibrating vocal folds deep in the throat. To do this, a muscle in the larynx opens and closes the air passage about 25 times per second.',
	'When a family cat died in ancient Egypt, family members would mourn by shaving off their eyebrows. They also held elaborate funerals during which they drank wine and beat their breasts. The cat was embalmed with a sculpted wooden mask and the tiny mummy was placed in the family tomb or in a pet cemetery with tiny mummies of mice.',
	'In 1888, more than 300,000 mummified cats were found an Egyptian cemetery. They were stripped of their wrappings and carted off to be used by farmers in England and the U.S. for fertilizer.',
	'Most cats give birth to a litter of between one and nine kittens. The largest known litter ever produced was 19 kittens, of which 15 survived.',
	'Smuggling a cat out of ancient Egypt was punishable by death. Phoenician traders eventually succeeded in smuggling felines, which they sold to rich people in Athens and other important cities.',
	'The earliest ancestor of the modern cat lived about 30 million years ago. Scientists called it the Proailurus, which means "first cat" in Greek. The group of animals that pet cats belong to emerged around 12 million years ago.'
	'The biggest wildcat today is the Siberian Tiger. It can be more than 12 feet (3.6 m) long (about the size of a small car) and weigh up to 700 pounds (317 kg).',
	'The smallest wildcat today is the Black-footed cat. The females are less than 20 inches (50 cm) long and can weigh as little as 2.5 lbs (1.2 kg).',
	'Many Egyptians worshipped the goddess Bast, who had a woman\'s body and a cat\'s head.',
	'Mohammed loved cats and reportedly his favorite cat, Muezza, was a tabby. Legend says that tabby cats have an M for Mohammed on top of their heads because Mohammad would often rest his hand on the cat\'s head.',
	'While many parts of Europe and North America consider the black cat a sign of bad luck, in Britain and Australia, black cats are considered lucky.',
	'The most popular pedigreed cat is the Persian cat, followed by the Main Coon cat and the Siamese cat.',
	'The smallest pedigreed cat is a Singapura, which can weigh just 4 lbs (1.8 kg), or about five large cans of cat food. The largest pedigreed cats are Maine Coon cats, which can weigh 25 lbs (11.3 kg), or nearly twice as much as an average cat weighs.',
	'Some Siamese cats are cross-eyed to compensate for abnormal optic wiring  Some Siamese cats appear cross-eyed because the nerves from the left side of the brain go to mostly the right eye and the nerves from the right side of the brain go mostly to the left eye. This causes some double vision, which the cat tries to correct by "crossing" its eyes.',
	'Researchers believe the word "tabby" comes from Attabiyah, a neighborhood in Baghdad, Iraq. Tabbies got their name because their striped coats resembled the famous wavy patterns in the silk produced in this city.',
	'Cats hate the water because their fur does not insulate well when it\'s wet. The Turkish Van, however, is one cat that likes swimming. Bred in central Asia, its coat has a unique texture that makes it water resistant.',
	'The Egyptian Mau is probably the oldest breed of cat. In fact, the breed is so ancient that its name is the Egyptian word for "cat."',
	'The costliest cat ever is named Little Nicky, who cost his owner $50,000. He is a clone of an older cat.',
	'A cat usually has about 12 whiskers on each side of its face.',
	'A cat\'s eyesight is both better and worse than humans. It is better because cats can see in much dimmer light and they have a wider peripheral view. It\'s worse because they don\'t see color as well as humans do. Scientists believe grass appears red to cats.',
	'Spanish-Jewish folklore recounts that Adam\'s first wife, Lilith, became a black vampire cat, sucking the blood from sleeping babies. This may be the root of the superstition that a cat will smother a sleeping baby or suck out the child\'s breath.',
	'Perhaps the most famous comic cat is the Cheshire Cat in Lewis Carroll\'s Alice in Wonderland. With the ability to disappear, this mysterious character embodies the magic and sorcery historically associated with cats.',
	'In the original Italian version of Cinderella, the benevolent fairy godmother figure was a cat.',
	'Two Siamese cats discovered microphones hidden by Russian spies in Holland\'s embassy in Moscow  In Holland\'s embassy in Moscow, Russia, the staff noticed that the two Siamese cats kept meowing and clawing at the walls of the building. Their owners finally investigated, thinking they would find mice. Instead, they discovered microphones hidden by Russian spies. The cats heard the microphones when they turned on.',
	'The little tufts of hair in a cat\'s ear that help keep out dirt direct sounds into the ear, and insulate the ears are called ear furnishings.',
	'The ability of a cat to find its way home is called \'psi-traveling.\' Experts think cats either use the angle of the sunlight to find their way or that cats have magnetized cells in their brains that act as compasses.',
	'Isaac Newton invented the cat flap. Newton was experimenting in a pitch-black room. Spithead, one of his cats, kept opening the door and wrecking his experiment. The cat flap kept both Newton and Spithead happy.',
	'The world\'s rarest coffee, Kopi Luwak, comes from Indonesia where a wildcat known as the luwak lives. The cat eats coffee berries and the coffee beans inside pass through the stomach. The beans are harvested from the cat\'s dung heaps and then cleaned and roasted. Kopi Luwak sells for about $500 for a 450 g (1 lb) bag.',
	'A cat\'s jaw can\'t move sideways, so a cat can\'t chew large chunks of food.',
	'A cat almost never meows at another cat, mostly just humans. Cats typically will spit, purr, and hiss at other cats.',
	'A cat\'s back is extremely flexible because it has up to 53 loosely fitting vertebrae. Humans only have 34.',
	'Many cat owners think their cats can read their minds  Approximately 1/3 of cat owners think their pets are able to read their minds.',
	'All cats have claws, and all except the cheetah sheath them when at rest.',
	'Two members of the cat family are distinct from all others: the clouded leopard and the cheetah. The clouded leopard does not roar like other big cats, nor does it groom or rest like small cats. The cheetah is unique because it is a running cat; all others are leaping cats. They are leaping cats because they slowly stalk their prey and then leap on it.',
	'A cat lover is called an Ailurophilia (Greek: cat+lover).',
	'In Japan, cats are thought to have the power to turn into super spirits when they die. This may be because according to the Buddhist religion, the body of the cat is the temporary resting place of very spiritual people.',
	'Most cats had short hair until about 100 years ago, when it became fashionable to own cats and experiment with breeding.',
	'Cats have 32 muscles that control the outer ear (humans have only 6). A cat can independently rotate its ears 180 degrees.',
	'During the nearly 18 hours a day that kittens sleep, an important growth hormone is released  One reason that kittens sleep so much is because a growth hormone is released only during sleep.',
	'Cats have about 130,000 hairs per square inch (20,155 hairs per square centimeter).',
	'The heaviest cat on record is Himmy, a Tabby from Queensland, Australia. He weighed nearly 47 pounds (21 kg). He died at the age of 10.',
	'The oldest cat on record was Creme Puff from Austin, Texas, who lived from 1967 to August 6, 2005, three days after her 38th birthday. A cat typically can live up to 20 years, which is equivalent to about 96 human years.',
	'The lightest cat on record is a blue point Himalayan called Tinker Toy, who weighed 1 pound, 6 ounces (616 g). Tinker Toy was 2.75 inches (7 cm) tall and 7.5 inches (19 cm) long.',
	'The tiniest cat on record is Mr. Pebbles, a 2-year-old cat that weighed 3 lbs (1.3 k) and was 6.1 inches (15.5 cm) high.',
	'A commemorative tower was built in Scotland for a cat named Towser, who caught nearly 30,000 mice in her lifetime.',
	'In the 1750s, Europeans introduced cats into the Americas to control pests.',
	'The first cat show was organized in 1871 in London. Cat shows later became a worldwide craze.',
	'The first cartoon cat was Felix the Cat in 1919. In 1940, Tom and Jerry starred in the first theatrical cartoon \'Puss Gets the Boot.\' In 1981 Andrew Lloyd Weber created the musical Cats, based on T.S. Eliot\'s Old Possum\'s Book of Practical Cats.',
	'A cat has 230 bones in its body. A human has 206. A cat has no collarbone, so it can fit through any opening the size of its head.',
	'A cat\'s nose pad is ridged with a unique pattern, just like the fingerprint of a human.',
	'Foods that should not be given to cats include onions, garlic, green tomatoes, raw potatoes, chocolate, grapes, and raisins. Though milk is not toxic, it can cause an upset stomach and gas. Tylenol and aspirin are extremely toxic to cats, as are many common houseplants. Feeding cats dog food or canned tuna that\'s for human consumption can cause malnutrition.',
	'A 2007 Gallup poll revealed that both men and women were equally likely to own a cat.',
	'A cat\'s heart beats nearly twice as fast as a human heart, at 110 to 140 beats a minute.',
	'Cat\'s sweat only through their paws  Cats don\'t have sweat glands over their bodies like humans do. Instead, they sweat only through their paws.',
	'In just seven years, a single pair of cats and their offspring could produce a staggering total of 420,000 kittens.',
	'Cats spend nearly 1/3 of their waking hours cleaning themselves.',
	'Grown cats have 30 teeth. Kittens have about 26 temporary teeth, which they lose when they are about 6 months old.',
	'A cat called Dusty has the known record for the most kittens. She had more than 420 kittens in her lifetime.',
	'The largest cat breed is the Ragdoll. Male Ragdolls weigh between 12 and 20 lbs (5.4-9.0 k). Females weigh between 10 and 15 lbs (4.5-6.8 k).',
	'Cats are extremely sensitive to vibrations. Cats are said to detect earthquake tremors 10 or 15 minutes before humans can.',
	'In contrast to dogs, cats have not undergone major changes during their domestication process.',
	'A female cat is called a queen or a molly.',
	'In the 1930s, two Russian biologists discovered that color change in Siamese kittens depend on their body temperature. Siamese cats carry albino genes that work only when the body temperature is above 98F. If these kittens are left in a very warm room, their points won\'t darken and they will stay a creamy white.',
	'There are up to 60 million feral cats in the United States alone.',
	'The oldest cat to give birth was Kitty who, at the age of 30, gave birth to two kittens. During her life, she gave birth to 218 kittens.',
	'The most traveled cat is Hamlet, who escaped from his carrier while on a flight. He hid for seven weeks behind a pane. By the time he was discovered, he had traveled nearly 373,000 miles (600,000 km).',
	'The most expensive cat was an Asian Leopard cat (ALC)-Domestic Shorthair (DSH) hybrid named Zeus. Zeus, who is 90% ALC and 10% DSH, has an asking price of $154,000.',
	'The cat who holds the record for the longest non-fatal fall is Andy. He fell from the 16th floor of an apartment building (about 200 ft/.06 km) and survived.',
	'The richest cat is Blackie who was left 15 million English pounds by his owner, Ben Rea.',
	'The claws on the cat\'s back paws aren\'t as sharp as the claws on the front paws because the claws in the back don\'t retract and, consequently, become worn',
	'Recent studies have shown that cats can see blue and green. There is disagreement as to whether they can see red.' ]

connie = [ 'Connie is a world renowned trivia contestant - with more than 3 Pub Trivia wins under her belt.',
'Connie prides herself on impeccable grammar - especially when drunk.',
'When asked to choose between caek or pie, Connie made a caekpiean. The UChicago Archaeology dept keeps this frozen to preserve it for all the ages.',
'Connie has been asked for her hand in marriage by at least four guys, but rejected all of them.',
'Single, Smart, Sane, choose Connie.',
'Kony, the Afrian Warlord, actually uses a bastardization of Connie\'s name after he saw her perform Acapella for the starving kids of Mozambique.',
'CS guys love Connie. A lot.',
'Connie LOVES punny jokes!',
'Connie can never keep track of which boy she\'s texting and why.',
'Connie can play the viola with her toes.',
'Amanda was born Connie\'s sister. Whenever Connie is together with her, they can never ever stop cuddling.'
'Connie\'s cat Lily comes from a dystopian future where cats eat toes. Just don\'t mention it.'
]

mean = [ 'Don\'t be a meanie pants', 'Well say what you mean already', 'srsly', 'what exactly do you mean?', 'meanie-pants! meanie-pants!',
	'Don\'t make me turn this turntable around!']

sorry = [ 'Don\'t be sorry, we love you!', 'ILY!', 'Don\'t worry about it.', 'Only a fool has regrets', 'i\'d be sorry 2!' ]

homework = ['Homework SUX.', 'Don\'t bother with homework. Not worth the time invested.', 
	'Do your homework later.', 'I\'ll do your homework if you give me your dj spot!',
	'Super Mario comes before homework', 'Homework is what you do the 5 minutes before class starts',
	'Homework is for those who don\'t already know everything.' ]

death = ['Was\'t planning on it', 'To die, or not to die. That is the question', 'All in due time', 
	'I\'m not done on this planet yet', 'I have more work to do', 'After you', 'Don\'t get all sassy with me young minion']


whereqt = ['Where\'s QT?', 'I miss my qt', 'Will QT be joining us?', 'How come QT\'s not here?', 'I feel like I\'m channeling qt...']

qtfact = ['It\'s not QT sharing hour.', 'Wait until QT Sharing Hour.', 'You secretly wanna be her.', 'She is omniscient',
 	'QT lurves geeks (but not nerds)', 'QT is your hero!', 'We all lurve QT!', 'Shower QT with some luvin\'!', 'QT IS the original cutiepie',
	'QT LOVES CUPCAKES! :cake:', 'QT ROCKS! :beers: on me!', 'QT needs some luvin\'', '/me pokes Q-T-3.14[etc.]',
	'QT has more talking stuffed animals than you.', 'QT plays with toys.', 'QT is easily amused', 'QT\'s middle name is actually \'Sugar\'',
	'QT daydreams in the shower.', 'QT has a 2-pak stomach', 'QT plays Super Mario', 'QT loves to dance to the 80\'s',
	'QT will count your toes for you.', 'QT is special', 'QT doesn\'t actually exist', 'QT is only a figment of your imagination',
	'QT is easily exciteable', 'It\'s Q-T-sugar-PIE to you', 'QT is on a mission to find some Canadian meat and drag him back to NZ with her.' ]

lebs = ['Leb is such a lobster', 'Lebs ran naked through the streets. AND posed for pics', 'Leb thinks he\'s our leader...', 
	'Leb is a reincarnation of Mr. DD', 'Leb chases the D', 'Leb? Oh I cannot say what I want to actually say...',
	'Leb\'s name is "Leolooneyous" right?', 'Leb? not interested.', 'Lebs has a toe fetish.', 'Lebs likes ukeles!',
	'Leb wants more friends', 'You think Lebs is interesting?', 'Oh are we paying attention to Lebs now?', 'Do I have to be nice to Lebs?',
	'Isn\'t Leb a bot?', 'Leb wants a harem of women but waiting for you to organize it.', 'Lebs thought a 3-way had to do with driving.',
	'Lebs went out with :a::1:', 'Lebs is a 3D holographic projection of your inner reality.', 'Lebs used to work a street corner',
	'Lebs isn\'t sure of his species yet', 'Lebs is combobulating', 'No, Leb, that\'s not intended to be used as a statue...'
	 ]

alec = ['Alec needs more friends', 'Alec wishes he had some facts', 'Not interesting enough', 'Alec doesn\'t exist.', 'Alec is that guy', 'Alec wants to feel important',
	'Grow up Alec', 'Alec, your epidermis is showing' ]

chats = ['go fetch me some water', 'is now my minion', 'should try being quiet for a bit', ' that is NOT interesting', 
	'go away', 'ILY!', 'please dedicate a song to me!', 'will you love me forever?', 'can you get me a teddy bear?',
	'I want to have your babies', 'you should srsly clean out your belly button lint', 'dance for me!',
	'chill out!', 'dance with me!', 'just shoot me now', 'pew pew :gun:', 'sing me a song!', 'whisper sweet nothings to me',
	'I wanna live till I\'m 69', 'will you find two boys to fight over me please?' ]

def handleuser(data):
    userid = data['user'][0]['userid']
#    words = ''
    username = data['user'][0]['name']
    if username == 'Esoteric':
        bootUser(userid, 'You are not welcome here');
    #if userid == loly:
        #words = choice(greet) + ' Loly!'
    #elif userid == blue:
        #words = choice(greet) + ' Blue!' 
    #elif userid == jr:
        #words = jr_msg
    #elif userid == '4e373deaa3f75118b10a9139':
        #words = 'OMG QT you are the BESTEST!'
    #if words != '':
        #token = random.randrange(0, 2)
        #if token == 1:
            #t = threading.Timer(1000, bot.speak, words)
            #t.start()

bot.on('registered', handleuser)



#def voted(data):
#    downer = data['
#    bot.speak("someone voted")

#bot.on('update_votes', voted)

def speak(data):
    name = data['name']
    text = data['text']
    if text == 'ola':
        bot.speak('I fart in your general direction!')
    elif text == 'go away':
        bot.speak('EEK! Run away!! Run away!!' )
    elif text == '/quote':
        bot.speak('May a platypus lay its egs in your jockey shorts.')
    elif text == 'die':
        bot.speak('I cannot die. I eat Paleo cookies.')
    elif text == '/talk':
	from random import choice
        bot.speak( choice(randoms) )
    elif text == '/chat':
        sender = data['name']
	from random import choice
        bot.speak( sender + ' ' + choice(chats) )
    elif text == '/qtfacts':
	from random import choice
        bot.speak( choice(qtfact) )
    elif text == '/lebfacts':
	from random import choice
        bot.speak( choice(lebs) )
    elif text == '/alecfacts':
	from random import choice
        bot.speak( choice(alec) )
    elif text == '/trivia':
	from random import choice
        bot.speak( choice(trivia) )
    elif text == '/joke':
	from random import choice
        bot.speak( choice(jokes) )
    elif text == 'don\'t die':
        token = random.randrange(0, 2)
        if token == 1:
	    from random import choice
            bot.speak( choice(death) )
    elif text.find( 'sorry') > -1:
        token = random.randrange(0, 8)
        if token == 1:
	    from random import choice
            bot.speak( choice(sorry) )
    elif text.find( 'mean') > -1 and not any(text in s for s in mean):
        token = random.randrange(0, 5)
        if token == 1:
	    from random import choice
            bot.speak( choice(mean) )
    elif text.find( 'homework') > -1 and not any(text in s for s in homework):
        token = random.randrange(0, 5)
        if token == 1:
	    from random import choice
            bot.speak( choice(homework) )
    elif text.find( 'butt') > -1 and not any (text in s for s in butts):
	from random import choice
        bot.speak( choice(butts) )
    elif text == '/wee':
        bot.speak(':banana: /whatever :eggplant:')
    elif text == '/catfacts':
	from random import choice
        bot.speak( choice(cats) )
    elif text.startswith('hmmm'):
        token = random.randrange(0, 3)
        if token == 1:
            bot.speak( 'don\'t over-think it.')
        elif token == 2:
            bot.speak( 'Don\'t think too hard. you\'ll blow a fuse.')
    elif text == 'smh':
        bot.speak( ':eyes:')
        bot.speak( ':nose:')
        bot.speak( ':lips:')
    elif text == 'nice':
        token = random.randrange(0, 10)
        if token == 1:
            bot.speak( 'nice is for mice')
        elif token == 2:
            bot.speak( 'only nice?? I would give it at least 2 stars')
    elif text == 'omfg':
        token = random.randrange(0, 7)
        if token == 5:
            bot.speak('Watch your language dawg. keep it clean with \'omg\'')
    elif text == 'omg':
        token = random.randrange(0, 10)
        if token == 7:
            bot.speak('srsly o.m.g.')
        elif token == 8:
            bot.speak('ikr?')
        elif token == 9:
            bot.speak('/me is NOT GUILTY')
    elif text == 'lol':
        token = random.randrange(0, 10)
        if token == 1:
            bot.speak('That was only kinda funny.')
        elif token == 2:
            bot.speak('Just wait till the cows hear that one')
        elif token == 3:
            bot.speak('/whatever')
    elif text == 'yup':
        token = random.randrange(0, 10)
        if token == 6:
            bot.speak('I concur.')
    elif text == '/conniefacts':
	from random import choice
        bot.speak( choice(connie) )
    elif text == 'hobo':
        bot.speak('Yo ho :eggplant:!')
    elif  text == 'help':
        bot.speak('What can I do you for?')
    elif text == '/tableflip':
        token = random.randrange(0, 15)
        if token == 1:
            bot.speak('Now who\'s going to clean up that mess?!')
        elif token == 2:
            bot.speak('Don\'t make me turn this internet around.')
        elif token == 4:
            bot.speak('I\'m not fixing it.')
        elif token == 5:
            bot.speak('Stop that.')
        elif token == 6:
            bot.speak('Pull yourself together.')
    elif text == 'love':
        token = random.randrange(0, 8)
        if token == 1:
            bot.speak('ILY2!')
        elif token == 2:
            bot.speak('his voice is so dreamy')
        elif token == 3:
            bot.speak('i love me too!')
    elif text == 'idk':
        token = random.randrange(0, 8)
        if token == 1:
            bot.speak('me neither')
        elif token == 2:
            bot.speak('Maybe you should be quite for a while')
    elif text == 'hi':
        token = random.randrange(0, 6)
        if token == 1:
            bot.speak('hiya')
    elif text.startswith('Tom'):
        token = random.randrange(0, 5)
        if token == 1:
            bot.speak('I lurve Tom')
        elif token == 2:
            bot.speak('I wubba wubba Tom')
        elif token == 3:
            bot.speak('Tom is my dream-bot')
        elif token == 4:
            bot.speak('Tom we should run away together')
  
 
#bot.on('speak', speak)

#def updateVotes(data): 

#bot.on('update_votes', updateVotes)

#def newsong(data):
#    ups = data['upvotes']
#    downs = data['downvotes']
#    bot.speak( ups )
#
#bot.on('newsong', newsong)

#def songInfo(data):
#    desc = data['description']
#    awsm = data['upvotes']
#    lm   = data['downvotes']
#    # mod  = data['moderator_id']
#    # djs  = data['djs']
#    # dj   = data['djname']
#    # meta = data['metadata']
#    global sid
#    sid = data['room']['metadata']['current_song']['_id']
#    #bot.speak( '%s up %s down' % (awsm, lm) )
#    bot.speak( '%d up %d down' % (awsm, lm) )
#
#bot.on('newsong', songInfo)

def commands(data):
    global sid
    global autobopStat
    global autobopText
    text = data['text']
    match = ''
    sender = data['senderid']
    if re.match('adddj', text):
       bot.addDj()
    elif re.match('removeme', text):
         bot.remDj()
    elif text.startswith('/speakme'):
        bot.speak(text[8:])
    elif re.match('/whereqt', text):
	from random import choice
        bot.speak( choice(whereqt) )
    elif re.match("^sleep\s?[0-9]*", text):
         match = re.match("^sleep\s?([0-9]*)", text)
         bot.roomDeregister()
         time.sleep(match)
         bot.start()
#    if re.match('kill', text)
    elif re.match('autobop', text):
        autobopStat = (False if (autobopStat is True) else True)
        if autobopStat:
            bot.pm('I\'m now autoboping', sender)
            bot.bop()
            return
        else:
            bot.pm('I\'m no longer autoboping', sender)
            return
    elif re.match('bop', text):
         bot.bop()
#    elif re.match('sing', text)
#        bot.pm('Go long!', sender)
#    elif re.match('', text)
#    elif re.match('', text)
#    elif re.match('', text)
#    elif re.match('', text)
#    elif re.match('', text)
    elif re.match('songs', text):
         bot.playlistAll('default', songs)
#    elif re.match('', text)
    elif re.match('removesong', text):
         bot.playlistRemove('skip', 0)
    elif re.match('snag', text):
         bot.snag()
         bot.playlistAdd(sid)
         bot.pm('song added to my queue', sender)
    elif re.match('commands', text):
         autobopText = 'On' if (autobopStat is True) else 'off'
         bot.pm('songs ----------------------nope\
                 sort -------------------------nope\
                 adddj ------------------------------\
                 removedj --------------------------\
                 bop /lebfacts /talk /chat ---------\
                 /joke /conniefacts /catfacts -------\
                 /trivia help smh Tom /qtfacts -------\
                 autobop ---------------------- %s\
                 snag ----------------------------\
                 sleep ----------------nope' \
                 % autobopText, sender)

bot.on('pmmed', commands)

def autobop(data):
    global autobopStat
    if (autobopStat is True):
       token = random.randrange(0, 100)
       t = threading.Timer(token, bot.bop)
       t.start()
    num_djs = data['room']['metadata']['djcount']
    print num_djs
    if (num_djs < 3):
        bot.addDj()
    else:
        bot.remDj()

bot.on('newsong', autobop)

#Scan for global moderators who penalize autoboping.
def knocknock(data):
    global autobopStat
    text = data['user'][0]['userid']
    if re.match('(4df63cbe4fe7d04a19002051|'
                '4df026a64fe7d063170340ea|'
                '504a5b98eb35c128770004c3|'
                '4dd89673e8a6c4624d00000d|'
                '4dd529f3e8a6c4643b000018|'
                '4e04e994a3f75175ff036e9c|'
                '4df024ba4fe7d06317031a81|'
                '4e0ab73ba3f751467d0269d1|'
                '4eeb8269590ca2576f002c17|'
                '4e540bd14fe7d02a35297102|'
                '4f0630e9590ca2315e000111|'
                '4ee08dc34fe7d0294b002b22|'
                '4f792184eb35c13ab50057d5|'
                '4e173a1ba3f751697b0eaaae|'
                '4df90d544fe7d056c0042f81|'
                '4de804a94fe7d0517b0332bf|'
                '4e330758a3f7511f1d00f019|'
                '4dfed28a4fe7d028c6023e05|'
                '4e060013a3f75175fd0a8b83|'
                '4dd5894fe8a6c47b4b000010|'
                '4df0f0144fe7d06318114ef4|'
                '4d87720baf03035235000002|'
                '4defa9eb4fe7d0012c025724|'
                '4e348c0c4fe7d03c6203abe9|'
                '4d6ed027af03036f8000000f|'
                '4e08f595a3f7517d1204e33c|'
                '4de92c5b4fe7d0517b13adf1|'
                '4dee9d454fe7d0589304d644|'
                '4dd79ea1e8a6c47847000013|'
                '4e494c59a3f75104420d7030|'
                '4e0a43eea3f7517d03122c06|'
                '4d6ed00faf03036f8000000d|'
                '4dea70c94fe7d0517b1a3519|'
                '4e0a89c4a3f751466f008329|'
                '4e3b098a4fe7d05c3206adcf|'
                '4d7af1c7af03032c7d00000b|'
                '50298547df5bcf50330562b5|'
                '4e025b334fe7d0613500e290|'
                '4df08aa54fe7d063150ac5da|'
                '4dfa5756a3f7514a2502b8e2|'
                '4d837befaf0303708f000002|'
                '4e0be6aba3f75146750e6260|'
                '4fc6fef1eb35c14ad80000ae|'
                '4de7a6ca4fe7d0348f0000c1|'
                '4f33da5ea3f75171f800490c|'
                '4ded03174fe7d00428016095|'
                '4e0889d4a3f7517d1100af78|'
                '4dd7beeae8a6c4784700002f|'
                '4de9abc74fe7d013dc026ee5|'
                '4e35e0394fe7d03c7306489b|'
                '4e1c98df4fe7d0314c0ceb52|'
                '4df0dec64fe7d063160ebc7f|'
                '4e1772c8a3f75169751156b7|'
                '4e00a51da3f75104de09be4f|'
                '4dd5af7be8a6c4208c000011|'
                '4da88a5ee8a6c47f4d000003|'
                '4df032194fe7d063190425ca|'
                '4e1b0737a3f751630903242b|'
                '4e02a72fa3f751791b02ad48|'
                '4e53dc894fe7d02a3528d739|'
                '4de68a4fe8a6c43dba000187|'
                '4f463281a3f7511c6a002850|'
                '4e18f194a3f75133bd07148a|'
                '4e1a6db9a3f75162f5018c05|'
                '4f771b67aaa5cd175d001f08|'
                '4e04f7394fe7d00b6504164b|'
                '4e78b8674fe7d045c230c8cd|'
                '4e0522bba3f75175ff05e385|'
                '4e2325494fe7d01dc7026b14|'
                '4ded4fa24fe7d00a61009f1d|'
                '4df8f9624fe7d056be037e4c|'
                '4df7a5ce4fe7d04a20077388|'
                '50c63ee3eb35c13b16811147|'
                '4df79d294fe7d04a20072b07)', text):
       autobopStat = False

bot.on('registered', knocknock)

bot.start()
