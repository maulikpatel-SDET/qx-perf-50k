"""Service module 46901: business logic, no crypto."""


def calculate_total_46901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46901():
    return 'module 46901 handles orders and invoices'
