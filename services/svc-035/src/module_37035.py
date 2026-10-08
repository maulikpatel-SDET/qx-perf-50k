"""Service module 37035: business logic, no crypto."""


def calculate_total_37035(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37035():
    return 'module 37035 handles orders and invoices'
