"""Service module 5886: business logic, no crypto."""


def calculate_total_5886(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5886():
    return 'module 5886 handles orders and invoices'
