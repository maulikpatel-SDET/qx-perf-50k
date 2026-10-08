"""Service module 13762: business logic, no crypto."""


def calculate_total_13762(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13762():
    return 'module 13762 handles orders and invoices'
