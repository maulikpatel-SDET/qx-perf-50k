"""Service module 46328: business logic, no crypto."""


def calculate_total_46328(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46328():
    return 'module 46328 handles orders and invoices'
