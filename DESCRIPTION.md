# Architecture of Collaborative Modding

## The Idea

The idea of collaborative modding is that one mod can make changes that would normally break other mods, because the collaborative aspect allows the mod to fix anything that it broke for other mods.

It has also been developed in a way that no standards are required to work. The most dominant way compatibility is handled is by setting standards. But standards don't work with interoperability, authority must be centralized, and this often limits mod capability.

There are 2 issues that need to be overcome:

- How will a mod know what it is modifying, when it has been modified by other mods?

- How will a mod be able to do things that require accomodation?

These are easy to overcome by setting standards (eg. Use Git-style blaming for edits and collaboration), but standards aren't preferable for a project like this.

What is OK to use is some form of symmetrical rule-of-thumb (eg. Don't rely on other mods or trust them to handle their implentation properly if what you're doing will throw them off), and this is needed in the final implementation, unless I find a way to avoid it (unlikely).

## Architecture and version

As of now, this documentation covers a modder that allows for modding a single apparatus. It lets each mod modify it and correct for any imcompatibilities it causes. Read the section below for its flaws. With work, the abilities of this modder will increase. The goal is to have a modder that doesn't allow mods to throttle the ability for the modder to work, that can support mods made for different procedures to generate an apparatus and parse it (with compatibility layers that are made by programmers, that don't need to treat any method as the "main" method), has a sandboxed variant that mitigates remote code execution vulnerabilities for *specific untrusted mods*, and works inside of other modders/modloaders.

Commits with this message in it are using a beta version intended to draft communication before implementing properly.

## Input

This modding architecture takes an apparatus. This is what you want to mod. It can be anything, although usually, it will be a game installation's directory tree. 

A version that allows mods for slightly different versions of an apparatus (combined with the format you want it to output) will come eventually, and will also be part of this proof of concept.

## Operation

The first mod receives the original apparatus and changes it, and sets event handlers for when others modify it. Then, the second mod sees the slightly modified version and adds its own modifcation, and setting event handlers. This continues until completion, then whatever mods set an event handler get to modify the apparatus again.

## Limitations (as of now)

- Each mod has its own idea of how basic modifications work, and enforces it, which may cause problems

- Any mod is able to throttle or supress the ability of the modder to work

- All the mods must be designed for a single version of the apparatus. If the apparatus is generated and parsed in a slightly different method, all mods will be incompatible with that method unless specifically designed


## Why this will be better than a naive system

This largely depends on what the modding system is. This documentation will run through a few examples.

### Tynker, Minecraft Bedrock mods, or similar

The way these work is by providing a set of ways to modify the way Minecraft behaves. Even though this has full compatibility, it is very limiting in what you can do. For example, if you want to add a thirst bar, you can't. It also is designed for a single game, and has a central authority controlling it.

### Fabric or similar

Fabric allows you to hook into the code by adding places to execute code. However, you cannot do anything that makes it hard for other mods to load (eg. high-quality skins like on Bedrock). It is also designed for a single game (even though it may not be necessary).

### Bukkit, Forge, or similar

These just run on top of Minecraft, using APIs that were injected by developers. It involves a central authority, is designed for a specific game, and is limiting. The only reason why this is different from Tynker, Bedrock mods, or similar is that these have an API that is used by running code instead of using a static, beginner-facing generic creation.


## What this modder will NOT be

- The mod loader will never give 100% compatibility unless an arbitrator specifically combines 2 mods. While the architecture permits this, any 2 mods cannot be expected for certain to account for eachother

- This modder will not be adapted for any game

- This modder will not make use of standards. Even it can fit into another mod system.

- This modder will not have a clean menu inside of the apparatus's app content (if applicable) by default. However, mods can add this, and it is encouraged, as the game files themselves at install-time would also make use of the system.
