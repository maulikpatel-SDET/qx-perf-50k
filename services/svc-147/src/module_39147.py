"""Service module 39147: business logic, no crypto."""


def calculate_total_39147(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39147():
    return 'module 39147 handles orders and invoices'
