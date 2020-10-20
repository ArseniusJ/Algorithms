#include <stdio.h>
#include <string.h>
#include <stdlib.h>


#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)


typedef struct trie
{
    struct trie* row[26];
    int isEnd;
}trie;

trie* addNewRow()
{
    trie* obj = (trie*)malloc(sizeof(trie));
    rep(i,0,26)
    {
        obj->row[i] = NULL;
    }
    return obj;
}

void insert(trie* root, char str[] , int len)
{
    int j = 0;
    trie* ptr = root;
    while(1)
    {
        int i = str[j] - 'a';
        if(ptr->row[i] == NULL)
        {
            break;
        }
        if(j == len)
        {
            break;
        }
        ptr = ptr->row[i];
        j++;
    }
    if(j != len)
    {
        while(j<len)
        {
            int i = str[j++] - 'a';
            ptr->row[i] = addNewRow();
            ptr = ptr->row[i];
        }
    }
    ptr->isEnd = 1;
}

int searchTrie(trie* ptr , char str[] , int len)
{
    rep(i,0,len)
    {
        if(ptr->row[str[i]-'a'] == NULL)
        {
            return 0;
        }
        ptr = ptr->row[str[i]-'a'];
    }
    if(ptr->isEnd)
    {
        return 1;
    }
    return 0;
}

void deleteTrie(trie* ptr , char* str , int len)
{
    if(!searchTrie(ptr , str , len))
    {
        printf("Please enter a valid key\n");
        return;
    }
    trie* ar[len];
    rep(i,0,len)
    {
        ar[i] = ptr;
        ptr = ptr->row[str[i] - 'a'];
    }
    ptr->isEnd = 0;
    for(int i = len-1 ; i >= 0 ; i--)
    {
        if(ar[i]->isEnd)
        {
            return;
        }
        for(int i = 0 ; i < 26 ; i++)
        {
            if(i != str[i]-'a' && ar[i] != NULL)
            {
                return;
            }
        }
        trie* tmp = ar[i];
        ar[i] = NULL;
        free(tmp);
    }
}

void printTrie(trie* ptr , char st[] , int pos)
{
    char aux[30];
    strcpy(aux , st);
    rep(i,0,26)
    {
        if(ptr->row[i] != NULL)
        {
            aux[pos] = i + 'a';
            printTrie(ptr->row[i] , aux , pos + 1);
        }
    }
    if(ptr->isEnd)
    {
        aux[pos] = '\0';
        printf("%s \n" , aux);
    }
}

int main(void) 
{
    trie* root = addNewRow();
    root->isEnd = 1;
    printf("Please enter the number of keys to Insert in the Trie Created : ");
    int n;
    scanf("%d",&n);
    
    printf("Please enter the keys to be inserted : ");
    
    char ch = getchar();
    
    rep(i,0,n)
    {
        char str[30] = "";
        scanf("%s" , str);
        insert(root, str, strlen(str));
    }
    
    char st[30] = "";
    printf("All the keys in Trie after Insertion : \n");
    printTrie(root , st , 0);
    
    printf("Enter the number of keys to Search for : ");
    scanf("%d",&n);

    printf("Enter the keys : ");

    rep(i,0,n)
    {
        char sg[30] = "";
        scanf(" %s",sg);
        
        if(searchTrie(root, sg, strlen(sg)))
            printf("%s key exists in TRIE\n", sg);
        else
            printf("Key does not exist in TRIE\n");
    }
    
    
    
    printf("Enter the number of keys to Delete : ");
    scanf("%d",&n);

    printf("Enter the keys : ");
    
    rep(i,0,n)
    {
        char str[30] = "";
        scanf(" %s", str);
        
        deleteTrie(root , str , strlen(str));
    }
    
    printf("All the keys in TRIE after Deletions : \n");
    printTrie(root , st , 0);
    
	return 0;
}
