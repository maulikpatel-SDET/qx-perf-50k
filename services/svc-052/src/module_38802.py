"""Service module 38802: business logic, no crypto."""


def calculate_total_38802(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38802():
    return 'module 38802 handles orders and invoices'
