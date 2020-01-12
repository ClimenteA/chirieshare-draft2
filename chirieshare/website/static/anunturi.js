
//Adauga la favorite, redirectioneaza spre pagina detalii anunt si alte mici detalii

document.addEventListener("DOMContentLoaded", function(){

  function goToLink(link){
    window.history.pushState('Object', 'Title', '/anunturi');
    let a = document.createElement("a");
    a.setAttribute('href', link);
    a.click();
  }
  
  //Inputuri de filtrare anunturi  
  let cambtn = document.getElementById("cam");
  let apbtn = document.getElementById("ap");
  let ap_val = document.getElementById("ap_val"); 
  let not_selected = "sm darkish bold";
  let selected = "sm secondary bold";

  let loc = document.getElementById("loc");
  let zona = document.getElementById("zona");
  let pret = document.getElementById("pret");

  let helper = document.getElementById("filter-helper");
  
  loc.addEventListener("change", function(event){
    helper.innerText = "Completeaza si zona sau alege una din optiunile de mai sus";
  },false);

  //Trimite get request pentru noi anunturi in functie de inputuri
  function filtreazaAnunturi(){
    let localitate = loc.value ? loc.value : 'toate';
    let reper_zona = zona.value ? zona.value : 'toate'; 
    goToLink(`anunturi/filtreaza/${localitate}/${reper_zona}/${ap_val.value}/${pret.value}/`);
  };

  //Cand un button care arata pretul anuntului este clicked modifica inputul hidden cu pret
  let btn_preturi = document.querySelectorAll(".price");
  btn_preturi.forEach(btn => {
    btn.addEventListener("click", function(event){
        pret.value = event.target.innerText.split(" ")[0].trim();
    },false);

  });


  if (ap_val.value == "1"){
    cambtn.className = not_selected;
    apbtn.className  = selected;
    ap_val.value = "1";
  }

  //Toggle intre camere si apartament
  cambtn.addEventListener("click", function(e){
      e.preventDefault();
      cambtn.className = selected;
      apbtn.className  = not_selected;
      ap_val.value = "0";
      filtreazaAnunturi();
  },false);

  apbtn.addEventListener("click", function(e){
      e.preventDefault();
      cambtn.className = not_selected;
      apbtn.className  = selected;
      ap_val.value = "1";
      filtreazaAnunturi();
  },false);



  var awesomplete = new Awesomplete(loc);

  awesomplete.minChars = 3;
  awesomplete.maxItems = 5;
  awesomplete.autoFirst = true;
  awesomplete.filter = Awesomplete.FILTER_STARTSWITH;

  awesomplete.list = ["Bucuresti", "Cluj-Napoca", "Timisoara", "Iasi", "Constanta", "Craiova", "Brasov", "Galati", "Ploiesti", "Oradea", "Braila", "Arad", "Pitesti", "Sibiu", "Bacau", "Targu Mures", "Baia Mare", "Buzau", "Botosani", "Satu Mare", "Suceava", "Ramnicu Valcea", "Drobeta-Turnu Severin", "Piatra-Neamt", "Targoviste", "Targu Jiu", "Focsani", "Tulcea", "Resita", "Slatina", "Bistrita", "Calarasi", "Giurgiu", "Deva", "Hunedoara", "Zalau", "Barlad", "Alba Iulia", "Sfantu Gheorghe", "Roman", "Vaslui", "Turda", "Medias", "Alexandria", "Voluntari", "Pipera (Voluntari)", "Slobozia", "Lugoj", "Medgidia", "Onesti", "Miercurea-Ciuc", "Petrosani", "Tecuci", "Mangalia", "Odorheiu Secuiesc", "Ramnicu Sarat", "Sighetu Marmatiei", "Campina", "Navodari", "Campulung", "Caracal", "Sacele", "Fagaras", "Dej", "Rosiori de Vede", "Mioveni", "Curtea de Arges", "Husi", "Reghin", "Sighisoara", "Pantelimon", "Pascani", "Oltenita", "Turnu Magurele", "Caransebes", "Falticeni", "Radauti", "Lupeni", "Dorohoi", "Vulcan", "Campia Turzii", "Zarnesti", "Borsa", "Popesti-Leordeni", "Codlea", "Carei", "Moinesti", "Petrila", "Sebes", "Tarnaveni", "Floresti", "Gherla", "Fetesti-Gara", "Buftea", "Cugir", "Moreni", "Gheorgheni", "Comanesti", "Salonta", "Cernavoda", "Targu Secuiesc", "Bailesti", "Campulung Moldovenesc", "Aiud", "Valea Caselor (Dragasani)", "Dragasani", "Bals", "Bocsa", "Motru", "Corabia", "Bragadiru", "Urziceni", "Rasnov", "Rasnov Romacril", "Buhusi", "Zimnicea", "Marghita", "Mizil", "Cisnadie", "Targu Neamt", "Calafat", "Vatra Dornei", "Adjud", "Gaesti", "Tandarei", "Gura Humorului", "Chitila", "Viseu de Sus", "Otopeni", "Ludus", "Dragu-Brad", "Brad", "Valu lui Traian", "Cumpana", "Sannicolau Mare", "Valenii de Munte", "Jilava", "Dabuleni", "Filiasi", "Blaj", "Ovidiu", "Simleu Silvaniei", "Matca", "Pecica", "Rovinari", "Videle", "Baicoi", "Pucioasa", "Jimbolia", "Baia Sprie", "Targu Frumos", "Vicovu de Sus", "Orsova", "Sinaia", "Negresti-Oas", "Beius", "Santana", "Pechea", "Simeria", "Boldesti-Scaeni", "Poienile de sub Munte", "Valea lui Mihai", "Covasna", "Targu Ocna", "Toplita", "Sovata", "Otelu Rosu", "Oravita", "Moisei", "Harsova", "Murfatlar", "Beclean", "Poiana Mare", "Huedin", "Babadag", "Marasesti", "Topoloveni", "Sangeorgiu de Mures", "Jibou", "Sabaoani", "Hateg", "Avrig", "Darmanesti", "Marginea", "Moldova Veche", "Ineu", "Bolintin-Vale", "Mihail Kogalniceanu", "Macin", "Tomesti", "Nasaud", "Uricani", "Rosu", "Calan", "Borcea", "Afumati", "Domnesti", "Draganesti-Olt", "Cristuru Secuiesc", "1 Decembrie", "Lumina", "Fetesti", "Mogosoaia", "Modelu", "Dumbravita", "Seini", "Alesd", "Sangeorz-Bai", "Curtici", "Darabani", "Nadlac", "Victoria", "Amara", "Branesti", "Harlau", "Lipova", "Techirghiol", "Agnita", "Sacueni", "Titu", "Siret", "Segarcea", "Odobesti", "Podu Iloaiei", "Ocna Mures", "Urlati", "Strehaia", "Tasnad", "Cajvana", "Tuzla", "Sadova", "Vlahita", "Stei", "Diosig", "Cobadin", "Gilau", "Vladimirescu", "Dancu", "Bumbesti-Jiu", "Busteni", "Peretu", "Cudalbi", "Bosanci", "Balotesti", "Lunca Cetatuii", "Dragalina", "Fieni", "Chisineu-Cris", "Balan", "Sandominic", "Strejnicu", "Baciu", "Fundulea", "Ianca", "Remetea", "Fagetel (Remetea)", "Roseti", "Breaza de Sus", "Cornetu", "Insuratei", "Apahida", "Berceni", "Vicovu de Jos", "Savinesti (Poiana Teiului)", "Savinesti", "Teius", "Barbulesti", "Plosca", "Toflea", "Magurele", "Feldru", "Anina", "Valea Mare (Negresti)", "Negresti", "Peris", "Fundeni", "Giroc", "Baile Borsa", "Oituz", "Rucar", "Curcani", "Valea Mare (Babeni)", "Babeni", "Rodna", "Deta", "Ruscova", "Intorsura Buzaului", "Pancota", "Glina", "Talmaciu", "Copsa Mica", "Motatei", "Gugesti", "Schela Cladovei", "Sancraiu de Mures", "Iernut", "Targu Lapus", "Maieru", "Prejmer", "Pogoanele", "Dobroesti", "Baraolt", "Arbore", "Homocea", "Corund", "Tufesti", "Giarmata", "Baia", "Dumbraveni", "Eforie Nord", "Horodnic de Sus", "Greci", "Tudora", "Straja", "Rasinari", "Sebis", "Raducaneni", "Siria", "Paunesti", "Saveni", "Tunari"];


  //Du-te la pagina detalii anunt 
  let anunturi = document.querySelectorAll(".card.product");

  anunturi.forEach(anunt => {
    
    let titlu_anunt = anunt.getElementsByTagName("h3")[0];
    let img_anunt = anunt.getElementsByTagName("img")[0];
    
    //Create a gost a href element an simulate a user click

    titlu_anunt.addEventListener("click", function(event){
      let favid = event.target.parentElement.getAttribute("id");
      goToLink(`detalii-anunt/${favid}/`);
    },false);

    img_anunt.addEventListener("click", function(event){
      let favid = event.target.parentElement.getAttribute("id");
      goToLink(`detalii-anunt/${favid}/`);
    },false);

  });

  //Adauga la favorite
  const fav_unselected = "data:image/svg+xml,%3Csvg width='22' height='21' viewBox='0 0 22 21' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M11.1016 17.1094C12.7266 15.6536 13.9284 14.5534 14.707 13.8086C15.4857 13.0638 16.332 12.1836 17.2461 11.168C18.1602 10.1523 18.7865 9.25521 19.125 8.47656C19.4974 7.69792 19.6836 6.9362 19.6836 6.19141C19.6836 5.10807 19.3112 4.21094 18.5664 3.5C17.8555 2.78906 16.9583 2.43359 15.875 2.43359C15.0286 2.43359 14.2331 2.67057 13.4883 3.14453C12.7773 3.61849 12.2865 4.22786 12.0156 4.97266H9.98438C9.71354 4.22786 9.20573 3.61849 8.46094 3.14453C7.75 2.67057 6.97135 2.43359 6.125 2.43359C5.04167 2.43359 4.1276 2.78906 3.38281 3.5C2.67188 4.21094 2.31641 5.10807 2.31641 6.19141C2.31641 6.9362 2.48568 7.69792 2.82422 8.47656C3.19661 9.25521 3.83984 10.1523 4.75391 11.168C5.66797 12.1836 6.51432 13.0638 7.29297 13.8086C8.07161 14.5534 9.27344 15.6536 10.8984 17.1094L11 17.2109L11.1016 17.1094ZM15.875 0.25C17.5677 0.25 18.9727 0.825521 20.0898 1.97656C21.2409 3.1276 21.8164 4.53255 21.8164 6.19141C21.8164 7.17318 21.6302 8.13802 21.2578 9.08594C20.8854 10 20.1914 11.0326 19.1758 12.1836C18.194 13.3346 17.2969 14.2995 16.4844 15.0781C15.6719 15.8568 14.3685 17.0586 12.5742 18.6836L11 20.1055L9.42578 18.7344C7.08984 16.6354 5.39714 15.0612 4.34766 14.0117C3.33203 12.9622 2.38411 11.7266 1.50391 10.3047C0.623698 8.88281 0.183594 7.51172 0.183594 6.19141C0.183594 4.53255 0.742188 3.1276 1.85938 1.97656C3.01042 0.825521 4.43229 0.25 6.125 0.25C8.08854 0.25 9.71354 1.01172 11 2.53516C12.2865 1.01172 13.9115 0.25 15.875 0.25Z' fill='%23EE6352'/%3E%3C/svg%3E%0A";
  const fav_selected   = "data:image/svg+xml,%3Csvg width='22' height='21' viewBox='0 0 22 21' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M11 20.1055L9.42578 18.6836C7.63151 17.0586 6.32812 15.8568 5.51562 15.0781C4.70312 14.2995 3.78906 13.3346 2.77344 12.1836C1.79167 11.0326 1.11458 10 0.742188 9.08594C0.369792 8.13802 0.183594 7.17318 0.183594 6.19141C0.183594 4.53255 0.742188 3.1276 1.85938 1.97656C3.01042 0.825521 4.43229 0.25 6.125 0.25C8.08854 0.25 9.71354 1.01172 11 2.53516C12.2865 1.01172 13.9115 0.25 15.875 0.25C17.5677 0.25 18.9727 0.825521 20.0898 1.97656C21.2409 3.1276 21.8164 4.53255 21.8164 6.19141C21.8164 7.51172 21.3763 8.88281 20.4961 10.3047C19.6159 11.7266 18.651 12.9622 17.6016 14.0117C16.5859 15.0612 14.9102 16.6354 12.5742 18.7344L11 20.1055Z' fill='%23EE6352'/%3E%3C/svg%3E%0A";
  let favli = document.querySelectorAll(".fav");

  favli.forEach(fav => {

    fav.addEventListener("click", function(event){
      
      let favid = event.target.parentElement.getAttribute("id");
    
        if (event.target.getAttribute("src") != fav_selected){
            event.target.setAttribute("src", fav_selected);
            addToFav(favid);
        }
        else {
            event.target.setAttribute("src", fav_unselected);
            delFromFav(favid);
        }
    }, false);

  });

  //Trimite un get request pentru a adauga/scoate de la favorite 
  function addToFav(favid){
    fetch(`adauga-la-favorite/${favid}/`)
      .then((response) => {
        if (response.status != 200){
          new Toast({
            message: "Anuntul nu a putut fi adaugat la favorite! Mai incearca!",
            type: 'danger'
          });
        }else {
          console.log("Anunt adaugat la favorite!");
        }
      });
  };

  function delFromFav(favid){
    fetch(`scoate-de-la-favorite/${favid}/`)
      .then((response) => {
        if (response.status != 200){
          new Toast({
            message: "Anuntul nu a putut fi scos de la favorite! Mai incearca!",
            type: 'danger'
          });
        }else {
          console.log("Anunt scos de la favorite!");
        }
      });
  };






//DOM loaded    
});
