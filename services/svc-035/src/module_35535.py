"""Service module 35535: business logic, no crypto."""


def calculate_total_35535(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35535():
    return 'module 35535 handles orders and invoices'
