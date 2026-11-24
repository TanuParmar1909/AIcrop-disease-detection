"""
Disease metadata, agricultural advisory, and styling data for Crop Disease Detection.
Supports 38 classes from the PlantVillage dataset.
"""

CLASS_NAMES = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry_(including_sour)___Powdery_mildew',
    'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Strawberry___healthy',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

DISEASE_DETAILS = {
    'Apple___Apple_scab': {
        'crop': 'Apple',
        'disease': 'Apple Scab',
        'status': 'Diseased',
        'severity': 'Moderate to High',
        'cause': 'Fungus (Venturia inaequalis)',
        'symptoms': 'Olive-green to black velvety spots on leaves, yellowing, premature leaf drop, scabby lesions on fruit.',
        'treatment': 'Apply protective copper-based or sulfur fungicides early in the season. Use systemic fungicides such as myclobutanil if infection is established.',
        'prevention': 'Rake and destroy fallen leaves in autumn, prune canopy to maximize sunlight and airflow, choose scab-resistant apple cultivars.'
    },
    'Apple___Black_rot': {
        'crop': 'Apple',
        'disease': 'Black Rot',
        'status': 'Diseased',
        'severity': 'High',
        'cause': 'Fungus (Botryosphaeria obtusa)',
        'symptoms': 'Frogeye leaf spots (purple margins with tan centers), black sunken rot on fruit, cankers on limbs and twigs.',
        'treatment': 'Prune out dead wood and infected twigs during dormancy. Apply captan or sulfur-based fungicides during petal fall.',
        'prevention': 'Maintain orchard sanitation, remove mummified apples, avoid mechanical wounding during harvest.'
    },
    'Apple___Cedar_apple_rust': {
        'crop': 'Apple',
        'disease': 'Cedar Apple Rust',
        'status': 'Diseased',
        'severity': 'Moderate',
        'cause': 'Fungus (Gymnosporangium juniperi-virginianae)',
        'symptoms': 'Bright yellow-orange circular leaf spots that develop tube-like structures on the underside; fruit distortion.',
        'treatment': 'Apply preventative fungicides (mancozeb or myclobutanil) beginning at tight cluster through petal fall.',
        'prevention': 'Remove nearby Eastern red cedar/juniper hosts within 1-2 miles if possible; plant resistant varieties.'
    },
    'Apple___healthy': {
        'crop': 'Apple',
        'disease': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'cause': 'N/A',
        'symptoms': 'Uniform green foliage without discoloration, lesions, or curling.',
        'treatment': 'No treatment needed. Continue balanced fertilization and regular irrigation.',
        'prevention': 'Inspect orchards weekly, maintain balanced nutrition, and ensure adequate drainage.'
    },
    'Blueberry___healthy': {
        'crop': 'Blueberry',
        'disease': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'cause': 'N/A',
        'symptoms': 'Vibrant, waxy green leaves free of spots, necrosis, or chlorosis.',
        'treatment': 'No treatment needed. Maintain optimal soil pH between 4.5 and 5.2.',
        'prevention': 'Provide organic mulch (pine bark) to retain moisture and suppress weed competition.'
    },
    'Cherry_(including_sour)___Powdery_mildew': {
        'crop': 'Cherry',
        'disease': 'Powdery Mildew',
        'status': 'Diseased',
        'severity': 'Moderate',
        'cause': 'Fungus (Podosphaera clandestina)',
        'symptoms': 'White powdery fungal patches on new leaf growth, leaf curling, distorted shoot growth, fruit blemishes.',
        'treatment': 'Apply potassium bicarbonate, neem oil, or horticultural sulfur spray at first signs of mildew.',
        'prevention': 'Prune trees to open the canopy for airflow; avoid overhead irrigation; apply dormant oil before bud break.'
    },
    'Cherry_(including_sour)___healthy': {
        'crop': 'Cherry',
        'disease': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'cause': 'N/A',
        'symptoms': 'Firm, glossy green foliage showing robust shoot elongation.',
        'treatment': 'No action required. Follow standard seasonal fertilizer and irrigation schedules.',
        'prevention': 'Regular canopy scouting and sanitary pruning of crossing branches.'
    },
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': {
        'crop': 'Corn (Maize)',
        'disease': 'Gray Leaf Spot (Cercospora)',
        'status': 'Diseased',
        'severity': 'High',
        'cause': 'Fungus (Cercospora zeae-maydis)',
        'symptoms': 'Narrow, rectangular grayish-brown lesions restricted between leaf veins; blight spreads upwards on the plant.',
        'treatment': 'Apply strobilurin or triazole fungicides at tassel emergence (VT to R1 stage) if disease pressure is high.',
        'prevention': 'Practice crop rotation with non-host crops (soybeans), till crop residue under, and select tolerant corn hybrids.'
    },
    'Corn_(maize)___Common_rust_': {
        'crop': 'Corn (Maize)',
        'disease': 'Common Rust',
        'status': 'Diseased',
        'severity': 'Moderate',
        'cause': 'Fungus (Puccinia sorghi)',
        'symptoms': 'Small, powdery cinnamon-brown to red pustules on both upper and lower leaf surfaces.',
        'treatment': 'Fungicide applications (such as azoxystrobin or pyraclostrobin) if lesions appear before silking on susceptible hybrids.',
        'prevention': 'Plant rust-resistant hybrids; avoid late planting dates which expose crops to peak spore migration.'
    },
    'Corn_(maize)___Northern_Leaf_Blight': {
        'crop': 'Corn (Maize)',
        'disease': 'Northern Leaf Blight',
        'status': 'Diseased',
        'severity': 'High',
        'cause': 'Fungus (Exserohilum turcicum)',
        'symptoms': 'Large, cigar-shaped elongated grayish-green to tan lesions that can measure 1 to 6 inches long.',
        'treatment': 'Foliar fungicides applied between silking and 2 weeks post-silking if lesions are present on lower ear leaves.',
        'prevention': 'Plant resistant hybrids containing Ht genes, perform 1-2 year crop rotation, and manage harvest residues.'
    },
    'Corn_(maize)___healthy': {
        'crop': 'Corn (Maize)',
        'disease': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'cause': 'N/A',
        'symptoms': 'Broad, deep green leaves with crisp edges and no necrotic or chlorotic spotting.',
        'treatment': 'No treatment needed. Monitor nitrogen levels and maintain timely irrigation during pollination.',
        'prevention': 'Soil testing and balanced side-dressing of nitrogen at V6 stage.'
    },
    'Grape___Black_rot': {
        'crop': 'Grape',
        'disease': 'Black Rot',
        'status': 'Diseased',
        'severity': 'High',
        'cause': 'Fungus (Guignardia bidwellii)',
        'symptoms': 'Small reddish-brown circular spots on leaves with tiny black pycnidia; shriveled, black mummified berries.',
        'treatment': 'Apply myclobutanil, captan, or mancozeb sprays from bud break until 4-6 weeks after bloom.',
        'prevention': 'Sanitation: remove all mummified berries from vines and ground during winter pruning. Keep canopy open.'
    },
    'Grape___Esca_(Black_Measles)': {
        'crop': 'Grape',
        'disease': 'Esca (Black Measles)',
        'status': 'Diseased',
        'severity': 'High to Severe',
        'cause': 'Fungal complex (Phaeomoniella, Phaeoacremonium)',
        'symptoms': '"Tiger-stripe" interveinal leaf chlorosis and necrosis; dark spots and cracking on berries; internal trunk rot.',
        'treatment': 'No chemical cure available. Prune out symptomatic canes back to healthy white wood; apply wound sealants.',
        'prevention': 'Sanitize pruning shears between vines; avoid pruning wounds during wet weather.'
    },
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': {
        'crop': 'Grape',
        'disease': 'Leaf Blight (Isariopsis)',
        'status': 'Diseased',
        'severity': 'Moderate',
        'cause': 'Fungus (Pseudocercospora cladosporioides)',
        'symptoms': 'Irregular brown spots with faint yellow halos, coalescing to cause leaf scorch and early defoliation.',
        'treatment': 'Spray copper fungicides or broad-spectrum protectant fungicides after harvest or at initial symptom sighting.',
        'prevention': 'Ensure good vine aeration, prune suckers, and rake fallen leaves post-harvest.'
    },
    'Grape___healthy': {
        'crop': 'Grape',
        'disease': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'cause': 'N/A',
        'symptoms': 'Broad, vibrant green leaves with well-defined lobes and clear veins.',
        'treatment': 'No treatment needed. Maintain canopy management and trellis training.',
        'prevention': 'Regular scouting for mildew and berry moth activity.'
    },
    'Orange___Haunglongbing_(Citrus_greening)': {
        'crop': 'Orange / Citrus',
        'disease': 'Huanglongbing (Citrus Greening)',
        'status': 'Diseased',
        'severity': 'Critical',
        'cause': 'Bacterium (Candidatus Liberibacter asiaticus) vectored by Asian Citrus Psyllid',
        'symptoms': 'Asymmetric blotchy mottle on leaves, yellow shoots, small lopsided bitter fruits that remain green at bottom.',
        'treatment': 'No cure exists. Manage psyllid vector populations with systemic insecticides (imidacloprid) and foliar micronutrients.',
        'prevention': 'Plant certified disease-free nursery stock; install psyllid traps; immediately remove infected trees.'
    },
    'Peach___Bacterial_spot': {
        'crop': 'Peach',
        'disease': 'Bacterial Spot',
        'status': 'Diseased',
        'severity': 'Moderate to High',
        'cause': 'Bacterium (Xanthomonas arboricola pv. pruni)',
        'symptoms': 'Water-soaked angular purple-brown spots on leaves leading to shot-hole appearance; cracked fruit lesions.',
        'treatment': 'Apply copper sprays during dormancy and oxytetracycline / kasugamycin during the growing season.',
        'prevention': 'Choose resistant cultivars, plant windbreaks to prevent sandblasting wounds, avoid excessive nitrogen.'
    },
    'Peach___healthy': {
        'crop': 'Peach',
        'disease': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'cause': 'N/A',
        'symptoms': 'Long, slender, vibrant green leaves free of blemishes or curling.',
        'treatment': 'No treatment needed. Maintain consistent watering and thinning of fruit set.',
        'prevention': 'Apply dormant copper spray in late winter to prevent leaf curl and bacterial cankers.'
    },
    'Pepper,_bell___Bacterial_spot': {
        'crop': 'Bell Pepper',
        'disease': 'Bacterial Spot',
        'status': 'Diseased',
        'severity': 'High',
        'cause': 'Bacterium (Xanthomonas campestris pv. vesicatoria)',
        'symptoms': 'Small water-soaked circular to irregular dark brown lesions with yellow halos on foliage; scabby blisters on peppers.',
        'treatment': 'Spray fixed copper combined with mancozeb, or use bio-bactericides like Bacillus subtilis.',
        'prevention': 'Use certified disease-free seed, avoid overhead sprinkler irrigation, practice 2-3 year crop rotation.'
    },
    'Pepper,_bell___healthy': {
        'crop': 'Bell Pepper',
        'disease': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'cause': 'N/A',
        'symptoms': 'Broad, deep emerald leaves without holes, chlorosis, or curling.',
        'treatment': 'No treatment needed. Maintain drip irrigation and support plants with stakes or cages.',
        'prevention': 'Mulch base of plants to prevent soil splash onto lower foliage.'
    },
    'Potato___Early_blight': {
        'crop': 'Potato',
        'disease': 'Early Blight',
        'status': 'Diseased',
        'severity': 'Moderate to High',
        'cause': 'Fungus (Alternaria solani)',
        'symptoms': 'Target-board or concentric ring brown-black spots on older leaves, surrounded by chlorotic yellow zone.',
        'treatment': 'Apply chlorothalonil, mancozeb, or azoxystrobin at early symptom onset, especially after rain events.',
        'prevention': 'Rotate away from solanaceous crops for 3 years; maintain optimum plant fertility; avoid overhead watering.'
    },
    'Potato___Late_blight': {
        'crop': 'Potato',
        'disease': 'Late Blight',
        'status': 'Diseased',
        'severity': 'Critical',
        'cause': 'Oomycete (Phytophthora infestans)',
        'symptoms': 'Large dark brown/black water-soaked lesions on leaves and stems; white fuzzy fungal growth on underside in humid air.',
        'treatment': 'Immediate spray with translaminar/systemic oomycide (mefenoxam, cymoxanil, mandipropamid). Destroy infected foliage.',
        'prevention': 'Use certified seed tubers, eliminate volunteer potatoes, monitor late blight forecasts, bury cull piles.'
    },
    'Potato___healthy': {
        'crop': 'Potato',
        'disease': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'cause': 'N/A',
        'symptoms': 'Lush green compound foliage with sturdy stems and no lesions or wilting.',
        'treatment': 'No action required. Hill soil properly around stems to protect developing tubers.',
        'prevention': 'Maintain steady moisture without waterlogging; practice regular field scouting.'
    },
    'Raspberry___healthy': {
        'crop': 'Raspberry',
        'disease': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'cause': 'N/A',
        'symptoms': 'Serrated green compound leaflets with uniform green coloration and healthy cane development.',
        'treatment': 'No treatment needed. Support canes on trellises and prune old floricanes after fruiting.',
        'prevention': 'Maintain weed-free beds with organic woodchip mulching.'
    },
    'Soybean___healthy': {
        'crop': 'Soybean',
        'disease': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'cause': 'N/A',
        'symptoms': 'Trifoliate leaves with vibrant green surface, clean margins, and active nodulation.',
        'treatment': 'No treatment required. Ensure adequate phosphorus and potassium nutrition.',
        'prevention': 'Regular scouting during flowering (R1-R3 stages) for insect pests and fungal diseases.'
    },
    'Squash___Powdery_mildew': {
        'crop': 'Squash',
        'disease': 'Powdery Mildew',
        'status': 'Diseased',
        'severity': 'Moderate',
        'cause': 'Fungus (Podosphaera xanthii)',
        'symptoms': 'Talcum powder-like white fungal coating on leaves and stems; leaves turn yellow, crisp, and die back.',
        'treatment': 'Spray with potassium bicarbonate, sulfur, neem oil, or bio-fungicide (Bacillus amyloliquefaciens).',
        'prevention': 'Space plants adequately for ventilation; water at base with drip lines; choose powdery mildew tolerant varieties.'
    },
    'Strawberry___Leaf_scorch': {
        'crop': 'Strawberry',
        'disease': 'Leaf Scorch',
        'status': 'Diseased',
        'severity': 'Moderate',
        'cause': 'Fungus (Diplocarpon earlianum)',
        'symptoms': 'Numerous small, irregular purplish spots on upper leaf surfaces that enlarge and cause leaves to look scorched.',
        'treatment': 'Apply captan, thiram, or copper-based fungicides during crown development and post-renovation.',
        'prevention': 'Renovate strawberry beds after harvest, remove dead foliage, avoid overhead sprinklers.'
    },
    'Strawberry___healthy': {
        'crop': 'Strawberry',
        'disease': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'cause': 'N/A',
        'symptoms': 'Deep green, glossy trifoliate leaves with healthy runner development and white flower blooms.',
        'treatment': 'No treatment needed. Maintain strawberry beds clean and well mulched with straw.',
        'prevention': 'Use straw mulch to prevent soil splashing and keep fruit clean.'
    },
    'Tomato___Bacterial_spot': {
        'crop': 'Tomato',
        'disease': 'Bacterial Spot',
        'status': 'Diseased',
        'severity': 'High',
        'cause': 'Bacterium (Xanthomonas perforans / euvesicatoria)',
        'symptoms': 'Small, angular, greasy dark brown to black spots with yellow halo; ragged holes in leaves; fruit scab.',
        'treatment': 'Copper hydroxide spray mixed with mancozeb or actigard; biological bactericide sprays.',
        'prevention': 'Use certified pathogen-free seeds, avoid working in wet foliage, sanitize stakes and trellising cages.'
    },
    'Tomato___Early_blight': {
        'crop': 'Tomato',
        'disease': 'Early Blight',
        'status': 'Diseased',
        'severity': 'High',
        'cause': 'Fungus (Alternaria solani)',
        'symptoms': 'Dark concentric target-like rings on lower leaves, surrounded by yellow tissue; bottom-up defoliation.',
        'treatment': 'Prune lower diseased foliage. Apply chlorothalonil, copper fungicide, or Bacillus-based biologicals weekly.',
        'prevention': 'Mulch soil surface, water strictly at base with drip irrigation, practice 3-year crop rotation.'
    },
    'Tomato___Late_blight': {
        'crop': 'Tomato',
        'disease': 'Late Blight',
        'status': 'Diseased',
        'severity': 'Critical',
        'cause': 'Oomycete (Phytophthora infestans)',
        'symptoms': 'Rapidly spreading dark greasy green-brown patches on leaves and stems; white fuzzy fungal growth under leaves.',
        'treatment': 'Apply copper fungicides proactively or systemic oomycides (cymoxanil, mandipropamid); bag and discard severely infected plants.',
        'prevention': 'Plant late blight resistant cultivars (e.g., Mountain Magic, Defiant); ensure excellent airflow and morning sun.'
    },
    'Tomato___Leaf_Mold': {
        'crop': 'Tomato',
        'disease': 'Leaf Mold',
        'status': 'Diseased',
        'severity': 'Moderate',
        'cause': 'Fungus (Passalora fulva)',
        'symptoms': 'Pale greenish-yellow spots on upper leaf surfaces with olive-brown velvety mold on the corresponding undersides.',
        'treatment': 'Improve ventilation; apply copper fungicides or bio-fungicides; keep greenhouse humidity below 85%.',
        'prevention': 'Provide aggressive air circulation in high tunnels/greenhouses; avoid wetting foliage; prune suckers.'
    },
    'Tomato___Septoria_leaf_spot': {
        'crop': 'Tomato',
        'disease': 'Septoria Leaf Spot',
        'status': 'Diseased',
        'severity': 'High',
        'cause': 'Fungus (Septoria lycopersici)',
        'symptoms': 'Many small circular spots (1-3mm) with dark brown borders and grayish-white centers with tiny black specks.',
        'treatment': 'Apply chlorothalonil, mancozeb, or copper sprays starting when lower leaves first show symptoms.',
        'prevention': 'Strip lower leaves up to 12 inches from ground; apply mulch; avoid overhead sprinkler watering.'
    },
    'Tomato___Spider_mites Two-spotted_spider_mite': {
        'crop': 'Tomato',
        'disease': 'Two-Spotted Spider Mite Damage',
        'status': 'Pest Infestation',
        'severity': 'Moderate to High',
        'cause': 'Arachnid Pest (Tetranychus urticae)',
        'symptoms': 'Fine yellow stippling or bronzing on leaves; fine silky webbing on leaf undersides and growing tips; leaf drop.',
        'treatment': 'Spray insecticidal soap, neem oil, or miticide (bifenazate, abamectin); release predatory mites (Phytoseiulus persimilis).',
        'prevention': 'Avoid dusty, hot dry conditions; mist plants during heatwaves; do not overuse broad-spectrum synthetic pyrethroids.'
    },
    'Tomato___Target_Spot': {
        'crop': 'Tomato',
        'disease': 'Target Spot',
        'status': 'Diseased',
        'severity': 'Moderate to High',
        'cause': 'Fungus (Corynespora cassiicola)',
        'symptoms': 'Pinpoint dark brown spots that expand into circular brown lesions with light brown centers and dark concentric rings.',
        'treatment': 'Apply azoxystrobin, difenoconazole, or copper fungicides on regular protective intervals.',
        'prevention': 'Increase plant spacing for rapid drying, avoid excess nitrogen, remove plant debris after final harvest.'
    },
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {
        'crop': 'Tomato',
        'disease': 'Tomato Yellow Leaf Curl Virus (TYLCV)',
        'status': 'Viral Infection',
        'severity': 'Severe',
        'cause': 'Virus (Begomovirus) transmitted by Whiteflies (Bemisia tabaci)',
        'symptoms': 'Severe stunting, erect upward curling of leaves, bright yellow margins, failure to set fruit.',
        'treatment': 'No cure once infected. Control whitefly vectors using insecticidal soaps, imidacloprid, or yellow sticky cards.',
        'prevention': 'Use insect-proof netting in greenhouses; plant TYLCV-resistant varieties; clear surrounding weed hosts.'
    },
    'Tomato___Tomato_mosaic_virus': {
        'crop': 'Tomato',
        'disease': 'Tomato Mosaic Virus (ToMV)',
        'status': 'Viral Infection',
        'severity': 'High',
        'cause': 'Tobamovirus (Mechanically transmitted)',
        'symptoms': 'Mottled light and dark green mosaic pattern on leaves, fern-like leaf distortion, internal browning in fruit.',
        'treatment': 'No cure exists. Immediately rogued out (remove and destroy) infected plants. Wash hands with milk or soap before handling plants.',
        'prevention': 'Sanitize pruning tools with 20% non-fat dry milk solution; purchase certified virus-free seed.'
    },
    'Tomato___healthy': {
        'crop': 'Tomato',
        'disease': 'Healthy Leaf',
        'status': 'Healthy',
        'severity': 'None',
        'cause': 'N/A',
        'symptoms': 'Lush, dark green compound leaves, strong stems, healthy flower clusters and firm green/red fruit.',
        'treatment': 'No treatment needed. Keep soil evenly moist to prevent blossom end rot.',
        'prevention': 'Stake or cage vines, prune suckers for airflow, and apply 2 inches of clean straw mulch.'
    }
}


def get_disease_info(raw_class_name):
    """Retrieve structured metadata for a given raw class name."""
    if raw_class_name in DISEASE_DETAILS:
        return DISEASE_DETAILS[raw_class_name]

    # Fallback parser if not found
    parts = raw_class_name.split('___')
    crop = parts[0].replace('_', ' ').strip()
    disease = parts[1].replace('_', ' ').strip() if len(parts) > 1 else 'Unknown'
    is_healthy = 'healthy' in disease.lower()

    return {
        'crop': crop,
        'disease': disease,
        'status': 'Healthy' if is_healthy else 'Diseased',
        'severity': 'None' if is_healthy else 'Moderate',
        'cause': 'N/A' if is_healthy else 'Unknown Pathogen',
        'symptoms': 'No symptoms noted.' if is_healthy else 'Discoloration or lesion on foliage.',
        'treatment': 'No treatment necessary.' if is_healthy else 'Consult your local agricultural extension service.',
        'prevention': 'Maintain routine crop hygiene and monitoring.'
    }
