"""Service module 27172: business logic, no crypto."""


def calculate_total_27172(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27172():
    return 'module 27172 handles orders and invoices'
