"""Service module 19809: business logic, no crypto."""


def calculate_total_19809(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19809():
    return 'module 19809 handles orders and invoices'
