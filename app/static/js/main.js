


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
    $("#search_result").append(`
    <div class="container-fluid"">
      <table class="table table-bordered">
        <thead class="thead-dark">
          <tr>
                <th scope="col">Full name</th>
                <th scope="col">Birthdate</th>
                <th scope="col">Address</th>
                <th scope="col">Phone</th>
                <th scope="col">Gender</th>
                <th scope="col">Major</th>
                <th scope="col">CV Content</th>
          </tr>
        </thead>
        <tbody>
    `);
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
       
        <tr>
          <td>
            ${fullname}
          </td>
          <td>
            ${birthdate}
          </td>
          <td>
            ${address}
          </td>
          <td>
            ${phone}
          </td>
          <td>
            ${gender}
          </td>
          <td>
            ${major}
          </td>
          <td>
            ${cvContent}
          </td>
        </tr>


       `;

       $("#search_result").append(teamplate);
    });
    $("#search_result").append(`
    </tbody>
    </table>
    </div>`)
    $('html, body').animate({scrollTop:$(document).height()/3.5 - 20}, 'slow');
}