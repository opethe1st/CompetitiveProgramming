 function binaryGap(n){
         var maxgap = 0;
    var gap = 0;
    while (n%2==0){
         n/=2;
     }
     //console.log(n);
     while(n>0){
         if (n&1){
             if(gap>maxgap){
                 maxgap=gap;
                 
             }
             gap=0;
         }else{
             gap+=1;
         }
         n>>=1;
         //console.log(n);
         //console.log('maxgap',maxgap);
     }
     return maxgap;
 }
console.time()
console.log(binaryGap(1<<20-23345))
console.timeEnd()