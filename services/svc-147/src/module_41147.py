"""Service module 41147: business logic, no crypto."""


def calculate_total_41147(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41147():
    return 'module 41147 handles orders and invoices'
