// async function getRequestAPI(url,category,data){
//     axios.get(url, {
//         method: 'GET',
//         mode: 'cors',
//         withCredentials: false,
//         headers: {
//             'Access-Control-Allow-Origin': '*',
//             'Content-Type': 'application/json',
//         },
//         data
//     }).then(res => {
//         if (category == 'report') {
//             console.log("success")
//         }
//     }
//     )
// }
// fetch('result')
//   .then(response => response.text())
//   .then(html => {
//     // get a reference to the container element
//     const container = document.querySelector('#content');
    
//     // set the HTML content of the container element
//     container.innerHTML = html;
//   })
//   .catch(error => console.error(error));
var result;
async function postRequestAPI(url, category, data) {
    axios.defaults.headers.common['X-CSRFToken'] = data['csrf_token'];
    // token.push(data['csrf_token'])
    // console.log(data)
    axios.post(url, {
        method: 'POST',
        mode: 'cors',
        withCredentials: false,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
        },
        data
    }).then(res => {
     
        if (category == 'output') {
            console.log("saved")
        }
      
        if (category == 'predict') {
            console.log(res)
            localStorage.setItem('result',res.data);

            console.log(result)
            console.log("aruna")
            
            
            // document.getElementById("report").innerHTML="success"
            // document.getElementById("report").innerHTML=res.data['result']
            // document.getElementById("answer").innerHTML=res.data['result']
            // document.getElementById("answer").style.display="block";  
            // document.getElementById("answer").style.color="red";  
        }
    }
    )
}

document.getElementById("output").onclick = function() {
    var entire_dataset="";
    const datas={
            // 'csrf_token':$("input[name=csrfmiddlewaretoken]").val(),
            'Time':document.getElementById("time").value,
            'V1':document.getElementById("v1").value,
            'V2':document.getElementById("v2").value,
            'V3':document.getElementById("v3").value,
            'V4':document.getElementById("v4").value,
            'V5':document.getElementById("v5").value,
            'V6':document.getElementById("v6").value,
            'V7':document.getElementById("v7").value,
            'V8':document.getElementById("v8").value,
            'V9':document.getElementById("v9").value,
            'V10':document.getElementById("v10").value,
            'V11':document.getElementById("v11").value,
            'V12':document.getElementById("v12").value,
            'V13':document.getElementById("v13").value,
            'V14':document.getElementById("v14").value,
            'V15':document.getElementById("v15").value,
            'V16':document.getElementById("v16").value,
            'V17':document.getElementById("v17").value,
            'V18':document.getElementById("v18").value,
            'V19':document.getElementById("v19").value,
            'V20':document.getElementById("v20").value,
            'V21':document.getElementById("v21").value,
            'V22':document.getElementById("v22").value,
            'V23':document.getElementById("v23").value,
            'V24':document.getElementById("v24").value,
            'V25':document.getElementById("v25").value,
            'V26':document.getElementById("v26").value,
            'V27':document.getElementById("v27").value,
            'V28':document.getElementById("v28").value,
            'Amount':document.getElementById("amount").value,
            // 'csrf_token': $("input[name=csrfmiddlewaretoken]").val(),
            // 'V1':'89',
            // 'Time':'89',
            // 'V3':'89',
            // 'V2':'89',
            // 'V4':'89',
            // 'V6':'89',
            // 'V5':'89',
            // 'V7':'89',
            // 'V8':'89',
            // 'V9':'89',
            // 'V10':'89',           
            // 'V11':'89',
            // 'V12':'89',
            // 'V13':'89',
            // 'V14':'89',
            // 'V15':'89',
            // 'V16':'89',
            // 'V17':'89',
            // 'V18':'89',
            // 'V19':'89',
            // 'V20':'89',
            // 'V21':'89',
            // 'V22':'89',
            // 'V23':'89',
            // 'V24':'89',
            // 'V25':'89',
            // 'V26':'89',
            // 'V27':'89',
            // 'V28':'89',
            // 'Amount':'89',
        }
        var val=Object.values(datas);
        for(var i in val){
            if(i<val.length-1){
                entire_dataset+=val[i]+",";
            }  
            else{
                entire_dataset+=val[i];
            }         
         }
        
        const data={
            'csrf_token': $("input[name=csrfmiddlewaretoken]").val(),
            'entire_data':entire_dataset,
            'datas':datas
        }
  
    postRequestAPI("http://127.0.0.1:8000/result/", "output", data)
    postRequestAPI("http://127.0.0.1:8000/predicte/", "predict", data)
    // getRequestAPI("http://127.0.0.1:8000/report/", "report", data)
}

function loadresult(a)
{
    result=a;
}