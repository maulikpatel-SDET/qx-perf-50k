"""Service module 44248: business logic, no crypto."""


def calculate_total_44248(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44248():
    return 'module 44248 handles orders and invoices'
