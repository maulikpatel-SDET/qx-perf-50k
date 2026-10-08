"""Service module 25423: business logic, no crypto."""


def calculate_total_25423(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25423():
    return 'module 25423 handles orders and invoices'
