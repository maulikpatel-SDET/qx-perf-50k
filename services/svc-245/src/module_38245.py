"""Service module 38245: business logic, no crypto."""


def calculate_total_38245(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38245():
    return 'module 38245 handles orders and invoices'
