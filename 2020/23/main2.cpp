#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

struct Node {
    Node* next;
    int val;
};

// Indexed by (val - 1)
typedef vector<Node*> Int2Node;

void Print(Node* current) {
    std::stringstream ss;
    ss << "cups:";

    Node* n = current;
    do {
        if (n == current) {
            ss << " (" << n->val << ") ";
        } else {
            ss << "  " << n->val << "  ";
        }
        n = n->next;
    } while (n != current);

    cout << ss.str() << endl;
};


Node* BuildList(const vector<int>& input, Int2Node* int2node) {
    // Memory management is for the weak...
    Node* prev = new Node();
    prev->val = input[0];
    int2node->operator[](prev->val - 1) = prev;
    Node* current = prev;
    for (int i = 1; i < input.size(); ++i) {
        Node* node = new Node();
        node->val = input[i];
        int2node->operator[](node->val - 1) = node;
        prev->next = node;
        prev = node;
    }
    prev->next = current;
    return current;
}

// Naive version
Node* FindDestination(Node* current) {
    int label = current->val;
    while (true) {
        label--;
        if (label <= 0) {
            // TODO: Won't work with 1 mllion inputs
            label = 9;
        }
        Node* first = current;
        do {
            if (current->val == label) {
                return current;
            }
            current = current->next;
        } while (current != first);
    }
}

// Lookup table optimized version
Node* FindDestination2(Node* current, int p1, int p2, int p3, const Int2Node& int2node) {
    int label = current->val;
    while (true) {
        label--;
        if (label <= 0) {
            label = int2node.size();
        }
        if (label != p1 && label != p2 && label != p3) {
            break;
        }
    }
    //cout << "label = " << label << endl;
    Node* r = int2node[label - 1];
    if (!r) {
        cout << "Invalid missing node for label=" << label << endl;
        abort();
    }
    return r;
}

Node* Move(Node* current, const Int2Node& int2node, bool verbose=false) {
    if (verbose) {
        Print(current);
    }
    // Pick sublist of 3 nodes, p = first, n = last
    Node* p = current->next;
    Node* n = p;
    for (int i = 0; i < 2; ++i) {
        n = n->next;
    }

    // Print 'picks up'
    if (verbose) {
        cout << "pick up: ";
        Node* tmp = p;
        do {
            cout << tmp->val << ", ";
            tmp = tmp->next;
        } while (tmp != n->next);
        cout << endl;
    }

    // "Remove" the 3
    current->next = n->next;
    // Select destination cup
    //Node* dest = FindDestination(current);
    Node* dest = FindDestination2(current, p->val, p->next->val, p->next->next->val, int2node);

    if (verbose) {
        cout << "destination: " << dest->val << endl;
    }
    // Place immediately clockwise of destination
    Node* dest_next = dest->next;
    //cout << "p->val=" << p->val << ", n->val=" << n->val << endl;
    dest->next = p;
    n->next = dest_next;
    //Print(current);
    return current->next;
}

int main () {
    //vector<int> input = {3, 8, 9, 1, 2, 5, 4, 6, 7};
    vector<int> input = {4, 1, 8, 9, 7, 6, 2, 3, 5};

    for (int i = input.size() + 1; i <= 1000000; ++i) {
        input.push_back(i);
    }
    Int2Node int2node(input.size(), nullptr);

    //vector<int> input = {4, 1, 8, 9, 7, 6, 2, 3, 5};

    const bool verbose = false;

    Node* current = BuildList(input, &int2node);
    //const int nmoves = 100;
    const int nmoves = 10000000;

    for (int i = 1; i < 1 + nmoves; ++i) {
        if (verbose || i % 10000 == 0) {
            cout << endl << "-- move " << i << " --" << endl;
        }
        current = Move(current, int2node, verbose);
    }

    if (verbose) {
        cout << endl << "-- final --" << endl;
        Print(current);
    }

    // Print solution (starting at cup labeled 1) for part 1
    if (false)
    {
        Node* one = current;
        while (one->val != 1) {
            one = one->next;
        }
        Node* n = one->next;
        cout << "result" << endl;
        while (n != one) {
            cout << n->val;
            n = n->next;
        }
        cout << endl;
    } else {
        // Part 2: two label just clockwise of one
        Node* one = current;
        while (one->val != 1) {
            one = one->next;
        }
        cout << "result" << endl;
        cout << one->next->val << endl;
        cout << one->next->next->val << endl;

        cout << "mult: " << static_cast<int64_t>(one->next->val) * static_cast<int64_t>(one->next->next->val) << endl;
    }

    return 0;
}
