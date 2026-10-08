"""Service module 44857: business logic, no crypto."""


def calculate_total_44857(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44857():
    return 'module 44857 handles orders and invoices'
