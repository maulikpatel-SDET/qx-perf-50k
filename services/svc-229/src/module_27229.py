"""Service module 27229: business logic, no crypto."""


def calculate_total_27229(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27229():
    return 'module 27229 handles orders and invoices'
