"""Service module 34248: business logic, no crypto."""


def calculate_total_34248(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34248():
    return 'module 34248 handles orders and invoices'
