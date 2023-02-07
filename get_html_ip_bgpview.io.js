ip = "";
$('#table-prefixes-v4').find('tbody tr').each((i,v)=>{
  //console.log($(v).html())
  ip += $(v).find('td').eq(1).find('a').html() + "\n"
})
console.log(ip)
