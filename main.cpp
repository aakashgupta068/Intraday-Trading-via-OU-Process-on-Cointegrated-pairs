/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;

void maxArrK(int arr[], int n, int d)
{
    int s=arr[0], i=1, mx = arr[0];
    while(i<d)
    {
        s+=arr[i];
        i++;
    }
    mx = s;
    while(i<n)
    {
        s = s + arr[i] - arr[i-d];
        mx = max(mx , s);
        i++;
    }
    cout<<mx;
}

void subArrSumK(int arr[], int n, int k)
{
    int i=1,t=arr[0],s=arr[0], j=0;
    while(i<n)
    {
        while(j<i & s>k)
        {
            s = s - arr[j];
            j = min(j+1, i);
            //cout<<" s>k, arr[j]: "<<arr[j]<<", arr[i]: "<<arr[i]<<", s: "<<s<<endl;
        }
        
        t=s;
        while(t==k)
        {
            cout<<"j: "<<j<<", i: "<<i<<",t :"<<t<<endl;
            t = t-arr[j];
            if(t<k)
                break;
            j = min(j+1, i);
        }
        
    
        i++;
        s = s+ arr[i];
        //cout<<"arr["<<j<<"]: "<<arr[j]<<", arr["<<i<<"]: "<<arr[i]<<", s: "<<s<<endl;
    }
    
}

int binSearch(int arr[], int n, int k)
{
    int l=0, r=n-1;
    int m = (l+r)/2;
    while(r>l)
    {
        if(arr[m]==k)
        {
            cout<<"present at "<<m<<endl;
            return m;
        }
        else if( k > arr[m])
        {
            l = m+1;
            m= (l+r)/2;
        }
        else
        {
            r= m-1;
            m = (l+r)/2;
        }
    }
    if(arr[m]==k)
        return m;
    return -1;
}

int binSearchRecurr(int arr[], int k, int l, int r)
{
    int m = (l+r)/2;
    if(r==l)
    {
        if(arr[m] == k)
            return m;
        else
            return -1;
    }
    else if(k>arr[m])
        return binSearchRecurr(arr, k, m+1, r);
    else
        return binSearchRecurr(arr, k, r, m-1);
}

int main()
{
    int arr[] = {1,5,5,5,5,7,9,10,11,13};
    int n = sizeof(arr)/sizeof(n);
    
    int eleInd = binSearchRecurr(arr, 5, 0, n-1);
    int i = 0;
    if(eleInd!=-1)
    {
        for(i=0; arr[i]!=arr[eleInd]; i++);
        cout<<i;
    }
    
    return 0;
}