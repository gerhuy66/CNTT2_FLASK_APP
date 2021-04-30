


async function searchCv()
{
    
    let searchFilter = $("#filterSelect").val();
    let searchValue = $("#search").val();

    let ro = {
        "searchFilter": searchFilter,
        "searchVal":searchValue
    }
    let rp = await axios.post("/searchCV",ro);
    let rslist = rp.data.res;
    $("#search_result").text("");
    rslist.forEach(function(item){
       let source = item._source;
       let fullname = source.full_name != undefined ? source.full_name : "";
       let birthdate = source.birth_date != undefined ? source.birth_date : "";
       let address = source.address != undefined ? source.address : "";
       let phone = source.phone != undefined ? source.phone : "";
       let gender = source.gender != undefined ? source.gender : "";
       let major = source.major != undefined ? source.major : "";
       let cvContent = source.cv_content;
       let teamplate = `
       
       <div style="background-color:lightblue;padding:10px;box-shadow: 0px 0px 1px 1px grey">
        "full name: " ${fullname}<br>
        "Birthdate" ${birthdate}<br>
        "Address: " ${address}<br>
        "Phone: " ${phone}<br>
        "Gender: " ${gender}<br>
        "Major: " ${major}<br>
        "Cv Content: " ${cvContent}<br>
       <div>
       
       `;

       $("#search_result").append(teamplate);
    });

    $('html, body').animate({scrollTop:$(document).height()/3.5 - 20}, 'slow');
}