"""Service module 44229: business logic, no crypto."""


def calculate_total_44229(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44229():
    return 'module 44229 handles orders and invoices'
