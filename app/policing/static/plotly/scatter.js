// You can reproduce this figure in plotly.js with the following code!

// Learn more about plotly.js here: https://plot.ly/javascript/getting-started

/* Here's an example minimal HTML template
 *
 * <!DOCTYPE html>
 *   <head>
 *     <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
 *   </head>
 *   <body>
 *   <!-- Plotly chart will be drawn inside this div -->
 *   <div id="plotly-div"></div>
 *     <script>
 *     // JAVASCRIPT CODE GOES HERE
 *     </script>
 *   </body>
 * </html>
 */

var trace1 = {
  x: [0.141442155309, 0.113065326633, 0.0877016129032, 0.308805790109, 0.02224797219, 0.0756646216769, 0.0697674418605, 0.0770519262982, 0.0303448275862, 0.0636942675159, 0.119610570236, 0.0461095100865, 0.041404140414, 0.135478408129, 0.0888722927558, 0.0325960419092, 0.0455868089234, 0.0390193370166, 0.0560058953574, 0.0478048780488, 0.208083832335, 0.0412979351032, 0.0585106382979, 0.0414012738854, 0.036231884058, 0.0353800502168, 0.112033195021, 0.0673712021136, 0.0333333333333, 0.0591549295775, 0.125, 0.0, 0.0155440414508, 0.0787401574803, 0.0473933649289, 0.0, 0.0328638497653, 0.101147901668, 0.148102163888, 0.126842241347, 0.031525851198, 0.0713196033562, 0.0199320832718, 0.165799067709, 0.129018854205, 0.00176991150442, 0.109289859567, 0.158206356117, 0.099635701275, 0.0176470588235, 0.0718356069763, 0.0796749403763, 0.0891171902998, 0.0669145955006, 0.0423241136068, 0.137200827342, 0.200612557427, 0.117647058824, 0.146470918122, 0.130651662077, 0.0368029739777, 0.0578091640663, 0.0316690077896, 0.123350191193, 0.0381936643451, 0.0558890222756, 0.0634580012262, 0.0316458178111, 0.0744115413819, 0.0935503812075, 0.154639175258, 0.044, 0.0962809917355, 0.0403687665875, 0.0650953984287, 0.0589512876202, 0.107236842105, 0.00355450236967, 0.0623145400593, 0.0464015151515, 0.0913043478261, 0.0938219895288, 0.0135440180587, 0.142470490941, 0.0325984038956, 0.0494331908567, 0.109859446052, 0.0139322603891, 0.00216567406605, 0.0896084337349, 0.177805408766, 0.214285714286, 0.15873015873, 0.0430298719772, 0.119010474705, 0.0432801822323, 0.0680539592281, 0.037530622244, 0.00739957716702, 0.0591288648161, 0.0, 0.173382240228, 0.226636274829, 0.0882352941176, 0.158595340982, 0.0230769230769, 0.011673151751, 0.0, 0.142857142857, 0.0, 0.0734835355286, 0.0492610837438, 0.0418665503707, 0.215189873418, 0.0935251798561, 0.0139616055846, 0.0278481012658, 0.0992248062016, 0.0599467547967, 0.0120754716981, 0.132777777778, 0.240295748614, 0.6, 0.03125, 0.0734939759036, 0.0, 0.0909090909091, 0.0909090909091, 0.0, 0.0851063829787, 0.0314285714286, 0.0403225806452, 0.0226130653266, 0.0818181818182, 0.0909090909091, 0.0783761033393, 0.0719900057259, 0.0734528629265, 0.0372189907247, 0.0566870248037, 0.0965517241379, 0.0582215408202, 0.0529788838612, 0.0808823529412, 0.0229270772002, 0.0635054229628, 0.0766750979517, 0.0626597871055, 0.0361970941251, 0.0825231505785, 0.0880829015544, 0.0907639604882, 0.0664727980286, 0.0593319015706, 0.02298298573, 0.0822350554081, 0.0506402629408, 0.0621213625981, 0.0628231975725, 0.14032658518, 0.0678329789291, 0.132581100141, 0.0284508576096, 0.109375, 0.0589887640449, 0.0881924822331, 0.0494625119064, 0.0186084142395, 0.146935348447, 0.0425837320574, 0.0497108475962, 0.0213392200147, 0.097571633685, 0.0481085238794, 0.106104651163, 0.054347826087, 0.0461373390558, 0.076404372179, 0.0290633910945, 0.0528846153846, 0.0331345261763, 0.0335499471059, 0.0178790534619, 0.0363596777705, 0.08228980322, 0.037037037037, 0.0, 0.118942731278, 0.168358714044, 0.103658536585, 0.0540540540541, 0.0, 0.0434782608696, 0.0577239789196, 0.116822916667, 0.302469135802, 0.0891608391608, 0.0181818181818, 0.0561224489796, 0.0607814761216, 0.0571428571429, 0.0585106382979, 0.0846325167038, 0.0982116681325, 0.118406889128, 0.203703703704, 0.140776699029, 0.0, 0.0230769230769, 0.0, 0.0791788856305, 0.0785714285714, 0.365853658537, 0.0611741109311, 0.0774774774775, 0.104555638536, 0.0841818181818, 0.137142857143, 0.104635984673, 0.0699166132136, 0.141568734627, 0.0938477580813, 0.155485498108, 0.176851544337, 0.0792205041305, 0.0436874518861, 0.102129451129, 0.0816489893936, 0.179250720461, 0.0569306930693, 0.14613741545, 0.129095354523, 0.151295009476, 0.0875912408759, 0.0852797392721, 0.0970125281079, 0.0300489168414, 0.159488358149, 0.0466573816156, 0.0788013318535, 0.145921676228, 0.143790849673, 0.0929211015374, 0.12203934163, 0.0611398963731, 0.218763700132], 
  y: [0.0924369747899, 0.355555555556, 0.298850574713, 0.20703125, 0.34375, 0.387387387387, 0.666666666667, 0.130434782609, 0.113636363636, 0.45, 0.406976744186, 0.53125, 0.391304347826, 0.196875, 0.285714285714, 0.214285714286, 0.148936170213, 0.194690265487, 0.565789473684, 0.525510204082, 0.323741007194, 0.25, 0.545454545455, 0.25641025641, 0.0666666666667, 0.354838709677, 0.12962962963, 0.411764705882, 0.0, 0.261904761905, 0.0, 0.0, 0.666666666667, 0.522222222222, 0.5, 0.0, 0.514285714286, 0.227339981937, 0.336526946108, 0.212871287129, 0.235, 0.101604278075, 0.385185185185, 0.166174379171, 0.188405797101, 0.0, 0.198621807864, 0.285635663181, 0.219378427788, 0.0666666666667, 0.223557692308, 0.106430155211, 0.235924932976, 0.0471624266145, 0.200292397661, 0.230437903805, 0.213740458015, 0.166666666667, 0.150143579926, 0.270616982285, 0.0808080808081, 0.127840909091, 0.153225806452, 0.225, 0.141176470588, 0.24522673031, 0.167874396135, 0.00495662949195, 0.244897959184, 0.120044052863, 0.3, 0.261363636364, 0.105150214592, 0.16955017301, 0.241379310345, 0.178947368421, 0.171779141104, 0.666666666667, 0.285714285714, 0.183673469388, 0.199134199134, 0.220982142857, 0.166666666667, 0.0955145118734, 0.0580912863071, 0.124060150376, 0.276575729069, 0.396551724138, 0.5, 0.201680672269, 0.202797202797, 0.259259259259, 0.2125, 0.338842975207, 0.239700374532, 0.105263157895, 0.313777777778, 0.156657963446, 0.0714285714286, 0.103053435115, 0.0, 0.230817808652, 0.155172413793, 0.25, 0.167554024428, 0.0, 0.166666666667, 0.0, 0.0, 0.0, 0.160377358491, 0.24, 0.114583333333, 0.529411764706, 0.0641025641026, 0.375, 0.136363636364, 0.203125, 0.271056661562, 0.375, 0.192468619247, 0.2, 0.0, 0.0, 0.377049180328, 0.0, 0.0, 0.0, 0.0, 0.75, 0.272727272727, 0.15, 0.148148148148, 0.444444444444, 0.714285714286, 0.269754898072, 0.301518438178, 0.304461942257, 0.30464625132, 0.236587510994, 0.339285714286, 0.228110599078, 0.345195729537, 0.181818181818, 0.351624231782, 0.268571110369, 0.286869340233, 0.290801186944, 0.284467713787, 0.211450381679, 0.529411764706, 0.482594356907, 0.294588964265, 0.299462131124, 0.27263681592, 0.272851503189, 0.166345275551, 0.322941646683, 0.290476190476, 0.27934671657, 0.253348532345, 0.535615171138, 0.33971291866, 0.333333333333, 0.267573696145, 0.236893203883, 0.22833562586, 0.413043478261, 0.265714285714, 0.426966292135, 0.366627497062, 0.344827586207, 0.241842610365, 0.276162790698, 0.260273972603, 0.4, 0.418604651163, 0.246975088968, 0.305660377358, 0.333333333333, 0.311428571429, 0.336711711712, 0.473039215686, 0.191616766467, 0.336956521739, 1.0, 0.0, 0.296296296296, 0.256281407035, 0.411764705882, 0.0, 0.0, 0.0, 0.259629101284, 0.325011145787, 0.224489795918, 0.156862745098, 0.0, 0.0, 0.452380952381, 0.0, 0.181818181818, 0.421052631579, 0.189552238806, 0.3, 0.438016528926, 0.172413793103, 0.0, 0.0, 0.0, 0.0740740740741, 0.454545454545, 0.133333333333, 0.220050441362, 0.383720930233, 0.228571428571, 0.272138228942, 0.318181818182, 0.281690140845, 0.268974145121, 0.335907335907, 0.288888888889, 0.367396593674, 0.299530516432, 0.326203208556, 0.281938325991, 0.326968973747, 0.210784313725, 0.257234726688, 0.5, 0.213763702801, 0.0795454545455, 0.277661795407, 0.166666666667, 0.273885350318, 0.314569536424, 0.43023255814, 0.354636591479, 0.309452736318, 0.549295774648, 0.25641025641, 0.454545454545, 0.325454545455, 0.164473684211, 0.474576271186, 0.458917835671], 
  mode: "markers", 
  name: "Black Drivers", 
  text: ["Bridgeport Police Department", "New London Police Department", "Westport Police Department", "Waterbury Police Department", "Hartford Police Department", "Wethersfield Police Department", "Plainfield Police Department", "Danbury Police Department", "Hamden Police Department", "New Britain Police Department", "Meriden Police Department", "Trumbull Police Department", "Fairfield Police Department", "Norwalk Police Dept", "Stratford Police Department", "Greenwich Police Department", "West Haven Police Department", "Stamford Police Dept", "Manchester Police Department", "East Hartford Police Department", "Milford Police Department", "Bristol Police Department", "Darien Connecticut Police Dept", "Enfield Police Department", "Branford Police Department", "Bloomfield Police Department", "Wilton Police Department", "Vernon Police Department", "Sheldon Police Department", "Torrington Police Department", "Wolcott Police Department", "Easton Police Department", "Cromwell Police Department", "Wallingford Police Department", "New Milford Police Department", "Putnam Police Department", "Groton Police Department", "Chicago Police Department", "Peoria Il Police Department", "Waukegan Police Department", "Alton Police Department", "Elmwood Park Police Dept", "Alsip Police Department", "Springfield Police Department", "Rock Island Police Department", "Harwood Heights Police Department", "Evanston Police Department", "Bloomington Il Police Department", "Cicero Police Dept", "Crystal Lake Police", "Carol Stream Police Department", "Woodridge Police Department", "Elmhurst Police Department", "Evergreen Park Police Dept", "Blue Island Police Department", "Joliet Police Department", "Galesburg Police Department", "Marquette Heights Police Departmen", "Aurora Police Department", "Belleville Police Department", "Palatine Police Department", "Oak Lawn Police Department", "Schaumburg Police Department", "Elgin Police Department", "Arlington Heights Police", "Bolingbrook Police Department", "Skokie Police Dept", "Oak Park Police Dept", "Northbrook Police Department", "North Chicago Police Department", "Chillicothe Police Dept", "Carpentersville Police Department", "Addison Police Department", "Wheaton Police Dept", "Winifield Police Dept", "Lockport Police Department", "East Peoria Police Dept", "Riverwoods Police Dept", "Marengo Police Department", "Vernon Hills Police Dept", "Minooka Police Department", "Benkeley Police Department", "Palos Park Police Department", "Normal Police Department", "Westchester Police Department", "Glenwood Police Department", "Urbana Police Department", "Burr Ridge Police Department", "Troy Police Department", "Milan Il Police Department", "Peoria Heights Police Department", "Canton Police Department", "Mattoon Police Department", "Charleston Police Department", "Posen Police Department", "Round Lake Heights Police Dept", "Naperville Police Department", "Tinley Park Police Department", "Stone Park Police Department", "Mount Prospect Police Department", "New Boston Police Department", "Decatur Police Department", "Jacksonville Police Dept", "Eureka Police Department", "Rockford Police Department", "Richmond Police Dept", "Lake Forest Police Department", "Ludlow Police Department", "Grayville Police Department", "Elmwood Police Department", "Wheeling Police Department", "Lake Bluff Police Department", "Niles Police Dept", "Montgomery Police Department", "Morton Police Department", "Willmington Police Department", "Manteno Police Department", "Peotone Police Department", "Carbondale Police Department", "Momence Police Dept", "Murphysboro Police Department", "Mt Zion Police Department", "Bushnell Police Department", "Granville Police Dept", "Sparta Police Department", "Leland Police Dept", "Hillsdale Police Department", "Albers Police Dept", "Apple River Police Dept", "Casey Police Department", "Carterville Police Dept", "Kenilworth Police Dept", "East Dundee Police Dept", "Robinson Police Department", "Kure Beach Police Dept", "Charlotte-Mecklenburg Police Dept", "Jacksonville Police Department", "Holly Springs Police Department", "Concord Police Department", "Greenville Police Department", "Surf City Police Department", "Goldsboro Police Department", "Mint Hill Police Department", "Pilot Mountain Police Dept", "Winston-Salem Police Department", "Fayetteville Police Department", "Burlington Police Department", "Monroe Police Dept", "Salisbury Police Department", "Wilmington Police Dept", "Murphy Police Department", "Gastonia Police Department", "Greensboro Police Department", "High Point Police Dept", "Cary Police Department", "Durham Police Department", "Raleigh Police Dept", "Chapel Hill Police Department", "Wilson Police Department", "Asheville Police Department", "Rocky Mount Police Department", "Gaston County Police Dept", "Morrisville Police Department", "Ocean Isle Beach Police Dept", "Asheboro Police Department", "Wake Forest Police Department", "Huntersville Police Department", "Claremont Police Dept", "Hendersonville Police Department", "Conover Police Department", "Lumberton Police Department", "Troutman Police Department", "Shelby Police Department", "Hope Mills Police Department", "Jonesville Police Dept", "Biscoe Police Department", "Mount Holly Police Department", "Hickory Police Department", "Kings Mountain Police Department", "Lake Lure Police Department", "Pineville Police Department", "Kannapolis Police Department", "Tarboro Police Department", "Cornelius Police Department", "Kenly Police Department", "Edgar County Illinois Sheriff Dept", "Franklin County Sheriffs Office", "Dewitt County Sheriff", "Vermilion County Illinois Sheriffs", "Saline County Sheriffs Office", "Fulton County Sheriffs Office", "Kane County Sheriff Dept", "Lake County Sheriff", "Will County Sheriffs Office", "Champaign County Sheriffs Office", "Winnebago County Sheriffs Dept", "Ogle County Sheriffs Office", "Clay County Illinois", "Mclean County Sheriffs Office", "Whiteside County Sheriff", "Wayne County Sheriff Dept", "Ford County Sheriffs Office", "Perry County Sheriffs Office", "Kannakee County Sheriffs Office", "Piatt County Sheriffs Office", "Jo Daviess County Sheriffs Office", "Morgan Count Sheriffs Office", "Mchenry County Sheriffs Office", "Putnam County Sheriffs Office", "Wabath Co Sheriffs Office", "Lee County Sheriffs Dept", "Clark Co Il Sheriffs Office", "Hancock County Sheriffs Office", "Cumberland County Sheriffs Office", "Lenoir County Sheriffs Office", "Catawba County Sheriff Office", "Rowan Sheriff Office", "Brunswick County Sheriffs Office", "Durham County Sheriffs Office", "Guilford County Sheriffs Office", "Pitt County Sheriffs Office", "Henderson County Sheriffs Office", "Iredell County Sheriffs Office", "Davidson County Sheriffs Office", "New Hanover County Sheriff'S", "Cabarrus County Sheriffs Office", "Wake County Sheriff'S Office", "Orange County Sheriff'S Office", "Warren County Sheriff Office", "Stanly County Sheriffs Office", "Halifax County Sheriffs Office", "Pender County Sheriffs Office", "Beaufort County Sheriffs Office", "Carteret County Sheriff", "Moore County Sheriffs Office", "Randolph County Sheriffs Office", "Camden County Sheriffs Office", "Alamance County Sheriff'S Office", "Forsyth County Sheriffs Office", "Scotland County Sheriffs Office", "Currituck County Sheriffs Office", "Bertie County Sheriffs Office", "Chatham County Sheriffs Office", "Onslow County Sheriffs Office", "Washington County Sheriff Office", "Duplin County Sheriff Office"], 
  textsrc: "along528:23:78869a", 
  type: "scatter", 
  xsrc: "along528:23:e6625d", 
  ysrc: "along528:23:54a0f3"
};
var trace2 = {
  x: [0.0863179592888, 0.0854700854701, 0.0285950608531, 0.227620087336, 0.0130248237818, 0.057544547981, 0.0175644028103, 0.0636441647597, 0.0127189324437, 0.0411471321696, 0.0595630050883, 0.0314910025707, 0.0217578013169, 0.0586403736378, 0.0580193397799, 0.0157734887822, 0.034034034034, 0.022373540856, 0.0320040640081, 0.030989272944, 0.0863945578231, 0.0217587034814, 0.025931164545, 0.0269208549971, 0.0316205533597, 0.0116346713205, 0.081954744248, 0.0641583297086, 0.0329113924051, 0.0155390659101, 0.0493421052632, 0.0125, 0.00983248361253, 0.0524050004139, 0.0175607873408, 0.0061505065123, 0.0168054946661, 0.0168792893183, 0.0446986976676, 0.0458119471443, 0.0110553978131, 0.0458085528179, 0.0158331724271, 0.0562198258359, 0.0881200857756, 0.000998701687806, 0.0162062363239, 0.0508353343892, 0.0611025443331, 0.00684057656288, 0.0324228171074, 0.0275542691751, 0.0330874530109, 0.024910097908, 0.0231202251709, 0.0456271171028, 0.0955905611438, 0.0490762124711, 0.0509346222568, 0.0677157975967, 0.00928088994835, 0.029857756307, 0.0135178777393, 0.0372144556327, 0.0127742832657, 0.0264397543066, 0.020115232993, 0.0121706627769, 0.0256679312293, 0.0246104558031, 0.0793211584578, 0.0158107076655, 0.0343017647393, 0.0209584248637, 0.0348365035264, 0.0327684055042, 0.0288795097132, 0.00680272108844, 0.027225236086, 0.0267665255617, 0.0336592469316, 0.0355231143552, 0.0092676997873, 0.0500460249019, 0.0109633776534, 0.0345892526251, 0.0361460722921, 0.00520473305412, 0.00206676025581, 0.0591358024691, 0.068457019542, 0.0850759606792, 0.0479582750286, 0.0247431112929, 0.0656697009103, 0.0258302583026, 0.0319583719558, 0.0150958183277, 0.00287150035894, 0.0212708467809, 0.0133928571429, 0.0651345209296, 0.138083097912, 0.0387382401771, 0.0709166838523, 0.0164271047228, 0.000992685475444, 0.0, 0.0141093474427, 0.0110024449878, 0.0279671570593, 0.012402653591, 0.0295966474594, 0.1197057069, 0.0362012223789, 0.00775623268698, 0.0129616884607, 0.0415735914619, 0.0155997056659, 0.0159857904085, 0.0629560738303, 0.0985039502437, 0.522052205221, 0.0, 0.027150084317, 0.00406504065041, 0.0, 0.0096256684492, 0.0, 0.0311688311688, 0.0125063808065, 0.0140299951621, 0.00948076287069, 0.115436543654, 0.117428924598, 0.0383935333709, 0.0273149859267, 0.0410088372555, 0.0296067547494, 0.0322296865003, 0.078106624853, 0.0333453534989, 0.0484789008832, 0.066725585506, 0.0178971395353, 0.0330948566652, 0.0545679786265, 0.0308797959893, 0.0172536323437, 0.0352827308938, 0.0419551370811, 0.0601824602707, 0.0324202220737, 0.0373353979636, 0.0167090510786, 0.037295546855, 0.0293351039885, 0.0301348556885, 0.0426631288622, 0.0650540210856, 0.0441868095811, 0.117501456028, 0.0161144977472, 0.0684371807967, 0.0367536548709, 0.0518580649867, 0.0294299238526, 0.0267661610836, 0.0846445709184, 0.0248031496063, 0.0491665589869, 0.0194558944765, 0.0523748159057, 0.0364550898204, 0.0862591338442, 0.0434782608696, 0.0307486631016, 0.0379463210138, 0.0253554287784, 0.0542865069823, 0.0259439610441, 0.022468665923, 0.0208264680683, 0.0210113766262, 0.0661274976213, 0.0168279343711, 0.0458937198068, 0.0618124672603, 0.0692048286985, 0.0601819454164, 0.00221116639027, 0.0367647058824, 0.0173775671406, 0.0168771192292, 0.0272242153818, 0.0863095238095, 0.0372278544125, 0.0204788001154, 0.020156774916, 0.0209661187521, 0.0387748452265, 0.0273368606702, 0.055626481853, 0.0378966251822, 0.0425716768028, 0.0317238412733, 0.0693319838057, 0.0245775729647, 0.0295151089248, 0.0147441457069, 0.0247694334651, 0.0757483200977, 0.388321763985, 0.0612969989652, 0.080793242747, 0.0756636310792, 0.0697553657974, 0.096282754418, 0.0728234167465, 0.0708522624023, 0.103917821309, 0.0608786144354, 0.141339396445, 0.114394099052, 0.0458941690691, 0.0446573323508, 0.0696002664125, 0.0433193342666, 0.187883435583, 0.0405750798722, 0.125920964501, 0.103706222373, 0.139306736429, 0.0747271200672, 0.0677903994137, 0.093758987633, 0.0204978038067, 0.122716817751, 0.038098961242, 0.0569823434992, 0.0782057068352, 0.145161290323, 0.0574316290131, 0.079749297601, 0.0381194409149, 0.173589229447], 
  y: [0.107462686567, 0.346666666667, 0.413223140496, 0.187050359712, 0.364705882353, 0.40625, 0.266666666667, 0.0629213483146, 0.16393442623, 0.530303030303, 0.326633165829, 0.397959183673, 0.539473684211, 0.241150442478, 0.224137931034, 0.155279503106, 0.107843137255, 0.214046822742, 0.619047619048, 0.509615384615, 0.422572178478, 0.406896551724, 0.4, 0.296137339056, 0.153571428571, 0.525, 0.0556844547564, 0.508474576271, 0.192307692308, 0.522471910112, 0.0222222222222, 0.0, 0.703703703704, 0.516587677725, 0.549450549451, 0.588235294118, 0.55652173913, 0.276961218346, 0.398353909465, 0.214541120381, 0.207650273224, 0.0850077279753, 0.536585365854, 0.199839486356, 0.174561972745, 0.3, 0.212376933896, 0.290452261307, 0.391167192429, 0.281746031746, 0.236620666442, 0.170168067227, 0.259378349411, 0.169652265543, 0.269565217391, 0.248629795715, 0.218398411648, 0.2, 0.178772205982, 0.322344322344, 0.143835616438, 0.231460674157, 0.195676905575, 0.242556917688, 0.20253164557, 0.275982532751, 0.202680067002, 0.00749063670412, 0.342767295597, 0.094674556213, 0.474418604651, 0.455172413793, 0.136476426799, 0.235248447205, 0.263803680982, 0.272835112693, 0.191191191191, 0.302325581395, 0.243542435424, 0.347931873479, 0.244746600742, 0.260273972603, 0.327868852459, 0.101968376896, 0.0780141843972, 0.25, 0.384219554031, 0.6640625, 0.415094339623, 0.206680584551, 0.262697022767, 0.278361344538, 0.259946949602, 0.386363636364, 0.316831683168, 0.225563909774, 0.370797626895, 0.327564894932, 0.0, 0.122794636556, 0.666666666667, 0.283061339336, 0.199600798403, 0.242857142857, 0.19483824064, 0.303571428571, 0.105263157895, 0.0, 0.125, 0.777777777778, 0.178113207547, 0.302325581395, 0.117572692794, 0.43023255814, 0.236363636364, 0.4375, 0.194690265487, 0.310447761194, 0.313679245283, 0.285714285714, 0.284090909091, 0.225255972696, 0.0224137931034, 0.0, 0.434782608696, 0.333333333333, 0.0, 0.444444444444, 0.0, 0.388888888889, 0.244897959184, 0.379310344828, 0.255813953488, 0.335282651072, 0.326315789474, 0.237909769555, 0.294301327088, 0.333333333333, 0.24346448376, 0.227667493797, 0.400250941029, 0.188295165394, 0.338731443995, 0.264900662252, 0.282541198949, 0.238875526158, 0.230853391685, 0.286036036036, 0.263157894737, 0.196243933319, 0.448844884488, 0.517726161369, 0.298454367026, 0.271395655036, 0.231282952548, 0.200392445426, 0.121844548454, 0.24633431085, 0.315057283142, 0.294491880127, 0.247524752475, 0.492734031767, 0.430921052632, 0.313432835821, 0.283767038414, 0.251758087201, 0.205486820871, 0.366666666667, 0.239288068556, 0.404761904762, 0.266754270696, 0.398305084746, 0.24165202109, 0.258869908016, 0.303719008264, 0.454545454545, 0.379446640316, 0.251428571429, 0.275, 0.318568994889, 0.267692307692, 0.344626168224, 0.48417721519, 0.200777202073, 0.374100719424, 0.475, 0.578947368421, 0.343220338983, 0.322033898305, 0.412790697674, 0.375, 0.4, 0.181818181818, 0.269090909091, 0.345514950166, 0.384236453202, 0.220982142857, 0.352112676056, 0.166666666667, 0.338666666667, 0.126050420168, 0.524193548387, 0.495081967213, 0.247041420118, 0.394557823129, 0.481355932203, 0.321167883212, 0.25, 0.785714285714, 0.294117647059, 0.241134751773, 0.366935483871, 0.0515247108307, 0.214969048959, 0.440909090909, 0.239436619718, 0.287841191067, 0.320411392405, 0.293310463122, 0.244421646576, 0.335632183908, 0.23137973138, 0.29687042995, 0.27781871776, 0.369807497467, 0.293729372937, 0.290876093054, 0.224416517056, 0.10612244898, 0.425196850394, 0.189716312057, 0.0819672131148, 0.271126760563, 0.38202247191, 0.224324324324, 0.204498977505, 0.396825396825, 0.295112091143, 0.301377895045, 0.521126760563, 0.324783584482, 0.333333333333, 0.386128364389, 0.176151761518, 0.4, 0.372937293729], 
  mode: "markers", 
  name: "White Drivers", 
  text: ["Bridgeport Police Department", "New London Police Department", "Westport Police Department", "Waterbury Police Department", "Hartford Police Department", "Wethersfield Police Department", "Plainfield Police Department", "Danbury Police Department", "Hamden Police Department", "New Britain Police Department", "Meriden Police Department", "Trumbull Police Department", "Fairfield Police Department", "Norwalk Police Dept", "Stratford Police Department", "Greenwich Police Department", "West Haven Police Department", "Stamford Police Dept", "Manchester Police Department", "East Hartford Police Department", "Milford Police Department", "Bristol Police Department", "Darien Connecticut Police Dept", "Enfield Police Department", "Branford Police Department", "Bloomfield Police Department", "Wilton Police Department", "Vernon Police Department", "Sheldon Police Department", "Torrington Police Department", "Wolcott Police Department", "Easton Police Department", "Cromwell Police Department", "Wallingford Police Department", "New Milford Police Department", "Putnam Police Department", "Groton Police Department", "Chicago Police Department", "Peoria Il Police Department", "Waukegan Police Department", "Alton Police Department", "Elmwood Park Police Dept", "Alsip Police Department", "Springfield Police Department", "Rock Island Police Department", "Harwood Heights Police Department", "Evanston Police Department", "Bloomington Il Police Department", "Cicero Police Dept", "Crystal Lake Police", "Carol Stream Police Department", "Woodridge Police Department", "Elmhurst Police Department", "Evergreen Park Police Dept", "Blue Island Police Department", "Joliet Police Department", "Galesburg Police Department", "Marquette Heights Police Departmen", "Aurora Police Department", "Belleville Police Department", "Palatine Police Department", "Oak Lawn Police Department", "Schaumburg Police Department", "Elgin Police Department", "Arlington Heights Police", "Bolingbrook Police Department", "Skokie Police Dept", "Oak Park Police Dept", "Northbrook Police Department", "North Chicago Police Department", "Chillicothe Police Dept", "Carpentersville Police Department", "Addison Police Department", "Wheaton Police Dept", "Winifield Police Dept", "Lockport Police Department", "East Peoria Police Dept", "Riverwoods Police Dept", "Marengo Police Department", "Vernon Hills Police Dept", "Minooka Police Department", "Benkeley Police Department", "Palos Park Police Department", "Normal Police Department", "Westchester Police Department", "Glenwood Police Department", "Urbana Police Department", "Burr Ridge Police Department", "Troy Police Department", "Milan Il Police Department", "Peoria Heights Police Department", "Canton Police Department", "Mattoon Police Department", "Charleston Police Department", "Posen Police Department", "Round Lake Heights Police Dept", "Naperville Police Department", "Tinley Park Police Department", "Stone Park Police Department", "Mount Prospect Police Department", "New Boston Police Department", "Decatur Police Department", "Jacksonville Police Dept", "Eureka Police Department", "Rockford Police Department", "Richmond Police Dept", "Lake Forest Police Department", "Ludlow Police Department", "Grayville Police Department", "Elmwood Police Department", "Wheeling Police Department", "Lake Bluff Police Department", "Niles Police Dept", "Montgomery Police Department", "Morton Police Department", "Willmington Police Department", "Manteno Police Department", "Peotone Police Department", "Carbondale Police Department", "Momence Police Dept", "Murphysboro Police Department", "Mt Zion Police Department", "Bushnell Police Department", "Granville Police Dept", "Sparta Police Department", "Leland Police Dept", "Hillsdale Police Department", "Albers Police Dept", "Apple River Police Dept", "Casey Police Department", "Carterville Police Dept", "Kenilworth Police Dept", "East Dundee Police Dept", "Robinson Police Department", "Kure Beach Police Dept", "Charlotte-Mecklenburg Police Dept", "Jacksonville Police Department", "Holly Springs Police Department", "Concord Police Department", "Greenville Police Department", "Surf City Police Department", "Goldsboro Police Department", "Mint Hill Police Department", "Pilot Mountain Police Dept", "Winston-Salem Police Department", "Fayetteville Police Department", "Burlington Police Department", "Monroe Police Dept", "Salisbury Police Department", "Wilmington Police Dept", "Murphy Police Department", "Gastonia Police Department", "Greensboro Police Department", "High Point Police Dept", "Cary Police Department", "Durham Police Department", "Raleigh Police Dept", "Chapel Hill Police Department", "Wilson Police Department", "Asheville Police Department", "Rocky Mount Police Department", "Gaston County Police Dept", "Morrisville Police Department", "Ocean Isle Beach Police Dept", "Asheboro Police Department", "Wake Forest Police Department", "Huntersville Police Department", "Claremont Police Dept", "Hendersonville Police Department", "Conover Police Department", "Lumberton Police Department", "Troutman Police Department", "Shelby Police Department", "Hope Mills Police Department", "Jonesville Police Dept", "Biscoe Police Department", "Mount Holly Police Department", "Hickory Police Department", "Kings Mountain Police Department", "Lake Lure Police Department", "Pineville Police Department", "Kannapolis Police Department", "Tarboro Police Department", "Cornelius Police Department", "Kenly Police Department", "Edgar County Illinois Sheriff Dept", "Franklin County Sheriffs Office", "Dewitt County Sheriff", "Vermilion County Illinois Sheriffs", "Saline County Sheriffs Office", "Fulton County Sheriffs Office", "Kane County Sheriff Dept", "Lake County Sheriff", "Will County Sheriffs Office", "Champaign County Sheriffs Office", "Winnebago County Sheriffs Dept", "Ogle County Sheriffs Office", "Clay County Illinois", "Mclean County Sheriffs Office", "Whiteside County Sheriff", "Wayne County Sheriff Dept", "Ford County Sheriffs Office", "Perry County Sheriffs Office", "Kannakee County Sheriffs Office", "Piatt County Sheriffs Office", "Jo Daviess County Sheriffs Office", "Morgan Count Sheriffs Office", "Mchenry County Sheriffs Office", "Putnam County Sheriffs Office", "Wabath Co Sheriffs Office", "Lee County Sheriffs Dept", "Clark Co Il Sheriffs Office", "Hancock County Sheriffs Office", "Cumberland County Sheriffs Office", "Lenoir County Sheriffs Office", "Catawba County Sheriff Office", "Rowan Sheriff Office", "Brunswick County Sheriffs Office", "Durham County Sheriffs Office", "Guilford County Sheriffs Office", "Pitt County Sheriffs Office", "Henderson County Sheriffs Office", "Iredell County Sheriffs Office", "Davidson County Sheriffs Office", "New Hanover County Sheriff'S", "Cabarrus County Sheriffs Office", "Wake County Sheriff'S Office", "Orange County Sheriff'S Office", "Warren County Sheriff Office", "Stanly County Sheriffs Office", "Halifax County Sheriffs Office", "Pender County Sheriffs Office", "Beaufort County Sheriffs Office", "Carteret County Sheriff", "Moore County Sheriffs Office", "Randolph County Sheriffs Office", "Camden County Sheriffs Office", "Alamance County Sheriff'S Office", "Forsyth County Sheriffs Office", "Scotland County Sheriffs Office", "Currituck County Sheriffs Office", "Bertie County Sheriffs Office", "Chatham County Sheriffs Office", "Onslow County Sheriffs Office", "Washington County Sheriff Office", "Duplin County Sheriff Office"], 
  textsrc: "along528:23:78869a", 
  type: "scatter", 
  xsrc: "along528:23:5b11d8", 
  ysrc: "along528:23:2832e9"
};
var data = [trace1, trace2];
var layout = {hovermode: "closest"};
Plotly.plot('scatter', data, layout);