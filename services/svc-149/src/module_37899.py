"""Service module 37899: business logic, no crypto."""


def calculate_total_37899(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37899():
    return 'module 37899 handles orders and invoices'
