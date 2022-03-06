#!/usr/bin/env python3

# Keep the function signature,
# but replace its body with your implementation.
#
# Note that this is the driver function.
# Please write a well-structured implemention by creating other
# functions outside of this one,
# each of which has a designated purpose.
#
# As a good programming practice,
# please do not use any script-level variables that are modifiable.
# This is because those variables live on forever once the script is imported,
# and the changes to them will persist across different invocations
# of the imported functions.

import os
import sys
import zlib


class CommitNode:
    def __init__(self, commit_hash):
        """
        :type commit_hash: str
        """
        self.commit_hash = commit_hash
        self.parents = set()
        self.children = set()


def get_git_path():
    path = os.getcwd()

    while (path != os.path.dirname(path)):
        if (os.path.isdir("%s/.git" % path)):
            return os.path.join(path, ".git")
        else:
            path = os.path.dirname(path)

    sys.exit("Not inside a Git repository")


def get_branches():

    # Go to the directory containing the branches
    git_dir = get_git_path()
    branch_dir = os.path.join(git_dir, "refs", "heads")
    branches = []

    for root_path, dirs, files in os.walk(branch_dir):
        for file in files:
            branch_path = os.path.join(root_path, file)
            branches.append(branch_path[len(branch_dir) + 1:])

    branch_ids = {}

    for branch in branches:
        branch_path = os.path.join(branch_dir, branch)
        branch_id = open(branch_path, "r").read().replace("\n", "")
        branch_ids[branch] = branch_id

    return branch_ids


def get_commit_parents(commit):
    git_path = get_git_path()
    path = os.path.join(git_path, "objects", commit[:2], commit[2:])

    commit_data = zlib.decompress(open(path, "rb").read())
    is_commit = commit_data[:6] == b"commit"

    parents = []
    if is_commit:
        commit_data = commit_data.decode().split("\n")
        for commit in sorted(commit_data):
            commit_type, commit_message = commit[:6], commit[7:]
            if(commit_type == "parent"):
                parents.append(commit_message)

    return parents


def create_graph():
    branches = get_branches()

    graph = {}
    for commit in sorted(branches.values()):
        git_path = get_git_path()
        path = os.path.join(git_path, "objects", commit[:2], commit[2:])

        commit_data = zlib.decompress(open(path, "rb").read())
        is_commit = commit_data[:6] == b"commit"

        if is_commit:
            commits_stack = [commit]

            while(commits_stack != []):
                commit = commits_stack.pop()

                if commit in graph:
                    node = graph[commit]
                else:
                    node = CommitNode(commit)

                parents = get_commit_parents(commit)
                for parent in sorted(parents):
                    node.parents.add(parent)

                    if parent in graph:
                        parent_node = graph[parent]
                    else:
                        parent_node = CommitNode(parent)
                        commits_stack.append(parent)

                    parent_node.children.add(commit)
                    graph[parent] = parent_node

                graph[commit] = node

    return graph


def create_topo_order():
    graph = create_graph()
    root_commits = []

    topo_order = []
    visited = set()

    for commit in sorted(graph):
        if len(graph[commit].parents) == 0:
            root_commits.append(commit)

    for root in root_commits:
        if root not in visited:
            commits_stack = [root]

        while (commits_stack != []):
            commit = commits_stack.pop()

            if commit not in visited:
                if len(graph[commit].parents) >= 2:

                    parent_stack = []
                    parent_visited = []

                    for parent in sorted(graph[commit].parents):
                        if parent not in visited:
                            parent_stack = [parent]

                            visited.add(parent)
                            while (parent_stack != []):
                                parent_commit = parent_stack.pop()

                                for parent in sorted(
                                        graph[parent_commit].parents):
                                    if parent not in visited:
                                        parent_stack.append(parent)

                                    parent_visited.append(parent_commit)
                                    visited.add(parent_commit)

                    for node in reversed(parent_visited):
                        topo_order.append(node)

                for child in sorted(graph[commit].children):
                    if child not in visited:
                        commits_stack.append(child)

                topo_order.append(commit)
                visited.add(commit)

    return topo_order


def print_topo_order_graph():
    branches = get_branches()
    graph = create_graph()
    topo_order = create_topo_order()[::-1]

    is_sticky = False
    for i in range(len(topo_order)):
        commit = topo_order[i]
        node = graph[commit]

        if is_sticky:
            is_sticky = False
            sticky_commits = "="

            for child in sorted(node.children):
                sticky_commits += "%s " % child
            print(sticky_commits.rstrip())

        print(commit, end="")

        for branch in sorted(branches.keys()):
            if branches[branch] == commit:
                output = " " + branch
                print(output, end="")

        print()

        if i != len(topo_order) - 1:
            next_node = graph[topo_order[i + 1]]

            if commit not in next_node.children:
                output = ""

                for parent in sorted(node.parents):
                    output += "%s " % parent

                print(output.strip() + "=", end="\n\n")
                is_sticky = True


def topo_order_commits():
    return print_topo_order_graph()


if __name__ == "__main__":
    topo_order_commits()
