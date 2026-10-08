"""Service module 15075: business logic, no crypto."""


def calculate_total_15075(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15075():
    return 'module 15075 handles orders and invoices'
