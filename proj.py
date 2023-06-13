from abc import ABC, abstractmethod


class Material(ABC):
    def __init__(self, strength):
        self.strength = strength


class Wood(Material):
    def __init__(self, strength):
        super().__init__(strength)


class Metal(Material):
    def __init__(self, strength, purity):
        super().__init__(strength)
        self.purity = purity


class Gemstone(Material):
    def __init__(self, strength, magic_power):
        super().__init__(strength)
        self.magic_power = magic_power

class Maple(Wood):
    def __init__(self, strength=5):
        super().__init__(strength)


class Ash(Wood):
    def __init__(self, strength=3):
        super().__init__(strength)


class Oak(Wood):
    def __init__(self, strength=4):
        super().__init__(strength)


class Bronze(Metal):
    def __init__(self, strength=3, purity=1.3):
        super().__init__(strength, purity)


class Iron(Metal):
    def __init__(self, strength=6, purity=1.1):
        super().__init__(strength, purity)


class Steel(Metal):
    def __init__(self, strength=10, purity=1.8):
        super().__init__(strength, purity)


class Ruby(Gemstone):
    def __init__(self, strength=1, magicPower=1.8):
        super().__init__(strength, magicPower)


class Sapphire(Gemstone):
    def __init__(self, strength=1.2, magicPower=1.6):
        super().__init__(strength, magicPower)


class Emerald(Gemstone):
    def __init__(self, strength=1.6, magicPower=1.1):
        super().__init__(strength, magicPower)


class Diamond(Gemstone):
    def __init__(self, strength=2.1, magicPower=2.2):
        super().__init__(strength, magicPower)


class Amethyst(Gemstone):
    def __init__(self, strength=1.8, magicPower=3.2):
        super().__init__(strength, magicPower)


class Onyx(Gemstone):
    def __init__(self, strength=0.1, magicPower=4.6):
        super().__init__(strength, magicPower)

class Weapon:
    def __init__(self, name, damage, primary_material, catalyst_material):
        self.name = name
        self.damage = damage
        self.primary_material = primary_material
        self.catalyst_material = catalyst_material
        self.enchanted = False
        self.enchantment = None

    def attack(self):
        return f"The {self.name} attacks for {self.damage} damage."

    def add_enchantment(self, enchantment):
        self.enchanted = True
        self.enchantment = enchantment

    def remove_enchantment(self):
        self.enchanted = False
        self.enchantment = None


class Workshop:
    def __init__(self):
        self.enchanter = Enchanter()
        self.forge = Forge()
        self.weapons = []
        self.enchantments = []
        self.materials = {}

    def addMaterial(self, material_name, quantity):
        if material_name in self.materials:
            self.materials[material_name] += quantity
        else:
            self.materials[material_name] = quantity

    def addWeapon(self, weapon):
        self.weapons.append(weapon)

    def removeWeapon(self, weapon):
        self.weapons.remove(weapon)

    def add_enchantment(self, enchantment):
        self.enchantments.append(enchantment)

    def remove_enchantment(self, enchantment):
        self.enchantments.remove(enchantment)

    def displayWeapons(self):
        for weapon in self.weapons:
            if weapon.enchanted:
                print(f"The {weapon.name} is imbued with a {weapon.enchantment.useEffect()}. {weapon.attack()}")
            else:
                print(f"The {weapon.name} is not enchanted. {weapon.attack()}")

    def displayEnchantments(self):
        for enchantment in self.enchantments:
            print(f"A {enchantment.name} enchantment is stored in the workshop.")

    def displayMaterials(self):
        for material, count in self.materials.items():
            print(f"{material}: {count} remaining.")


class Crafter(ABC):
    @abstractmethod
    def craft(self):
        pass

    @abstractmethod
    def disassemble(self):
        pass


class Forge(Crafter):
    def __init__(self):
        self.materials = {}

    def craft(self, name, damage, primary_material, catalyst_material):
        weapon = Weapon(name, damage, primary_material, catalyst_material)
        return weapon

    def disassemble(self, weapon):
        return weapon

    def update_materials(self, primary_material, catalyst_material):
        self.materials[primary_material.__class__.__name__] -= 1
        self.materials[catalyst_material.__class__.__name__] -= 1
        self.materials[primary_material.__class__.__name__] += 1
        self.materials[catalyst_material.__class__.__name__] += 1


class Enchanter(Crafter):
    def __init__(self):
        self.materials = {}
        self.recipes = {
            "Holy": "pulses a blinding beam of light",
            "Lava": "melts the armor off an enemy",
            "Pyro": "applies a devastating burning effect",
            "Darkness": "binds the enemy in dark vines",
            "Cursed": "causes the enemy to become crazed",
            "Hydro": "envelops the enemy in a suffocating bubble",
            "Venomous": "afflicts a deadly, fast-acting toxin"
        }

    def craft(self, name, primary_material, catalyst_material):
        enchantment = Enchantment(name, primary_material, catalyst_material)
        enchantment.set_effect(self.recipes[name])
        return enchantment

    def disassemble(self, enchantment):
        return enchantment

    def enchant(self, weapon, enchantment_name, enchantment):
        weapon.enchanted




# Create a workshop, forge, enchanter.
workshop = Workshop()
# Create a set of materials and lists for testing.
materials = [Maple(), Oak(), Ash(), Bronze(), Iron(), Steel(),
Ruby(), Sapphire(), Emerald(), Diamond(), Amethyst(), Onyx()]
weaponBlueprints = {
"Sword": [Steel(), Maple()],
"Shield": [Bronze(), Oak()],
"Axe": [Iron(), Ash()],
"Scythe": [Steel(), Ash()],
"Bow": [Oak(), Maple()],
"Wand": [Ash(), Oak()],
"Staff": [Bronze(), Maple()],
"Dagger": [Bronze(), Bronze()]}
enchantmentBlueprints = {
"Holy": [Diamond(), Diamond()],
"Lava": [Ruby(), Onyx()],
"Pyro": [Ruby(), Diamond()],
"Darkness": [Onyx(), Amethyst()],
"Cursed": [Onyx(), Onyx()],
"Hydro": [Sapphire(), Emerald()],
"Venomous": [Emerald(), Amethyst()],
"Earthly": [Emerald(), Emerald()]}
enchantedWeapons = ["Holy Greatsword", "Molten Defender", "Berserker Axe", "Soul Eater",
"Twisted Bow", "Wand of the Deep", "Venemous Battlestaff"]
# Adds a number of materials to use for crafting.
for material in materials:
    if isinstance(material, Wood):
        workshop.addMaterial(material.__class__.__name__, 20)
    elif isinstance(material, Metal):
        workshop.addMaterial(material.__class__.__name__, 10)
    else:
        workshop.addMaterial(material.__class__.__name__, 5)
print("--------------------------------Material Store--------------------------------")
print(workshop.displayMaterials())

# Crafts the following: Sword, Shield, Axe, Scythe, Bow, Wand and Staff weapons.
for weapon, materials in weaponBlueprints.items():
    craftedWeapon = workshop.forge.craft(
        weapon, materials[0], materials[1], workshop.materials)
    workshop.addWeapon(craftedWeapon)
# Disassemble the extra weapon.
workshop.removeWeapon(workshop.forge.disassemble(
    workshop.weapons[7], workshop.materials))
print("------------------------------------Armoury-----------------------------------")
print(workshop.displayWeapons())
# Crafts the following: Holy, Lava, Pyro, Darkness, Cursed, Hydro and Venomous enchantments.
for enchantment, materials in enchantmentBlueprints.items():
    craftedEnchantment = workshop.enchanter.craft(
        enchantment, materials[0], materials[1], workshop.materials)
    workshop.addEnchantment(craftedEnchantment)
# Disassemble the extra enchantment.
workshop.removeEnchantment(workshop.enchanter.disassemble(
    workshop.enchantments[7], workshop.materials))
print("------------------------------------Enchantments------------------------------------")
print(workshop.displayEnchantments())
print("-----------------------------------Material Store-----------------------------------")
print(workshop.displayMaterials())
# Enchant the following weapons: Sword, Shield, Axe, Scythe, Bow, Wand and Staff.
for i in range(len(enchantedWeapons)):
    workshop.enchanter.enchant(
        workshop.weapons[i], enchantedWeapons[i], workshop.enchantments[i])
print("-----------------------------------Enchanted Armoury----------------------------------")
print(workshop.displayWeapons())
