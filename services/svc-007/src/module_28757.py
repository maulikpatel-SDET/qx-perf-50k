"""Service module 28757: business logic, no crypto."""


def calculate_total_28757(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28757():
    return 'module 28757 handles orders and invoices'
