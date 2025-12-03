This file is a merged representation of a subset of the codebase, containing specifically included files, combined into a single document by Repomix.
The content has been processed where content has been compressed (code blocks are separated by ⋮---- delimiter).

# File Summary

## Purpose
This file contains a packed representation of a subset of the repository's contents that is considered the most important context.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Only files matching these patterns are included: src, docs/mkdoc
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Content has been compressed - code blocks are separated by ⋮---- delimiter
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
src/
  flowerpower/
    cfg/
      pipeline/
        __init__.py
        adapter.py
        builder_adapter.py
        builder_executor.py
        builder.py
        run.py
      project/
        __init__.py
        adapter.py
      __init__.py
      base.py
      exceptions.py
    cli/
      __init__.py
      cfg.py
      pipeline.py
      utils.py
    pipeline/
      __init__.py
      base.py
      config_manager.py
      executor.py
      io.py
      lifecycle_manager.py
      manager.py
      pipeline.py
      registry.py
      visualizer.py
    plugins/
      io/
        __init__.py
    settings/
      __init__.py
      executor.py
      general.py
      hamilton.py
      logging.py
      retry.py
    utils/
      __init__.py
      adapter.py
      callback.py
      config.py
      env.py
      executor.py
      filesystem.py
      logging.py
      misc.py
      open_telemetry.py
      security.py
      templates.py
      yaml_env.py
    __init__.py
    flowerpower.py
```

# Files

## File: src/flowerpower/settings/executor.py
````python
# EXECUTOR
EXECUTOR = os.getenv("FP_EXECUTOR", "threadpool")
EXECUTOR_MAX_WORKERS = int(
EXECUTOR_NUM_CPUS = int(os.getenv("FP_EXECUTOR_NUM_CPUS", os.cpu_count() or 1))
````

## File: src/flowerpower/settings/general.py
````python
PIPELINES_DIR = os.getenv("FP_PIPELINES_DIR", "pipelines")
CONFIG_DIR = os.getenv("FP_CONFIG_DIR", "conf")
HOOKS_DIR = os.getenv("FP_HOOKS_DIR", "hooks")
CACHE_DIR = os.getenv("FP_CACHE_DIR", "~/.flowerpower/cache")
````

## File: src/flowerpower/settings/hamilton.py
````python
# HAMILTON
HAMILTON_MAX_LIST_LENGTH_CAPTURE = int(
HAMILTON_MAX_DICT_LENGTH_CAPTURE = int(
HAMILTON_CAPTURE_DATA_STATISTICS = bool(
⋮----
HAMILTON_AUTOLOAD_EXTENSIONS = int(os.getenv("HAMILTON_AUTOLOAD_EXTENSIONS", 0))
HAMILTON_TELEMETRY_ENABLED = bool(os.getenv("HAMILTON_TELEMETRY_ENABLED", False))
HAMILTON_API_URL = os.getenv("HAMILTON_API_URL", "http://localhost:8241")
HAMILTON_UI_URL = os.getenv("HAMILTON_UI_URL", "http://localhost:8242")
````

## File: src/flowerpower/settings/retry.py
````python
# RETRY
MAX_RETRIES = int(os.getenv("FP_MAX_RETRIES", 1))
RETRY_DELAY = float(os.getenv("FP_RETRY_DELAY", 1.0))
JITTER_FACTOR = float(os.getenv("FP_JITTER_FACTOR", 0.1))
````

## File: src/flowerpower/utils/open_telemetry.py
````python
# If you wanted to use another OpenTelemetry destination such as the open-source Jaeger,
# setup the container locally and use the following code
⋮----
# Add more open telemetry exporters here
⋮----
jaeger_exporter = JaegerExporter(
⋮----
agent_host_name=host,  # Replace with your Jaeger agent host
agent_port=port,  # Replace with your Jaeger agent port
⋮----
span_processor = SimpleSpanProcessor(jaeger_exporter)
provider = TracerProvider(
````

## File: src/flowerpower/utils/templates.py
````python
PIPELINE_PY_TEMPLATE = """# FlowerPower pipeline {name}.py
⋮----
HOOK_TEMPLATE__MQTT_BUILD_CONFIG = '''
````

## File: src/flowerpower/cfg/pipeline/builder_adapter.py
````python
"""
Adapter builder for RunConfig.
"""
⋮----
class AdapterBuilder
⋮----
"""Builder for creating WithAdapterConfig objects."""
⋮----
def __init__(self, adapter_config: Optional[WithAdapterConfig] = None)
⋮----
"""Initialize the AdapterBuilder.
        
        Args:
            adapter_config: Initial adapter configuration to build upon.
        """
⋮----
def enable_hamilton_tracker(self, enabled: bool = True, **kwargs) -> "AdapterBuilder"
⋮----
"""Enable or disable Hamilton tracker adapter.
        
        Args:
            enabled: Whether to enable the adapter
            **kwargs: Additional configuration options
            
        Returns:
            Self for method chaining
        """
⋮----
def enable_mlflow(self, enabled: bool = True, **kwargs) -> "AdapterBuilder"
⋮----
"""Enable or disable MLflow adapter.
        
        Args:
            enabled: Whether to enable the adapter
            **kwargs: Additional configuration options
            
        Returns:
            Self for method chaining
        """
⋮----
def enable_ray(self, enabled: bool = True, **kwargs) -> "AdapterBuilder"
⋮----
"""Enable or disable Ray adapter.
        
        Args:
            enabled: Whether to enable the adapter
            **kwargs: Additional configuration options
            
        Returns:
            Self for method chaining
        """
⋮----
def enable_opentelemetry(self, enabled: bool = True, **kwargs) -> "AdapterBuilder"
⋮----
"""Enable or disable OpenTelemetry adapter.
        
        Args:
            enabled: Whether to enable the adapter
            **kwargs: Additional configuration options
            
        Returns:
            Self for method chaining
        """
⋮----
def enable_progressbar(self, enabled: bool = True, **kwargs) -> "AdapterBuilder"
⋮----
"""Enable or disable progress bar adapter.
        
        Args:
            enabled: Whether to enable the adapter
            **kwargs: Additional configuration options
            
        Returns:
            Self for method chaining
        """
⋮----
def enable_future(self, enabled: bool = True, **kwargs) -> "AdapterBuilder"
⋮----
"""Enable or disable future adapter.
        
        Args:
            enabled: Whether to enable the adapter
            **kwargs: Additional configuration options
            
        Returns:
            Self for method chaining
        """
⋮----
def with_adapter_config(self, adapter_name: str, config: dict[str, Any]) -> "AdapterBuilder"
⋮----
"""Set configuration for a specific adapter.
        
        Args:
            adapter_name: Name of the adapter
            config: Configuration dictionary
            
        Returns:
            Self for method chaining
        """
⋮----
def build(self) -> WithAdapterConfig
⋮----
"""Build the final WithAdapterConfig object.
        
        Returns:
            Fully configured WithAdapterConfig object
        """
⋮----
def get_adapter_configs(self) -> dict[str, dict[str, Any]]
⋮----
"""Get the collected adapter configurations.
        
        Returns:
            Dictionary of adapter configurations
        """
````

## File: src/flowerpower/cfg/exceptions.py
````python
"""
Custom exceptions for the cfg module.
"""
⋮----
class ConfigError(Exception)
⋮----
"""Base exception for configuration-related errors."""
⋮----
class ConfigLoadError(ConfigError)
⋮----
"""Exception raised when configuration loading fails."""
⋮----
def __init__(self, message: str, path: Optional[str] = None, original_error: Optional[Exception] = None)
⋮----
class ConfigSaveError(ConfigError)
⋮----
"""Exception raised when configuration saving fails."""
⋮----
class ConfigValidationError(ConfigError)
⋮----
"""Exception raised when configuration validation fails."""
⋮----
def __init__(self, message: str, field: Optional[str] = None, value: Any = None)
⋮----
class ConfigSecurityError(ConfigError)
⋮----
"""Exception raised for security-related configuration errors."""
⋮----
def __init__(self, message: str, details: Optional[Dict[str, Any]] = None)
⋮----
class ConfigPathError(ConfigSecurityError)
⋮----
"""Exception raised for path-related security errors."""
⋮----
def __init__(self, message: str, path: Optional[str] = None)
````

## File: src/flowerpower/pipeline/__init__.py
````python
__all__ = [
````

## File: src/flowerpower/plugins/io/__init__.py
````python

````

## File: src/flowerpower/settings/__init__.py
````python
# flake8: noqa
````

## File: src/flowerpower/settings/logging.py
````python
# LOGGING
LOG_LEVEL = os.getenv("FP_LOG_LEVEL", "CRITICAL")
````

## File: src/flowerpower/utils/callback.py
````python
# Configure a logger. In a real application, you might get this from a central logging config.
# To see the debug logs from the decorator, set the logging level:
# logging.basicConfig(level=logging.DEBUG)
⋮----
def _add_exception_to_simple_callback(callback_fn: Callable, context_exception: Exception, cb_args: list, cb_kwargs: Dict[str, Any])
⋮----
"""Add exception to simple callback arguments."""
⋮----
sig = inspect.signature(callback_fn)
⋮----
first_param = next(iter(sig.parameters.values()))
⋮----
def _parse_tuple_callback_args(callback_info: tuple, cb_args: list, cb_kwargs: Dict[str, Any])
⋮----
"""Parse args and kwargs from tuple callback info."""
callback_fn = callback_info[0]
⋮----
# Args: callback_info[1]
⋮----
# Kwargs: callback_info[2]
⋮----
def _add_exception_to_tuple_callback(callback_fn: Callable, context_exception: Exception, cb_kwargs: Dict[str, Any])
⋮----
"""Add exception to tuple callback kwargs if accepted."""
⋮----
def _prepare_callback_details(callback_info: Any, context_exception: Exception = None) -> tuple[Callable | None, tuple, Dict[str, Any]]
⋮----
"""Prepare callback function and arguments for execution."""
⋮----
callback_fn = None
cb_args = []
cb_kwargs = {}
⋮----
callback_fn = callback_info
⋮----
def _execute_callback(callback_info: Any, context_exception: Exception = None)
⋮----
"""
    Helper to execute a callback.
    The callback_info can be a callable, or a tuple (callable, args_tuple, kwargs_dict).
    If context_exception is provided (for on_failure), it can be passed to the callback.
    """
⋮----
callback_name = getattr(callback_fn, "__name__", str(callback_fn))
⋮----
callback_name_err = getattr(callback_fn, "__name__", str(callback_fn))
⋮----
def run_with_callback(on_success: Any = None, on_failure: Any = None)
⋮----
"""
    A Python decorator that executes a function within a try-except-finally block,
    allowing for `on_success` and `on_failure` callbacks.

    The `on_success` and `on_failure` arguments can be:
    1. A callable: `my_callback_func`
       - If `on_failure` is a simple callable that accepts one argument or an
         `exception` keyword argument, the caught exception will be passed.
    2. A tuple: `(my_callback_func, (arg1, arg2), {"kwarg1": val1})`
       - The args tuple and kwargs dict are optional (can be `None` or empty).
       - If `on_failure` is used and an exception occurs, the exception instance
         will be passed as a keyword argument `exception` to the failure callback,
         provided the callback accepts it and it's not already in the user-supplied kwargs.

    The decorated function's return value is returned if successful.
    If an exception occurs in the decorated function, it is re-raised after
    the `on_failure` callback is attempted.
    """
⋮----
def decorator(func: Callable) -> Callable
⋮----
@functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any
⋮----
success_flag = False
result_value = None
caught_exception = None
⋮----
result_value = func(*args, **kwargs)
success_flag = True
⋮----
caught_exception = e
# The original exception will be re-raised after the finally block.
⋮----
# logger.debug(f"Executing on_success callback for {func.__name__}")
⋮----
# logger.debug(f"Executing on_failure callback for {func.__name__}")
````

## File: src/flowerpower/utils/env.py
````python
"""
Environment overlay utilities for FlowerPower.

Features:
- Parse namespaced env vars into nested dicts using double-underscore separators.
- Support global FP_* shims (e.g., FP_LOG_LEVEL) and namespaced forms
  (FP_PROJECT__..., FP_PIPELINE__...).
- Coerce scalar types (int, float, bool) and JSON objects/arrays for rich values.
- Merge overrides into msgspec-based config structs with clear precedence.
"""
⋮----
def _coerce_value(raw: str) -> Any
⋮----
s = raw.strip()
# JSON object/array/bool/null/number
⋮----
# Strict bools
low = s.lower()
⋮----
# Int
⋮----
# Float
⋮----
# Comma-list fallback (strings)
⋮----
def _set_nested(dct: dict, path: list[str], value: Any) -> None
⋮----
cur = dct
⋮----
cur = cur[key]
⋮----
def parse_env_overrides(env: Mapping[str, str] | None = None, prefix: str = "FP_") -> dict
⋮----
"""Parse env vars into nested overrides dict.

    Supports keys like:
    - FP_PROJECT__ADAPTER__HAMILTON_TRACKER__API_KEY
    - FP_PIPELINE__RUN__EXECUTOR__TYPE
    - FP_LOG_LEVEL (global shim)
    """
env = dict(env or os.environ)
overrides: dict[str, Any] = {}
⋮----
rest = key[len(prefix):]
⋮----
value = _coerce_value(raw)
# Namespaced?
⋮----
path = [p.lower() for p in rest.split("__")]
⋮----
# Global shim, keep upper for later mapping
⋮----
def _merge_dict(target: dict, source: dict) -> dict
⋮----
def build_specific_overlays(overrides: dict) -> tuple[dict, dict]
⋮----
"""Return (project_overlay, pipeline_overlay) from parsed overrides.

    Example output paths (lowercased):
    - project: {"project": {"adapter": {"hamilton_tracker": {"api_key": "..."}}}}
    - pipeline: {"pipeline": {"run": {"log_level": "DEBUG"}}}
    """
project: dict[str, Any] = {}
pipeline: dict[str, Any] = {}
⋮----
# Project overlay
⋮----
project = {"project": overrides["project"]}
⋮----
# Pipeline overlay
⋮----
pipeline = {"pipeline": overrides["pipeline"]}
⋮----
def apply_global_shims(overrides: dict, project_overlay: dict, pipeline_overlay: dict) -> None
⋮----
"""Map legacy global FP_* envs into reasonable defaults if specific keys are absent.

    Example mappings:
    - FP_LOG_LEVEL -> pipeline.run.log_level (only if not already set)
    - FP_EXECUTOR  -> pipeline.run.executor.type
    - FP_EXECUTOR_MAX_WORKERS -> pipeline.run.executor.max_workers
    - FP_EXECUTOR_NUM_CPUS    -> pipeline.run.executor.num_cpus
    - FP_MAX_RETRIES -> pipeline.run.retry.max_retries
    - FP_RETRY_DELAY -> pipeline.run.retry.retry_delay
    - FP_JITTER_FACTOR -> pipeline.run.retry.jitter_factor
    """
g = overrides.get("_global", {})
⋮----
def ensure_path(base: dict, path: list[str]) -> dict
⋮----
cur = base
⋮----
cur = cur[p]
⋮----
tgt = ensure_path(pipeline_overlay.setdefault("pipeline", {}), ["run"])
⋮----
tgt = ensure_path(pipeline_overlay.setdefault("pipeline", {}), ["run", "executor"])
⋮----
tgt = ensure_path(pipeline_overlay.setdefault("pipeline", {}), ["run", "retry"])
⋮----
def merge_overlays_into_config(config_struct, project_overlay: dict, pipeline_overlay: dict)
⋮----
"""Merge parsed overlays into a Config-like struct (has .project and .pipeline)."""
# Use BaseConfig.merge_dict semantics via .update/merge_dict if present
⋮----
cfg = getattr(config_struct, "project")
⋮----
cfg = getattr(config_struct, "pipeline")
````

## File: src/flowerpower/utils/logging.py
````python
def setup_logging(level: str | None = None) -> None
⋮----
"""
    Configures the Loguru logger.

    Determines the logging level based on the following precedence:
    1. The 'level' argument passed to the function.
    2. The 'FP_LOG_LEVEL' environment variable.
    3. The 'LOG_LEVEL' from ..settings (which defaults to "CRITICAL").

    If the effective logging level is "CRITICAL", logging for the "flowerpower" module
    is disabled. Otherwise, logging is enabled and configured.
    """
# Remove all existing handlers to prevent duplicate logs
⋮----
# Determine the effective logging level
effective_level = level or os.getenv("FP_LOG_LEVEL") or LOG_LEVEL
````

## File: src/flowerpower/utils/security.py
````python
"""Security utilities for input validation and sanitization."""
⋮----
class SecurityError(Exception)
⋮----
"""Raised when security validation fails."""
⋮----
"""Validate and sanitize file paths to prevent directory traversal attacks.
    
    Args:
        path: File path to validate
        allowed_extensions: List of allowed file extensions (e.g., ['.yaml', '.yml'])
        allow_absolute: Whether to allow absolute paths
        allow_relative: Whether to allow relative paths
        
    Returns:
        Validated Path object
        
    Raises:
        SecurityError: If path is invalid or potentially dangerous
        ValueError: If path is empty or None
    """
⋮----
# Convert to Path object
path_obj = Path(path)
⋮----
# Check for directory traversal attempts
path_str = str(path_obj)
⋮----
# Check absolute vs relative path restrictions
⋮----
# Validate file extension if specified
⋮----
# Check for potentially dangerous characters
dangerous_chars = ['|', '&', ';', '`', '$', '<', '>', '"', "'"]
⋮----
def validate_pipeline_name(name: str) -> str
⋮----
"""Validate pipeline name to prevent injection attacks.
    
    Args:
        name: Pipeline name to validate
        
    Returns:
        Validated name
        
    Raises:
        ValueError: If name is invalid
        SecurityError: If name contains dangerous characters
    """
⋮----
name = name.strip()
⋮----
# Check for dangerous characters
⋮----
# Check length constraints
⋮----
"""Validate configuration dictionary to prevent malicious content.
    
    Args:
        config: Configuration dictionary to validate
        allowed_keys: List of allowed top-level keys
        max_depth: Maximum nesting depth to prevent DoS attacks
        
    Returns:
        Validated configuration dictionary
        
    Raises:
        SecurityError: If configuration contains dangerous content
        ValueError: If configuration is invalid
    """
⋮----
# Check for allowed keys
⋮----
invalid_keys = set(config.keys()) - set(allowed_keys)
⋮----
# Check nesting depth
def check_depth(obj, depth=0)
⋮----
def sanitize_log_data(data: Any) -> Any
⋮----
"""Sanitize data for safe logging to prevent log injection.
    
    Args:
        data: Data to sanitize for logging
        
    Returns:
        Sanitized data safe for logging
    """
⋮----
# Remove potential log injection characters
sanitized = re.sub(r'[\r\n\t]', ' ', data)
# Limit length to prevent log flooding
⋮----
sanitized = sanitized[:997] + "..."
⋮----
# For complex objects, convert to string and sanitize
⋮----
def validate_executor_type(executor_type: str) -> str
⋮----
"""Validate executor type to prevent arbitrary code execution.
    
    Args:
        executor_type: Executor type string to validate
        
    Returns:
        Validated executor type
        
    Raises:
        SecurityError: If executor type is invalid or dangerous
    """
⋮----
allowed_executors = {
⋮----
def validate_callback_function(callback: Any) -> bool
⋮----
"""Validate callback function to ensure it's safe to execute.
    
    Args:
        callback: Callback function or callable to validate
        
    Returns:
        True if callback is valid
        
    Raises:
        SecurityError: If callback is dangerous or invalid
    """
⋮----
# Check if it's a built-in function that could be dangerous
dangerous_functions = {'eval', 'exec', 'compile', '__import__'}
````

## File: src/flowerpower/utils/yaml_env.py
````python
"""
YAML environment variable interpolation utilities.

Supports a Docker Compose–style syntax inside YAML values:
- ${VAR}                -> substitute value of VAR (empty string if unset)
- ${VAR:-default}       -> default if VAR is unset or empty
- ${VAR-default}        -> default if VAR is unset (but not when set to empty)
- ${VAR:?err}           -> raise error if VAR is unset or empty
- ${VAR?err}            -> raise error if VAR is unset (but not when set to empty)
- $VAR                  -> simple substitution for alnum/underscore names
- $$                    -> escaped dollar sign

After interpolation, if the resulting string is valid JSON (object/array/number/bool/null),
it is coerced to the corresponding Python type. Otherwise the string is returned.

This module performs interpolation after YAML is parsed, by recursively walking the
loaded dict/list structure and transforming string values in-place.
"""
⋮----
_VAR_PATTERN = re.compile(
⋮----
def _is_empty(value: str | None) -> bool
⋮----
def _expand_match(match: re.Match, env: Mapping[str, str]) -> str
⋮----
token = match.group(0)
# Escaped dollar
⋮----
return "\x00_DOLLAR_\x00"  # temporary placeholder
⋮----
# ${...} forms
⋮----
inner = token[2:-1]
# Parse operators: :-, -, :?, ?
op = None
name = inner
arg = None
⋮----
parts = inner.split(candidate, 1)
name = parts[0]
op = candidate
arg = parts[1]
⋮----
name = name.strip()
value = env.get(name)
⋮----
# No operator, empty becomes empty string
⋮----
# default if unset or empty
⋮----
# default if unset only
⋮----
# Fallback shouldn't occur, but return empty to be safe
⋮----
# $VAR simple form
var_name = token[1:]
⋮----
def _maybe_json(value: str) -> Any
⋮----
s = value.strip()
# Fast-path: looks like JSON or a JSON scalar
⋮----
# Try number parsing via json for consistency (handles -1, 1.0)
⋮----
def interpolate_string(s: str, env: Mapping[str, str] | None = None, json_coerce: bool = True) -> Any
⋮----
"""Interpolate variables in a single string.

    Returns a possibly type-coerced value when json_coerce is True.
    """
env = env or os.environ
⋮----
expanded = _VAR_PATTERN.sub(lambda m: _expand_match(m, env), s)
# Restore escaped dollars
expanded = expanded.replace("\x00_DOLLAR_\x00", "$")
⋮----
def interpolate_env_in_data(data: Any, env: Mapping[str, str] | None = None, json_coerce: bool = True) -> Any
⋮----
"""Recursively interpolate environment variables for all string values in data.

    Modifies lists and dicts recursively; returns the transformed structure.
    """
````

## File: src/flowerpower/cfg/pipeline/adapter.py
````python
class HamiltonTracerConfig(BaseConfig)
⋮----
project_id: int | None = msgspec.field(default=None)
dag_name: str | None = msgspec.field(default=None)
tags: dict = msgspec.field(default_factory=dict)
capture_data_statistics: bool = msgspec.field(
max_list_length_capture: int = msgspec.field(
max_dict_length_capture: int = msgspec.field(
⋮----
def __post_init__(self)
⋮----
class MLFlowConfig(BaseConfig)
⋮----
experiment_name: str | None = msgspec.field(default=None)
experiment_tags: dict | None = msgspec.field(default_factory=dict)
experiment_description: str | None = msgspec.field(default=None)
run_id: str | None = msgspec.field(default=None)
run_name: str | None = msgspec.field(default=None)
run_tags: dict | None = msgspec.field(default_factory=dict)
run_description: str | None = msgspec.field(default=None)
⋮----
class AdapterConfig(BaseConfig)
⋮----
hamilton_tracker: HamiltonTracerConfig = msgspec.field(
mlflow: MLFlowConfig = msgspec.field(default_factory=MLFlowConfig)
````

## File: src/flowerpower/cfg/pipeline/builder_executor.py
````python
"""
Executor builder for RunConfig.
"""
⋮----
class ExecutorBuilder
⋮----
"""Builder for creating ExecutorConfig objects."""
⋮----
def __init__(self, executor_config: Optional[ExecutorConfig] = None)
⋮----
"""Initialize the ExecutorBuilder.

        Args:
            executor_config: Initial executor configuration to build upon.
        """
⋮----
def with_type(self, executor_type: str) -> "ExecutorBuilder"
⋮----
"""Set the executor type.

        Args:
            executor_type: Type of executor ('synchronous', 'threadpool', 'processpool', 'ray', 'dask')

        Returns:
            Self for method chaining
        """
⋮----
def with_max_workers(self, max_workers: int) -> "ExecutorBuilder"
⋮----
"""Set the maximum number of workers.

        Args:
            max_workers: Maximum number of worker threads/processes

        Returns:
            Self for method chaining
        """
⋮----
def with_num_cpus(self, num_cpus: int) -> "ExecutorBuilder"
⋮----
"""Set the number of CPUs to use.

        Args:
            num_cpus: Number of CPUs to allocate

        Returns:
            Self for method chaining
        """
⋮----
def with_config(self, config: dict[str, Any]) -> "ExecutorBuilder"
⋮----
"""Apply additional configuration options.

        Args:
            config: Dictionary of additional configuration options

        Returns:
            Self for method chaining
        """
⋮----
def build(self) -> ExecutorConfig
⋮----
"""Build the final ExecutorConfig object.

        Returns:
            Fully configured ExecutorConfig object

        Raises:
            ValueError: If configuration is invalid
        """
⋮----
def _validate_config(self) -> None
⋮----
"""Validate the executor configuration.

        Raises:
            ValueError: If configuration is invalid
        """
⋮----
valid_executors = [
````

## File: src/flowerpower/cfg/project/adapter.py
````python
class HamiltonTrackerConfig(BaseConfig)
⋮----
username: str | None = msgspec.field(default=None)
api_url: str = msgspec.field(default=settings.HAMILTON_API_URL)
ui_url: str = msgspec.field(default=settings.HAMILTON_UI_URL)
api_key: str | None = msgspec.field(default=None)
verify: bool = msgspec.field(default=False)
⋮----
def __post_init__(self)
⋮----
# Load API key from environment variable if not explicitly set
⋮----
class MLFlowConfig(BaseConfig)
⋮----
tracking_uri: str | None = msgspec.field(default=None)
registry_uri: str | None = msgspec.field(default=None)
artifact_location: str | None = msgspec.field(default=None)
⋮----
class OpenTelemetryConfig(BaseConfig)
⋮----
host: str = msgspec.field(default="localhost")
port: int = msgspec.field(default=6831)
⋮----
class RayConfig(BaseConfig)
⋮----
ray_init_config: dict | None = msgspec.field(default=None)
shutdown_ray_on_completion: bool = msgspec.field(default=False)
⋮----
class AdapterConfig(BaseConfig)
⋮----
hamilton_tracker: HamiltonTrackerConfig = msgspec.field(
mlflow: MLFlowConfig = msgspec.field(default_factory=MLFlowConfig)
ray: RayConfig = msgspec.field(default_factory=RayConfig)
opentelemetry: OpenTelemetryConfig = msgspec.field(
````

## File: src/flowerpower/cli/utils.py
````python
def convert_string_booleans(obj)
⋮----
"""Convert string 'true'/'false' to boolean values recursively."""
⋮----
def _parse_json(value: str)
⋮----
"""Parse value as JSON string."""
⋮----
def _parse_python_literal(value: str, param_type: str)
⋮----
"""Parse value as Python literal (dict/list)."""
⋮----
parsed = ast.literal_eval(value)
⋮----
# Validate type
⋮----
def _parse_key_value_pairs(value: str)
⋮----
"""Parse value as comma-separated key=value pairs."""
⋮----
def _parse_comma_separated_list(value: str)
⋮----
"""Parse value as comma-separated list with optional quotes."""
# Remove surrounding square brackets and whitespace
value = value.strip()
⋮----
value = value[1:-1].strip()
⋮----
# Parse list-like string with or without quotes
# This regex handles: a,b | 'a','b' | "a","b" | a, b | 'a', 'b'
list_items = re.findall(r"['\"]?(.*?)['\"]?(?=\s*,|\s*$)", value)
⋮----
# Remove any empty strings and strip whitespace
⋮----
"""
    Parse dictionary or list parameters from various input formats.

    Supports:
    - JSON string
    - Python literal (dict/list)
    - Comma-separated key=value pairs (for dicts)
    - Comma-separated values (for lists)
    - List-like string with or without quotes

    Args:
        value (str, optional): Input string to parse
        param_type (str): Type of parameter to parse ('dict' or 'list')

    Returns:
        dict | list | None: Parsed parameter or None if parsing fails
    """
⋮----
# Try parsing as JSON first
parsed = _parse_json(value)
⋮----
# Try parsing as Python literal
parsed = _parse_python_literal(value, param_type)
⋮----
# For dicts, try parsing as comma-separated key=value pairs
⋮----
parsed = _parse_key_value_pairs(value)
⋮----
# For lists, try parsing as comma-separated values
⋮----
parsed = _parse_comma_separated_list(value)
⋮----
# If all parsing fails, log warning and return None
⋮----
"""
    Load a hook function from a specified path.
    This function dynamically imports the module and retrieves the function


    Args:
        pipeline_name (str): Name of the pipeline
        function_path (str): Path to the function in the format 'module_name.function_name'
        base_dir (str, optional): Base directory for the pipeline
        storage_options (str, optional): Storage options as JSON or dict string
    Returns:
        Callable: The loaded hook function
    """
⋮----
path_segments = function_path.rsplit(".", 2)
⋮----
# If the function path is in the format 'module_name.function_name'
⋮----
module_path = ""
⋮----
# If the function path is in the format 'package.[subpackage.]module_name.function_name'
⋮----
# Construct the full path to the module file
hooks_dir = posixpath.join(
module_file_path = os.path.join(hooks_dir, f"{module_name}.py")
⋮----
# Validate that the module file exists
⋮----
# Use importlib.util to safely load the module without modifying sys.path
spec = importlib.util.spec_from_file_location(module_name, module_file_path)
⋮----
hook_module = importlib.util.module_from_spec(spec)
⋮----
# Get the function from the loaded module
⋮----
hook_function = getattr(hook_module, function_name)
````

## File: src/flowerpower/pipeline/lifecycle_manager.py
````python
"""Pipeline lifecycle management."""
⋮----
class PipelineLifecycleManager
⋮----
"""Handles pipeline creation, deletion, and metadata management.
    
    This class is responsible for:
    - Creating new pipelines
    - Deleting existing pipelines
    - Managing pipeline metadata and summaries
    - Displaying pipeline information
    - Managing hooks
    """
⋮----
def __init__(self, registry: "PipelineRegistry")
⋮----
"""Initialize the lifecycle manager.
        
        Args:
            registry: Pipeline registry for pipeline operations
        """
⋮----
"""Create a new pipeline.
        
        Args:
            name: Name of the pipeline to create
            overwrite: Whether to overwrite existing pipeline
            template: Template to use for pipeline creation
            tags: Tags to associate with the pipeline
            description: Description of the pipeline
        """
⋮----
"""Delete a pipeline.
        
        Args:
            name: Name of the pipeline to delete
            cfg: Whether to delete configuration file
            module: Whether to delete module file
        """
⋮----
"""Get pipeline summary information.
        
        Args:
            name: Name of pipeline to summarize, or None for all pipelines
            cfg: Whether to include configuration information
            code: Whether to include code information
            project: Whether to include project information
            
        Returns:
            dict: Summary information
        """
⋮----
# Get summary for all pipelines
⋮----
# Get summary for specific pipeline
pipeline = self._registry.get_pipeline_object(name=name)
⋮----
"""Display pipeline summary.
        
        Args:
            name: Name of pipeline to summarize, or None for all pipelines
            cfg: Whether to include configuration information
            code: Whether to include code information
            project: Whether to include project information
            to_html: Whether to output HTML
            to_svg: Whether to output SVG
        """
summary = self.get_summary(name=name, cfg=cfg, code=code, project=project)
⋮----
# Display all pipelines in a table
⋮----
table = Table(title="Pipeline Summaries")
⋮----
tags = ", ".join(info.get("tags", []))
desc = info.get("description", "")[:50] + "..." if len(info.get("description", "")) > 50 else info.get("description", "")
modified = info.get("modified", "N/A")
⋮----
# Display single pipeline details
⋮----
def show_pipelines(self) -> None
⋮----
"""Display available pipelines in a formatted table."""
pipelines = self.list_pipelines()
⋮----
# Get pipeline info for display
pipeline_info = []
⋮----
summary = self.get_summary(name=name, cfg=False, code=False, project=False)
⋮----
# Display as table
⋮----
table = Table(title="Available Pipelines")
⋮----
def list_pipelines(self) -> list[str]
⋮----
"""List all available pipeline names.
        
        Returns:
            list[str]: List of pipeline names
        """
⋮----
@property
    def pipelines(self) -> list[str]
⋮----
"""Get list of available pipeline names.
        
        Returns:
            list[str]: List of pipeline names
        """
⋮----
@property
    def summary(self) -> dict[str, dict | str]
⋮----
"""Get complete summary of all pipelines.
        
        Returns:
            dict[str, dict | str]: Complete summary information
        """
⋮----
"""Add a hook to a pipeline.
        
        Args:
            name: Name of the pipeline
            type: Type of hook to add
            to: Target for the hook
            function_name: Name of the function to hook
        """
````

## File: src/flowerpower/utils/__init__.py
````python
"""
Utility modules for FlowerPower.

This package contains utility classes and functions that help simplify
the main codebase by centralizing common operations.
"""
⋮----
__all__ = [
````

## File: src/flowerpower/utils/adapter.py
````python
"""
Adapter utilities for FlowerPower pipeline management.

This module provides helper classes for managing adapter configurations
and creating adapter instances with proper error handling and validation.
"""
⋮----
class AdapterManager
⋮----
"""
    Helper class for adapter configuration and instance creation.

    This class centralizes adapter configuration merging, validation,
    and instance creation to reduce complexity in the Pipeline class.
    """
⋮----
def __init__(self)
⋮----
"""Initialize the adapter manager."""
⋮----
def _merge_configs(self, base_config: Any, override_config: Any) -> Any
⋮----
"""Merge override config into base config."""
⋮----
"""
        Resolve and merge WithAdapterConfig.

        Args:
            with_adapter_cfg: Input configuration (dict or instance)
            base_config: Base configuration to merge with

        Returns:
            WithAdapterConfig: Merged configuration
        """
⋮----
with_adapter_cfg = WithAdapterConfig.from_dict(with_adapter_cfg)
⋮----
"""
        Resolve and merge PipelineAdapterConfig.

        Args:
            pipeline_adapter_cfg: Input configuration (dict or instance)
            base_config: Base configuration to merge with

        Returns:
            PipelineAdapterConfig: Merged configuration
        """
⋮----
pipeline_adapter_cfg = PipelineAdapterConfig.from_dict(
⋮----
"""
        Resolve and merge ProjectAdapterConfig from project context.

        Args:
            project_adapter_cfg: Input configuration (dict or instance)
            project_context: Project context to extract base config from

        Returns:
            ProjectAdapterConfig: Merged configuration
        """
⋮----
# Get base configuration from project context
base_cfg = self._extract_project_adapter_config(project_context)
⋮----
project_adapter_cfg = ProjectAdapterConfig.from_dict(
⋮----
# Use base configuration or create default
⋮----
"""
        Extract adapter configuration from project context.

        Args:
            project_context: Project context (PipelineManager or FlowerPowerProject)

        Returns:
            ProjectAdapterConfig or None: Extracted configuration
        """
# Try direct access to project config
project_cfg = getattr(project_context, "project_cfg", None) or getattr(project_context, "_project_cfg", None)
⋮----
# Try via pipeline_manager if available
⋮----
pm = project_context.pipeline_manager
pm_cfg = getattr(pm, "project_cfg", None) or getattr(pm, "_project_cfg", None)
⋮----
"""
        Create adapter instances based on configurations.

        Args:
            with_adapter_cfg: WithAdapter configuration
            pipeline_adapter_cfg: Pipeline adapter configuration
            project_adapter_cfg: Project adapter configuration

        Returns:
            list: List of adapter instances
        """
adapters = []
⋮----
# Hamilton Tracker adapter
⋮----
adapter = self._create_hamilton_tracker(
⋮----
# MLFlow adapter
⋮----
adapter = self._create_mlflow_adapter(
⋮----
# OpenTelemetry adapter
⋮----
adapter = self._create_opentelemetry_adapter(
⋮----
"""Create HamiltonTracker adapter instance."""
⋮----
tracker_kwargs = project_config.to_dict()
⋮----
# Set capture constants
⋮----
"""Create MLFlow adapter instance."""
⋮----
mlflow_kwargs = project_config.to_dict()
⋮----
"""Create OpenTelemetry adapter instance."""
⋮----
otel_kwargs = project_config.to_dict()
⋮----
def clear_cache(self) -> None
⋮----
"""Clear the adapter cache."""
⋮----
def create_adapter_manager() -> AdapterManager
⋮----
"""
    Factory function to create an AdapterManager instance.

    Returns:
        AdapterManager: Configured manager instance
    """
````

## File: src/flowerpower/utils/executor.py
````python
"""
Executor utilities for FlowerPower pipeline management.

This module provides factory methods for creating executor instances
with proper error handling and dependency management.
"""
⋮----
# Lazy imports to avoid circular dependencies
⋮----
class ExecutorFactory
⋮----
"""
    Factory class for creating executor instances.

    This class centralizes executor type selection and instance creation
    to reduce complexity in the Pipeline class.
    """
⋮----
def __init__(self)
⋮----
"""Initialize the executor factory."""
⋮----
"""
        Create an executor instance based on configuration.

        Args:
            executor_cfg: Executor configuration (string, dict, or ExecutorConfig)

        Returns:
            Executor instance
        """
# Normalize configuration
executor_cfg = self._normalize_config(executor_cfg)
⋮----
# Create executor based on type
executor_type = executor_cfg.type or "synchronous"
cache_key = f"{executor_type}_{hash(str(executor_cfg.to_dict()))}"
⋮----
executor = self._create_executor_by_type(executor_cfg)
⋮----
"""Normalize executor configuration to ExecutorConfig instance."""
⋮----
def _create_executor_by_type(self, executor_cfg: Any) -> Any
⋮----
"""Create executor based on type."""
⋮----
def _create_synchronous_executor(self) -> Any
⋮----
"""Create synchronous/local executor."""
⋮----
def _create_threadpool_executor(self, executor_cfg: Any) -> Any
⋮----
"""Create thread pool executor."""
⋮----
# Extract max workers from config
⋮----
def _create_processpool_executor(self, executor_cfg: Any) -> Any
⋮----
"""Create process pool executor."""
⋮----
def _create_ray_executor(self, executor_cfg: Any) -> Any
⋮----
"""Create Ray executor."""
⋮----
# Extract configuration
config = {}
⋮----
def _create_dask_executor(self, executor_cfg: Any) -> Any
⋮----
"""Create Dask executor."""
⋮----
def clear_cache(self) -> None
⋮----
"""Clear the executor cache."""
⋮----
def create_executor_factory() -> ExecutorFactory
⋮----
"""
    Factory function to create an ExecutorFactory instance.

    Returns:
        ExecutorFactory: Configured factory instance
    """
````

## File: src/flowerpower/utils/filesystem.py
````python
"""
Filesystem utilities for FlowerPower pipeline management.

This module provides helper classes and functions for common filesystem operations
used throughout the FlowerPower codebase.
"""
⋮----
class FilesystemHelper
⋮----
"""
    Helper class for filesystem operations with caching and error handling.

    This class provides centralized filesystem operations with proper error handling
    and logging for common operations like directory creation, path resolution,
    and filesystem initialization.
    """
⋮----
def __init__(self, base_dir: str, storage_options: Optional[Dict[str, Any]] = None)
⋮----
"""
        Initialize the filesystem helper.

        Args:
            base_dir: Base directory for filesystem operations
            storage_options: Storage options for filesystem access
        """
# Validate base directory for security
⋮----
def get_filesystem(self, cached: bool = False, cache_storage: Optional[str] = None) -> AbstractFileSystem
⋮----
"""
        Get a filesystem instance with optional caching.

        Args:
            cached: Whether to use cached filesystem
            cache_storage: Storage path for cached filesystem

        Returns:
            AbstractFileSystem: Configured filesystem instance
        """
cache_key = f"{self._base_dir}_{cached}_{cache_storage}"
⋮----
# Ensure cache storage directory exists
cache_path = Path(cache_storage)
⋮----
"""
        Ensure that the specified directories exist.

        Args:
            fs: Filesystem instance
            *directories: Directory paths to create
            exist_ok: Whether to ignore existing directories

        Raises:
            RuntimeError: If directory creation fails
        """
⋮----
# Validate directory path for security
⋮----
def resolve_path(self, fs: AbstractFileSystem, *path_parts: str) -> str
⋮----
"""
        Resolve a path in the filesystem.

        Args:
            fs: Filesystem instance
            *path_parts: Path components to join

        Returns:
            str: Resolved path
        """
⋮----
base_path = fs.path
⋮----
base_path = self._base_dir
⋮----
resolved_path = fs.join(base_path, *path_parts)
# Validate resolved path for security
⋮----
"""
        Clean specified paths if they exist.

        Args:
            fs: Filesystem instance
            *paths: Paths to clean
            recursive: Whether to remove recursively
        """
⋮----
# Validate path for security before cleaning
⋮----
def sync_filesystem(self, fs: AbstractFileSystem) -> None
⋮----
"""
        Sync filesystem cache if applicable.

        Args:
            fs: Filesystem instance to sync
        """
⋮----
# Log sync information if available
⋮----
def get_project_path(self, fs: AbstractFileSystem) -> str
⋮----
"""
        Get the project path for the filesystem.

        Args:
            fs: Filesystem instance

        Returns:
            str: Project path
        """
⋮----
project_path = fs._mapper.directory
⋮----
project_path = getattr(fs, 'path', self._base_dir)
⋮----
# Validate project path for security
⋮----
def clear_cache(self) -> None
⋮----
"""Clear the filesystem cache."""
⋮----
"""
    Factory function to create a FilesystemHelper instance.

    Args:
        base_dir: Base directory for filesystem operations
        storage_options: Storage options for filesystem access

    Returns:
        FilesystemHelper: Configured helper instance
    """
````

## File: src/flowerpower/cli/cfg.py
````python
app = typer.Typer(help="Config management commands")
````

## File: src/flowerpower/pipeline/executor.py
````python
"""Pipeline execution handling."""
⋮----
class PipelineExecutor
⋮----
"""Handles pipeline execution with comprehensive parameter handling.
    
    This class is responsible for:
    - Executing pipelines with various configurations
    - Merging runtime parameters with pipeline defaults
    - Setting up execution environment (logging, etc.)
    - Delegating to Pipeline objects for actual execution
    """
⋮----
"""Initialize the pipeline executor.
        
        Args:
            config_manager: Configuration manager for accessing pipeline configs
            registry: Pipeline registry for accessing pipeline objects
            project_context: Optional project context for execution
        """
⋮----
"""Execute a pipeline synchronously and return its results.
        
        This is the main method for running pipelines directly. It handles configuration
        loading, adapter setup, and execution via Pipeline objects.
        
        Args:
            name: Name of the pipeline to run. Must be a valid identifier.
            run_config: Run configuration object containing all execution parameters.
                If None, the default configuration from the pipeline will be used.
            **kwargs: Additional parameters to override the run_config.
                
        Returns:
            dict[str, Any]: Results of pipeline execution
            
        Raises:
            ValueError: If pipeline configuration cannot be loaded
            Exception: If pipeline execution fails
        """
# Load pipeline configuration
pipeline_config = self._config_manager.load_pipeline_config(name=name)
⋮----
# Initialize run_config with pipeline defaults if not provided
run_config = run_config or pipeline_config.run
⋮----
# Merge kwargs into run_config
⋮----
run_config = merge_run_config_with_kwargs(run_config, kwargs)
⋮----
# Set up logging for this specific run if log_level is provided
⋮----
# Get the pipeline object from registry
pipeline = self._registry.get_pipeline(
⋮----
# Execute the pipeline
⋮----
"""Execute a pipeline asynchronously and return its results.
        
        Args:
            name: Name of the pipeline to run
            run_config: Run configuration object
            **kwargs: Additional parameters to override the run_config
            
        Returns:
            dict[str, Any]: Results of pipeline execution
        """
⋮----
# Execute the pipeline asynchronously
````

## File: src/flowerpower/__init__.py
````python
__version__ = importlib.metadata.version("FlowerPower")
⋮----
__all__ = [
````

## File: src/flowerpower/cfg/pipeline/builder.py
````python
class RunConfigBuilder
⋮----
"""A fluent builder for creating RunConfig objects.

    This builder provides a clean interface for constructing RunConfig objects
    with proper configuration merging from project and pipeline defaults.
    """
⋮----
"""Initialize the RunConfigBuilder.

        Args:
            pipeline_name: Name of the pipeline to build config for
            base_dir: Base directory for the project (defaults to current directory)
            fs: Optional filesystem instance
            storage_options: Options for filesystem access
        """
⋮----
# Initialize with empty config
⋮----
# Initialize sub-builders
⋮----
# Load defaults from pipeline and project configs
⋮----
def _load_defaults(self)
⋮----
"""Load default configuration from pipeline and project YAML files."""
⋮----
# Load pipeline configuration
⋮----
pipeline_cfg = PipelineConfig.load(
⋮----
# If pipeline config doesn't exist, use defaults
⋮----
# Load project configuration for adapter defaults
⋮----
project_cfg = ProjectConfig.load(
⋮----
# Store project adapter config for merging
⋮----
def with_inputs(self, inputs: dict) -> "RunConfigBuilder"
⋮----
"""Set pipeline input values.

        Args:
            inputs: Dictionary of input values to override defaults

        Returns:
            Self for method chaining
        """
⋮----
def with_final_vars(self, final_vars: list[str]) -> "RunConfigBuilder"
⋮----
"""Set the final output variables.

        Args:
            final_vars: List of variable names to return from execution

        Returns:
            Self for method chaining
        """
⋮----
def with_config(self, config: dict) -> "RunConfigBuilder"
⋮----
"""Set Hamilton driver configuration.

        Args:
            config: Dictionary of configuration values for Hamilton

        Returns:
            Self for method chaining
        """
⋮----
def with_cache(self, cache: Union[dict, bool]) -> "RunConfigBuilder"
⋮----
"""Set cache configuration.

        Args:
            cache: Cache configuration (dict) or enable/disable flag (bool)

        Returns:
            Self for method chaining
        """
⋮----
def with_executor(self, executor_type: str, **kwargs) -> "RunConfigBuilder"
⋮----
"""Set executor configuration.

        Args:
            executor_type: Type of executor ('synchronous', 'threadpool', 'processpool', 'ray', 'dask')
            **kwargs: Additional executor configuration options

        Returns:
            Self for method chaining
        """
⋮----
def with_adapter(self, adapter_name: str, **kwargs) -> "RunConfigBuilder"
⋮----
"""Enable and configure a specific adapter.

        Args:
            adapter_name: Name of the adapter ('hamilton_tracker', 'mlflow', 'opentelemetry', etc.)
            **kwargs: Adapter-specific configuration options

        Returns:
            Self for method chaining
        """
# Enable the adapter using the adapter builder
enable_method = getattr(self._adapter_builder, f"enable_{adapter_name}", None)
⋮----
"""Configure retry behavior.

        Args:
            max_attempts: Maximum number of retry attempts
            delay: Base delay between retries in seconds
            jitter: Random jitter factor to add to retry delay
            exceptions: List of exception types that should trigger retries

        Returns:
            Self for method chaining
        """
# Ensure nested retry exists
⋮----
"""Set success and failure callbacks.

        Args:
            on_success: Callback function to execute on successful completion
            on_failure: Callback function to execute on failure

        Returns:
            Self for method chaining
        """
⋮----
def with_log_level(self, log_level: str) -> "RunConfigBuilder"
⋮----
"""Set the log level for execution.

        Args:
            log_level: Log level ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')

        Returns:
            Self for method chaining
        """
⋮----
def with_reload(self, reload: bool = True) -> "RunConfigBuilder"
⋮----
"""Set whether to reload the pipeline module.

        Args:
            reload: Whether to force reload of the pipeline module

        Returns:
            Self for method chaining
        """
⋮----
def with_pipeline_adapter_config(self, config: dict) -> "RunConfigBuilder"
⋮----
"""Set pipeline-specific adapter configuration.

        Args:
            config: Pipeline adapter configuration dictionary

        Returns:
            Self for method chaining
        """
⋮----
def with_project_adapter_config(self, config: dict) -> "RunConfigBuilder"
⋮----
"""Set project-level adapter configuration.

        Args:
            config: Project adapter configuration dictionary

        Returns:
            Self for method chaining
        """
⋮----
def with_custom_adapter(self, name: str, adapter: Any) -> "RunConfigBuilder"
⋮----
"""Add a custom adapter instance.

        Args:
            name: Name/identifier for the adapter
            adapter: Adapter instance

        Returns:
            Self for method chaining
        """
⋮----
def build(self) -> RunConfig
⋮----
"""Build the final RunConfig object.

        This method merges all configurations and validates the final result.

        Returns:
            Fully configured RunConfig object

        Raises:
            ValueError: If configuration is invalid
        """
# Create a deep copy to avoid modifying the internal state
final_config = copy.deepcopy(self._config)
⋮----
# Build executor configuration
⋮----
# Build adapter configuration
⋮----
# Merge adapter configurations
adapter_configs = self._adapter_builder.get_adapter_configs()
⋮----
# Validate configuration
⋮----
"""Merge adapter configurations from builder with project/pipeline configs."""
⋮----
# Merge project adapter defaults
⋮----
# Merge with project config
⋮----
project_config = getattr(
adapter_config = {**project_config, **adapter_config}
⋮----
# Store in pipeline adapter config
⋮----
def _validate_config(self, config: RunConfig)
⋮----
"""Validate the final configuration.

        Args:
            config: RunConfig object to validate

        Raises:
            ValueError: If configuration is invalid
        """
# Validate retry configuration
retry_cfg = config.retry or RetryConfig()
⋮----
# Validate executor configuration
⋮----
valid_executors = [
⋮----
# Validate log level
⋮----
valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
````

## File: src/flowerpower/pipeline/config_manager.py
````python
"""Configuration management for pipelines."""
⋮----
class PipelineConfigManager
⋮----
"""Handles loading, validation, and access to pipeline configurations.
    
    This class is responsible for:
    - Loading project and pipeline configurations
    - Validating configuration files
    - Providing convenient access to configuration objects
    - Managing configuration reload logic
    """
⋮----
"""Initialize the configuration manager.
        
        Args:
            base_dir: Base directory for the project
            fs: Filesystem instance for file operations
            storage_options: Storage options for filesystem
            cfg_dir: Configuration directory name
        """
⋮----
def load_project_config(self, reload: bool = False) -> ProjectConfig
⋮----
"""Load project configuration.
        
        Args:
            reload: Whether to reload the configuration even if already loaded
            
        Returns:
            ProjectConfig: The loaded project configuration
        """
⋮----
# Construct config file path
cfg_path = f"{self._base_dir}/{self._cfg_dir}/project.yml"
⋮----
# Load configuration using provided filesystem
fs = self._fs
⋮----
# Apply environment overlays (project-only part)
⋮----
overrides = parse_env_overrides()
⋮----
# Add pipelines directory to Python path
⋮----
def load_pipeline_config(self, name: str, reload: bool = False) -> PipelineConfig
⋮----
"""Load pipeline configuration.

        Args:
            name: Name of the pipeline to load
            reload: Whether to reload the configuration even if already loaded

        Returns:
            PipelineConfig: The loaded pipeline configuration
        """
⋮----
# Ensure project config is loaded first
⋮----
# Use existing filesystem
⋮----
# Try different file locations and extensions
cfg_path = None
possible_paths = [
⋮----
# Try .yml extension in pipelines/ subdirectory first
⋮----
# Then try .yaml extension in pipelines/ subdirectory
⋮----
# Fallback to old paths for backward compatibility
⋮----
cfg_path = path
⋮----
# Load configuration
⋮----
# Apply environment overlays (pipeline-only part)
⋮----
# Update current pipeline name
⋮----
@property
    def project_config(self) -> ProjectConfig
⋮----
"""Get the current project configuration.
        
        Returns:
            ProjectConfig: The current project configuration
            
        Raises:
            ValueError: If project configuration has not been loaded
        """
⋮----
@property
    def pipeline_config(self) -> PipelineConfig
⋮----
"""Get the current pipeline configuration.
        
        Returns:
            PipelineConfig: The current pipeline configuration
            
        Raises:
            ValueError: If pipeline configuration has not been loaded
        """
⋮----
@property
    def current_pipeline_name(self) -> Optional[str]
⋮----
"""Get the name of the currently loaded pipeline.
        
        Returns:
            str | None: Name of the current pipeline, or None if none loaded
        """
⋮----
def _add_modules_path(self, python_path: list[str]) -> None
⋮----
"""Add module paths to Python path.
        
        Args:
            python_path: List of paths to add to sys.path
        """
⋮----
path_obj = Path(self._base_dir) / path
````

## File: src/flowerpower/utils/config.py
````python
"""
Configuration utilities for FlowerPower.

This module provides shared configuration handling utilities to avoid code duplication.
"""
⋮----
def prefer_executor_override(base: ExecutorConfig, override: str | dict | ExecutorConfig | None) -> ExecutorConfig
⋮----
"""Merge executor configs preferring explicit runtime overrides.

    Rules:
    - If override is None -> return base
    - String -> treated as type override
    - Dict -> fields present (including explicit None) override base
    - ExecutorConfig -> fields that are not None override base
    """
⋮----
# Normalize override to ExecutorConfig
⋮----
ov = ExecutorConfig(type=override)
⋮----
# Preserve explicit None vs missing by checking keys
ov = ExecutorConfig.from_dict(override)
type_set = 'type' in override
max_workers_set = 'max_workers' in override
num_cpus_set = 'num_cpus' in override
merged = ExecutorConfig(
⋮----
ov = override
⋮----
# Build merged with explicit precedence: if ov.field is not None, use it
# Note: for dict-based overrides, explicit None is kept as None (clears base)
⋮----
def _merge_inputs(run_config: RunConfig, value)
⋮----
"""Merge inputs into run config."""
⋮----
def _merge_config(run_config: RunConfig, value)
⋮----
"""Merge config into run config."""
⋮----
def _set_cache(run_config: RunConfig, value)
⋮----
"""Set cache in run config."""
⋮----
def _merge_adapter(run_config: RunConfig, value)
⋮----
"""Merge adapter into run config."""
⋮----
def _set_executor_cfg(run_config: RunConfig, value)
⋮----
"""Set executor config."""
⋮----
def _set_with_adapter_cfg(run_config: RunConfig, value)
⋮----
"""Set with adapter config."""
⋮----
def _set_pipeline_adapter_cfg(run_config: RunConfig, value)
⋮----
"""Set pipeline adapter config."""
⋮----
def _set_project_adapter_cfg(run_config: RunConfig, value)
⋮----
"""Set project adapter config."""
⋮----
def _set_retry_cfg(run_config: RunConfig, value)
⋮----
"""Set retry config (nested)."""
⋮----
_attr_handlers = {
⋮----
def merge_run_config_with_kwargs(run_config: RunConfig, kwargs: Dict[str, Any]) -> RunConfig
⋮----
"""Merge kwargs into a RunConfig object.
    
    This utility function updates the RunConfig object with values from kwargs,
    handling different types of attributes appropriately.
    
    Args:
        run_config: The RunConfig object to update
        kwargs: Dictionary of additional parameters to merge
        
    Returns:
        RunConfig: Updated RunConfig object
    """
# Handle complex attributes with specific logic
⋮----
# Handle simple attributes
simple_attrs = [
⋮----
value = kwargs[attr]
# Validate callbacks for security
⋮----
# Map deprecated flat fields into nested retry configuration
⋮----
class RunConfigBuilder
⋮----
"""Builder pattern for constructing RunConfig objects with fluent interface."""
⋮----
def __init__(self, base_config: RunConfig | None = None)
⋮----
def with_inputs(self, inputs: Dict[str, Any] | None) -> 'RunConfigBuilder'
⋮----
"""Set inputs configuration."""
⋮----
def with_config(self, config: Dict[str, Any] | None) -> 'RunConfigBuilder'
⋮----
"""Set pipeline configuration."""
⋮----
def with_cache(self, cache: bool | None) -> 'RunConfigBuilder'
⋮----
"""Set caching configuration."""
⋮----
def with_adapter(self, adapter: Dict[str, Any] | None) -> 'RunConfigBuilder'
⋮----
"""Set adapter configuration."""
⋮----
def with_executor(self, executor_cfg: str | Dict[str, Any] | ExecutorConfig | None) -> 'RunConfigBuilder'
⋮----
"""Set executor configuration."""
⋮----
"""Set retry configuration."""
⋮----
def with_logging(self, log_level: str | None = None) -> 'RunConfigBuilder'
⋮----
"""Set logging configuration."""
⋮----
def with_callbacks(self, on_success: str | None = None, on_failure: str | None = None) -> 'RunConfigBuilder'
⋮----
"""Set callback configurations."""
⋮----
# Additional methods for backward compatibility with tests
def with_final_vars(self, final_vars: list[str] | None) -> 'RunConfigBuilder'
⋮----
"""Set final variables."""
⋮----
def with_executor_cfg(self, executor_cfg: str | Dict[str, Any] | ExecutorConfig | None) -> 'RunConfigBuilder'
⋮----
"""Set executor configuration (alias for with_executor)."""
⋮----
def with_with_adapter_cfg(self, with_adapter_cfg: Dict[str, Any] | WithAdapterConfig | None) -> 'RunConfigBuilder'
⋮----
"""Set with_adapter configuration."""
⋮----
def with_pipeline_adapter_cfg(self, pipeline_adapter_cfg: Any | None) -> 'RunConfigBuilder'
⋮----
"""Set pipeline adapter configuration."""
⋮----
def with_project_adapter_cfg(self, project_adapter_cfg: Any | None) -> 'RunConfigBuilder'
⋮----
"""Set project adapter configuration."""
⋮----
def with_reload(self, reload: bool | None) -> 'RunConfigBuilder'
⋮----
"""Set reload flag."""
⋮----
def with_log_level(self, log_level: str | None) -> 'RunConfigBuilder'
⋮----
"""Set log level (alias for with_logging)."""
⋮----
def with_max_retries(self, max_retries: int | None) -> 'RunConfigBuilder'
⋮----
"""Set max retries."""
⋮----
def with_retry_delay(self, retry_delay: float | None) -> 'RunConfigBuilder'
⋮----
"""Set retry delay."""
⋮----
def with_jitter_factor(self, jitter_factor: float | None) -> 'RunConfigBuilder'
⋮----
"""Set jitter factor."""
⋮----
def with_retry_exceptions(self, retry_exceptions: list | None) -> 'RunConfigBuilder'
⋮----
"""Set retry exceptions."""
⋮----
def with_on_success(self, on_success: Any | None) -> 'RunConfigBuilder'
⋮----
"""Set on_success callback."""
⋮----
def with_on_failure(self, on_failure: Any | None) -> 'RunConfigBuilder'
⋮----
"""Set on_failure callback."""
⋮----
def reset(self) -> 'RunConfigBuilder'
⋮----
"""Reset builder to default values."""
⋮----
@classmethod
    def from_config(cls, config: RunConfig) -> 'RunConfigBuilder'
⋮----
"""Create builder from existing config."""
⋮----
def build(self) -> RunConfig
⋮----
"""Build and return the RunConfig object."""
# Create a new copy to ensure immutability
````

## File: src/flowerpower/cfg/base.py
````python
def validate_file_path(path: str) -> str
⋮----
"""
    Validate a file path to prevent directory traversal attacks.
    
    Args:
        path: The file path to validate
        
    Returns:
        str: The validated path
        
    Raises:
        ConfigPathError: If the path contains directory traversal attempts
    """
⋮----
# Use the comprehensive security validation
validated_path = security_validate_file_path(
⋮----
allow_absolute=False,  # Config files should be relative
⋮----
# Convert security errors to config path errors for consistency
⋮----
class BaseConfig(msgspec.Struct, kw_only=True)
⋮----
# Class-level cache for filesystem instances
_fs_cache = {}
⋮----
@classmethod
@lru_cache(maxsize=32)
    def _get_cached_filesystem(cls, base_dir: str, storage_options_hash: int) -> AbstractFileSystem
⋮----
"""Get a cached filesystem instance.
        
        Args:
            base_dir: Base directory for the filesystem.
            storage_options_hash: Hash of storage options for cache key.
            
        Returns:
            Cached filesystem instance.
        """
cache_key = (base_dir, storage_options_hash)
⋮----
@classmethod
    def _hash_storage_options(cls, storage_options: dict | None) -> int
⋮----
"""Create a hash of storage options for caching.
        
        Args:
            storage_options: Storage options to hash.
            
        Returns:
            Hash of storage options.
        """
⋮----
# Convert to frozenset of items for consistent hashing
⋮----
# If items are not hashable, use string representation
⋮----
def to_dict(self) -> dict[str, Any]
⋮----
# Convert to dictionary, handling special cases like type objects
result = {}
⋮----
value = getattr(self, field)
⋮----
# Convert type objects to string representation
⋮----
# Recursively convert nested msgspec structs
⋮----
# Handle Munch objects by converting to regular dict
⋮----
# Handle regular dictionaries that might contain Munch objects
⋮----
# Handle lists that might contain type objects or Munch objects
converted_list = []
⋮----
# Handle Munch objects in lists
⋮----
# Handle dictionaries in lists
⋮----
def _convert_dict_recursively(self, d: dict) -> dict
⋮----
"""Recursively convert dictionaries, handling Munch objects."""
⋮----
# Convert Munch objects to regular dict
⋮----
# Recursively handle nested dictionaries
⋮----
# Handle lists within dictionaries
⋮----
def to_yaml(self, path: str, fs: AbstractFileSystem | None = None) -> None
⋮----
"""
        Converts the instance to a YAML file.

        Args:
            path: The path to the YAML file.
            fs: An optional filesystem instance to use for file operations.

        Raises:
            ConfigSaveError: If saving the configuration fails.
            ConfigPathError: If the path contains directory traversal attempts.
        """
# Validate the path to prevent directory traversal
⋮----
validated_path = validate_file_path(path)
⋮----
# Default to fsspec.filesystem when fs is not provided (testable/mocked)
⋮----
import fsspec  # type: ignore
fs = fsspec.filesystem("file")
⋮----
# Fallback to project helper if fsspec is unavailable in context
fs = get_filesystem(fs)
⋮----
# Surface underlying capability error as-is (expected by tests)
⋮----
@classmethod
    def from_dict(cls, data: dict[str, Any]) -> "BaseConfig"
⋮----
"""
        Converts a dictionary to an instance of the class.
        Args:
            data: The dictionary to convert.

        Returns:
            An instance of the class with the values from the dictionary.
        """
⋮----
@classmethod
    def from_yaml(cls, path: str, fs: AbstractFileSystem | None = None) -> "BaseConfig"
⋮----
"""
        Loads a YAML file and converts it to an instance of the class.

        Args:
            path: The path to the YAML file.
            fs: An optional filesystem instance to use for file operations.

        Returns:
            An instance of the class with the values from the YAML file.

        Raises:
            ConfigLoadError: If loading the configuration fails.
            ConfigPathError: If the path contains directory traversal attempts.
        """
# Validate the path to prevent directory traversal (skip for fsspec URLs when fs provided)
⋮----
validated_path = path
⋮----
# tests expect default mode when fs provided
⋮----
def _apply_dict_updates(self, target: Self, d: dict[str, Any]) -> None
⋮----
"""
        Helper method to apply dictionary updates to a target instance.
        
        Args:
            target: The target instance to apply updates to.
            d: The dictionary containing updates to apply.
        """
⋮----
current_value = getattr(target, k)
⋮----
# For dictionaries, avoid mutating original nested dicts
new_dict = dict(current_value)
⋮----
# For nested msgspec structs, create a new instance with merged values
⋮----
# For primitive values, direct assignment is fine
⋮----
# Use object.__setattr__ to bypass msgspec.Struct's restrictions
⋮----
def update(self, d: dict[str, Any]) -> None
⋮----
"""
        Updates this instance with values from the provided dictionary.
        
        Args:
            d: The dictionary containing updates to apply.
        """
⋮----
def merge_dict(self, d: dict[str, Any]) -> Self
⋮----
"""
        Creates a copy of this instance and updates the copy with values
        from the provided dictionary. The original instance (self) is not modified.

        Args:
            d: The dictionary to get values from.

        Returns:
            A new instance of the struct with updated values.
        """
# Use shallow copy for better performance
self_copy = copy.copy(self)
⋮----
def merge(self, source: Self) -> Self
⋮----
"""
        Creates a copy of this instance and updates the copy with values
        from the source struct, only if the source field's value is not
        its default value. The original instance (self) is not modified.

        Args:
            source: The msgspec.Struct instance of the same type to get values from.

        Returns:
            A new instance of the struct with updated values.

        Raises:
            TypeError: If source is not of the same type as self.
        """
⋮----
updated_instance = copy.copy(self)
⋮----
# Get default values if they exist
defaults = getattr(source, "__struct_defaults__", {})
⋮----
source_value = getattr(source, field)
has_explicit_default = field in defaults
is_default_value = False
⋮----
is_default_value = source_value == defaults[field]
⋮----
is_default_value = source_value is None
````

## File: src/flowerpower/pipeline/visualizer.py
````python
# Import necessary config types and utility functions
⋮----
from .base import load_module  # Import module loading utility
⋮----
class PipelineVisualizer
⋮----
"""Handles the visualization of pipeline DAGs."""
⋮----
def __init__(self, project_cfg: ProjectConfig, fs: AbstractFileSystem)
⋮----
"""
        Initializes the PipelineVisualizer.

        Args:
            project_cfg: The project configuration object.
            fs: The filesystem instance.
        """
⋮----
# Attributes like fs and base_dir are accessed via self.project_cfg
⋮----
def _get_dag_object(self, name: str, reload: bool = False)
⋮----
"""Get the Hamilton DAG object for a pipeline.

        Args:
            name (str): The name of the pipeline.
            reload (bool): Whether to reload the module.

        Returns:
            Hamilton DAG object.

        Raises:
            ImportError: If the module cannot be loaded.

        """
# Load pipeline-specific config
pipeline_cfg = PipelineConfig.load(name=name, fs=self._fs)
⋮----
# Load the pipeline module
# Ensure the pipelines directory is in sys.path (handled by PipelineManager usually)
module = load_module(name=name, reload=reload)
⋮----
# Create a basic driver builder for visualization purposes
# Use the run config from the loaded pipeline_cfg
builder = (
⋮----
# No adapters or complex executors needed for display_all_functions
⋮----
# Build the driver
dr = builder.build()
⋮----
# Return the visualization object
⋮----
"""
        Save an image of the graph of functions for a given pipeline name.

        Args:
            name (str): The name of the pipeline graph.
            format (str, optional): The format of the graph file. Defaults to "png".
            reload (bool, optional): Whether to reload the pipeline data. Defaults to False.

        Raises:
            ImportError: If the module cannot be loaded.

        Example:
            >>> from flowerpower.pipeline.visualizer import PipelineVisualizer
            >>> visualizer = PipelineVisualizer(project_cfg, fs)
            >>> visualizer.save_dag(name="example_pipeline", format="png")
        """
dag = self._get_dag_object(name=name, reload=reload)
⋮----
# Determine final output path
⋮----
graph_dir = posixpath.join(base_dir, "graphs")
⋮----
base = posixpath.join(graph_dir, name)
final_path = f"{base}.{format}"
render_path = base
⋮----
# If output_path already has an extension, use as-is; otherwise append format
⋮----
final_path = output_path
# Remove extension for graphviz render base path
render_path = final_path.rsplit(".", 1)[0]
fmt = final_path.rsplit(".", 1)[1]
⋮----
# Honor explicit extension if it differs from format argument
format = fmt
⋮----
final_path = f"{output_path}.{format}"
render_path = output_path
⋮----
# Render the DAG using the graphviz object returned by display_all_functions
⋮----
render_path,  # graphviz appends the format automatically
⋮----
"""
        Display the graph of functions for a given pipeline name.

        Args:
            name (str): The name of the pipeline graph.
            format (str, optional): The format of the graph file. Defaults to "png".
            reload (bool, optional): Whether to reload the pipeline data. Defaults to False.
            raw (bool, optional): Whether to return the raw graph object instead of displaying. Defaults to False.

        Returns:
            Optional[graphviz.Digraph]: The generated graph object if raw=True, else None.

        Raises:
            ImportError: If the module cannot be loaded.

        Example:
            >>> from flowerpower.pipeline.visualizer import PipelineVisualizer
            >>> visualizer = PipelineVisualizer(project_cfg, fs)
            >>> visualizer.show_dag(name="example_pipeline", format="png")
        """
⋮----
# Use view_img utility to display the rendered graph
⋮----
return None  # Explicitly return None when not raw
````

## File: src/flowerpower/cfg/project/__init__.py
````python
class ProjectConfig(BaseConfig)
⋮----
"""A configuration class for managing project-level settings in FlowerPower.

    This class handles project-wide configuration including adapter settings.
    It supports loading from and saving to YAML files, with filesystem abstraction.

    Attributes:
        name (str | None): The name of the project.
        adapter (AdapterConfig): Configuration for the adapter component.

    Example:
        ```python
        # Create a new project config
        project = ProjectConfig(name="my-project")

        # Load existing project config
        project = ProjectConfig.load(base_dir="path/to/project")

        # Save project config
        project.save(base_dir="path/to/project")
        ```
    """
⋮----
name: str | None = msgspec.field(default=None)
adapter: AdapterConfig = msgspec.field(default_factory=AdapterConfig)
⋮----
def __post_init__(self)
⋮----
# Validate project name if provided
⋮----
def _validate_project_name(self) -> None
⋮----
"""Validate project name parameter.
        
        Raises:
            ValueError: If project name contains invalid characters.
        """
⋮----
# Check for directory traversal attempts
⋮----
# Check for empty string
⋮----
@classmethod
    def _load_project_config(cls, fs: AbstractFileSystem, name: str | None) -> "ProjectConfig"
⋮----
"""Centralized project configuration loading logic.
        
        Args:
            fs: Filesystem instance.
            name: Project name.
            
        Returns:
            Loaded project configuration.
        """
⋮----
project = cls.from_yaml(path="conf/project.yml", fs=fs)
⋮----
project = cls(name=name)
⋮----
def _save_project_config(self, fs: AbstractFileSystem) -> None
⋮----
"""Centralized project configuration saving logic.
        
        Args:
            fs: Filesystem instance.
        """
⋮----
"""Load project configuration from a YAML file.

        Args:
            base_dir (str, optional): Base directory for the project. Defaults to ".".
            name (str | None, optional): Project name. Defaults to None.
            fs (AbstractFileSystem | None, optional): Filesystem to use. Defaults to None.
            storage_options (dict | Munch, optional): Options for filesystem. Defaults to empty Munch.

        Returns:
            ProjectConfig: Loaded project configuration.

        Example:
            ```python
            project = ProjectConfig.load(
                base_dir="my_project",
                name="pipeline1"
                )
            ```
        """
⋮----
# Use cached filesystem for better performance
storage_options_hash = cls._hash_storage_options(storage_options)
fs = cls._get_cached_filesystem(base_dir, storage_options_hash)
⋮----
@classmethod
    def from_yaml(cls, path: str, fs: AbstractFileSystem)
⋮----
raw = f.read()
⋮----
data = _yaml.safe_load(raw) or {}
data = interpolate_env_in_data(data)
⋮----
instance = msgspec.convert(data, cls)
⋮----
"""Save project configuration to a YAML file.

        Args:
            base_dir (str, optional): Base directory for the project. Defaults to ".".
            fs (AbstractFileSystem | None, optional): Filesystem to use. Defaults to None.
            storage_options (dict | Munch, optional): Options for filesystem. Defaults to empty Munch.

        Example:
            ```python
            project_config.save(base_dir="my_project")
            ```
        """
⋮----
storage_options_hash = self._hash_storage_options(storage_options)
fs = self._get_cached_filesystem(base_dir, storage_options_hash)
⋮----
"""Initialize a new project configuration.

    This function creates a new project configuration and saves it to disk.

    Args:
        base_dir (str, optional): Base directory for the project. Defaults to ".".
        name (str | None, optional): Project name. Defaults to None.
        fs (AbstractFileSystem | None, optional): Filesystem to use. Defaults to None.
        storage_options (dict | Munch, optional): Options for filesystem. Defaults to empty Munch.

    Returns:
        ProjectConfig: The initialized project configuration.

    Example:
        ```python
        project = init_project_config(
            base_dir="my_project",
            name="test_project"
        )
        ```
    """
project = ProjectConfig.load(
````

## File: src/flowerpower/cli/__init__.py
````python
app = typer.Typer(
⋮----
"""
    Initialize a new FlowerPower project.

    This command creates a new FlowerPower project with the necessary directory structure
    and configuration files. If no project name is provided, the current directory name
    will be used as the project name.

    Args:
        project_name: Name of the FlowerPower project to create. If not provided,
                      the current directory name will be used
        base_dir: Base directory where the project will be created. If not provided,
                  the current directory's parent will be used
        storage_options: Storage options for filesystem access, as a JSON or dict string

    Examples:
        # Create a project in the current directory using its name
        $ flowerpower init

        # Create a project with a specific name
        $ flowerpower init --name my-awesome-project

        # Create a project in a specific location
        $ flowerpower init --name my-project --base-dir /path/to/projects
    """
parsed_storage_options = {}
⋮----
parsed_storage_options = (
⋮----
"""
    Start the Hamilton UI web application.

    This command launches the Hamilton UI, which provides a web interface for
    visualizing and interacting with your FlowerPower pipelines. The UI allows you
    to explore pipeline execution graphs, view results, and manage jobs.

    Args:
        port: Port to run the UI server on
        base_dir: Base directory where the UI will store its data
        no_migration: Skip running database migrations on startup
        no_open: Prevent automatically opening the browser
        settings_file: Settings profile to use (mini, dev, prod)
        config_file: Optional custom configuration file path

    Examples:
        # Start the UI with default settings
        $ flowerpower ui

        # Run the UI on a specific port
        $ flowerpower ui --port 9000

        # Use a custom data directory
        $ flowerpower ui --base-dir ~/my-project/.hamilton-data

        # Start without opening a browser
        $ flowerpower ui --no-open

        # Use production settings
        $ flowerpower ui --settings prod
    """
````

## File: src/flowerpower/pipeline/base.py
````python
def load_module(name: str, reload: bool = False)
⋮----
"""
    Load a module.

    Args:
        name (str): The name of the module.

    Returns:
        module: The loaded module.
    """
⋮----
class BasePipeline
⋮----
"""
    Base class for all pipelines.
    """
⋮----
fs = filesystem(self._base_dir, **self._storage_options)
⋮----
def _setup_paths(self) -> None
⋮----
"""Set up configuration and pipeline directory paths."""
⋮----
def _setup_directories(self) -> None
⋮----
"""Set up required directories with proper error handling."""
⋮----
def __enter__(self) -> "BasePipeline"
⋮----
def _add_modules_path(self)
⋮----
"""
        Sync the filesystem.

        Returns:
            None
        """
⋮----
modules_path = posixpath.join(
⋮----
modules_path = posixpath.join(self._fs.path, self._pipelines_dir)
⋮----
def _load_project_cfg(self) -> ProjectConfig
⋮----
"""
        Load the project configuration.

        Returns:
            ProjectConfig: The loaded project configuration.
        """
⋮----
def _load_pipeline_cfg(self, name: str) -> PipelineConfig
⋮----
"""
        Load the pipeline configuration.

        Args:
            name (str): The name of the pipeline.

        Returns:
            PipelineConfig: The loaded pipeline configuration.
        """
````

## File: src/flowerpower/cfg/__init__.py
````python
class Config(BaseConfig)
⋮----
"""Main configuration class for FlowerPower, combining project and pipeline settings.

    This class serves as the central configuration manager, handling both project-wide
    and pipeline-specific settings. It provides functionality for loading and saving
    configurations using various filesystem abstractions.

    Attributes:
        pipeline (PipelineConfig): Configuration for the pipeline.
        project (ProjectConfig): Configuration for the project.
        fs (AbstractFileSystem | None): Filesystem abstraction for I/O operations.
        base_dir (str | None): Base directory for the configuration.
        base_dir_path (pathlib.Path | None): Base directory as a Path object (property).
        storage_options (Munch): Options for filesystem operations.

    Example:
        ```python
        # Load configuration
        config = Config.load(
            base_dir="my_project",
            name="project1",
            pipeline_name="data-pipeline"
        )

        # Save configuration
        config.save(project=True, pipeline=True)
        ```
    """
⋮----
pipeline: PipelineConfig = msgspec.field(default_factory=PipelineConfig)
project: ProjectConfig = msgspec.field(default_factory=ProjectConfig)
fs: AbstractFileSystem | None = None
base_dir: str | None = None
storage_options: Munch = msgspec.field(default_factory=Munch)
⋮----
def __post_init__(self)
⋮----
"""Handle conversion of storage_options from dict to Munch if needed."""
⋮----
# Validate storage_options
⋮----
# Validate base_dir if provided
⋮----
def _validate_storage_options(self) -> None
⋮----
"""Validate storage_options parameter.
        
        Raises:
            ValueError: If storage_options contains invalid values.
        """
⋮----
def _validate_base_dir(self) -> None
⋮----
"""Validate base_dir parameter.
        
        Raises:
            ValueError: If base_dir contains invalid characters or is empty.
        """
# Convert Path to string if needed
base_dir_str = str(self.base_dir) if hasattr(self.base_dir, '__str__') else self.base_dir
⋮----
# Check for directory traversal attempts (but allow absolute paths)
⋮----
# Check for empty string
⋮----
@property
    def base_dir_path(self) -> Path | None
⋮----
"""Get base_dir as a pathlib.Path object.
        
        Returns:
            pathlib.Path | None: The base directory as a Path object, or None if base_dir is None.
        """
⋮----
"""Load both project and pipeline configurations.

        Args:
            base_dir (str, optional): Base directory for configurations. Defaults to ".".
            name (str | None, optional): Project name. Defaults to None.
            pipeline_name (str | None, optional): Pipeline name. Defaults to None.
            fs (AbstractFileSystem | None, optional): Filesystem to use. Defaults to None.
            storage_options (dict | Munch, optional): Options for filesystem. Defaults to empty Munch.

        Returns:
            Config: Combined configuration instance.

        Example:
            ```python
            config = Config.load(
                base_dir="my_project",
                name="test_project",
                pipeline_name="etl",
            )
            ```
        """
⋮----
# Use cached filesystem for better performance
storage_options_hash = cls._hash_storage_options(storage_options)
fs = cls._get_cached_filesystem(base_dir, storage_options_hash)
⋮----
project = ProjectConfig.load(
⋮----
pipeline = PipelineConfig.load(
⋮----
config = cls(
⋮----
# Apply environment overlays with specificity and shims
⋮----
overrides = parse_env_overrides()
⋮----
# Fail-open: ignore overlay errors to avoid breaking existing flows
⋮----
"""Save project and/or pipeline configurations.

        Args:
            project (bool, optional): Whether to save project config. Defaults to False.
            pipeline (bool, optional): Whether to save pipeline config. Defaults to True.
            fs (AbstractFileSystem | None, optional): Filesystem to use. Defaults to None.
            storage_options (dict | Munch, optional): Options for filesystem. Defaults to empty Munch.

        Example:
            ```python
            config.save(project=True, pipeline=True)
            ```
        """
⋮----
storage_options_hash = self._hash_storage_options(storage_options)
⋮----
h_params = self.pipeline.pop("h_params") if self.pipeline.h_params else None
# Validate pipeline name to prevent directory traversal
⋮----
"""Helper function to load configuration.

    This is a convenience wrapper around Config.load().

    Args:
        base_dir (str): Base directory for configurations.
        name (str | None, optional): Project name. Defaults to None.
        pipeline_name (str | None, optional): Pipeline name. Defaults to None.
        storage_options (dict | Munch, optional): Options for filesystem. Defaults to empty Munch.
        fs (AbstractFileSystem | None, optional): Filesystem to use. Defaults to None.

    Returns:
        Config: Combined configuration instance.

    Example:
        ```python
        config = load(base_dir="my_project", name="test", pipeline_name="etl")
        ```
    """
⋮----
"""Helper function to save configuration.

    This is a convenience wrapper around Config.save().

    Args:
        config (Config): Configuration instance to save.
        project (bool, optional): Whether to save project config. Defaults to False.
        pipeline (bool, optional): Whether to save pipeline config. Defaults to True.
        fs (AbstractFileSystem | None, optional): Filesystem to use. Defaults to None.
        storage_options (dict | Munch, optional): Options for filesystem. Defaults to empty Munch.

    Example:
        ```python
        config = load(base_dir="my_project")
        save(config, project=True, pipeline=True)
        ```
    """
⋮----
"""Initialize a new configuration with both project and pipeline settings.

    This function creates and initializes both project and pipeline configurations,
    combining them into a single Config instance.

    Args:
        base_dir (str, optional): Base directory for configurations. Defaults to ".".
        name (str | None, optional): Project name. Defaults to None.
        pipeline_name (str | None, optional): Pipeline name. Defaults to None.
        fs (AbstractFileSystem | None, optional): Filesystem to use. Defaults to None.
        storage_options (dict | Munch, optional): Options for filesystem. Defaults to empty Munch.

    Returns:
        Config: The initialized configuration instance.

    Example:
        ```python
        config = init_config(
            base_dir="my_project",
            name="test_project",
            pipeline_name="data-pipeline",
        )
        ```
    """
pipeline_cfg = init_pipeline_config(
project_cfg = init_project_config(
⋮----
# Helper methods for centralized load/save logic
⋮----
"""Centralized configuration loading logic.
    
    Args:
        config_class: The configuration class to load.
        base_dir: Base directory for configurations.
        name: Configuration name.
        fs: Filesystem instance.
        storage_options: Options for filesystem.
        
    Returns:
        Loaded configuration instance.
    """
⋮----
def _save_pipeline_config(self) -> None
⋮----
"""Save pipeline configuration with proper handling of h_params."""
⋮----
def _save_project_config(self) -> None
⋮----
"""Save project configuration."""
````

## File: src/flowerpower/utils/misc.py
````python
# from collections.abc import Iterable
⋮----
# if importlib.util.find_spec("joblib"):
#     from joblib import Parallel, delayed
#     from rich.progress import (BarColumn, Progress, TextColumn,
#                                TimeElapsedColumn)
⋮----
#     def _prepare_parallel_args(
#         args: tuple, kwargs: dict
#     ) -> tuple[list, list, dict, dict, int]:
#         """Prepare and validate arguments for parallel execution.
⋮----
#         Args:
#             args: Positional arguments
#             kwargs: Keyword arguments
⋮----
#         Returns:
#             tuple: (iterables, fixed_args, iterable_kwargs, fixed_kwargs, first_iterable_len)
⋮----
#         Raises:
#             ValueError: If no iterable arguments or length mismatch
#         """
#         iterables = []
#         fixed_args = []
#         iterable_kwargs = {}
#         fixed_kwargs = {}
#         first_iterable_len = None
⋮----
#         # Process positional arguments
#         for arg in args:
#             if isinstance(arg, (list, tuple)) and not isinstance(arg[0], (list, tuple)):
#                 iterables.append(arg)
#                 if first_iterable_len is None:
#                     first_iterable_len = len(arg)
#                 elif len(arg) != first_iterable_len:
#                     raise ValueError(
#                         f"Iterable length mismatch: argument has length {len(arg)}, expected {first_iterable_len}"
#                     )
#             else:
#                 fixed_args.append(arg)
⋮----
#         # Process keyword arguments
#         for key, value in kwargs.items():
#             if isinstance(value, (list, tuple)) and not isinstance(
#                 value[0], (list, tuple)
#             ):
⋮----
#                     first_iterable_len = len(value)
#                 elif len(value) != first_iterable_len:
⋮----
#                         f"Iterable length mismatch: {key} has length {len(value)}, expected {first_iterable_len}"
⋮----
#                 iterable_kwargs[key] = value
⋮----
#                 fixed_kwargs[key] = value
⋮----
#         if first_iterable_len is None:
#             raise ValueError("At least one iterable argument is required")
⋮----
#         return iterables, fixed_args, iterable_kwargs, fixed_kwargs, first_iterable_len
⋮----
#     def _execute_parallel_with_progress(
#         func: callable,
#         iterables: list,
#         fixed_args: list,
#         iterable_kwargs: dict,
#         fixed_kwargs: dict,
#         param_combinations: list,
#         parallel_kwargs: dict,
#     ) -> list:
#         """Execute parallel tasks with progress tracking.
⋮----
#             func: Function to execute
#             iterables: List of iterable arguments
#             fixed_args: List of fixed arguments
#             iterable_kwargs: Dictionary of iterable keyword arguments
#             fixed_kwargs: Dictionary of fixed keyword arguments
#             param_combinations: List of parameter combinations
#             parallel_kwargs: Parallel execution configuration
⋮----
#             list: Results from parallel execution
⋮----
#         results = [None] * len(param_combinations)
#         with Progress(
#             TextColumn("[progress.description]{task.description}"),
#             BarColumn(),
#             "[progress.percentage]{task.percentage:>3.0f}%",
#             TimeElapsedColumn(),
#             transient=True,
#         ) as progress:
#             task = progress.add_task(
#                 "Running in parallel...", total=len(param_combinations)
#             )
⋮----
#             def wrapper(idx, param_tuple):
#                 res = func(
#                     *(list(param_tuple[: len(iterables)]) + fixed_args),
#                     **{
#                         k: v
#                         for k, v in zip(
#                             iterable_kwargs.keys(), param_tuple[len(iterables) :]
#                         )
#                     },
#                     **fixed_kwargs,
#                 )
#                 progress.update(task, advance=1)
#                 return idx, res
#
#             for idx, result in Parallel(**parallel_kwargs)(
#                 delayed(wrapper)(i, param_tuple)
#                 for i, param_tuple in enumerate(param_combinations)
⋮----
#                 results[idx] = result
#         return results
⋮----
#     def _execute_parallel_without_progress(
⋮----
#         """Execute parallel tasks without progress tracking.
⋮----
#         return Parallel(**parallel_kwargs)(
#             delayed(func)(
#                 *(list(param_tuple[: len(iterables)]) + fixed_args),
#                 **{
#                     k: v
#                     for k, v in zip(
#                         iterable_kwargs.keys(), param_tuple[len(iterables) :]
⋮----
#                 },
#                 **fixed_kwargs,
⋮----
#             for param_tuple in param_combinations
#         )
⋮----
#     def run_parallel(
⋮----
#         *args,
#         n_jobs: int = -1,
#         backend: str = "threading",
#         verbose: bool = True,
#         **kwargs,
#     ) -> list[any]:
#         """Runs a function for a list of parameters in parallel.
⋮----
#             func (Callable): function to run in parallel
#             *args: Positional arguments. Can be single values or iterables
#             n_jobs (int, optional): Number of joblib workers. Defaults to -1
#             backend (str, optional): joblib backend. Valid options are
#                 `loky`,`threading`, `mutliprocessing` or `sequential`. Defaults to "threading"
#             verbose (bool, optional): Show progress bar. Defaults to True
#             **kwargs: Keyword arguments. Can be single values or iterables
⋮----
#             list[any]: Function output
⋮----
#         Examples:
#             >>> # Single iterable argument
#             >>> run_parallel(func, [1,2,3], fixed_arg=42)
⋮----
#             >>> # Multiple iterables in args and kwargs
#             >>> run_parallel(func, [1,2,3], val=[7,8,9], fixed=42)
⋮----
#             >>> # Only kwargs iterables
#             >>> run_parallel(func, x=[1,2,3], y=[4,5,6], fixed=42)
⋮----
#         parallel_kwargs = {"n_jobs": n_jobs, "backend": backend, "verbose": 0}
⋮----
#         # Prepare and validate arguments
#         iterables, fixed_args, iterable_kwargs, fixed_kwargs, first_iterable_len = _prepare_parallel_args(
#             args, kwargs
⋮----
#         # Create parameter combinations
#         all_iterables = iterables + list(iterable_kwargs.values())
#         param_combinations = list(zip(*all_iterables))
⋮----
#         # Execute with or without progress tracking
#         if not verbose:
#             return _execute_parallel_without_progress(
#                 func, iterables, fixed_args, iterable_kwargs, fixed_kwargs,
#                 param_combinations, parallel_kwargs
⋮----
#         else:
#             return _execute_parallel_with_progress(
⋮----
# else:
⋮----
#     def run_parallel(*args, **kwargs):
#         raise ImportError("joblib not installed")
⋮----
"""Get the dataset partitions from the file path.

    Args:
        path (str): File path.
        partitioning (str | list[str] | None, optional): Partitioning type. Defaults to None.

    Returns:
        list[tuple]: Partitions.
    """
⋮----
path = os.path.dirname(path)
⋮----
parts = path.split("/")
⋮----
def _validate_image_format(format: str) -> str
⋮----
"""Validate image format to prevent injection attacks.
    
    Args:
        format: Image format to validate
        
    Returns:
        str: Validated format
        
    Raises:
        ValueError: If format is not supported
    """
allowed_formats = {"svg", "png", "jpg", "jpeg", "gif", "pdf", "html"}
⋮----
def _create_temp_image_file(data: str | bytes, format: str) -> str
⋮----
"""Create a temporary file with image data.
    
    Args:
        data: Image data as string or bytes
        format: Validated image format
        
    Returns:
        str: Path to temporary file
        
    Raises:
        OSError: If file creation fails
    """
⋮----
tmp_path = tmp.name
⋮----
# Validate the temporary file path for security
⋮----
def _open_image_viewer(tmp_path: str) -> None
⋮----
"""Open image viewer with the given file path.
    
    Args:
        tmp_path: Path to temporary image file
        
    Raises:
        OSError: If platform is not supported
        subprocess.CalledProcessError: If subprocess fails
        subprocess.TimeoutExpired: If subprocess times out
    """
⋮----
platform_system = platform.system()
⋮----
if platform_system == "Darwin":  # macOS
⋮----
def _cleanup_temp_file(tmp_path: str) -> None
⋮----
"""Clean up temporary file.
    
    Args:
        tmp_path: Path to temporary file to remove
    """
⋮----
pass  # File might already be deleted or in use
⋮----
def view_img(data: str | bytes, format: str = "svg")
⋮----
"""View image data using the system's default image viewer.
    
    Args:
        data: Image data as string or bytes
        format: Image format (svg, png, jpg, jpeg, gif, pdf, html)
        
    Raises:
        ValueError: If format is not supported
        RuntimeError: If file opening fails
        OSError: If platform is not supported
    """
# Validate format to prevent injection attacks
validated_format = _validate_image_format(format)
⋮----
# Create a temporary file with validated extension
tmp_path = _create_temp_image_file(data, validated_format)
⋮----
# Open image viewer with secure subprocess call
⋮----
# Clean up temp file on error
⋮----
# Optional: Remove the temp file after a delay
time.sleep(2)  # Wait for viewer to open
⋮----
"""
    Updates a msgspec.Struct instance with values from a dictionary.
    Handles nested msgspec.Struct objects and nested dictionaries.

    Args:
        obj: The msgspec.Struct object to update
        update_dict: Dictionary containing update values

    Returns:
        Updated msgspec.Struct instance
    """
# Convert the struct to a dictionary for easier manipulation
obj_dict = msgspec.to_builtins(struct)
⋮----
# Update the dictionary recursively
⋮----
# Handle nested dictionaries
⋮----
# Direct update for non-nested values
⋮----
# Convert back to the original struct type
⋮----
"""Helper function to update nested dictionaries"""
result = original.copy()
⋮----
# Recursively update nested dictionaries
⋮----
# Direct update
⋮----
def get_filesystem(fs: AbstractFileSystem | None = None, fs_type: str = "file") -> AbstractFileSystem
⋮----
"""
    Helper function to get a filesystem instance.
    
    Args:
        fs: An optional filesystem instance to use. If provided, this will be returned directly.
        fs_type: The type of filesystem to create if fs is None. Defaults to "file".
        
    Returns:
        An AbstractFileSystem instance.
    """
⋮----
fs = filesystem(fs_type)
````

## File: src/flowerpower/cfg/pipeline/run.py
````python
from requests.exceptions import HTTPError, ConnectionError, Timeout # Example exception
⋮----
DEPRECATED_RETRY_FIELDS = (
⋮----
def migrate_legacy_retry_fields(run_data: dict[str, Any]) -> bool
⋮----
"""Normalize legacy retry fields into nested retry configuration.

    Args:
        run_data: Raw run configuration dictionary loaded from YAML.

    Returns:
        True if the dictionary was mutated, otherwise False.
    """
⋮----
mutated = False
existing_retry = run_data.get("retry")
retry_block = existing_retry if isinstance(existing_retry, dict) else None
collected: dict[str, Any] = {}
⋮----
value = run_data.pop(field)
mutated = True
⋮----
value = int(value)
⋮----
value = float(value)
⋮----
value = [value]
⋮----
merged = retry_block.copy()
⋮----
class WithAdapterConfig(BaseConfig)
⋮----
hamilton_tracker: bool = msgspec.field(default=False)
mlflow: bool = msgspec.field(default=False)
# openlineage: bool = msgspec.field(default=False)
ray: bool = msgspec.field(default=False)
opentelemetry: bool = msgspec.field(default=False)
progressbar: bool = msgspec.field(default=False)
future: bool = msgspec.field(default=False)
⋮----
class ExecutorConfig(BaseConfig)
⋮----
type: str | None = msgspec.field(default=settings.EXECUTOR)
max_workers: int | None = msgspec.field(default=settings.EXECUTOR_MAX_WORKERS)
num_cpus: int | None = msgspec.field(default=settings.EXECUTOR_NUM_CPUS)
⋮----
class CallbackSpec(msgspec.Struct)
⋮----
"""Specification for a callback function with optional arguments."""
func: Callable
args: tuple | None = None
kwargs: dict | None = None
⋮----
class RetryConfig(BaseConfig)
⋮----
"""Retry configuration for pipeline execution."""
max_retries: int = msgspec.field(default=3)
retry_delay: float = msgspec.field(default=1.0)
jitter_factor: float | None = msgspec.field(default=0.1)
# Accept strings or classes; will be converted to exception classes in __post_init__
retry_exceptions: list[Any] = msgspec.field(default_factory=lambda: ["Exception"])  # type: ignore[assignment]
⋮----
def __post_init__(self)
⋮----
def _convert_exception_strings(self, exception_list: list) -> list
⋮----
"""Convert exception strings to actual exception classes using dynamic import.
        
        Args:
            exception_list: List of exception names or classes.
            
        Returns:
            List of exception classes.
        """
converted_exceptions = []
⋮----
exc_class = self._import_exception_class(exc)
⋮----
def _import_exception_class(self, exception_name: str) -> type
⋮----
"""Dynamically import an exception class by name."""
built_in_exceptions = {
⋮----
module = importlib.import_module(module_name)
⋮----
common_modules = [
⋮----
def to_dict(self) -> dict[str, Any]
⋮----
"""Convert RetryConfig to dictionary, properly handling exception classes.
        
        This ensures that exception classes are converted to their string names
        rather than their full string representation (e.g., "ValueError" instead of 
        "<class 'ValueError'>").
        """
data = super().to_dict()
⋮----
# Convert exception classes to their names for proper YAML serialization
⋮----
# Extract the class name from the full string representation
class_name = exc[8:-2]  # Remove "<class '" and "'>"
⋮----
class RunConfig(BaseConfig)
⋮----
inputs: dict | None = msgspec.field(default_factory=dict)
final_vars: list[str] | None = msgspec.field(default_factory=list)
config: dict | None = msgspec.field(default_factory=dict)
cache: dict | bool | None = msgspec.field(default=False)
with_adapter: WithAdapterConfig = msgspec.field(default_factory=WithAdapterConfig)
executor: ExecutorConfig = msgspec.field(default_factory=ExecutorConfig)
log_level: str | None = msgspec.field(default="INFO")
# New nested retry configuration
retry: RetryConfig | None = msgspec.field(default=None)
# Deprecated top-level retry fields (kept for backward compatibility)
⋮----
retry_delay: int | float = msgspec.field(default=1)
⋮----
retry_exceptions: list[str] = msgspec.field(default_factory=lambda: ["Exception"])  # type: ignore[assignment]
# New fields for comprehensive configuration
pipeline_adapter_cfg: dict | None = msgspec.field(default=None)
project_adapter_cfg: dict | None = msgspec.field(default=None)
adapter: dict[str, Any] | None = msgspec.field(default=None)
reload: bool = msgspec.field(default=False)
on_success: CallbackSpec | None = msgspec.field(default=None)
on_failure: CallbackSpec | None = msgspec.field(default=None)
⋮----
retry_data = data.get("retry")
⋮----
exceptions: list[Any] = []
⋮----
raw_exceptions = retry_data.get("retry_exceptions", [])
⋮----
# if isinstance(self.inputs, dict):
#     self.inputs = munchify(self.inputs)
⋮----
# Convert adapter instances if needed
⋮----
# Normalize retry configuration (prefer nested RetryConfig)
⋮----
# Build nested retry from (deprecated) top-level fields
⋮----
# Keep top-level fields in sync for backward compatibility
⋮----
# Ensure top-level exceptions reflect converted classes
⋮----
# Handle callback conversions
⋮----
# Handle on_failure callback conversions (mirror on_success behavior)
````

## File: src/flowerpower/cli/pipeline.py
````python
# Import necessary libraries
⋮----
app = typer.Typer(help="Pipeline management commands")
⋮----
# Note: common_options decorator removed as it was causing TypeError
# Options are now defined directly in each function's parameter list
⋮----
"""Parse common CLI options and return processed values."""
parsed_storage_options = parse_dict_or_list_param(storage_options, "dict")
# Ensure storage_options is always a dict, not None or list
⋮----
parsed_storage_options = {}
⋮----
# This should not happen with param_type="dict", but being safe
⋮----
"""
    Run a pipeline immediately.

    This command executes a pipeline with the specified configuration and inputs.
    The pipeline will run synchronously, and the command will wait for completion.

    Args:
        name: Name of the pipeline to run
        executor: Type of executor to use
        base_dir: Base directory containing pipelines and configurations
        inputs: Input parameters for the pipeline
        final_vars: Final variables to request from the pipeline
        config: Configuration for the Hamilton executor
        cache: Cache configuration for improved performance
        storage_options: Options for storage backends
        log_level: Set the logging level
        with_adapter: Configuration for adapters like trackers or monitors
        max_retries: Maximum number of retry attempts on failure
        retry_delay: Base delay between retries in seconds
        jitter_factor: Random factor applied to delay for jitter (0-1)

    Examples:
        # Run a pipeline with default settings
        $ pipeline run my_pipeline

        # Run with custom inputs
        $ pipeline run my_pipeline --inputs '{"data_path": "data/myfile.csv", "limit": 100}'

        # Specify which final variables to calculate
        $ pipeline run my_pipeline --final-vars '["output_table", "summary_metrics"]'

        # Configure caching
        $ pipeline run my_pipeline --cache '{"type": "memory", "ttl": 3600}'

        # Use a different executor
        $ pipeline run my_pipeline --executor distributed

        # Enable adapters for monitoring/tracking
        $ pipeline run my_pipeline --with-adapter '{"tracker": true, "opentelemetry": true}'

        # Set a specific logging level
        $ pipeline run my_pipeline --log-level debug

        # Configure automatic retries on failure
        $ pipeline run my_pipeline --max-retries 3 --retry-delay 2.0 --jitter-factor 0.2
    """
# Parse parameters with proper type handling
parsed_inputs = parse_dict_or_list_param(inputs, "dict") or {}
parsed_config = parse_dict_or_list_param(config, "dict") or {}
parsed_cache = parse_dict_or_list_param(cache, "dict") or {}
parsed_final_vars = parse_dict_or_list_param(final_vars, "list") or []
parsed_storage_options = parse_dict_or_list_param(storage_options, "dict") or {}
parsed_with_adapter = parse_dict_or_list_param(with_adapter, "dict") or {}
parsed_executor_cfg = parse_dict_or_list_param(executor_cfg, "dict") or {}
⋮----
# Ensure proper types for RunConfig
⋮----
parsed_inputs = {}
⋮----
parsed_config = {}
⋮----
parsed_cache = False
⋮----
parsed_final_vars = []
⋮----
parsed_with_adapter = {}
⋮----
# Ensure storage_options is a dict for FlowerPowerProject.load
⋮----
# Create WithAdapterConfig object if needed
⋮----
with_adapter_config = WithAdapterConfig.from_dict(parsed_with_adapter)
⋮----
with_adapter_config = WithAdapterConfig()
⋮----
# Use FlowerPowerProject for better consistency with the new architecture
project = FlowerPowerProject.load(
⋮----
# Construct RunConfig object from parsed CLI arguments
run_config = RunConfig(
⋮----
with_adapter=with_adapter_config,  # type: ignore
⋮----
# Handle executor configuration (type + config + convenience flags)
⋮----
# Validate type
⋮----
_ = project.run(name=name, run_config=run_config)
⋮----
"""
    Create a new pipeline structure.

    This command creates a new pipeline with the necessary directory structure,
    configuration file, and skeleton module file. It prepares all the required
    components for you to start implementing your pipeline logic.

    Args:
        name: Name for the new pipeline
        base_dir: Base directory to create the pipeline in
        storage_options: Options for storage backends
        log_level: Set the logging level
        overwrite: Whether to overwrite existing pipeline with the same name

    Examples:
        # Create a new pipeline with default settings
        $ pipeline new my_new_pipeline

        # Create a pipeline, overwriting if it exists
        $ pipeline new my_new_pipeline --overwrite

        # Create a pipeline in a specific directory
        $ pipeline new my_new_pipeline --base-dir /path/to/project
    """
⋮----
"""
    Delete a pipeline's configuration and/or module files.

    This command removes a pipeline's configuration file and/or module file from the project.
    If neither --cfg nor --module is specified, both will be deleted.

    Args:
        name: Name of the pipeline to delete
        base_dir: Base directory containing the pipeline
        cfg: Delete only the configuration file
        module: Delete only the pipeline module
        storage_options: Options for storage backends
        log_level: Set the logging level

    Examples:
        # Delete a pipeline (both config and module)
        $ pipeline delete my_pipeline

        # Delete only the configuration file
        $ pipeline delete my_pipeline --cfg

        # Delete only the module file
        $ pipeline delete my_pipeline --module
    """
⋮----
# If neither flag is set, default to deleting both
delete_cfg = cfg or not (cfg or module)
delete_module = module or not (cfg or module)
⋮----
deleted_parts = []
⋮----
"""
    Show the DAG (Directed Acyclic Graph) of a pipeline.

    This command generates and displays a visual representation of the pipeline's
    execution graph, showing how nodes are connected and dependencies between them.

    Args:
        name: Name of the pipeline to visualize
        base_dir: Base directory containing the pipeline
        storage_options: Options for storage backends
        log_level: Set the logging level
        format: Output format for the visualization

    Examples:
        # Show pipeline DAG in PNG format (default)
        $ pipeline show-dag my_pipeline

        # Generate SVG format visualization
        $ pipeline show-dag my_pipeline --format svg

        # Get raw graphviz object
        $ pipeline show-dag my_pipeline --format raw
    """
⋮----
is_raw = format.lower() == "raw"
⋮----
# Manager's show_dag likely handles rendering or returning raw object
⋮----
graph_or_none = manager.show_dag(
⋮----
# print(graph_or_none) # Or handle as needed
⋮----
"""
    Save the DAG (Directed Acyclic Graph) of a pipeline to a file.

    This command generates a visual representation of the pipeline's execution graph
    and saves it to a file in the specified format.

    Args:
        name: Name of the pipeline to visualize
        base_dir: Base directory containing the pipeline
        storage_options: Options for storage backends
        log_level: Set the logging level
        format: Output format for the visualization
        output_path: Custom file path to save the output (defaults to pipeline name)

    Examples:
        # Save pipeline DAG in PNG format (default)
        $ pipeline save-dag my_pipeline

        # Save in SVG format
        $ pipeline save-dag my_pipeline --format svg

        # Save to a custom location
        $ pipeline save-dag my_pipeline --output-path ./visualizations/my_graph.png
    """
⋮----
file_path = manager.save_dag(
⋮----
"""
    List all available pipelines in the project.

    This command displays a list of all pipelines defined in the project,
    providing an overview of what pipelines are available to run or schedule.

    Args:
        base_dir: Base directory containing pipelines
        storage_options: Options for storage backends
        log_level: Set the logging level
        format: Output format for the list (table, json, yaml)

    Examples:
        # List all pipelines in table format (default)
        $ pipeline show-pipelines

        # Output in JSON format
        $ pipeline show-pipelines --format json

        # List pipelines from a specific directory
        $ pipeline show-pipelines --base-dir /path/to/project
    """
⋮----
"""
    Show summary information for one or all pipelines.

    This command displays detailed information about pipelines including their
    configuration, code structure, and project context. You can view information
    for a specific pipeline or get an overview of all pipelines.

    Args:
        name: Name of specific pipeline to summarize (all if not specified)
        cfg: Include configuration details
        code: Include code/module details
        project: Include project context information
        base_dir: Base directory containing pipelines
        storage_options: Options for storage backends
        log_level: Set the logging level
        to_html: Generate HTML output instead of text
        to_svg: Generate SVG output (where applicable)
        output_file: File path to save the output instead of printing to console

    Examples:
        # Show summary for all pipelines
        $ pipeline show-summary

        # Show summary for a specific pipeline
        $ pipeline show-summary --name my_pipeline

        # Show only configuration information
        $ pipeline show-summary --name my_pipeline --cfg --no-code --no-project

        # Generate HTML report
        $ pipeline show-summary --to-html --output-file pipeline_report.html
    """
⋮----
# Assumes manager.show_summary handles printing/returning formatted output
summary_output = manager.show_summary(
⋮----
# Otherwise, assume manager printed the summary
⋮----
"""
    Add a hook to a pipeline configuration.

    This command adds a hook function to a pipeline's configuration. Hooks are functions
    that are called at specific points during pipeline execution to perform additional
    tasks like logging, monitoring, or data validation.

    Args:
        name: Name of the pipeline to add the hook to
        function_name: Name of the hook function (must be defined in the pipeline module)
        type: Type of hook (determines when the hook is called during execution)
        to: Target node or tag (required for node-specific hooks)
        base_dir: Base directory containing the pipeline
        storage_options: Options for storage backends
        log_level: Set the logging level

    Examples:
        # Add a post-run hook
        $ pipeline add-hook my_pipeline --function log_results

        # Add a pre-run hook
        $ pipeline add-hook my_pipeline --function validate_inputs --type PRE_RUN

        # Add a node-specific hook (executed before a specific node runs)
        $ pipeline add-hook my_pipeline --function validate_data --type NODE_PRE_EXECUTE --to data_processor

        # Add a hook for all nodes with a specific tag
        $ pipeline add-hook my_pipeline --function log_metrics --type NODE_POST_EXECUTE --to @metrics
    """
⋮----
# Validate 'to' argument for node hooks
````

## File: src/flowerpower/pipeline/io.py
````python
# mypy: disable-error-code="attr-defined"
# pylint: disable=no-member, E1136, W0212, W0201
"""
Manages the import and export of pipelines.
"""
⋮----
# Import necessary config types and utility functions
⋮----
console = Console()
⋮----
class PipelineIOManager
⋮----
"""Handles importing and exporting pipeline configurations and code."""
⋮----
"""
        Initializes the PipelineIOManager.

        Args:
            registry: The pipeline registry instance.
        """
⋮----
def _get_pipeline_files(self, name: str) -> list[str]
⋮----
"""Get the list of files for a single pipeline."""
⋮----
def _get_many_pipeline_files(self, names: list[str]) -> list[str]
⋮----
"""Get the list of files for multiple pipelines."""
files = ["conf/project.yml"]
⋮----
def _get_all_pipeline_files(self) -> list[str] | None
⋮----
"""Get all pipeline files (returns None to let _sync_filesystem auto-discover)."""
⋮----
def _print_import_success(self, names: list[str], src_base_dir: str) -> None
⋮----
"""Print success message for import operations."""
⋮----
def _print_export_success(self, names: list[str] | None, dest_base_dir: str) -> None
⋮----
"""Print success message for export operations."""
⋮----
"""
        Synchronizes the source and destination filesystems.

        Args:
            src_base_dir (str): The source base directory.
            dest_base_dir (str): The destination base directory.
            src_fs (AbstractFileSystem | None, optional): The source filesystem. Defaults to None.
            dest_fs (AbstractFileSystem | None, optional): The destination filesystem. Defaults to None.
            src_storage_options (dict | BaseStorageOptions | None, optional): Storage options for the source filesystem. Defaults to None.
            dest_storage_options (dict | BaseStorageOptions | None, optional): Storage options for the destination filesystem. Defaults to None.
            overwrite (bool, optional): Whether to overwrite existing files. Defaults to False.
        Returns:
            tuple: A tuple containing the source and destination filesystems.
        """
⋮----
def _get_filesystem(base_dir, fs, storage_options)
⋮----
fs = filesystem(base_dir, storage_options=storage_options)
⋮----
fs = DirFileSystem(base_dir, fs=fs)
⋮----
src_fs = _get_filesystem(src_base_dir, src_fs, src_storage_options)
⋮----
dest_fs = _get_filesystem(dest_base_dir, dest_fs, dest_storage_options)
⋮----
# try:
#     src_mapper = src_fs.get_mapper(check=True, create=True)
# except NotImplementedError:
⋮----
#     src_mapper = src_fs.get_mapper(check=True, create=False)
⋮----
#     src_mapper = src_fs.get_mapper(check=False, create=False)
⋮----
#     dest_mapper = dest_fs.get_mapper(check=True, create=False)
⋮----
#     raise NotImplementedError(
#         f"The destination filesystem {dest_fs }does not support get_mapper."
#     )
⋮----
files = src_fs.glob("**/*.py")
⋮----
content = src_fs.read_bytes(file)
⋮----
"""
        Import a pipeline from a given path.

        Args:
            name (str): The name of the pipeline.
            src_base_dir (str): The path of the flowerpower project directory.
            src_fs (AbstractFileSystem | None, optional): The source filesystem. Defaults to None.
            src_storage_options (BaseStorageOptions | None, optional): The storage options. Defaults to None.
            overwrite (bool, optional): Whether to overwrite an existing pipeline. Defaults to False.

        Returns:
            None

        Raises:
            ValueError: If the pipeline already exists and overwrite is False.

        Examples:
            ```python
            pm = PipelineManager()
            pm.import_pipeline("my_pipeline", "/path/to/pipeline")
            ```
        """
files = self._get_pipeline_files(name)
⋮----
"""
        Import multiple pipelines from given paths.

        Args:
            names (list[str]): A list of pipeline names to import.
            src_base_dir (str): The base path of the flowerpower project directory.
            src_fs (AbstractFileSystem | None, optional): The source filesystem. Defaults to None.
            src_storage_options (BaseStorageOptions | None, optional): The storage options. Defaults to None.
            overwrite (bool, optional): Whether to overwrite existing pipelines. Defaults to False.

        Returns:
            None

        Examples:
            ```python
            pm = PipelineManager()


            # Import multiple pipelines from a list
            pipelines_to_import = ["pipeline1", "pipeline2"]
            pm.import_many(pipelines_to_import, "/path/to/fp_project", overwrite=True)
            ```
        """
⋮----
files = self._get_many_pipeline_files(names)
⋮----
"""Import all pipelines from a given path.

        Args:
            src_base_dir (str): The base path containing pipeline modules and configurations.
            src_fs (AbstractFileSystem | None, optional): The source filesystem. Defaults to None.
            src_storage_options (BaseStorageOptions | None, optional): Storage options for the source path. Defaults to None.
            overwrite (bool, optional): Whether to overwrite existing pipelines. Defaults to False.

        Returns:
            None

        Examples:
            ```python
            pm = PipelineManager()
            # Import all pipelines from a local directory
            pm.import_all("/path/to/exported_pipelines", overwrite=True)
            # Import all pipelines from an S3 bucket
            # pm.import_all("s3://my-bucket/pipelines_backup", storage_options={"key": "...", "secret": "..."}, overwrite=False)
            ```
        """
files = self._get_all_pipeline_files()
⋮----
"""
        Export a pipeline to a given path.

        Args:
            name (str): The name of the pipeline.
            dest_base_dir (str): The destination path.
            dest_fs (AbstractFileSystem | None, optional): The destination filesystem. Defaults to None.
            dest_storage_options (BaseStorageOptions | None, optional): Storage options for the destination path. Defaults to None.
            overwrite (bool, optional): Whether to overwrite existing files at the destination. Defaults to False.

        Returns:
            None

        Raises:
            ValueError: If the pipeline does not exist or if the destination exists and overwrite is False.

        Examples:
            ```python
            pm = PipelineManager()
            pm.export("my_pipeline", "/path/to/export_dir")
            # Export to S3
            # pm.export("my_pipeline", "s3://my-bucket/exports", storage_options={"key": "...", "secret": "..."})
            ```
        """
⋮----
"""
        Export multiple pipelines to a directory.

        Args:
            pipelines (list[str]): A list of pipeline names to export.
            dest_base_dir (str): The destination directory path.
            dest_fs (AbstractFileSystem | None, optional): The destination filesystem. Defaults to None.
            dest_storage_options (BaseStorageOptions | None, optional): Storage options for the destination path. Defaults to None.
            overwrite (bool, optional): Whether to overwrite existing files at the destination. Defaults to False.

        Returns:
            None

        Examples:
            ```python
            pm = PipelineManager()
            pipelines_to_export = ["pipeline1", "pipeline2.subpipeline"]
            pm.export_many(pipelines_to_export, "/path/to/export_dir", overwrite=True)
            ```
        """
# Check if pipelines exist in the registry
⋮----
"""Export all pipelines to a given path.

        Args:
            dest_base_dir (str): The destination directory path.
            dest_fs (AbstractFileSystem | None, optional): The destination filesystem. Defaults to None.
            dest_storage_options (BaseStorageOptions | None, optional): Storage options for the destination path. Defaults to None.
            overwrite (bool, optional): Whether to overwrite existing files at the destination. Defaults to False.

        Returns:
            None

        Examples:
            ```python
            pm = PipelineManager()
            # Export all pipelines to a local directory
            pm.export_all("/path/to/backup_dir", overwrite=True)
            # Export all pipelines to S3
            # pm.export_all("s3://my-bucket/pipelines_backup", storage_options={"key": "...", "secret": "..."}, overwrite=False)
            ```
        """
````

## File: src/flowerpower/pipeline/registry.py
````python
"""Pipeline Registry for discovery, listing, creation, and deletion."""
⋮----
# Import necessary config types and utility functions
⋮----
# Assuming view_img might be used indirectly or needed later
⋮----
# Import base utilities
⋮----
class HookType(str, Enum)
⋮----
MQTT_BUILD_CONFIG = "mqtt-build-config"
⋮----
def default_function_name(self) -> str
⋮----
def __str__(self) -> str
⋮----
class CachedPipelineData(msgspec.Struct)
⋮----
"""Container for cached pipeline data."""
pipeline: "Pipeline"
config: PipelineConfig
module: Any
⋮----
class PipelineRegistry
⋮----
"""Manages discovery, listing, creation, and deletion of pipelines."""
⋮----
"""
        Initializes the PipelineRegistry.

        Args:
            project_cfg: The project configuration object.
            fs: The filesystem instance.
            base_dir: The base directory path.
            storage_options: Storage options for filesystem operations.
        """
⋮----
# Consolidated cache for pipeline data
⋮----
# Ensure module paths are added
⋮----
"""
        Create a PipelineRegistry from filesystem parameters.

        This factory method creates a complete PipelineRegistry instance by:
        1. Creating the filesystem if not provided
        2. Loading the ProjectConfig from the base directory
        3. Initializing the registry with the loaded configuration

        Args:
            base_dir: The base directory path for the FlowerPower project
            fs: Optional filesystem instance. If None, will be created from base_dir
            storage_options: Optional storage options for filesystem access

        Returns:
            PipelineRegistry: A fully configured registry instance

        Raises:
            ValueError: If base_dir is invalid or ProjectConfig cannot be loaded
            RuntimeError: If filesystem creation fails

        Example:
            ```python
            # Create registry from local directory
            registry = PipelineRegistry.from_filesystem("/path/to/project")

            # Create registry with S3 storage
            registry = PipelineRegistry.from_filesystem(
                "s3://my-bucket/project",
                storage_options={"key": "secret"}
            )
            ```
        """
# Create filesystem if not provided
⋮----
fs = filesystem(
⋮----
# Load project configuration
project_cfg = ProjectConfig.load(base_dir=base_dir, fs=fs)
⋮----
# Ensure we have a ProjectConfig instance
⋮----
# Create and return registry instance
⋮----
def _add_modules_path(self) -> None
⋮----
"""Add pipeline module paths to Python path."""
⋮----
project_path = self._fs._mapper.directory
modules_path = posixpath.join(project_path, self._pipelines_dir)
⋮----
# Use the base directory directly if not using cache
⋮----
project_path = self._fs.path
⋮----
project_path = self._base_dir
⋮----
# Fallback for mocked filesystems
project_path = "."
⋮----
# Handle case where filesystem is mocked or doesn't have required properties
⋮----
# --- Pipeline Factory Methods ---
⋮----
"""Get a Pipeline instance for the given name.

        This method creates a fully-formed Pipeline object by loading its configuration
        and Python module, then injecting the project context.

        Args:
            name: Name of the pipeline to get
            project_context: Reference to the FlowerPowerProject
            reload: Whether to reload configuration and module from disk

        Returns:
            Pipeline instance ready for execution

        Raises:
            FileNotFoundError: If pipeline configuration or module doesn't exist
            ImportError: If pipeline module cannot be imported
            ValueError: If pipeline configuration is invalid
        """
# Use cache if available and not reloading
⋮----
# Load pipeline configuration
config = self.load_config(name, reload=reload)
⋮----
# Load pipeline module
module = self.load_module(name, reload=reload)
⋮----
# Import Pipeline class here to avoid circular import
⋮----
# Create Pipeline instance
pipeline = Pipeline(
⋮----
# Cache the pipeline data
⋮----
def load_config(self, name: str, reload: bool = False) -> PipelineConfig
⋮----
"""Load pipeline configuration from disk.

        Args:
            name: Name of the pipeline
            reload: Whether to reload from disk even if cached

        Returns:
            PipelineConfig instance
        """
⋮----
# Load configuration from disk
config = PipelineConfig.load(
⋮----
# Cache the configuration (will be stored in consolidated cache when pipeline is created)
# For now, we'll create a temporary cache entry if it doesn't exist
⋮----
pipeline=None,  # type: ignore
⋮----
module=None,  # type: ignore
⋮----
def load_module(self, name: str, reload: bool = False) -> Any
⋮----
"""Load pipeline module from disk.

        Args:
            name: Name of the pipeline
            reload: Whether to reload from disk even if cached

        Returns:
            Loaded Python module
        """
⋮----
cached_data = self._pipeline_data_cache[name]
⋮----
# Convert pipeline name to module name
formatted_name = name.replace(".", "/").replace("-", "_")
module_name = f"pipelines.{formatted_name}"
⋮----
# Load the module
module = load_module(module_name, reload=reload)
⋮----
# Cache the module (will be stored in consolidated cache when pipeline is created)
# For now, we'll update the existing cache entry if it exists
⋮----
config=None,  # type: ignore
⋮----
def clear_cache(self, name: str | None = None)
⋮----
"""Clear cached pipelines, configurations, and modules.

        Args:
            name: If provided, clear cache only for this pipeline.
                 If None, clear entire cache.
        """
⋮----
# --- Methods moved from PipelineManager ---
def new(self, name: str, overwrite: bool = False)
⋮----
"""
        Adds a pipeline with the given name.

        Args:
            name (str): The name of the pipeline.
            overwrite (bool): Whether to overwrite an existing pipeline. Defaults to False.

        Raises:
            ValueError: If the configuration or pipeline path does not exist, or if the pipeline already exists.

        Examples:
            >>> pm = PipelineManager()
            >>> pm.new("my_pipeline")
        """
# Use attributes derived from self.project_cfg
⋮----
pipeline_file = posixpath.join(self._pipelines_dir, f"{formatted_name}.py")
cfg_file = posixpath.join(self._cfg_dir, PIPELINES_DIR, f"{formatted_name}.yml")
⋮----
def check_and_handle(path: str)
⋮----
# Ensure directories for the new files exist
⋮----
# Write pipeline code template
⋮----
# Create default pipeline config and save it directly
new_pipeline_cfg = PipelineConfig(name=name)
new_pipeline_cfg.save(fs=self._fs)  # Save only the pipeline part
⋮----
def delete(self, name: str, cfg: bool = True, module: bool = False)
⋮----
"""
        Delete a pipeline.

        Args:
            name (str): The name of the pipeline.
            cfg (bool, optional): Whether to delete the config file. Defaults to True.
            module (bool, optional): Whether to delete the module file. Defaults to False.

        Returns:
            None

        Raises:
            FileNotFoundError: If the specified files do not exist.

        Examples:
            >>> pm = PipelineManager()
            >>> pm.delete("my_pipeline")
        """
deleted_files = []
⋮----
pipeline_cfg_path = posixpath.join(
⋮----
)  # Changed to DEBUG
⋮----
pipeline_py_path = posixpath.join(self._pipelines_dir, f"{name}.py")
⋮----
# Sync filesystem if needed (using _fs)
⋮----
def _get_files(self) -> list[str]
⋮----
"""
        Get the list of pipeline files.

        Returns:
            list[str]: The list of pipeline files.
        """
⋮----
def _get_names(self) -> list[str]
⋮----
"""
        Get the list of pipeline names.

        Returns:
            list[str]: The list of pipeline names.
        """
files = self._get_files()
⋮----
"""
        Get a summary of the pipelines.

        Args:
            name (str | None, optional): The name of the pipeline. Defaults to None.
            cfg (bool, optional): Whether to show the configuration. Defaults to True.
            code (bool, optional): Whether to show the module. Defaults to True.
            project (bool, optional): Whether to show the project configuration. Defaults to True.
        Returns:
            dict[str, dict | str]: A dictionary containing the pipeline summary.

        Examples:
            ```python
            pm = PipelineManager()
            summary=pm.get_summary()
            ```
        """
⋮----
pipeline_names = [name]
⋮----
pipeline_names = self._get_names()
⋮----
summary = {}
⋮----
# Use self.project_cfg directly
⋮----
# Load pipeline config directly
⋮----
pipeline_summary = {}
⋮----
pipeline_cfg = PipelineConfig.load(name=name, fs=self._fs)
⋮----
module_content = self._fs.cat(
⋮----
if pipeline_summary:  # Only add if cfg or code was requested and found
⋮----
"""
        Show a summary of the pipelines.

        Args:
            name (str | None, optional): The name of the pipeline. Defaults to None.
            cfg (bool, optional): Whether to show the configuration. Defaults to True.
            code (bool, optional): Whether to show the module. Defaults to True.
            project (bool, optional): Whether to show the project configuration. Defaults to True.
            to_html (bool, optional): Whether to export the summary to HTML. Defaults to False.
            to_svg (bool, optional): Whether to export the summary to SVG. Defaults to False.

        Returns:
            None | str: The summary of the pipelines. If `to_html` is True, returns the HTML string.
                If `to_svg` is True, returns the SVG string.

        Examples:
            ```python
            pm = PipelineManager()
            pm.show_summary()
            ```
        """
⋮----
summary = self.get_summary(name=name, cfg=cfg, code=code, project=project)
project_summary = summary.get("project", {})
pipeline_summary = summary["pipelines"]
⋮----
def add_dict_to_tree(tree, dict_data, style="green")
⋮----
branch = tree.add(f"[cyan]{key}:", style="bold cyan")
⋮----
console = Console()
⋮----
# Create tree for project config
project_tree = Tree("📁 Project Configuration", style="bold magenta")
⋮----
# Print project configuration
⋮----
# Create tree for config
config_tree = Tree("📋 Pipeline Configuration", style="bold magenta")
⋮----
# Create syntax-highlighted code view
code_view = Syntax(
⋮----
# console.print(f"🔄 Pipeline: {pipeline}", style="bold blue")
⋮----
@property
    def summary(self) -> dict[str, dict | str]
⋮----
"""
        Get a summary of the pipelines.

        Returns:
            dict: A dictionary containing the pipeline summary.
        """
⋮----
"""
        Print all available pipelines in a formatted table.

        Args:
            show (bool, optional): Whether to print the table. Defaults to True.
            to_html (bool, optional): Whether to export the table to HTML. Defaults to False.
            to_svg (bool, optional): Whether to export the table to SVG. Defaults to False.

        Returns:
            list[str] | None: A list of pipeline names if `show` is False.

        Examples:
            ```python
            pm = PipelineManager()
            all_pipelines = pm._pipelines(show=False)
            ```
        """
⋮----
show = True
⋮----
pipeline_files = [
pipeline_names = [
⋮----
]  # Simplified name extraction
⋮----
return []  # Return empty list for consistency
⋮----
pipeline_info = []
⋮----
mod_time = self._fs.modified(path).strftime("%Y-%m-%d %H:%M:%S")
⋮----
mod_time = "N/A"
⋮----
size_bytes = self._fs.size(path)
size = f"{size_bytes / 1024:.1f} KB" if size_bytes else "0.0 KB"
⋮----
size = "N/A"
⋮----
size = "Error"
⋮----
table = Table(title="Available Pipelines")
⋮----
console = Console(record=True)
⋮----
def show_pipelines(self) -> None
⋮----
"""
        Print all available pipelines in a formatted table.

        Examples:
            ```python
            pm = PipelineManager()
            pm.show_pipelines()
            ```
        """
⋮----
def list_pipelines(self) -> list[str]
⋮----
"""
        Get a list of all available pipelines.

        Returns:
            list[str] | None: A list of pipeline names.

        Examples:
            ```python
            pm = PipelineManager()
            pipelines = pm.list_pipelines()
            ```
        """
⋮----
@property
    def pipelines(self) -> list[str]
⋮----
"""
        Get a list of all available pipelines.

        Returns:
            list[str] | None: A list of pipeline names.

        Examples:
            ```python
            pm = PipelineManager()
            pipelines = pm.pipelines
            ```
        """
⋮----
"""
        Add a hook to the pipeline module.

        Args:
            name (str): The name of the pipeline
            type (HookType): The type of the hook.
            to (str | None, optional): The name of the file to add the hook to. Defaults to the hook.py file in the pipelines hooks folder.
            function_name (str | None, optional): The name of the function. If not provided uses default name of hook type.

        Returns:
            None

        Examples:
            ```python
            pm = PipelineManager()
            pm.add_hook(HookType.PRE_EXECUTE)
            ```
        """
⋮----
to = f"hooks/{name}/hook.py"
⋮----
to = f"hooks/{name}/{to}"
⋮----
template = HOOK_TEMPLATE__MQTT_BUILD_CONFIG
⋮----
function_name = type.default_function_name()
⋮----
"""Create a new pipeline.

        This method provides compatibility with the lifecycle manager interface.
        Additional parameters (template, tags, description) are currently not used.

        Args:
            name: Name of the pipeline to create
            overwrite: Whether to overwrite existing pipeline
            template: Template to use (not currently implemented)
            tags: Tags for the pipeline (not currently implemented)
            description: Description of the pipeline (not currently implemented)
        """
⋮----
"""Delete a pipeline.

        This method provides compatibility with the lifecycle manager interface.

        Args:
            name: Name of the pipeline to delete
            cfg: Whether to delete configuration files
            module: Whether to delete module files
        """
````

## File: src/flowerpower/cfg/pipeline/__init__.py
````python
class PipelineConfig(BaseConfig)
⋮----
"""Configuration class for managing pipeline settings in FlowerPower.

    This class handles pipeline-specific configuration including run settings, scheduling,
    parameters, and adapter settings. It supports Hamilton-style parameter configuration
    and YAML serialization.

    Attributes:
        name (str | None): The name of the pipeline.
        run (RunConfig): Configuration for pipeline execution.
        params (dict): Pipeline parameters.
        adapter (AdapterConfig): Configuration for the pipeline adapter.
        h_params (dict): Hamilton-formatted parameters.

    Example:
        ```python
        # Create a new pipeline config
        pipeline = PipelineConfig(name="data-transform")

        # Set parameters
        pipeline.params = {
            "input_path": "data/input",
            "batch_size": 100
        }

        # Save configuration
        pipeline.save(name="data-transform")
        ```
    """
⋮----
name: str | None = msgspec.field(default=None)
run: RunConfig = msgspec.field(default_factory=RunConfig)
params: dict = msgspec.field(default_factory=dict)
adapter: AdapterConfig = msgspec.field(default_factory=AdapterConfig)
h_params: dict = msgspec.field(default_factory=dict)
⋮----
def __post_init__(self)
⋮----
# Validate pipeline name if provided
⋮----
def to_yaml(self, path: str, fs: AbstractFileSystem)
⋮----
"""Save pipeline configuration to YAML file.
        
        Args:
            path: Path to the YAML file.
            fs: Filesystem instance.
            
        Raises:
            ConfigSaveError: If saving the configuration fails.
            ConfigPathError: If the path contains directory traversal attempts.
        """
⋮----
# Validate the path to prevent directory traversal
validated_path = validate_file_path(path)
⋮----
d = self.to_dict()
⋮----
@classmethod
    def from_dict(cls, name: str, data: dict | Munch)
⋮----
# Handle null params field by converting to empty dict
# This fixes the issue where YAML parses empty sections with comments as null
⋮----
instance = msgspec.convert(data, cls)
# Manually call __post_init__ since msgspec.convert doesn't call it
⋮----
@classmethod
    def from_yaml(cls, name: str, path: str, fs: AbstractFileSystem)
⋮----
"""Load pipeline configuration from YAML file.
        
        Args:
            name: Pipeline name.
            path: Path to the YAML file.
            fs: Filesystem instance.
            
        Returns:
            Loaded pipeline configuration.
            
        Raises:
            ConfigLoadError: If loading the configuration fails.
            ConfigPathError: If the path contains directory traversal attempts.
        """
⋮----
raw = yaml.safe_load(f) or {}
data = interpolate_env_in_data(raw)
⋮----
migrated = False
⋮----
migrated = migrate_legacy_retry_fields(data['run'])
⋮----
pipeline = cls.from_dict(name=name, data=data)
⋮----
def update(self, d: dict | Munch)
⋮----
# Safe attribute access instead of eval()
⋮----
# self.params = munchify(self.params)
⋮----
@staticmethod
    def to_h_params(d: dict) -> dict
⋮----
"""Convert a dictionary of parameters to Hamilton-compatible format.

        This method transforms regular parameter dictionaries into Hamilton's function parameter
        format, supporting nested parameters and source/value decorators.

        Args:
            d (dict): The input parameter dictionary.

        Returns:
            dict: Hamilton-formatted parameter dictionary.

        Example:
            ```python
            params = {
                "batch_size": 100,
                "paths": {"input": "data/in", "output": "data/out"}
            }
            h_params = PipelineConfig.to_h_params(params)
            ```
        """
⋮----
def transform_recursive(val, original_dict, depth=1)
⋮----
# If we're at depth 3, wrap the entire dictionary in value()
⋮----
# Otherwise, continue recursing
⋮----
# If it's a string and matches a key in the original dictionary
⋮----
# For non-dictionary values at depth 3
⋮----
# For all other values
⋮----
result = {k: {k: d[k]} for k in d}  # Step 1: Wrap each parameter in its own dict
⋮----
# Step 2: Transform each parameter value recursively
⋮----
"""Load pipeline configuration from a YAML file.

        Args:
            base_dir (str, optional): Base directory for the pipeline. Defaults to ".".
            name (str | None, optional): Pipeline name. Defaults to None.
            fs (AbstractFileSystem | None, optional): Filesystem to use. Defaults to None.
            storage_options (dict | Munch, optional): Options for filesystem. Defaults to empty Munch.

        Returns:
            PipelineConfig: Loaded pipeline configuration.

        Example:
            ```python
            pipeline = PipelineConfig.load(
                base_dir="my_project",
                name="data-pipeline"
            )
            ```
        """
⋮----
# Use cached filesystem for better performance
storage_options_hash = cls._hash_storage_options(storage_options)
fs = cls._get_cached_filesystem(base_dir, storage_options_hash)
⋮----
pipeline = PipelineConfig.from_yaml(
⋮----
pipeline = PipelineConfig(name=name)
⋮----
# Helper methods for centralized load/save logic
⋮----
@classmethod
    def _load_pipeline_config(cls, base_dir: str, name: str | None, fs: AbstractFileSystem) -> "PipelineConfig"
⋮----
"""Centralized pipeline configuration loading logic.
        
        Args:
            base_dir: Base directory for the pipeline.
            name: Pipeline name.
            fs: Filesystem instance.
            
        Returns:
            Loaded pipeline configuration.
        """
⋮----
pipeline = cls.from_yaml(
⋮----
pipeline = cls(name=name)
⋮----
def _save_pipeline_config(self, fs: AbstractFileSystem) -> None
⋮----
"""Centralized pipeline configuration saving logic.
        
        Args:
            fs: Filesystem instance.
        """
h_params = getattr(self, "h_params")
⋮----
def _validate_pipeline_name(self) -> None
⋮----
"""Validate pipeline name parameter.
        
        Raises:
            ValueError: If pipeline name contains invalid characters.
        """
⋮----
# Check for directory traversal attempts
⋮----
# Check for empty string
⋮----
"""Save pipeline configuration to a YAML file.

        Args:
            name (str | None, optional): Pipeline name. Defaults to None.
            base_dir (str, optional): Base directory for the pipeline. Defaults to ".".
            fs (AbstractFileSystem | None, optional): Filesystem to use. Defaults to None.
            storage_options (dict | Munch, optional): Options for filesystem. Defaults to empty Munch.

        Raises:
            ValueError: If pipeline name is not set.

        Example:
            ```python
            pipeline_config.save(name="data-pipeline", base_dir="my_project")
            ```
        """
⋮----
storage_options_hash = self._hash_storage_options(storage_options)
fs = self._get_cached_filesystem(base_dir, storage_options_hash)
⋮----
# Validate pipeline name to prevent directory traversal
⋮----
"""Initialize a new pipeline configuration.

    This function creates a new pipeline configuration and saves it to disk.

    Args:
        base_dir (str, optional): Base directory for the pipeline. Defaults to ".".
        name (str | None, optional): Pipeline name. Defaults to None.
        fs (AbstractFileSystem | None, optional): Filesystem to use. Defaults to None.
        storage_options (dict | Munch, optional): Options for filesystem. Defaults to empty Munch.

    Returns:
        PipelineConfig: The initialized pipeline configuration.

    Example:
        ```python
        pipeline = init_pipeline_config(
            base_dir="my_project",
            name="etl-pipeline"
        )
        ```
    """
pipeline = PipelineConfig.load(
````

## File: src/flowerpower/pipeline/pipeline.py
````python
"""Active Pipeline class for FlowerPower."""
⋮----
h_opentelemetry = None
init_tracer = None
⋮----
h_mlflow = None
⋮----
distributed = None
⋮----
# from hamilton.plugins import h_ray
h_ray = None
⋮----
ray = None
⋮----
class Pipeline(msgspec.Struct)
⋮----
"""Active pipeline object that encapsulates its own execution logic.

    This class represents a single pipeline with its configuration, loaded module,
    and project context. It is responsible for its own execution, including
    setting up Hamilton drivers, managing adapters, and handling retries.

    Attributes:
        name: The name of the pipeline
        config: The pipeline configuration
        module: The loaded Python module containing Hamilton functions
        project_context: Reference to the FlowerPowerProject
    """
⋮----
name: str
config: PipelineConfig
module: Any
project_context: FlowerPowerProject
_adapter_manager: Any = None
_executor_factory: Any = None
⋮----
def __post_init__(self)
⋮----
"""Initialize Hamilton settings and utility managers."""
⋮----
# Initialize utility managers
⋮----
def run(self, run_config: RunConfig | None = None, **kwargs) -> dict[str, Any]
⋮----
"""Execute the pipeline with the given parameters.

        Args:
            run_config: Run configuration object containing all execution parameters.
                       If None, uses the pipeline's default configuration.
            **kwargs: Additional parameters to override or extend the run_config.

        Returns:
            The result of executing the pipeline
        """
start_time = dt.datetime.now()
⋮----
# Initialize run_config with pipeline defaults if not provided
run_config = run_config or self.config.run
⋮----
# Merge kwargs into the run_config
⋮----
run_config = merge_run_config_with_kwargs(run_config, kwargs)
⋮----
# Reload module if requested
⋮----
# Set up retry configuration (use nested RetryConfig)
retry_cfg = run_config.retry or self.config.run.retry
retry_config = self._setup_retry_config(
max_retries = retry_config["max_retries"]
retry_delay = retry_config["retry_delay"]
jitter_factor = retry_config["jitter_factor"]
retry_exceptions = retry_config["retry_exceptions"]
⋮----
# Execute with retry logic
⋮----
"""Set up retry configuration with defaults and validation."""
cfg = self.config.run.retry
max_retries = max_retries if max_retries is not None else (cfg.max_retries if cfg else 0)
retry_delay = retry_delay if retry_delay is not None else (cfg.retry_delay if cfg else 1.0)
jitter_factor = jitter_factor if jitter_factor is not None else (cfg.jitter_factor if cfg else 0.1)
⋮----
# Convert string exceptions to actual exception classes
⋮----
converted_exceptions = []
# Safe mapping of exception names to classes
exception_mapping = {
⋮----
exc_class = exception_mapping.get(exc)
⋮----
retry_exceptions = tuple(converted_exceptions)
⋮----
retry_exceptions = (Exception,)
⋮----
"""Execute pipeline with retry logic."""
⋮----
result = self._execute_pipeline(run_config=run_config)
⋮----
end_time = dt.datetime.now()
duration = humanize.naturaldelta(end_time - start_time)
⋮----
# Execute success callback if provided
⋮----
delay = retry_delay * (2**attempt)
jitter = delay * jitter_factor * random.random()
total_delay = delay + jitter
⋮----
# Execute failure callback if provided
⋮----
# Execute failure callback if provided
⋮----
"""Set up executor and adapters for pipeline execution."""
# Get executor and adapters
⋮----
adapters = self._get_adapters(
⋮----
"""Execute the pipeline with Hamilton."""
# Set up execution context
⋮----
synchronous_executor = True
⋮----
synchronous_executor = False
allow_experimental_mode = True
⋮----
# Create Hamilton driver
dr = (
⋮----
dr = dr.with_remote_executor(executor)
⋮----
dr = dr.build()
⋮----
# Execute the pipeline
result = dr.execute(
⋮----
# Clean up executor if needed
⋮----
"""Get the executor based on the provided configuration."""
⋮----
# Merge with default configuration (prefer explicit runtime overrides)
⋮----
override_raw = executor_cfg
⋮----
pass  # keep raw string
⋮----
pass  # keep raw dict
⋮----
# Prefer explicit override fields over YAML defaults
⋮----
executor_cfg = prefer_executor_override(
⋮----
# Fallback to existing merge behavior on any unexpected error
⋮----
# Normalize then merge
norm = (
executor_cfg = self.config.run.executor.merge(norm)
⋮----
executor_cfg = self.config.run.executor.merge(override_raw)
⋮----
executor_cfg = self.config.run.executor
⋮----
# Create executor using factory
executor = self._executor_factory.create_executor(executor_cfg)
⋮----
# Handle special cleanup for certain executor types
cleanup_fn = None
⋮----
# Handle temporary case where project_context is PipelineManager
project_cfg = getattr(self.project_context, "project_cfg", None) or getattr(
⋮----
cleanup_fn = (
⋮----
"""Set up the adapters for the pipeline."""
⋮----
# Resolve adapter configurations using the adapter manager
with_adapter_cfg = self._adapter_manager.resolve_with_adapter_config(
⋮----
pipeline_adapter_cfg = self._adapter_manager.resolve_pipeline_adapter_config(
⋮----
project_adapter_cfg = self._adapter_manager.resolve_project_adapter_config(
⋮----
# Create adapters
adapters = self._adapter_manager.create_adapters(
⋮----
# Add any additional adapters
⋮----
"""Execute a callback function with proper error handling."""
⋮----
args = args or ()
kwargs = kwargs or {}
⋮----
def _reload_module(self)
⋮----
"""Reload the pipeline module."""
````

## File: src/flowerpower/flowerpower.py
````python
def handle_errors(func)
⋮----
"""Decorator to handle exceptions, log them, and re-raise as RuntimeError."""
⋮----
@wraps(func)
    def wrapper(self, *args, **kwargs)
⋮----
# Extract operation name from function name for better logging
operation_name = func.__name__.replace('_', ' ').title()
# For methods like 'run', we want to log the pipeline name if available
⋮----
class FlowerPowerProject
⋮----
"""
        Initialize a FlowerPower project.
        Args:
            pipeline_manager (PipelineManager | None): Instance of PipelineManager to manage pipelines.
        """
⋮----
def _validate_pipeline_name(self, name: str) -> None
⋮----
"""Validate the pipeline name argument using security utilities."""
validate_pipeline_name(name)  # Use secure validation function
⋮----
def _inject_dependencies(self)
⋮----
"""Inject dependencies between managers for proper architecture.

        This method establishes the correct dependency flow:
        - Project context is properly established for pipeline execution
        """
# Store project reference for pipeline context
# This will be used when creating Pipeline instances
⋮----
# --- Convenience Methods for Pipeline Operations ---
⋮----
"""Execute a pipeline synchronously and return its results.

        This is a convenience method that delegates to the pipeline manager.
        It provides the same functionality as `self.pipeline_manager.run()`.

        Args:
            name: Name of the pipeline to run. Must be a valid identifier.
            run_config: Run configuration object containing all execution parameters.
                If None, the default configuration from the pipeline will be used.
            **kwargs: Additional parameters to override the run_config. Supported parameters include:
                inputs (dict | None): Override pipeline input values. Example: {"data_date": "2025-04-28"}
                final_vars (list[str] | None): Specify which output variables to return.
                    Example: ["model", "metrics"]
                config (dict | None): Configuration for Hamilton pipeline executor.
                    Example: {"model": "LogisticRegression"}
                cache (dict | None): Cache configuration for results. Example: {"recompute": ["node1", "final_node"]}
                executor_cfg (str | dict | ExecutorConfig | None): Execution configuration, can be:
                    - str: Executor name, e.g. "threadpool", "local"
                    - dict: Raw config, e.g. {"type": "threadpool", "max_workers": 4}
                    - ExecutorConfig: Structured config object
                with_adapter_cfg (dict | WithAdapterConfig | None): Adapter settings for pipeline execution.
                    Example: {"opentelemetry": True, "tracker": False}
                pipeline_adapter_cfg (dict | PipelineAdapterConfig | None): Pipeline-specific adapter settings.
                    Example: {"tracker": {"project_id": "123", "tags": {"env": "prod"}}}
                project_adapter_cfg (dict | ProjectAdapterConfig | None): Project-level adapter settings.
                    Example: {"opentelemetry": {"host": "http://localhost:4317"}}
                adapter (dict[str, Any] | None): Custom adapter instance for pipeline
                    Example: {"ray_graph_adapter": RayGraphAdapter()}
                reload (bool): Force reload of pipeline configuration.
                log_level (str | None): Logging level for the execution. Default None uses project config.
                    Valid values: "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
                max_retries (int): Maximum number of retries for execution.
                retry_delay (float): Delay between retries in seconds.
                jitter_factor (float): Random jitter factor to add to retry delay
                retry_exceptions (tuple): Exceptions that trigger a retry.
                on_success (Callable | tuple[Callable, tuple | None, dict | None] | None): Callback to run on successful pipeline execution.
                on_failure (Callable | tuple[Callable, tuple | None, dict | None] | None): Callback to run on pipeline execution failure.

        Returns:
            dict[str, Any]: Pipeline execution results, mapping output variable names to their computed values.

        Raises:
            ValueError: If pipeline name doesn't exist or configuration is invalid
            ImportError: If pipeline module cannot be imported
            RuntimeError: If execution fails due to pipeline or adapter errors

        Example:
            ```python
            project = FlowerPowerProject.load(".")

            # Simple execution
            result = project.run("my_pipeline")

            # Run with custom RunConfig
            from flowerpower.cfg.pipeline.run import RunConfig
            config = RunConfig(inputs={"date": "2025-04-28"}, final_vars=["result"])
            result = project.run("ml_pipeline", run_config=config)

            # Complex run with kwargs overrides
            result = project.run(
                "ml_pipeline",
                inputs={"training_date": "2025-04-28"},
                final_vars=["model", "metrics"],
                executor_cfg={"type": "threadpool", "max_workers": 4},
                with_adapter_cfg={"tracker": True},
                reload=True
            )
            ```
        """
# Validate pipeline manager is available
⋮----
# Validate required arguments
⋮----
# Initialize run_config - use provided config or create empty one
run_config = run_config or RunConfig()
⋮----
# Merge kwargs into run_config
⋮----
run_config = merge_run_config_with_kwargs(run_config, kwargs)
⋮----
@staticmethod
    def _check_project_exists(base_dir: str, fs: AbstractFileSystem | None = None) -> tuple[bool, str]
⋮----
fs = filesystem(base_dir, dirfs=True)
⋮----
# Determine the root path for existence checks
# For DirFileSystem, paths are relative to its root, so we check "." for the project root.
# For other filesystems, we use the base_dir directly.
root_path = "." if isinstance(fs, DirFileSystem) else base_dir
⋮----
# Check for required subdirectories
config_path = posixpath.join(root_path, settings.CONFIG_DIR)
pipelines_path = posixpath.join(root_path, settings.PIPELINES_DIR)
⋮----
"""
        Load an existing FlowerPower project.
        If the project does not exist, it will raise an error.

        Args:
            base_dir (str | None): The base directory of the project. If None, it defaults to the current working directory.
            storage_options (dict | BaseStorageOptions | None): Storage options for the filesystem.
            fs (AbstractFileSystem | None): An instance of AbstractFileSystem to use for file operations.
            log_level (str | None): The logging level to set for the project. If None, it uses the default log level.

        Returns:
            FlowerPowerProject: An instance of FlowerPowerProject if the project exists, otherwise None.
        Raises:
            FileNotFoundError: If the project does not exist at the specified base directory.
        """
⋮----
base_dir = base_dir or str(Path.cwd())
⋮----
cached = True
cache_storage = posixpath.join(
⋮----
cached = False
cache_storage = None
⋮----
fs = filesystem(
⋮----
pipeline_manager = PipelineManager(
⋮----
# Create the project instance
project = cls(
⋮----
# Inject dependencies after creation to avoid circular imports
⋮----
"""
        Initialize a new FlowerPower project.

        Args:
            name (str | None): The name of the project. If None, it defaults to the current directory name.
            base_dir (str | None): The base directory where the project will be created. If None, it defaults to the current working directory.
            storage_options (dict | BaseStorageOptions | None): Storage options for the filesystem.
            fs (AbstractFileSystem | None): An instance of AbstractFileSystem to use for file operations.
            hooks_dir (str): The directory where the project hooks will be stored.
            overwrite (bool): Whether to overwrite an existing project at the specified base directory.
        Returns:
            FlowerPowerProject: An instance of FlowerPowerProject initialized with the new project.
        Raises:
            FileExistsError: If the project already exists at the specified base directory and overwrite is False.
        """
⋮----
# Initialize project parameters
⋮----
# Setup filesystem
fs = cls._setup_filesystem(base_dir, storage_options, fs)
⋮----
# Handle existing project
⋮----
# Create project structure
⋮----
# Initialize project configuration
⋮----
# Print success message and getting started guide
⋮----
"""Resolve project name and base directory."""
⋮----
name = str(Path.cwd().name)
base_dir = posixpath.join(str(Path.cwd().parent), name)
⋮----
base_dir = posixpath.join(str(Path.cwd()), name)
⋮----
"""Setup filesystem for project operations."""
⋮----
"""Handle existing project directory."""
⋮----
# Use FilesystemHelper to clean existing files
fs_helper = FilesystemHelper(base_dir)
⋮----
error_msg = f"Project already exists at {base_dir}. Use overwrite=True to overwrite the existing project."
⋮----
"""Create project directory structure."""
⋮----
"""Initialize project configuration and create README."""
# Load project configuration
cfg = ProjectConfig.load(name=name, fs=fs)
⋮----
# Create README file
⋮----
# Save configuration
⋮----
@classmethod
    def _print_success_message(cls, name: str, base_dir: str) -> None
⋮----
"""Print success message and getting started guide."""
⋮----
"""
    Initialize a new FlowerPower project.
    
    
    This is a standalone function that directly calls FlowerPowerProject.new
    with the same arguments, providing easier, separately importable access.
    
    Args:
        name (str | None): The name of the project. If None, it defaults to the current directory name.
        base_dir (str | None): The base directory where the project will be created. If None, it defaults to the current working directory.
        storage_options (dict | BaseStorageOptions | None): Storage options for the filesystem.
        fs (AbstractFileSystem | None): An instance of AbstractFileSystem to use for file operations.
        hooks_dir (str): The directory where the project hooks will be stored.
        log_level (str | None): The logging level to set for the project.
    
    Returns:
        FlowerPowerProject: An instance of FlowerPowerProject initialized with the new project.
    """
⋮----
# Note: _check_project_exists expects base_dir to be a string.
# If base_dir is None, it will be handled by _check_project_exists or the load/init methods.
# We pass fs directly, as _check_project_exists can handle fs being None.
⋮----
error_message = "Project does not exist. Use `initialize_project()` or `FlowerPowerProject.new()` to create it."
⋮----
# Alias for backward compatibility or alternative naming
FlowerPower = create_project
⋮----
# The standalone init function is removed as it was a direct pass-through
# to FlowerPowerProject.new(). Users can now use FlowerPowerProject.new() directly
# or the new create_project() function which handles both loading and initialization.
````

## File: src/flowerpower/pipeline/manager.py
````python
Digraph = Any  # Type alias for when graphviz isn't installed
⋮----
GraphType = TypeVar("GraphType")  # Type variable for graphviz.Digraph
⋮----
class PipelineManager
⋮----
"""Central manager for FlowerPower pipeline operations.

    This class provides a unified interface for managing pipelines, including:
    - Configuration management and loading
    - Pipeline creation, deletion, and discovery
    - Pipeline execution via PipelineRunner
    - Visualization via PipelineVisualizer
    - Import/export operations via PipelineIOManager

    Attributes:
        registry (PipelineRegistry): Handles pipeline registration and discovery
        visualizer (PipelineVisualizer): Handles pipeline visualization
        io (PipelineIOManager): Manages pipeline import/export operations
        project_cfg (ProjectConfig): Current project configuration
        pipeline_cfg (PipelineConfig): Current pipeline configuration
        pipelines (list[str]): List of available pipeline names
        current_pipeline_name (str): Name of the currently loaded pipeline
        summary (dict[str, dict | str]): Summary of all pipelines

    Example:
        >>> from flowerpower.pipeline import PipelineManager
        >>>
        >>> # Create manager with default settings
        >>> manager = PipelineManager()
        >>>
        >>> # Create manager with custom settings
        >>> manager = PipelineManager(
        ...     base_dir="/path/to/project",
        ...     log_level="DEBUG"
        ... )
    """
⋮----
"""Initialize the PipelineManager.

        Args:
            base_dir: Root directory for the FlowerPower project. Defaults to current
                working directory if not specified.
            storage_options: Configuration options for filesystem access. Can be:
                - dict: Raw key-value options
                - Munch: Dot-accessible options object
                - BaseStorageOptions: Structured options class
                Used for S3, GCS, etc. Example: {"key": "abc", "secret": "xyz"}
            fs: Pre-configured fsspec filesystem instance. If provided, used instead
                of creating new filesystem from base_dir and storage_options.
            cfg_dir: Override default configuration directory name ('conf').
                Example: "config" or "settings".
            pipelines_dir: Override default pipelines directory name ('pipelines').
                Example: "flows" or "dags".

            log_level: Set logging level for the manager.
                Valid values: "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"

        Raises:
            ValueError: If provided configuration paths don't exist or can't be created
            RuntimeError: If filesystem operations fail during initialization
            ImportError: If required dependencies for specified worker type not installed

        Example:
            >>> # Basic initialization
            >>> manager = PipelineManager()
            >>>
            >>> # Custom configuration with S3 storage
            >>> manager = PipelineManager(
            ...     base_dir="s3://my-bucket/project",
            ...     storage_options={
            ...         "key": "ACCESS_KEY",
            ...         "secret": "SECRET_KEY"
            ...     },

            ...     log_level="DEBUG"
            ... )
        """
⋮----
"""Setup filesystem and configuration directories.

        Args:
            base_dir: Root directory for the project
            storage_options: Storage options for filesystem
            fs: Pre-configured filesystem instance
            cfg_dir: Configuration directory name
            pipelines_dir: Pipelines directory name
        """
⋮----
# Setup filesystem helper
⋮----
# Configure caching if storage options provided
⋮----
cached = True
cache_storage = posixpath.join(
⋮----
cached = False
cache_storage = None
⋮----
# Get filesystem instance (use local `filesystem` to allow tests to patch)
⋮----
def _initialize_managers(self) -> None
⋮----
"""Initialize all manager components."""
# Initialize config manager
⋮----
# Load project configuration
⋮----
# Initialize registry
⋮----
# Initialize specialized managers
⋮----
# Initialize other components
⋮----
def _ensure_directories_exist(self) -> None
⋮----
"""Ensure essential directories exist."""
⋮----
def _add_modules_path(self) -> None
⋮----
"""Add pipeline module paths to Python path.

        This internal method ensures that pipeline modules can be imported by:
        1. Syncing filesystem cache if needed
        2. Adding project root to Python path
        3. Adding pipelines directory to Python path
        """
⋮----
project_path = self._fs._mapper.directory
modules_path = posixpath.join(project_path, self._pipelines_dir)
⋮----
# Use the base directory directly if not using cache
project_path = self._fs.path
⋮----
def __enter__(self) -> "PipelineManager"
⋮----
"""Enter the context manager.

        Enables use of the manager in a with statement for automatic resource cleanup.

        Returns:
            PipelineManager: Self for use in context manager.

        Example:
            >>> from flowerpower.pipeline import PipelineManager
            >>>
            >>> with PipelineManager() as manager:
            ...     result = manager.run("my_pipeline")
        """
⋮----
"""Exit the context manager.

        Handles cleanup of resources when exiting a with statement.

        Args:
            exc_type: Type of exception that occurred, if any
            exc_val: Exception instance that occurred, if any
            exc_tb: Traceback of exception that occurred, if any

        Example:
            >>> from flowerpower.pipeline import PipelineManager
            >>>
            >>> with PipelineManager() as manager:
            ...     try:
            ...         result = manager.run("my_pipeline")
            ...     except Exception as e:
            ...         print(f"Error: {e}")
            ...     # Resources automatically cleaned up here
        """
# Add cleanup code if needed
⋮----
def load_pipeline(self, name: str, reload: bool = False) -> PipelineConfig
⋮----
"""Load or reload configuration for a specific pipeline.

        Args:
            name: Name of the pipeline whose configuration to load
            reload: Force reload configuration even if already loaded.
                When False, returns cached config if available.

        Returns:
            PipelineConfig: The loaded pipeline configuration object
        """
⋮----
@property
    def current_pipeline_name(self) -> str
⋮----
"""Get the name of the currently loaded pipeline.

        Returns:
            str: Name of the currently loaded pipeline, or None if none loaded.
        """
⋮----
@property
    def project_cfg(self) -> ProjectConfig
⋮----
"""Get the project configuration.

        Loads configuration if not already loaded.

        Returns:
            ProjectConfig: Project-wide configuration object.

        Raises:
            RuntimeError: If configuration loading fails.

        Example:
            >>> manager = PipelineManager()
            >>> cfg = manager.project_cfg
            >>> print(cfg.name)
            'my_project'
        """
⋮----
@property
    def pipeline_cfg(self) -> PipelineConfig
⋮----
"""Get the configuration for the currently loaded pipeline.

        Returns:
            PipelineConfig: Pipeline-specific configuration object.

        Warns:
            UserWarning: If no pipeline is currently loaded.

        Example:
            >>> manager = PipelineManager()
            >>> manager._load_pipeline_cfg("example_pipeline")
            >>> cfg = manager.pipeline_cfg
            >>> print(cfg.run.executor)
            'local'
        """
⋮----
# --- Core Execution Method ---
⋮----
"""Execute a pipeline synchronously and return its results.

        This is the main method for running pipelines directly. It handles configuration
        loading, adapter setup, and execution via PipelineRunner.

        Args:
            name (str): Name of the pipeline to run. Must be a valid identifier.
            run_config (RunConfig | None): Run configuration object containing all execution parameters.
                If None, the default configuration from the pipeline will be used.
            **kwargs: Additional parameters to override the run_config. Supported parameters include:
                inputs (dict | None): Override pipeline input values. Example: {"data_date": "2025-04-28"}
                final_vars (list[str] | None): Specify which output variables to return.
                    Example: ["model", "metrics"]
                config (dict | None): Configuration for Hamilton pipeline executor.
                    Example: {"model": "LogisticRegression"}
                cache (dict | None): Cache configuration for results. Example: {"recompute": ["node1", "final_node"]}
                executor_cfg (str | dict | ExecutorConfig | None): Execution configuration, can be:
                    - str: Executor name, e.g. "threadpool", "local"
                    - dict: Raw config, e.g. {"type": "threadpool", "max_workers": 4}
                    - ExecutorConfig: Structured config object
                with_adapter_cfg (dict | WithAdapterConfig | None): Adapter settings for pipeline execution.
                    Example: {"opentelemetry": True, "tracker": False}
                pipeline_adapter_cfg (dict | PipelineAdapterConfig | None): Pipeline-specific adapter settings.
                    Example: {"tracker": {"project_id": "123", "tags": {"env": "prod"}}}
                project_adapter_cfg (dict | ProjectAdapterConfig | None): Project-level adapter settings.
                    Example: {"opentelemetry": {"host": "http://localhost:4317"}}
                adapter (dict[str, Any] | None): Custom adapter instance for pipeline
                    Example: {"ray_graph_adapter": RayGraphAdapter()}
                reload (bool): Force reload of pipeline configuration.
                log_level (str | None): Logging level for the execution. Default None uses project config.
                    Valid values: "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
                max_retries (int): Maximum number of retries for execution.
                retry_delay (float): Delay between retries in seconds.
                jitter_factor (float): Random jitter factor to add to retry delay
                retry_exceptions (tuple): Exceptions that trigger a retry.
                on_success (Callable | tuple[Callable, tuple | None, dict | None] | None): Callback to run on successful pipeline execution.
                on_failure (Callable | tuple[Callable, tuple | None, dict | None] | None): Callback to run on pipeline execution failure.

        Returns:
            dict[str, Any]: Pipeline execution results, mapping output variable names
                to their computed values.

        Raises:
            ValueError: If pipeline name doesn't exist or configuration is invalid
            ImportError: If pipeline module cannot be imported
            RuntimeError: If execution fails due to pipeline or adapter errors

        Example:
            >>> from flowerpower.pipeline import PipelineManager
            >>>
            >>> manager = PipelineManager()
            >>>
            >>> # Basic pipeline run
            >>> results = manager.run("data_pipeline")
            >>>
            >>> # Run with custom RunConfig
            >>> from flowerpower.cfg.pipeline.run import RunConfig
            >>> config = RunConfig(inputs={"date": "2025-04-28"}, final_vars=["result"])
            >>> results = manager.run("ml_pipeline", run_config=config)
            >>>
            >>> # Complex run with kwargs overrides
            >>> results = manager.run(
            ...     "ml_pipeline",
            ...     inputs={"training_date": "2025-04-28"},
            ...     final_vars=["model", "metrics"],
            ...     executor_cfg={"type": "threadpool", "max_workers": 4},
            ...     with_adapter_cfg={"tracker": True},
            ...     reload=True
            ... )
        """
# Set project context for executor
⋮----
# Delegate to executor
⋮----
# --- Delegated Methods ---
⋮----
# Registry Delegations
def new(self, name: str, overwrite: bool = False) -> None
⋮----
"""Create a new pipeline with the given name.

        Creates necessary configuration files and pipeline module template.

        Args:
            name: Name for the new pipeline. Must be a valid Python identifier.
            overwrite: Whether to overwrite existing pipeline with same name.
                Default False for safety.

        Raises:
            ValueError: If name is invalid or pipeline exists and overwrite=False
            RuntimeError: If file creation fails
            PermissionError: If lacking write permissions

        Example:
            >>> from flowerpower.pipeline import PipelineManager
            >>>
            >>> # Create new pipeline
            >>> manager = PipelineManager()
            >>> manager.new("data_transformation")
            >>>
            >>> # Overwrite existing pipeline
            >>> manager.new("data_transformation", overwrite=True)
        """
⋮----
def delete(self, name: str, cfg: bool = True, module: bool = False) -> None
⋮----
"""
        Delete a pipeline and its associated files.

        Args:
            name: Name of the pipeline to delete
            cfg: Whether to delete configuration files. Default True.
            module: Whether to delete Python module file. Default False
                for safety since it may contain custom code.

        Raises:
            FileNotFoundError: If specified pipeline files don't exist
            PermissionError: If lacking delete permissions
            RuntimeError: If deletion fails partially, leaving inconsistent state

        Example:
            >>> from flowerpower.pipeline import PipelineManager
            >>>
            >>> # Delete pipeline config only
            >>> manager = PipelineManager()
            >>> manager.delete("old_pipeline")
            >>>
            >>> # Delete both config and module
            >>> manager.delete("test_pipeline", module=True)
        """
⋮----
"""Get a detailed summary of pipeline(s) configuration and code.

        Args:
            name: Specific pipeline to summarize. If None, summarizes all.
            cfg: Include pipeline configuration details. Default True.
            code: Include pipeline module code. Default True.
            project: Include project configuration. Default True.

        Returns:
            dict[str, dict | str]: Nested dictionary containing requested
                summaries. Structure varies based on input parameters:
                - With name: {"config": dict, "code": str, "project": dict}
                - Without name: {pipeline_name: {"config": dict, ...}, ...}

        Example:
            >>> from flowerpower.pipeline import PipelineManager
            >>>
            >>> manager = PipelineManager()
            >>>
            >>> # Get summary of specific pipeline
            >>> summary = manager.get_summary("data_pipeline")
            >>> print(summary["config"]["schedule"]["enabled"])
            True
            >>>
            >>> # Get summary of all pipelines' code
            >>> all_code = manager.get_summary(
            ...     cfg=False,
            ...     code=True,
            ...     project=False
            ... )
        """
⋮----
"""
        Show a summary of the pipelines.

        Args:
            name (str | None, optional): The name of the pipeline. Defaults to None.
            cfg (bool, optional): Whether to show the configuration. Defaults to True.
            code (bool, optional): Whether to show the module. Defaults to True.
            project (bool, optional): Whether to show the project configuration. Defaults to True.
            to_html (bool, optional): Whether to export the summary to HTML. Defaults to False.
            to_svg (bool, optional): Whether to export the summary to SVG. Defaults to False.

        Returns:
            None | str: The summary of the pipelines. If `to_html` is True, returns the HTML string.
                If `to_svg` is True, returns the SVG string.

        Examples:
            >>> pm = PipelineManager()
            >>> pm.show_summary()
        """
⋮----
def list_pipelines(self) -> list[str]
⋮----
"""Get list of all available pipeline names.

        Returns:
            list[str]: Names of all registered pipelines, sorted alphabetically.

        Example:
            >>> from flowerpower.pipeline import PipelineManager
            >>>
            >>> manager = PipelineManager()
            >>> pipelines = manager.list_pipelines()
            >>> print(pipelines)
            ['data_ingestion', 'model_training', 'reporting']
        """
⋮----
def show_pipelines(self, format: str = "table") -> None
⋮----
"""Display all available pipelines in a selected format.

        Args:
            format: One of "table", "json", or "yaml". Defaults to "table".
        """
fmt = (format or "table").lower()
⋮----
names = self._lifecycle_manager.list_pipelines()
⋮----
import yaml  # type: ignore
⋮----
@property
    def pipelines(self) -> list[str]
⋮----
"""Get list of all available pipeline names.

        Similar to list_pipelines() but as a property.

        Returns:
            list[str]: Names of all registered pipelines, sorted alphabetically.

        Example:
            >>> from flowerpower.pipeline import PipelineManager
            >>>
            >>> manager = PipelineManager()
            >>> print(manager.pipelines)
            ['data_ingestion', 'model_training', 'reporting']
        """
⋮----
@property
    def summary(self) -> dict[str, dict | str]
⋮----
"""Get complete summary of all pipelines.

        Returns:
            dict[str, dict | str]: Full summary including configuration,
            code, and project settings for all pipelines.

        Example:
            >>> from flowerpower.pipeline import PipelineManager
            >>>
            >>> manager = PipelineManager()
            >>> summary = manager.summary
            >>> for name, details in summary.items():
            ...     print(f"{name}: {details['config']['type']}")
            data_pipeline: batch
            ml_pipeline: streaming
        """
⋮----
"""Add a hook to the pipeline module.

        Args:
            name (str): The name of the pipeline
            type (HookType): The type of the hook.
            to (str | None, optional): The name of the file to add the hook to. Defaults to the hook.py file in the pipelines hooks folder.
            function_name (str | None, optional): The name of the function. If not provided uses default name of hook type.

        Returns:
            None

        Raises:
            ValueError: If the hook type is not valid

        Example:
            >>> from flowerpower.pipeline import PipelineManager
            >>>
            >>> manager = PipelineManager()
            >>> manager.add_hook(
            ...     name="data_pipeline",
            ...     type=HookType.PRE_EXECUTE,
            ...     to="pre_execute_hook",
            ...     function_name="my_pre_execute_function"
            ... )
        """
⋮----
# IO Delegations
⋮----
"""Import a pipeline from another FlowerPower project.

        Copies both pipeline configuration and code files from the source location
        to the current project.

        Args:
            name (str): Name for the new pipeline in the current project
            src_base_dir (str): Source FlowerPower project directory or URI
                Examples:
                    - Local: "/path/to/other/project"
                    - S3: "s3://bucket/project"
                    - GitHub: "github://org/repo/project"
            src_fs (AbstractFileSystem | None): Pre-configured source filesystem
                Example: S3FileSystem(key='ACCESS_KEY', secret='SECRET_KEY')
            src_storage_options (dict | BaseStorageOptions | None): Options for source filesystem access
                Example: {"key": "ACCESS_KEY", "secret": "SECRET_KEY"}
            overwrite: Whether to replace existing pipeline if name exists

        Raises:
            ValueError: If pipeline name exists and overwrite=False
            FileNotFoundError: If source pipeline not found
            RuntimeError: If import fails

        Example:
            >>> from flowerpower.pipeline import PipelineManager
            >>> from s3fs import S3FileSystem
            >>>
            >>> manager = PipelineManager()
            >>>
            >>> # Import from local filesystem
            >>> manager.import_pipeline(
            ...     "new_pipeline",
            ...     "/path/to/other/project"
            ... )
            >>>
            >>> # Import from S3 with custom filesystem
            >>> s3 = S3FileSystem(anon=False)
            >>> manager.import_pipeline(
            ...     "s3_pipeline",
            ...     "s3://bucket/project",
            ...     src_fs=s3
            ... )
        """
⋮----
src_base_dir: str,  # Base dir for source if pipelines is a list
⋮----
"""Import multiple pipelines from another project or location.


        Args:
            pipelines(list[str]): List of pipeline names to import
            src_base_dir (str, optional): Source project directory or URI
                Examples:
                    - Local: "/path/to/other/project"
                    - S3: "s3://bucket/project"
                    - GitHub: "github://org/repo/project"
            src_fs (AbstractFileSystem | None, optional): Pre-configured source filesystem
                Example: S3FileSystem(key='ACCESS_KEY', secret="SECRET_KEY")
            storage_options (dict | BaseStorageOptions | None, optional): Options for source filesystem access
                Example: {"key": "ACCESS_KEY", "secret": "SECRET_KEY"}
            overwrite (bool, optional): Whether to replace existing pipelines

        Raises:
            ValueError: If any pipeline exists and overwrite=False
            FileNotFoundError: If source pipelines not found
            RuntimeError: If import operation fails

        Example:
            >>> from flowerpower.pipeline import PipelineManager
            >>>
            >>> manager = PipelineManager()
            >>>
            >>> # Import keeping original names
            >>> manager.import_many(
            ...     names=["pipeline1", "pipeline2"],
            ...     src_base_dir="s3://bucket/source",
            ...     src_storage_options={
            ...         "key": "ACCESS_KEY",
            ...         "secret": "SECRET_KEY"
            ...     }
            ... )
        """
⋮----
"""Import all pipelines from another FlowerPower project.

        Args:
            src_base_dir (str): Source project directory or URI
                Examples:
                    - Local: "/path/to/other/project"
                    - S3: "s3://bucket/project"
                    - GitHub: "github://org/repo/project"
            src_fs (AbstractFileSystem | None): Pre-configured source filesystem
                Example: S3FileSystem(key='KEY',secret='SECRET')
            src_storage_options (dict | BaseStorageOptions | None): Options for source filesystem access
                Example: {"key": "ACCESS_KEY", "secret": "SECRET_KEY"}
            overwrite (bool): Whether to replace existing pipelines

        Raises:
            FileNotFoundError: If source location not found
            RuntimeError: If import fails

        Example:
            >>> from flowerpower.pipeline import PipelineManager
            >>>
            >>> manager = PipelineManager()
            >>>
            >>> # Import all from backup
            >>> manager.import_all("/path/to/backup")
            >>>
            >>> # Import all from S3 with credentials
            >>> manager.import_all(
            ...     "s3://bucket/backup",
            ...     src_storage_options={
            ...         "key": "ACCESS_KEY",
            ...         "secret": "SECRET_KEY"
            ...     }
            ... )
        """
⋮----
"""Export a pipeline to another location or project.

        Copies pipeline configuration and code files to the destination location
        while preserving directory structure.

        Args:
            name (str): Name of the pipeline to export
            dest_base_dir (str): Destination directory or URI
                Examples:
                    - Local: "/path/to/exports"
                    - S3: "s3://bucket/exports"
                    - Azure: "abfs://container/exports"
            dest_fs (AbstractFileSystem | None): Pre-configured destination filesystem
                Example: S3FileSystem(key='ACCESS_KEY', secret='SECRET_KEY')
            dest_storage_options (dict | BaseStorageOptions | None): Options for destination filesystem access
                Example: {"key": "ACCESS_KEY", "secret": "SECRET_KEY"}
            overwrite (bool): Whether to replace existing files at destination

        Raises:
            ValueError: If pipeline doesn't exist
            FileNotFoundError: If destination not accessible
            RuntimeError: If export fails

        Example:
            >>> from flowerpower.pipeline import PipelineManager
            >>> from gcsfs import GCSFileSystem
            >>>
            >>> manager = PipelineManager()
            >>>
            >>> # Export to local backup
            >>> manager.export_pipeline(
            ...     "my_pipeline",
            ...     "/path/to/backup"
            ... )
            >>>
            >>> # Export to Google Cloud Storage
            >>> gcs = GCSFileSystem(project='my-project')
            >>> manager.export_pipeline(
            ...     "prod_pipeline",
            ...     "gs://my-bucket/backups",
            ...     dest_fs=gcs
            ... )
        """
⋮----
"""Export multiple pipelines to another location.

        Efficiently exports multiple pipelines in a single operation,
        preserving directory structure and metadata.

        Args:
            names (list[str]): List of pipeline names to export
            dest_base_dir (str): Destination directory or URI
                Examples:
                    - Local: "/path/to/exports"
                    - S3: "s3://bucket/exports"
                    - Azure: "abfs://container/exports"
            dest_fs (AbstractFileSystem | None): Pre-configured destination filesystem
                Example: S3FileSystem(key='ACCESS_KEY', secret='SECRET_KEY')
            dest_storage_options (dict | BaseStorageOptions | None): Options for destination filesystem access
                Example: {"key": "ACCESS_KEY", "secret": "SECRET_KEY"}
            overwrite (bool): Whether to replace existing files at destination

        Raises:
            ValueError: If any pipeline doesn't exist
            FileNotFoundError: If destination not accessible
            RuntimeError: If export operation fails

        Example:
            >>> from flowerpower.pipeline import PipelineManager
            >>> from azure.storage.filedatalake import DataLakeServiceClient
            >>>
            >>> manager = PipelineManager()
            >>>
            >>> # Export multiple pipelines to Azure Data Lake
            >>> manager.export_many(
            ...     pipelines=["ingest", "process", "report"],
            ...     base_dir="abfs://data/backups",
            ...     dest_storage_options={
            ...         "account_name": "myaccount",
            ...         "sas_token": "...",
            ...     }
            ... )
        """
⋮----
"""Export all pipelines to another location.

        Args:
            dest_base_dir (str): Destination directory or URI
                Examples:
                    - Local: "/path/to/exports"
                    - S3: "s3://bucket/exports"
                    - Azure: "abfs://container/exports"
            dest_fs (AbstractFileSystem | None): Pre-configured destination filesystem
                Example: S3FileSystem(key='ACCESS_KEY', secret='SECRET_KEY')
            dest_storage_options (dict | BaseStorageOptions | None): Options for destination filesystem access
                Example: {"key": "ACCESS_KEY", "secret": "SECRET_KEY"}
            overwrite (bool): Whether to replace existing files at destination

        Example:
            >>> from flowerpower.pipeline import PipelineManager
            >>>
            >>> manager = PipelineManager()
            >>>
            >>> # Export all to backup directory
            >>> manager.export_all("/path/to/backup")
            >>>
            >>> # Export all to cloud storage
            >>> manager.export_all(
            ...     "gs://bucket/pipelines",
            ...     dest_storage_options={
            ...         "token": "SERVICE_ACCOUNT_TOKEN",
            ...         "project": "my-project"
            ...     }
            ... )
        """
⋮----
# Visualizer Delegations
⋮----
"""Save pipeline DAG visualization to a file.

        Creates a visual representation of the pipeline's directed acyclic graph (DAG)
        showing function dependencies and data flow.

        Args:
            name: Name of the pipeline to visualize
            format: Output file format. Supported formats:
                - "png": Standard bitmap image
                - "svg": Scalable vector graphic
                - "pdf": Portable document format
                - "dot": Graphviz DOT format
            reload: Whether to reload pipeline before visualization

        Raises:
            ValueError: If pipeline name doesn't exist
            ImportError: If required visualization dependencies missing
            RuntimeError: If graph generation fails

        Example:
            >>> from flowerpower.pipeline import PipelineManager
            >>>
            >>> manager = PipelineManager()
            >>>
            >>> # Save as PNG
            >>> manager.save_dag("data_pipeline")
            >>>
            >>> # Save as SVG with reload
            >>> manager.save_dag(
            ...     name="ml_pipeline",
            ...     format="svg",
            ...     reload=True
            ... )
        """
⋮----
"""Display pipeline DAG visualization interactively.

        Similar to save_dag() but displays the graph immediately in notebook
        environments or returns the raw graph object for custom rendering.

        Args:
            name: Name of the pipeline to visualize
            format: Output format (see save_dag() for options)
            reload: Whether to reload pipeline before visualization
            raw: If True, return the raw graph object instead of displaying

        Returns:
            Union[GraphType, None]: Raw graph object if raw=True, else None after
                displaying the visualization

        Raises:
            ValueError: If pipeline name doesn't exist
            ImportError: If visualization dependencies missing
            RuntimeError: If graph generation fails

        Example:
            >>> from flowerpower.pipeline import PipelineManager
            >>>
            >>> manager = PipelineManager()
            >>>
            >>> # Display in notebook
            >>> manager.show_dag("data_pipeline")
            >>>
            >>> # Get raw graph for custom rendering
            >>> graph = manager.show_dag(
            ...     name="ml_pipeline",
            ...     format="svg",
            ...     raw=True
            ... )
            >>> # Custom rendering
            >>> graph.render("custom_vis", view=True)
        """
```

