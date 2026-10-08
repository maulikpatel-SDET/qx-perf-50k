"""Service module 33639: business logic, no crypto."""


def calculate_total_33639(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33639():
    return 'module 33639 handles orders and invoices'
