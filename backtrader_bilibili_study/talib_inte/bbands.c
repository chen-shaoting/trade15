#include <stdio.h>
#include <stdlib.h>
#include <ta-lib/ta_libc.h>

void print_double_array(double* list, int n){
    for(int i=0; i<n; i++){
        printf("%f  ", list[i]);
    }
}

int main(){
    TA_RetCodeInfo info;

    TA_RetCode retCode = TA_Initialize();

    if( retCode != TA_SUCCESS )
    {
        TA_SetRetCodeInfo( retCode, &info );
        printf( "Error %d(%s): %s\n",
                retCode,
                info.enumStr,
                info.infoStr );
    }
    // init success
    
    // version
    const char* ver_str = TA_GetVersionString();
    printf( "ta-lib version: %s\n", ver_str );

    // BBANDS

    double* input_buff = (double*)calloc(100,sizeof(double));
    double* output_upper = (double*)calloc(100,sizeof(double));
    double* output_middle = (double*)calloc(100,sizeof(double));
    double* output_lower = (double*)calloc(100,sizeof(double));

    for(int i=0; i<100; i++){
        input_buff[i] = (double)rand() / RAND_MAX;
    }

    int outBegIdx = 0;
    int outNBElement = 0;
    TA_BBANDS(0, 99, input_buff, 5, 2.0, 2.0, 
            TA_MAType_SMA, &outBegIdx, &outNBElement,
            output_upper, output_middle, output_lower);
    printf("bi %d, nbe %d\n", outBegIdx, outNBElement);
    printf("upper\n");
    print_double_array(output_upper,100);
    printf("middle\n");
    print_double_array(output_middle,100);
    printf("lower\n");
    print_double_array(output_lower,100);

    free(input_buff);
    free(output_upper);
    free(output_middle);
    free(output_lower);

    // shutdown ta-lib
    TA_Shutdown();
}
