#include <stdio.h>
#include <stdlib.h>

typedef struct TreeNode
{
    struct TreeNode *left;
    struct TreeNode *right;
    char key;
} TreeNode;

TreeNode *tree;

TreeNode *createNode(char data)
{
    TreeNode *newNode = (TreeNode *)malloc(sizeof(TreeNode));
    newNode->key = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

TreeNode *searchTree(TreeNode *node, char data)
{
    if (node == NULL)
        return NULL;
    if (node->key == data)
        return node;
    else
    {
        TreeNode *tmp = searchTree(node->left, data);
        if (tmp != NULL)
            return tmp;
        return searchTree(node->right, data);
    }
}

void inorder(TreeNode *root)
{
    if (root)
    {
        inorder(root->left);
        printf("%c", root->key);
        inorder(root->right);
    }
}

void postorder(TreeNode *root)
{
    if (root)
    {
        postorder(root->left);
        postorder(root->right);
        printf("%c", root->key);
    }
}

void preorder(TreeNode *root)
{
    if (root)
    {
        printf("%c", root->key);
        preorder(root->left);
        preorder(root->right);
    }
}

int main(void)
{
    int n;
    scanf("%d", &n);
    getchar();

    for (int i = 0; i < n; i++)
    {
        char x, y, z;
        TreeNode *root, *left, *right;

        scanf("%c %c %c", &x, &y, &z);
        getchar();

        root = searchTree(tree, x);
        if (root == NULL)
        {
            root = createNode(x);
            if (i == 0)
                tree = root;
        }
        if (y != '.')
        {
            left = createNode(y);
            root->left = left;
        }
        if (z != '.')
        {
            right = createNode(z);
            root->right = right;
        }
    }
    postorder(tree);
    printf("\n");
    preorder(tree);
    printf("\n");
    inorder(tree);
    printf("\n");

    return 0;
}