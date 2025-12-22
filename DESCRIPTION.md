# Architecture of Collaborative Modding

## The Idea

The idea of collaborative modding is that one mod can make changes that would normally break other mods, because the collaborative aspect allows the mod to fix anything that it broke for other mods.

It has also been developed in a way that no standards are required to work. The most dominant way compatibility is handled is by settings standards. But standards don't work with interoperability, authority must be centralized, and this often limits mod capability.

There are 2 issues that need to be overcome:

- How will a mod know what it is modifying, when it has been modified by other mods?

- How will the collaborative aspect work?

These are easy to overcome by setting standards (eg. Use Git-style blaming for edits and collaboration), but standards aren't preferable for a project like this.

What is OK to use is some form of symmetrical rule-of-thumb (eg. Assume other mods are incompetent, so don't rely on them or trust them to pick up where you left off if what you're doing is complicated), and this is needed in the final implementation, unless I find a way (unlikely).


## Input

This modding architecture takes an apparatus. This is what you want to mod. It can be anything, although usually, it will be a game's directory tree. 

A version that allows mods for slightly different versions of an apparatus (combined with the format you want it to output) will come eventually, and will also be part of this proof of concept.