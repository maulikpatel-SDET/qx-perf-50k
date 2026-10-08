"""Service module 34328: business logic, no crypto."""


def calculate_total_34328(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34328():
    return 'module 34328 handles orders and invoices'
