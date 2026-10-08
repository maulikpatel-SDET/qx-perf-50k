"""Service module 20075: business logic, no crypto."""


def calculate_total_20075(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20075():
    return 'module 20075 handles orders and invoices'
