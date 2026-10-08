"""Service module 4274: business logic, no crypto."""


def calculate_total_4274(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4274():
    return 'module 4274 handles orders and invoices'
