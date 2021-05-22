// Función para enlazar los selects
const $carro = $("#car_id");
const $modelo = $("#car_model_id");
const $motor = $("#engine_id");

$carro.change(function(){
    $modelo.val('');
    
    $modelo.prop('disabled', !Boolean($carro.val()));
    $motor.prop('disabled', !Boolean($modelo.val()));
    $modelo.find('option[data-carro]').hide();
    $modelo.find('option[data-carro="' + $carro.val() + '"]').show();
    
});

$modelo.change(function(){
    $motor.val('');
    
    $motor.prop('disabled', !Boolean($modelo.val()));
    $modelo.prop('disabled', !Boolean($carro.val()));
    $motor.find('option[data-carro]').hide();
    $motor.find('option[data-carro="' + $modelo.val() + '"]').show();
    
});

// Función para filtrar
// function myFunction() {
//     // Declare variables 
//     var input, filter, table, tr, td, i, j, visible;
//     input = document.getElementById("myInput");
//     filter = input.value.toUpperCase();
//     table = document.getElementById("invoice");
//     tr = table.getElementsByTagName("tr");
  
//     // Loop through all table rows, and hide those who don't match the search query
//     for (i = 0; i < tr.length; i++) {
//       visible = false;
//       /* Obtenemos todas las celdas de la fila, no sólo la primera */
//       td = tr[i].getElementsByTagName("td");
//       for (j = 0; j < td.length; j++) {
//         if (td[j] && td[j].innerHTML.toUpperCase().indexOf(filter) > -1) {
//           visible = true;
//         }
//       }
//       if (visible === true) {
//         tr[i].style.display = "";
//       } else {
//         tr[i].style.display = "none";
//       }
//     }
//   }

// ----------------------------------------------------------------------------------------------

// Funcion filtrar
$(document).ready(function(){
    $("#myInput").on("keyup",function(){                                // Cuando se teclea algo
        var value = $(this).val().toLowerCase();                        // Toma el valor del input en minuscula
        $("#myTable tr").filter(function(){                             // 
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        })
    })
});

// ----------------------------------------------------------------------------------------------

//   Paginado
// $.fn.pageMe = function(opts){
//     var $this = this,
//         defaults = {
//             perPage: 7,
//             showPrevNext: false,
//             hidePageNumbers: false
//         },
//         settings = $.extend(defaults, opts);
    
//     var listElement = $this;
//     var perPage = settings.perPage; 
//     var children = listElement.children();
//     var pager = $('.pager');
    
//     if (typeof settings.childSelector!="undefined") {
//         children = listElement.find(settings.childSelector);
//     }
    
//     if (typeof settings.pagerSelector!="undefined") {
//         pager = $(settings.pagerSelector);
//     }
    
//     var numItems = children.size();
//     var numPages = Math.ceil(numItems/perPage);

//     pager.data("curr",0);
    
//     if (settings.showPrevNext){
//         $('<li><a href="#" class="prev_link">«</a></li>').appendTo(pager);
//     }
    
//     var curr = 0;
//     while(numPages > curr && (settings.hidePageNumbers==false)){
//         $('<li><a href="#" class="page_link">'+(curr+1)+'</a></li>').appendTo(pager);
//         curr++;
//     }
    
//     if (settings.showPrevNext){
//         $('<li><a href="#" class="next_link">»</a></li>').appendTo(pager);
//     }
    
//     pager.find('.page_link:first').addClass('active');
//     pager.find('.prev_link').hide();
//     if (numPages<=1) {
//         pager.find('.next_link').hide();
//     }
//   	pager.children().eq(1).addClass("active");
    
//     children.hide();
//     children.slice(0, perPage).show();
    
//     pager.find('li .page_link').click(function(){
//         var clickedPage = $(this).html().valueOf()-1;
//         goTo(clickedPage,perPage);
//         return false;
//     });
//     pager.find('li .prev_link').click(function(){
//         previous();
//         return false;
//     });
//     pager.find('li .next_link').click(function(){
//         next();
//         return false;
//     });
    
//     function previous(){
//         var goToPage = parseInt(pager.data("curr")) - 1;
//         goTo(goToPage);
//     }
     
//     function next(){
//         goToPage = parseInt(pager.data("curr")) + 1;
//         goTo(goToPage);
//     }
    
//     function goTo(page){
//         var startAt = page * perPage,
//             endOn = startAt + perPage;
        
//         children.css('display','none').slice(startAt, endOn).show();
        
//         if (page>=1) {
//             pager.find('.prev_link').show();
//         }
//         else {
//             pager.find('.prev_link').hide();
//         }
        
//         if (page<(numPages-1)) {
//             pager.find('.next_link').show();
//         }
//         else {
//             pager.find('.next_link').hide();
//         }
        
//         pager.data("curr",page);
//       	pager.children().removeClass("active");
//         pager.children().eq(page+1).addClass("active");
    
//     }
// };

// $(document).ready(function(){
    
//   $('#myTable').pageMe({pagerSelector:'#myPager',showPrevNext:true,hidePageNumbers:false,perPage:4});
    
// });

// Generar PDF desde HTML
function generatePDF(){
    const element = document.getElementById("invoice");
    var opt = {
        margin:       1,
        filename:     'report.pdf',
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 2 },
        enableLinks:  false,
        pagebreak:    {mode: "avoid-all"},
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
      };
    html2pdf()
    .set(opt)
    .from(element)
    .save();
}

function viewPDF(){
    const element = document.getElementById("invoice");
    var opt = {
        margin:       1,
        filename:     'report.pdf',
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 2 },
        enableLinks:  false,
        pagebreak:    {mode: "avoid-all"},
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
      };
    html2pdf()
    .set(opt)
    .from(element);
    
    html2pdf().set(opt).from(element).toPdf().get('pdf').then(function (pdf) {
        window.open(pdf.output('bloburl'), '_blank');
      });
}

// Intento de paginacion

/*
<h4>Select number of Rows</h4>
<div class="form-group">
    <select name="state" id="maxRows" class="form-control" style="width:150px">
        <option value="5000">Show all</option>
        <option value="5">5</option>
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
        <option value="50">50</option>
        <option value="75">75</option>
        <option value="100">100</option>
    </select>
</div>


{ <div class="pagination-container">
    <nav>
        <ul class="pagination"></ul>
    </nav>
</div> }

{ <script src="jquery.min.js"></script>
<script src="bootstrap.min.js"></script>
var table='#invoice'
$('#maxRows').on('change',function(){
    $(".pagination").html('')
    var trnum=0
    var maxRows=parseInt($(this).val())
    var totalRows=$(table+' tbody tr').length
    $(table+' tr:gt(0)').each(function(){
        trnum++
        if(trnum>maxRows){
            $(this).hide()
        }
        if(trnum<=maxRows){
            $(this).show()
        }
    })
    if(totalRows>maxRows){
        var pagenum=Math.ceil(totalRows/maxRows)
        for(var i=1;i<=pagenum;){
            $('.pagination').append('<li data-page="'+i+'">\<span>'+ i++ +'<span class="sr-only">(current)</span></span>\</li>').show()
        }
    }
    $('.pagination li:first-child').addClass('active')
    $('.pagination li').on('click',function(){
        var pageNum=$(this).attr('data-page')
        var trIndex=0;
        $('.pagination li').removeClass('active')
        $(this).addClass('active')
        $(table+' tr:gt(0)').each(function(){
            trIndex++
            if(trIndex>(maxRows*pageNum) || trIndex<=((maxRows*pageNum)-maxRows)){
                $(this).hide()
            }else{
                $(this).show()
            }
        })
    })
})
$(function(){
    $('table tr:eq(0)').prepend('<th>ID</th>')
    var id=0;
    $('table tr:gt(0)').each(function(){
        id++
        $(this).prepend('<td>'+id+'</td>')
    })
}) }*/

// $('select#maxRows').on('change',function(){
//     var valor = $(this).val();
//     return valor;
//     console.log(valor);
// });
// c=valor;


// $('select#maxRows').on('change',function(){
//     var valor = $(this).val();
// });
// // alert(num);



// El que mas sirve
// $(document).ready(function(){      
    
//     $('#invoice').after('<div id="nav"></div>');
    
//     var rowsShown = 10;                                                      //rowsShown -> Numero de filas por pagina
//     var rowsTotal = $('#invoice tbody tr').length;                          //rowsTotal -> Número de filas totales
//     var numPages = Math.ceil(rowsTotal/rowsShown);                                     //numPages -> Número de paginas (Total/Shown)
//     $('#nav').append('<a href="#" rel="0">First</a> ');
//     for(i = 0;i < numPages;i++) {
//         var pageNum = i + 1;
//         $('#nav').append('<a href="#" rel="'+i+'">'+pageNum+'</a> ');       //Agrega al nav el número de página
//     }
//     $('#nav').append('<a href="#" rel="'+(numPages-1)+'">Last</a> ');
//     $('#invoice tbody tr').hide();                                          //Oculta las paginas
//     $('#invoice tbody tr').slice(0, rowsShown).show();                      //Muestra desde 0 hata el numero de filas
//     $('#nav a:nth-child(2)').addClass('active');                                   //Agrega la clase active al primer link
//     $('#nav a').bind('click', function(e){
//     if($(this).is(':nth-child(1)')){
//         $('#nav a').removeClass('active');
//         $('#nav a:nth-child(2)').addClass('active');        
//     }else{
//         if($(this).is(':nth-child('+(numPages+2)+')')){
//             $('#nav a').removeClass('active');
//             $('#nav a:nth-child('+(numPages+1)+')').addClass('active');
//         }else{
//             $('#nav a').removeClass('active');
//             $(this).addClass('active');
//         }        
//     }
//         var currPage = $(this).attr('rel');
//         var startItem = currPage * rowsShown;
//         var endItem = startItem + rowsShown;
//         $('#invoice tbody tr').css('opacity','0.0').hide().slice(startItem, endItem).
//                 css('display','table-row').animate({opacity:1}, 300);
//                 e.preventDefault();
            
//     });
// });






// var table='#invoice';                                           // Guarda la tabla por el id
// $('#maxRows').on('change', function(){                          // Si se selecciona un tamaño
//     $('.pagination').html('')
//     var trnum = 0                                               // Numero de tr?
//     var maxRows = parseInt($(this).val())                       // Guarda el numero de filas máximas seleccionadas (maxRows)
//     var totalRows = $(table+' tbody tr').length                 // Numero total de filas (totalRows)
//     $(table+' tr:gt(0)').each(function(){                       // funcion que se ejecuta desde el tr[0] para cada hijo que consiga (td)
//         trnum++                                                 // Aumenta el trnum
//         if(trnum > maxRows){                                    // Si trnum es mayor a las filas maximas seleccionadas
//             $(this).hide()                                      // Oculta la tabla?
//         }
//         if(trnum <= maxRows){                                   // Si trnum es menor a las filas maximas seleccionadas
//             $(this).show()                                      // Muestra la tabla
//         }
//     })
//     if(totalRows > maxRows){                                    // Si el numero total de filas es mayor al numero de filas seleccionada
//         alert("TotalRows: "+totalRows)
//         alert("maxRows: "+maxRows)
//         var pagenum = Math.ceil(totalRows/MaxRows);              // Numero de paginas
//         alert("pagenum: "+pagenum)
//         for(var i=1; i <= pagenum;){                            // Repite para la cantidad de páginas
//             $('.pagination').append('<li data-page="'+i+'">\<span>'+ i++ +'<span class="sr-only">(current)</span></span>\</li>').show()
//         }
//     }
//     $('.pagination li:first-child').addClass('active')
//     $('.pagination li').on('click',function(){
//         var pageNum = $(this).attr('data-page')
//         var trIndex = 0;
//         $('.pagination li').removeClass('active')
//         $(this).addClass('active')
//         $(table+' tr:gt(0)').each(function(){
//             trIndex++
//             if(trIndex > (maxRows*pageNum) || trIndex <= ((maxRows*pageNum)-maxRows)){
//                 $(this).hide()
//             }else{
//                 $(this).show()
//             }
//         })
//     })
// })

