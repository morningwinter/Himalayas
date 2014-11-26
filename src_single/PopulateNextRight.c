/*
  Binary Tree: Populate the nextRight pointers in each node.
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

static int id = 0;

struct Node {
    int val;
    struct Node* leftChild ;
    struct Node* rightChild ;
    struct Node* nextRight ;
};

void generateTree(int level, struct Node* root)
{

    if (level == 0)
    {
        return;
    }

    struct Node* left = malloc( sizeof(struct Node));
    left->val = id++;
    struct Node* right = malloc( sizeof(struct Node));
    right->val = id++;
    // struct Node* nextRight = NULL;

    root->leftChild = left;
    root->rightChild = right;
    root->nextRight = NULL;

    generateTree(level - 1, left);
    generateTree(level - 1, right);
}


void printTree(struct Node* node)
{
    int level = 0;
    int size = pow(2, level);
    struct Node** nodes = malloc( sizeof(struct Node) * size);

    *nodes = node;
    struct Node* l = node->leftChild;

    while(1)
    {
        level++;
        size = pow(2, level);

        struct Node** tmp_nodes = malloc( sizeof(struct Node) * size);
        struct Node** copy = tmp_nodes;

        // **nodes -> Node
        // *nodes -> Node* -> pointer of a Node.
        // nodes -> pointer of Node pointer.
        while (*nodes)
        {
            int leftVal = -1;
            int rightVal = -1;
            int nextRightVal = -1;

            struct Node* left = (*nodes)->leftChild;
            if (left)
                leftVal = left->val;

            struct Node* right = (*nodes)->rightChild;
            if (right)
                rightVal = right->val;

            struct Node* nextRight = (*nodes)->nextRight;
            if (nextRight)
                nextRightVal = nextRight->val;

            printf("V: %d (%d, %d, %d), ", (**nodes).val, leftVal, rightVal, nextRightVal);
        
            *tmp_nodes = (*nodes)->leftChild;
            tmp_nodes++;
            *tmp_nodes = (*nodes)->rightChild;
            tmp_nodes++;
            nodes++;
        }
        printf("\n\n");
        nodes = copy;

        if(l)
            l = l->leftChild;
        else
            break;
            
    }
}

void populateNextRight(struct Node* parent)
{
    if (!parent->leftChild)
        return;
    struct Node* leftChild = parent->leftChild;
    struct Node* rightChild = parent->rightChild;

    leftChild->nextRight = rightChild;

    if(parent->nextRight)
    {
        rightChild->nextRight = parent->nextRight->leftChild;
    }

    populateNextRight(leftChild);
    populateNextRight(rightChild);
}

int main(int argc, const char* argv[])
{
    int level = 5;
    struct Node* root = malloc( sizeof(struct Node));
    root->val = id++;

    generateTree(5, root);
    printf("count: %d\n", id);

    printTree(root);

    populateNextRight(root);
    printTree(root);
}