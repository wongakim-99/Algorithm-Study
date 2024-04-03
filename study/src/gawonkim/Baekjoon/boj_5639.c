#include <stdio.h>
#include <stdlib.h>
typedef struct TreeNode
{
    struct TreeNode *left;
    struct TreeNode *right;
    int key;
} TreeNode;

TreeNode *createNode(int data)
{
    TreeNode *newNode = (TreeNode *)malloc(sizeof(TreeNode));
    newNode->key = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

TreeNode *insertNode(TreeNode *node, int data)
{
    if (node == NULL)
        return createNode(data);
    else if (node->key > data)
        node->left = insertNode(node->left, data);
    else if (node->key < data)
        node->right = insertNode(node->right, data);
    return node;
}

void postorder(TreeNode *root)
{
    if (root)
    {
        postorder(root->left);
        postorder(root->right);
        printf("%d\n", root->key);
    }
}

int main(void)
{
    int input;
    TreeNode *root = NULL;
    while (scanf("%d", &input) != EOF)
        root = insertNode(root, input);

    postorder(root);

    return 0;
}