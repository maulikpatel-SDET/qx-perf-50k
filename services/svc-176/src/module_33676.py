"""Service module 33676: business logic, no crypto."""


def calculate_total_33676(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33676():
    return 'module 33676 handles orders and invoices'
