"""Service module 19823: business logic, no crypto."""


def calculate_total_19823(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19823():
    return 'module 19823 handles orders and invoices'
